from django.http import HttpResponse
from .scraping import scrape_website  # Import your scraper function

def scrape_view(request):
    data = scrape_website()
    if data:
        return HttpResponse(f'Scraping successful! Data: {data}')
    else:
        return HttpResponse('Failed to scrape the website.')
