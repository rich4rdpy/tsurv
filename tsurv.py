import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

init(autoreset=True)

def search_google(query):
    try:
        url = f"https://www.google.com/search?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')
        with open('google.txt', 'w', encoding='utf-8') as f:
            for result in results:
                f.write(result.get_text() + "\n")
        print(Fore.GREEN + "[+] Google search completed. (google.txt)")
    except Exception as e:
        print(Fore.RED + f"[-] Error during Google search: {e}")

def search_duckduckgo(query):
    try:
        url = f"https://duckduckgo.com/html/?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', class_='result__a')
        with open('duckduckgo.txt', 'w', encoding='utf-8') as f:
            for result in results:
                f.write(result.get_text() + "\n")
        print(Fore.GREEN + "[+] DuckDuckGo search completed. (duckduckgo.txt)")
    except Exception as e:
        print(Fore.RED + f"[-] Error during DuckDuckGo search: {e}")

def search_yandex(query):
    try:
        url = f"https://yandex.com/search/?text={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('h2', class_='OrganicTitle-LinkText')
        with open('yandex.txt', 'w', encoding='utf-8') as f:
            for result in results:
                f.write(result.get_text() + "\n")
        print(Fore.GREEN + "[+] Yandex search completed. (yandex.txt)")
    except Exception as e:
        print(Fore.RED + f"[-] Error during Yandex search: {e}")

def search_qwant(query):
    try:
        url = f"https://www.qwant.com/?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', class_='result__a')
        with open('qwant.txt', 'w', encoding='utf-8') as f:
            for result in results:
                f.write(result.get_text() + "\n")
        print(Fore.GREEN + "[+] Qwant search completed. (qwant.txt)")
    except Exception as e:
        print(Fore.RED + f"[-] Error during Qwant search: {e}")

def search_yahoo(query):
    try:
        url = f"https://search.yahoo.com/search?p={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('h3', class_='title')
        with open('yahoo.txt', 'w', encoding='utf-8') as f:
            for result in results:
                f.write(result.get_text() + "\n")
        print(Fore.GREEN + "[+] Yahoo search completed. (yahoo.txt)")
    except Exception as e:
        print(Fore.RED + f"[-] Error during Yahoo search: {e}")

def search_bing(query):
    try:
        url = f"https://www.bing.com/search?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('li', class_='b_algo')
        with open('bing.txt', 'w', encoding='utf-8') as f:
            for result in results:
                f.write(result.find('a').get_text() + "\n")
        print(Fore.GREEN + "[+] Bing search completed. (bing.txt)")
    except Exception as e:
        print(Fore.RED + f"[-] Error during Bing search: {e}")

def main():
    print(Fore.BLUE + "------------------------------")
    print(Fore.BLUE + "     https:://github.com/rich4rdpy/tsurv   ")
    query = input(Fore.PURPLE + "     [=] Enter your search query: ")
    print(Fore.BLUE + "------------------------------")
    search_google(query)
    search_duckduckgo(query)
    search_yandex(query)
    search_qwant(query)
    search_yahoo(query)
    search_bing(query)

if __name__ == "__main__":
    main()
