import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(URL):
  page = requests.get(URL)
  bowl_of_soup = BeautifulSoup(page.content, "html.parser")
  citations_needed = bowl_of_soup.find_all("a", title="Wikipedia:Citation needed")
  return len(citations_needed)


def get_citations_needed_report(URL):
  page = requests.get(URL)
  bowl_of_soup = BeautifulSoup(page.content, "html.parser")
  citations_needed = bowl_of_soup.find_all("a", title="Wikipedia:Citation needed")
  for citation in citations_needed:
    print(f"Citation needed for '{citation.text}'")

total_count = get_citations_needed_count("https://en.wikipedia.org/wiki/Filipinos")
print(total_count)