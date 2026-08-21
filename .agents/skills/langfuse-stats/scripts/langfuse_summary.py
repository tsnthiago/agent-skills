import urllib.request
import json
import base64
import os
from pathlib import Path

def get_langfuse_stats():
    env_text = Path("/root/.hermes/.env").read_text()
    pk, sk = None, None
    for line in env_text.splitlines():
        if line.startswith("HERMES_LANGFUSE_PUBLIC_KEY"):
            pk = line.split("=", 1)[1].strip('"\'')
        if line.startswith("HERMES_LANGFUSE_SECRET_KEY"):
            sk = line.split("=", 1)[1].strip('"\'')

    if not pk or not sk:
        return "Erro: Chaves do Langfuse não encontradas no .env"

    auth = base64.b64encode(f"{pk}:{sk}".encode()).decode()
    url = "http://localhost:3031/api/public/traces?limit=100"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Basic {auth}")
    req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req) as response:
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