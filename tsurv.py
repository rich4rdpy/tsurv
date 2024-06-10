import os
import requests
import json
from colorama import Fore

search_engines = {
    "Qwant": "https://www.qwant.com/?q={query}",
    "Google": "https://www.google.com/search?q={query}",
    "Yandex": "https://yandex.com/search?q={query}",
    "DuckDuckGo": "https://duckduckgo.com/search?q={query}&format=json",
    "Yahoo": "https://search.yahoo.com/search?p={query}"
}

def search_query(query):
    if not os.path.exists(query):
        os.makedirs(query)

    for engine, url in search_engines.items():
        search_url = url.format(query=query)
        
        try:
            response = requests.get(search_url)
            response.raise_for_status()  
            
            content_type = response.headers.get('Content-Type')
            if 'application/json' in content_type:
                results = response.json()
            else:
                results = response.text  
            
            with open(f"{query}/{engine}.json", "w", encoding='utf-8') as file:
                json.dump(results, file, ensure_ascii=False, indent=4)
            
            print(Fore.GREEN + f"[+] {engine} has successfully been saved.")
        
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"[-] Erreur lors de la recherche avec {engine}: {e}")
        except json.JSONDecodeError as e:
            print(Fore.RED + f"[-] Erreur de décodage JSON pour {engine}: {e}")

if __name__ == "__main__":
    query = input("[=] Enter Search Query: ")
    search_query(query)
