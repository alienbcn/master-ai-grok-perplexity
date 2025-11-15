import requests
import json
from config import GROK_API_KEY, PERPLEXITY_API_KEY

def grok_generate_task():
    """Grok genera una tarea de búsqueda para Perplexity"""
    print("\n🧠 GROK: Generando tarea...")
    
    r = requests.post("https://api.x.ai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROK_API_KEY}"},
        json={
            "model": "grok-beta",
            "messages": [{
                "role": "user",
                "content": "Dame un tema interesante sobre IA y marketing para buscar en internet. Responde solo con el tema en una frase corta."
            }]
        }
    )
    
    if r.status_code == 200:
        task = r.json()['choices'][0]['message']['content']
        print(f"✅ GROK generó: '{task}'")
        return task
    else:
        print(f"❌ Error Grok: {r.status_code}")
        return None

def perplexity_search(query):
    """Perplexity ejecuta la búsqueda que Grok ordenó"""
    print(f"\n🔍 PERPLEXITY: Buscando '{query}'...")
    
    r = requests.post("https://api.perplexity.ai/chat/completions",
        headers={"Authorization": f"Bearer {PERPLEXITY_API_KEY}"},
        json={
            "model": "llama-3.1-sonar-small-128k-online",
            "messages": [{
                "role": "user",
                "content": query
            }]
        }
    )
    
    if r.status_code == 200:
        result = r.json()['choices'][0]['message']['content']
        print(f"✅ PERPLEXITY encontró: {result[:200]}...")
        return result
    else:
        print(f"❌ Error Perplexity: {r.status_code}")
        return None

def master_workflow():
    """Flujo completo: Grok ordena -> Perplexity ejecuta"""
    print("\n" + "="*60)
    print("🚀 SISTEMA MASTER AI - GROK + PERPLEXITY")
    print("="*60)
    
    # Paso 1: Grok genera la tarea
    task = grok_generate_task()
    
    if task:
        # Paso 2: Perplexity ejecuta la búsqueda
        result = perplexity_search(task)
        
        if result:
            print("\n" + "="*60)
            print("✅ FLUJO COMPLETADO CON ÉXITO")
            print("="*60)
            print(f"\n📋 GROK ordenó buscar: {task}")
            print(f"\n📊 PERPLEXITY encontró:\n{result}")
            return True
    
    print("\n❌ Flujo incompleto")
    return False

if __name__ == "__main__":
    master_workflow()
