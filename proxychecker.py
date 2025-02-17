import requests
from concurrent.futures import ThreadPoolExecutor

def check_proxy(proxy):
    url = "https://httpbin.org/ip"  # Test URL to check proxy
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            print(f"Working Proxy: {proxy}")
            return proxy
    except requests.RequestException:
        pass
    return None

def load_proxies(filename="proxies.txt"):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]

def main():
    proxies = load_proxies()
    working_proxies = []
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_proxy, proxies)
    
    working_proxies = [proxy for proxy in results if proxy]
    
    print("\nTotal Working Proxies:")
    for proxy in working_proxies:
        print(proxy)

if __name__ == "__main__":
    main()