import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import os

STATE_FILE = os.path.expanduser("~/.hermes/cache/seen_ai_news.json")

def load_seen():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return set(json.load(f))
        except:
            return set()
    return set()

def save_seen(seen):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(list(seen)[-1000:], f) # Mantém as últimas 1000 para não estourar o disco

def fetch_rss(url, limit=10):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            items = []
            for item in root.findall('.//item')[:limit]:
                title = item.find('title').text
                link = item.find('link').text if item.find('link') is not None else ""
                items.append({"title": title, "link": link})
            return items
    except Exception as e:
        return []

def main():
    urls = {
        "Google News BR - IA": "https://news.google.com/rss/search?q=" + urllib.parse.quote("Inteligência Artificial when:1d") + "&hl=pt-BR&gl=BR&ceid=BR:pt-419",
        "Google News Global - AI": "https://news.google.com/rss/search?q=" + urllib.parse.quote("Artificial Intelligence when:1d") + "&hl=en-US&gl=US&ceid=US:en",
        "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/",
        "Hacker News": "https://news.ycombinator.com/rss"
    }

    seen = load_seen()
    new_articles = {}
    has_new = False

    for source, url in urls.items():
        articles = fetch_rss(url, limit=15)
        source_new = []
        for art in articles:
            if art["title"] not in seen:
                source_new.append(art)
                seen.add(art["title"])
                has_new = True
        
        if source_new:
            # Limita a 3 destaques por fonte a cada hora para não poluir o WhatsApp
            new_articles[source] = source_new[:3]

    if has_new:
        save_seen(seen)
        print(json.dumps(new_articles, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"status": "no_new_articles"}, indent=2))

if __name__ == "__main__":
    main()