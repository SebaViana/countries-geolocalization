import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkintermapview import TkinterMapView

class Country:
    def __init__(self, short, name, latitude, longitude):
        self.short = short
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def printInfo(self):
        return(self.short, self.name, self.latitude, self.longitude)
        
df = pd.read_excel(r"DATA/countries.xls")
print(df) #


rows = list(range(0,len(df)))
countries = []
countries_names = []
for row in rows:
    short = df.iat[row, 0]
    latitude = df.iat[row, 1]
    longitude = df.iat[row, 2]
    name = df.iat[row, 3]
    country = Country(short, name, latitude, longitude)
    countries.append(country)
    countries_names.append(country.name)

print(countries[6].name)


#for i in countries:
#    print(i.printInfo())

#print(countries)

def check_input(event):
    value = event.widget.get()

    if value == '':
        combo_box['values'] = countries_names
    else:
        data = []
        for item in countries_names:
            if value.lower() in item.lower() and item.lower().startswith(value):
                data.append(item)

        combo_box['values'] = data
    

def update_popup():
    messagebox.showwarning(title="Warning", message="{} has been added".format(combo_box.get()))

master = Tk()
master.geometry("400x100")

w = Label(master, text="Country: ")
w.grid(column=1, row=1)



combo_box = ttk.Combobox(master)
combo_box['values'] = countries_names
combo_box.bind('<KeyRelease>', check_input)
#default_text = StringVar(master)
#default_text.set("   Please, select a country   ")
#combo_box = OptionMenuw = OptionMenu(master, default_text, *countries_names)
combo_box.grid(column=2, row=1)

w = Label(master, text="❗You can write to filter the list")
w.grid(column=3, row=1)

#----------------------

def openMap():
    selected_country = combo_box.get()

    if selected_country in countries_names:
        newWindow = Toplevel(master)

        newWindow.title(selected_country)

        newWindow.geometry("600x400")

        map_widget = TkinterMapView(newWindow, width=600, height=400, corner_radius=0)
        map_widget.grid(column=1, row= 10)


        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=12)
        
        map_widget.set_address(selected_country)
        map_widget.set_zoom(7)
    else:
        if selected_country == "":
            messagebox.showwarning(title="Warning", message="No option was given")
        else:
            messagebox.showwarning(title="Warning", message="{} is not a valid option, please, select a country from the drop down list.".format(selected_country))
    

#-------------------

run_button = Button(master, bg= "darkgray", text='Run', command=openMap)
run_button.grid(column=3, row=2)



mainloop()