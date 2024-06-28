from bs4 import BeautifulSoup
import requests

state = input("Enter the state abbreviation of your location: ")
city = input("Enter the name of the city of your location: ")

url = f"https://www.wunderground.com/weather/us/{state.lower()}/{city.lower()}"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

temperature = soup.select(".wu-value-to")[6].text
condition = soup.select("p")[8].text

print(temperature)
print(condition)
