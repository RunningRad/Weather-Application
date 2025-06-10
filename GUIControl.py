# Weather app that can tell you the weather when you enter a city and country name.

from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Gets the API key.
load_dotenv()  # Load from .env file

API_KEY = os.getenv('OPENWEATHER_API_KEY')

gui = Tk()

gui.title("Weather Around The World!")
gui.geometry('360x240')

introLabel = Label(gui, text="Enter a city and country name to find your location.")
introLabel.grid(column = 1, row = 0)

cityLabel = Label(gui, text="City:")
cityLabel.grid(column = 0, row = 1)

stateLabel = Label(gui, text="State:")
stateLabel.grid(column = 0, row = 2)

citySelector = Entry(gui)
citySelector.grid(column=1, row=1)

stateSelector = ttk.Combobox(gui, values = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Conneticut", "Delaware", "Florida", "Georgia",
                                                                             "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
                                                                             "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                                                                             "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
                                                                             "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"])
stateSelector.grid(column=1, row=2)


def findData():
    if citySelector.get() == "":
        print("Please enter a city for search for.")
        return
    elif stateSelector.get() == "":
        print("Please select a state to look in.")
        return
    print("Searching at " + citySelector.get() + ", " + stateSelector.get() + ".")

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{citySelector.get()},{stateSelector.get()},{"US"}",
        "appid": API_KEY,
        "units": "imperial"
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        vibes = data["main"]["feels_like"]
        speed = data["wind"]["speed"]
        humid = data["main"]["humidity"]


        temperatureLabel = Label(gui, text = f"The current temperature is: {temperature}°F.") 
        temperatureLabel.grid(column = 1, row = 4)
        feelsLikeLabel = Label(gui, text = f"The current  feels like: {vibes}°F.") 
        feelsLikeLabel.grid(column = 1, row = 5)
        cloudCover = Label(gui, text = f"The current weather is: {weather}.") 
        cloudCover.grid(column = 1, row = 6)
        windSpeed = Label(gui, text = f"The current wind speed is: {speed}.") 
        windSpeed.grid(column = 1, row = 7)
        humidity = Label(gui, text = f"The humidity percentage is {humid}%.") 
        humidity.grid(column = 1, row = 8)
    else:
        print(f"Error {response.status_code}: {data.get('message', 'Unknown error')}")

enterSelection = Button(gui, text= "Press here to confirm location", command=findData)
enterSelection.grid(column = 1, row = 3)

gui.mainloop()