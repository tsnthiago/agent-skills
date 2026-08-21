# Cleanup completo do proxy miner (Windows)
#
# Mata: proxy_mine, filhos, yt-dlp-sabr, temps proxy-yt-*
# Uso:
#   powershell -ExecutionPolicy Bypass -File .agents/skills/youtube-proxy-mine/scripts/cleanup.ps1
#   powershell -ExecutionPolicy Bypass -File .agents/skills/youtube-proxy-mine/scripts/cleanup.ps1 -AlsoClearResults

param(
    [switch] $AlsoClearResults,  # apaga results.jsonl (log grande)
    [string] $YoutubeRoot = ""
)

$ErrorActionPreference = "Continue"

if (-not $YoutubeRoot) {
    # skill em .agents/skills/youtube-proxy-mine/scripts → repo/youtube
    $YoutubeRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..\youtube")).Path
}

function Get-ProcessTreeIds([int] $RootId) {
    $ids = New-Object System.Collections.Generic.List[int]
    $queue = New-Object System.Collections.Generic.Queue[int]
    $queue.Enqueue($RootId)
    $all = @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue)
    while ($queue.Count -gt 0) {
        $id = $queue.Dequeue()
        if ($ids -contains $id) { continue }
        $ids.Add($id)
        foreach ($c in $all | Where-Object { $_.ParentProcessId -eq $id }) {
            $queue.Enqueue([int]$c.ProcessId)
        }
    }
    return $ids
}

Write-Host "=== proxy-mine cleanup ==="
Write-Host "youtube: $YoutubeRoot"

$roots = @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue | Where-Object {
    $_.CommandLine -and (
        $_.CommandLine -match 'modules\.proxy_mine' -or
        $_.CommandLine -match '[\\/]mine\.ps1'
    )
})

$killIds = New-Object System.Collections.Generic.HashSet[int]

foreach ($r in $roots) {
    foreach ($id in (Get-ProcessTreeIds ([int]$r.ProcessId))) {
        [void]$killIds.Add($id)
    }
}

# órfãos por commandline / nome
Get-CimInstance Win32_Process -ErrorAction SilentlyContinue | Where-Object {
    $_.CommandLine -and (
        $_.CommandLine -match 'yt-dlp-sabr' -or
        $_.CommandLine -match 'yt-dlp\.exe' -or
        $_.CommandLine -match 'modules\.proxy_mine'
    )
} | ForEach-Object { [void]$killIds.Add([int]$_.ProcessId) }

Get-Process -Name "yt-dlp*","yt-dlp-sabr*","python*" -ErrorAction SilentlyContinue | ForEach-Object {
    try {
        $cim = Get-CimInstance Win32_Process -Filter "ProcessId=$($_.Id)" -ErrorAction SilentlyContinue
        if ($cim -and $cim.CommandLine -and (
            $cim.CommandLine -match 'proxy_mine' -or
            $cim.CommandLine -match 'yt-dlp-sabr' -or
            $cim.CommandLine -match 'mine\.ps1'
        )) {
            [void]$killIds.Add([int]$_.Id)
        }
    } catch {}
}

if ($killIds.Count -eq 0) {
    Write-Host "Nenhum processo relacionado."
} else {
    Write-Host "Matando $($killIds.Count) PID(s)…"
    foreach ($id in ($killIds | Sort-Object -Descending)) {
        try {
            $p = Get-Process -Id $id -ErrorAction SilentlyContinue
            $name = if ($p) { $p.ProcessName } else { "?" }
            Write-Host "  kill $id ($name)"
            Stop-Process -Id $id -Force -ErrorAction SilentlyContinue
        } catch {}
    }
}

Start-Sleep -Seconds 1

# temps do deep download
$tempRoots = @(
    $env:TEMP,
    $env:TMP,
    [System.IO.Path]::GetTempPath()
) | Select-Object -Unique

foreach ($tr in $tempRoots) {
    if (-not $tr -or -not (Test-Path $tr)) { continue }
    Get-ChildItem -Path $tr -Directory -Filter "proxy-yt-*" -ErrorAction SilentlyContinue | ForEach-Object {
        Write-Host "  rm temp $($_.FullName)"
        Remove-Item -Recurse -Force $_.FullName -ErrorAction SilentlyContinue
    }
}

if ($AlsoClearResults) {
    $rj = Join-Path $YoutubeRoot "out\proxies\results.jsonl"
    if (Test-Path $rj) {
        Remove-Item -Force $rj -ErrorAction SilentlyContinue
        Write-Host "  rm results.jsonl"
    }
}

$left = @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue | Where-Object {
    $_.CommandLine -and ($_.CommandLine -match 'modules\.proxy_mine|yt-dlp-sabr')
})
if ($left.Count -eq 0) {
    Write-Host "OK — limpo."
    exit 0
}
Write-Host "AINDA RESTAM:"
$left | ForEach-Object { Write-Host "  PID=$($_.ProcessId) $($_.CommandLine.Substring(0, [Math]::Min(100, $_.CommandLine.Length)))" }
exit 1
