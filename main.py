import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


profile_name = []
company_name = []
locations = []
details = []

for i in range(1, 18):
    
    url = f"https://internshala.com/internships/computer%20science-internship/page-{i}"

    page = requests.get(url)

    soup = bs(page.content, 'html.parser')

    p = soup.find('h3',class_="heading_4_5 profile")

    cp = soup.find('div', class_='company_and_premium')

    l = soup.find('div', id="location_names")

    start_date = soup.find('div', class_="internship_other_details_container")



    for data in soup.findAll('div', class_='internship_meta'):
        profile = data.find('h3', class_='heading_4_5 profile')
        company = data.find('div', class_='company_and_premium')
        location = data.find('div', id='location_names')
        detail = data.find('div', class_='internship_other_details_container')

        profile_name.append(profile.text.strip() if profile else None)
        company_name.append(company.text.strip() if company else None)
        locations.append(location.text.strip() if location else None)
        details.append(detail.text.strip() if detail else None)

    print(f"{i} is Executed")

print(len(profile_name))
print(len(company_name))
print(len(locations))
print(len(details))




df = pd.DataFrame({'Profile Name': profile_name, 'Company Name': company_name, 'Locations': locations, 'Details': details})
df.to_excel('InternShala.xlsx', index=True)


