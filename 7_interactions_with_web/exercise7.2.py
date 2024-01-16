#!/usr/bin/python3
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re 
""" date_after=input("Give date after (in YYYY-MM-DD format): ")
print("\n")
date_before=input("Give date before (in YYYY-MM-DD form): ")
print("\n")
print("Species groups: [1] Birds | [2] Mammals | [3] Reptiles and amphibians | [4] Butterflies")
nr_species_group=input("Give number of species group: ")
print("\n")
print("Country division: [20] Vlaams-Brabant | [14] Limburg | [15] West-Vlaanderen | [16] Oost-Vlaanderen | [17] Antwerpen")
nr_country_division=input("Give number of province: ")
print("\n")
print("Rarities: [1] >=common | [2] >=relatively common | [3] >= rare | [4] very rare")
nr_rarity=input("Give number of rarity: ")

print(date_after, date_before, nr_species_group, nr_country_division, nr_rarity)



url="https://waarnemingen.be/photos/?date_after={}&date_before={}&species=&species_group={}&country_division={}&rarity={}&search=&likes=&user=&location=&sex=&type=&life_stage=&activity=&method=".format(date_after,date_before,nr_species_group, nr_country_division,nr_rarity) """

url="https://waarnemingen.be/photos/?date_after=2021-08-07&date_before=2021-09-09&species=&species_group=4&country_division=20&rarity=3&search=&likes=&user=&location=&sex=&type=&life_stage=&activity=&method="
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
data_content=response.read()
soup = BeautifulSoup(data_content, 'html.parser')
#print(soup.prettify())

tag_figure = soup.figure
Image=(tag_figure.find("a", class_="lightbox-gallery-image"))
Image_link=Image.get('href')
print("Image: {}".format(Image_link))
species=(tag_figure.find("span", class_="species-common-name"))
common_name=species.text
print("Species common name: {}".format(common_name))
name=(tag_figure.find("i", class_="species-scientific-name"))
scientific_name=name.text
print("Species scientific name: {}".format(scientific_name))
#print(tag_figure)
location=(tag_figure.find_all("a"))
#print(location)
for loc in location:
    if "locations" in loc.get('href'):
        location_name=loc.text
        print("the location: {} ".format(location_name))
