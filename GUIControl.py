# Weather app that can tell you the weather when you enter a city and country name.

from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

gui = Tk()

gui.title("Weather Around The World!")
gui.geometry('360x720')

introLabel = Label(gui, text="Enter a city and country name to find your location.")
introLabel.grid()

citySelector = Entry(gui)
citySelector.grid()

stateSelector = ttk.Combobox(gui, values = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Conneticut", "Delaware", "Florida", "Georgia",
                                                                             "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
                                                                             "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                                                                             "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
                                                                             "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"])
stateSelector.grid()


def findData():
    if citySelector.get() == "":
        print("Please enter a city for search for.")
        return
    elif stateSelector.get() == "":
        print("Please select a state to look in.")
        return
    print("Searching at " + citySelector.get() + ", " + stateSelector.get() + ".")

enterSelection = Button(gui, text= "Press here to confirm location", command=findData)
enterSelection.grid()

gui.mainloop()