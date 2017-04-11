# GUI for city information of California
from Tkinter import *
import collections
import json

# initialising fields for gui
fields = 'Longitude', 'Latitude', 'County'
entries = {}
ca_dict = {}

# method to make a form for 3 fields
def makeform(root, fields):
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field + ": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=BOTTOM, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries

# method to populate form entries with corresponding values
def select(a):
    city_name = var.get()
    (county, lat, lng) = ca_dict[city_name]

    # delete the previous value and insert new value if it is not null
    entries['County'].delete(0, END)
    if county :
        entries['County'].insert(0, county)
    entries['Latitude'].delete(0, END)
    if lat:
        entries['Latitude'].insert(0, lat)
    entries['Longitude'].delete(0, END)
    if lng:
        entries['Longitude'].insert(0, lng)


if __name__ == '__main__':

    # parsing and saving json data into a dictionary with key/value pairs as city names/full county name, latitude, longitude
    with open('ca.json') as data_file:
        all_cities = json.load(data_file)

    for each_city in all_cities:
        ca_dict[each_city["name"]] = [each_city["full_county_name"], each_city["primary_latitude"],
                                      each_city["primary_longitude"]]

    # sorting the dictionary based on key(city names)
    ca_dict = collections.OrderedDict(sorted(ca_dict.items()))

    #To create GUI
    root = Tk()
    # use width x height + x_offset + y_offset
    root.geometry("%dx%d+%d+%d" % (600, 130, 100, 100))
    root.title("California City Information")
    var = StringVar(root)
    # initial value of drop down menu set to empty space
    var.set('')
    choices = list(ca_dict.keys())

    row1 = Frame(root)
    label1 = Label(row1, width=22, text="City:", anchor='w')
    # creating drop down menu for all the cities
    option = OptionMenu(row1, var, *choices, command=select)
    row1.pack(fill=X, padx=5, pady=5)
    label1.pack(side=LEFT)
    option.pack(side=RIGHT, expand=YES, fill=X)

    # make form for remaining 3 fields
    ents = makeform(root, fields)

    root.mainloop()