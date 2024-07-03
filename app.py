#Import libraries
from bs4 import BeautifulSoup
import requests

def search(state, city):
    #Website used for data
    url = f"https://www.wunderground.com/weather/us/{state.lower()}/{city.lower()}"

    #Get the response code for the website
    page = requests.get(url)

    #Gets the html for the website 
    soup = BeautifulSoup(page.content, 'html.parser')

    #Select the class and p element that provides data
    temperature = soup.select(".wu-value-to")[6].text
    condition = soup.select("p")[8].text

    #print values
    return temperature, condition
