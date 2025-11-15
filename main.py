import requests
from config import GROK_API_KEY, PERPLEXITY_API_KEY

def test_grok():
    print("\n🧪 Probando Grok...")
    r = requests.post("https://api.x.ai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROK_API_KEY}"},
        json={"model": "grok-beta", "messages": [{"role": "user", "content": "Di: Sistema funcionando"}]})
    if r.status_code == 200:
        print(f"✅ Grok: {r.json()['choices'][0]['message']['content']}")
    else:
        print(f"❌ Error: {r.status_code}")

def test_perplexity():
    print("\n🔍 Probando Perplexity...")
    r = requests.post("https://api.perplexity.ai/chat/completions",
        headers={"Authorization": f"Bearer {PERPLEXITY_API_KEY}"},
        json={"model": "llama-3.1-sonar-small-128k-online", "messages": [{"role": "user", "content": "¿Qué día es hoy?"}]})
    if r.status_code == 200:
        print(f"✅ Perplexity: {r.json()['choices'][0]['message']['content'][:100]}...")
    else:
        print(f"❌ Error: {r.status_code}")

if __name__ == "__main__":
    print("🚀 Sistema Master AI - Grok + Perplexity")
    test_grok()
    test_perplexity()
    print("\n✅ Sistema listo para usar!")
