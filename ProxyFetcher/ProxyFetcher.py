import requests
from bs4 import BeautifulSoup
from threading import Thread, Lock
from queue import Queue
from ProxyFetcher.logger_config import setup_logger

logger = setup_logger()
PROXIES_SOURCE = "https://free-proxy-list.net/"
PROXY_TIMEOUT = 10;
PROXY_SSL_VERIFICATION = False

def get_proxy_addresses(num_of_proxies):
    try:
        response = requests.get(PROXIES_SOURCE)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            proxies = []
            
            table = soup.find('div', class_='table-responsive fpl-list')
            if table:
                rows = table.find('tbody').find_all('tr')
                for row in rows[:num_of_proxies]:
                    cells = row.find_all('td')
                    if len(cells) >= 7:  # Ensure there are enough cells for IP, port, and type
                        ip = cells[0].text
                        port = cells[1].text
                        if "yes" in cells[6].text.lower():  # Check if the proxy supports HTTPS
                            protocol = 'https'
                        else:
                            protocol = 'http'
                        proxies.append({'ip': ip, 'port': port, 'protocol': protocol})
            return proxies
        else:
            logger.error(f"Failed to fetch proxy addresses. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return None


def fetch_url(queue, url, lock, success, headers):
    while True:
        proxy_obj = queue.get()
        if proxy_obj is None:
            queue.task_done()
            break

        proxy_address = f"{proxy_obj['ip']}:{proxy_obj['port']}"
        proxy = {proxy_obj['protocol']: f"{proxy_obj['protocol']}://{proxy_address}"}
        try:
            logger.debug(f"Trying proxy: {proxy_address}")
            response = requests.get(url, proxies=proxy, headers=headers, timeout=PROXY_TIMEOUT, verify=PROXY_SSL_VERIFICATION)
            logger.debug(f"{proxy_address} response code: {response.status_code}")
            if response.status_code == 200:
                with lock:
                    if not success['flag']:
                        success['flag'] = True
                        success['response'] = response
                        logger.info(f"Successfully fetched with proxy: {proxy_address}")
                break
        except requests.RequestException as e:
            logger.error(f"Error with proxy {proxy_address}: {e}")
        finally:
            queue.task_done()

def fetch_with_proxies(url, num_of_proxies, num_threads, headers=None):
    if headers is None:
        headers = {}

    proxies = get_proxy_addresses(num_of_proxies)
    if not proxies:
        logger.error("Could not fetch proxy addresses.")
        return None
    
    queue = Queue()
    lock = Lock()
    success = {'flag': False, 'response': None}
    threads = []
    
    for _ in range(num_threads):
        thread = Thread(target=fetch_url, args=(queue, url, lock, success, headers))
        thread.start()
        threads.append(thread)
    
    for proxy in proxies:
        if success['flag']:
            break
        queue.put(proxy)
    
    for _ in range(num_threads):
        queue.put(None)

    for thread in threads:
        thread.join()

    return success['response']

if __name__ == '__main__':
    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = fetch_with_proxies("https://webscraper.io/test-sites/e-commerce/allinone", 10, 4, headers=custom_headers)
    if response:
        logger.info(f"Successfully fetched with proxy: {response.text}")
    else:
        logger.error("Failed to fetch with any of the proxies.")