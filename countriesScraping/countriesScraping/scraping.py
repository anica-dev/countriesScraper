import requests
from bs4 import BeautifulSoup

def scrape_website():
    url = "https://www.data.gv.at/"  # Replace with the website you want to scrape
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract the website title as an example
        title = soup.title.string if soup.title else "No Title Found"
        return {"url": url, "title": title}
    else:
        return {"error": f"Failed to fetch {url}, status code: {response.status_code}"}
