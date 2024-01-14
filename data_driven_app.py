#imports required libraries for the GUI to work
from tkinter import*
import requests
import json

#creates Tk window
main = Tk()
main.geometry('500x400')
main.resizable(0,0)
main.title('Data-Driven App')

#accesses API data
url = f"https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_HvGNTos8FRpSkjoSb4qtWWD9Dd1znbgScG8ITnus"
response = requests.get(url)
data = response.json()

#stores currency exchange rates from API to text file
with open('python/Year 2/assessment_exercises/currency.txt', 'w') as file:
    json.dump(data, file, indent = 4)

#loads JSON text file as dictionary
with open('python/Year 2/assessment_exercises/currency.txt') as f:
    currency = json.load(f)

#home page
def home_page():
    delete_pages()

    home_frame = Frame(display_frame)

    Label(home_frame, text = "Welcome to", font = ('Georgia')).pack()
    Label(home_frame, text = "Currency Converter", font = ('Georgia', 20)).pack()
    Label(home_frame, text = "Convert USD currency with \nup-to-date exchange rates!", font = ('Georgia', 15)).pack(pady = 75)
    Label(home_frame, text = "This GUI makes use of the freecurrencyapi.com API", font = ('Georgia', 10)).pack(pady = 20, side = BOTTOM)

    home_frame.pack()

#instructions for user
def instructions_page():
    delete_pages()

    instructions_frame = Frame(display_frame)

    Label(instructions_frame, text = "Currency Converter", font = ('Georgia', 20)).pack()
    Label(instructions_frame, text = "Instructions", font = ('Georgia')).pack(pady = 10)
    Label(instructions_frame, text = "Insert USD currency in \nthe entry field at the top, \nselect the currency to convert to, \nthen click the button to convert.", font = ('Georgia', 15)).pack(pady = 70)
    Label(instructions_frame, text = "This GUI makes use of the freecurrencyapi.com API", font = ('Georgia', 10)).pack(side = BOTTOM)

    instructions_frame.pack()

#creates main page for currency conversion
def convert_page():
    delete_pages()

    #function for calculations
    def convert():
        #stores user input into variables
        base_currency = float(base_curr.get())
        convert_select = curr_select.get()
        #matches selected currency with appropriate exchange rate in the dictionary
        convert_currency = float(currency["data"][f'{convert_select}'])

        #calculates conversion
        convert_result = base_currency * convert_currency

        #changes text label to reflect output
        result_update = f"{convert_select} {convert_result}"
        result.configure(text = result_update)

    convert_frame = Frame(display_frame)

    Label(convert_frame, text = "Conversion Page", font = ('Georgia')).pack(pady = 20)

    #Label and entry field for user input
    Label(convert_frame, text = "Enter USD amount:", font = ('Georgia', 10)).pack(pady = 5)
    base_curr = Entry(convert_frame)
    base_curr.pack(pady = 5)

    #dropdown menu using OptionMenu for conversion selection
    Label(convert_frame, text = "Select conversion:", font = ('Georgia', 10)).pack(pady = 5)
    #accesses the JSON dictionary as a list to display available currencies in the API
    curr_list = list(currency["data"])
    curr_select = StringVar(main)
    curr_select.set("Select Currency")
    dropdown = OptionMenu(convert_frame, curr_select, *curr_list)
    dropdown.pack(pady = 5)
    
    #calls the convert() function on button click
    Button(convert_frame, text = "Convert", command = convert).pack(pady = 10)

    Label(convert_frame, text = "Conversion result:", font = ('Georgia', 10)).pack(pady = 10)
    result = Label(convert_frame, text = "", font = ('Georgia', 10))
    result.pack(pady = 20)

    convert_frame.pack()

#function to delete frame elements
def delete_pages():
    for frame in display_frame.winfo_children():
        frame.destroy()

#navbar frame
select_frame = Frame(main, bg = "#212121")

home_button = Button(select_frame, text = 'Home', command = home_page)
home_button.place(x = 10, y = 50)

instruction_button = Button(select_frame, text = 'Instructions', command = instructions_page)
instruction_button.place(x = 10, y = 100)

convert_button = Button(select_frame, text = 'Convert', command = convert_page)
convert_button.place(x = 10, y = 150)

select_frame.pack(side = LEFT)
select_frame.pack_propagate(False)
select_frame.configure(width = 120, height = 400)

#display frame
display_frame = Frame(main)

Label(display_frame, text = "Welcome to", font = ('Georgia')).pack()
Label(display_frame, text = "Currency Converter", font = ('Georgia', 20)).pack()
Label(display_frame, text = "Convert USD currency with \nup-to-date exchange rates!", font = ('Georgia', 15)).pack(pady = 75)
Label(display_frame, text = "This GUI makes use of the freecurrencyapi.com API", font = ('Georgia', 10)).pack(pady = 20, side = BOTTOM)

display_frame.pack(side = LEFT, pady = 20)
display_frame.pack_propagate(False)
display_frame.configure(width = 500, height = 400) 

main.mainloop()