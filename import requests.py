
import requests
import threading
from bs4 import BeautifulSoup
import sys

def fetch_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        return [link.get('href') for link in links]
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def process_urls(urls):
    threads = [] # List to hold threads
    results = [] # List to hold results
    def worker(url):
        links = fetch_links(url)
        results.extend(links)

    for url in urls:
        thread = threading.Thread(target=worker, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

urls = [  'https://www.nfl.com/', 'https://www.fanduel.com/' ]

all_links = process_urls(urls)
print(all_links)



    