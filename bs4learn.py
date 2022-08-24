from bs4 import BeautifulSoup
import requests

page = requests.get('https://realpython.github.io/fake-jobs/')

soup = BeautifulSoup(page.content, "html.parser")

# results = soup.find(id = 'ResultsContainer')
# job_results = results.find_all('div', class_ = 'card-content')

# for job_result in job_results:
#     title_element = job_result.find("h2", class_="title")
#     company_element = job_result.find("h3", class_="company")
#     location_element = job_result.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()
element = soup.find('p', 'subtitle')

print(element.text.strip())
