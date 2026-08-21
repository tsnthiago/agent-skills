import urllib.request
import json
import base64
import os
from pathlib import Path

def get_langfuse_stats():
    pk = os.getenv("LANGFUSE_PUBLIC_KEY") or os.getenv("HERMES_LANGFUSE_PUBLIC_KEY")
    sk = os.getenv("LANGFUSE_SECRET_KEY") or os.getenv("HERMES_LANGFUSE_SECRET_KEY")
    base_url = os.getenv("LANGFUSE_BASE_URL", "http://localhost:3000")

    if not pk or not sk:
        env_file = Path.home() / ".hermes/.env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if line.startswith("HERMES_LANGFUSE_PUBLIC_KEY") or line.startswith("LANGFUSE_PUBLIC_KEY"):
                    pk = line.split("=", 1)[1].strip('"\'')
                if line.startswith("HERMES_LANGFUSE_SECRET_KEY") or line.startswith("LANGFUSE_SECRET_KEY"):
                    sk = line.split("=", 1)[1].strip('"\'')
                if line.startswith("HERMES_LANGFUSE_BASE_URL") or line.startswith("LANGFUSE_BASE_URL"):
                    base_url = line.split("=", 1)[1].strip('"\'')

    if not pk or not sk:
        return "Erro: Chaves do Langfuse não encontradas no ambiente nem no .env"

    auth = base64.b64encode(f"{pk}:{sk}".encode()).decode()
    url = f"{base_url.rstrip('/')}/api/public/traces?limit=100"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Basic {auth}")
    req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            traces = data.get("data", [])
            
            if not traces:
                return "Nenhum trace encontrado."
                
            total_traces = len(traces)
            total_cost = sum(t.get("totalCost") or 0.0 for t in traces)
            avg_latency = sum(t.get("latency") or 0.0 for t in traces) / total_traces if total_traces else 0
            
            output = [
                f"=== Panorama Langfuse (Últimos {total_traces} Traces) ===",
                f"Custo Total: ${total_cost:.5f}",
                f"Latência Média: {avg_latency:.2f}s",
                "Traces Recentes:"
            ]
            
            for t in traces[:5]:
                cost = t.get('totalCost') or 0
                lat = t.get('latency') or 0
                output.append(f" - {t.get('name')} (ID: {t.get('id')[:8]}...) | Custo: ${cost:.5f} | Latência: {lat:.2f}s")
                
            return "\n".join(output)
    except Exception as e:
        return f"Erro ao acessar API do Langfuse: {e}"

if __name__ == "__main__":
    print(get_langfuse_stats())
