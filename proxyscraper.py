import requests
from bs4 import BeautifulSoup

def get_proxies(url):
    # Fetch the page with the list of free proxies
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all of the rows in the table on the page
    rows = soup.find("table").tbody.find_all("tr")

    # Extract the IP addresses and ports of the proxies from the rows
    proxies = []
    for row in rows:
        cols = row.find_all("td")
        ip_address = cols[0].text
        port = cols[1].text
        proxy = f"{ip_address}:{port}"
        proxies.append(proxy)

    return proxies

urls = [
    "https://www.sslproxies.org/",
    "https://www.us-proxy.org/",
    "https://free-proxy-list.net/"
]

proxies = []
for url in urls:
    proxies += get_proxies(url)


f = open("proxy.txt", "a")
for i in proxies:
    f.write(i)
    f.write("\n")
for g in proxies:
    print(f"Found Proxy: {g}")
