import requests
from bs4 import BeautifulSoup

from listing import Listing


def sendRequest(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    pagination = soup.find('ul', class_='pages_ul mt30 mb30')
    pages = pagination.find_all('a')

    hrefs = [page.get('href') for page in pages if page.get('href')]

    seen = set()
    for href in hrefs:
        if href not in seen:
            seen.add(href)
            responsePaginated = requests.get(href)
            print(responsePaginated.status_code)
            scrapeJobs(responsePaginated)



def scrapeJobs(response):
    soup = BeautifulSoup(response.text, 'html.parser')

    job_lists = soup.find_all('a', class_='list_a can_visited list_a_has_logo')

    for job_list in job_lists:

        href = job_list.attrs['href']
        logo = job_list.find('img')['src'] if job_list.find('img') else ''
        title = job_list.find('h3').get_text(strip=True) if job_list.find('h3') else ''
        salary_amount = job_list.find('span', class_='salary_text').get_text(strip=True) if job_list.find('span', class_='salary_text') else ''
        salary_calculation = job_list.find('span', class_='salary_calculation').get_text(strip=True) if job_list.find('span', class_='salary_calculation') else ''
        location = job_list.find('span', class_='list_city').get_text(strip=True) if job_list.find('span', class_='list_city') else ''
        posted = job_list.find('span', class_='txt_list_2').get_text(strip=True) if job_list.find('span', class_='txt_list_2') else ''

        l = Listing(href, logo, title, salary_amount, salary_calculation, location, posted)

    return l

