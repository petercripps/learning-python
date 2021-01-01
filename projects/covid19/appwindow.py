# Creates a GUI
# # See http://effbot.org/tkinterbook/
from tkinter import *
from time import strftime 
from readargs import init_argdict
from covid19 import run_covid19
from readdata import country_data

rate = [
    ["Absolute","absolute"],
    ["Per hundred thousand","hundred"],
    ["Per million","million"],
    ["Change over previous","change"]]

measure = [["Deaths","Deaths"],
    ["Confirmed","Confirmed"],
    ["Recovered","Recovered"]]

operation = [["Information","info"], 
    ["Rate of change","rate"]]

country_group = [["None","none"],
    ["G7","g7"], 
    ["G20","g20"],
    ["EU","eu"]]

g7_countries = ["US","Japan","Canada","France","Germany","Italy","United Kingdom"]
g20_countries = ["India","US","South Korea","China","Canada","France","Germany","Italy","United Kingdom","Brazil","Russia","Indonesia","Mexico","Japan","Turkey","South Africa","Argentina","Saudi Arabia","Australia"]
eu_countries = ["Austria","Belgium","Bulgaria","Croatia","Cyprus","Czechia","Denmark","Estonia","Finland","France","Germany","Greece","Hungary","Ireland","Italy","Latvia","Lithuania","Luxembourg","Malta","Poland","Portugal","Netherlands","Romania","Slovakia","Slovenia","Spain","Sweden"]

countries = country_data()

debug_mode = True

# Create a menubar
def create_menubar(window): 
    menubar = Menu(window) 

    # Adding File Menu and commands 
    file = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='File', menu = file) 
    file.add_command(label ='New File', command = None) 
    file.add_command(label ='Open...', command = None) 
    file.add_command(label ='Close', command = None)
    file.add_command(label ='Save', command = None) 
    file.add_separator() 
    file.add_command(label ='Exit', command = window.destroy) 

    # Adding Edit Menu and commands 
    edit = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Edit', menu = edit) 
    edit.add_command(label ='Cut', command = None) 
    edit.add_command(label ='Copy', command = None) 
    edit.add_command(label ='Paste', command = None) 
    edit.add_command(label ='Select All', command = None) 
    edit.add_separator() 
    edit.add_command(label ='Find...', command = None) 
    edit.add_command(label ='Find again', command = None) 

    # Adding Help Menu 
    help_ = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Help', menu = help_) 
    help_.add_command(label ='Tk Help', command = None) 
    help_.add_command(label ='Demo', command = None) 
    help_.add_separator() 
    help_.add_command(label ='About Tk', command = None) 

    # Display Menu 
    window.config(menu = menubar) 

# Add buttons to window
def add_buttons(window):
    Button(window, text="Submit",command = submit, padx=5,pady=5).grid(row=10,column=0, sticky=W)
    Button(window, text="Clear",command = clear, padx=5,pady=5).grid(row=10,column=1, sticky=W)
    Button(window, text="Exit", command = window.destroy, padx=5,pady=5).grid(row=10,column=2, sticky=W)

# Add radio buttons in a group to window, return the first so it can be reset later
def add_radio(window, choices, cmd, opt, col_num, row_num):
    first = True
    for choice in choices:
        b = Radiobutton(window,
            text=choice[0],
            variable=opt, 
            command=cmd,
            value=choice[1])
        b.grid(padx=5, pady=5, row=row_num, column=col_num, sticky=W)
        row_num += 1
        if first:
            # Select the first button
            b.select()
            # Save the first button so it can be reset later.
            b1 = b
            first = False
    return b1

# Add a listbox of countries
def add_listbox(window):
    lb = Listbox(window, selectmode=EXTENDED, width=10)
    lb.grid(column=3, row=0, rowspan=4)
    count = 0
    for entry in countries:
        lb.insert(count, entry)
        count +=1
    return lb

# command for when rate selected
def cmd_rate():
   if debug_mode: 
        print("You selected the rate option " + opt_rate.get())
   return opt_rate.get()

# command for when operation selected
def cmd_operation():
   if debug_mode:
       print("You selected the operation option " + opt_operation.get())
   return opt_operation.get()

# command for when measure selected
def cmd_measure():
   if debug_mode:
       print("You selected the measure option " + opt_measure.get())
   return opt_measure.get()

# command for when country group selected
def cmd_country_group():
    c_group = opt_country_group.get()
    if debug_mode:
       print("You selected the country group option: " + c_group)
    # Clear whatever was previously selected
    lb.select_clear(0, last=END)
    if c_group == "g7":
        members = g7_countries
    elif c_group == "g20":
        members = g20_countries
    elif c_group == "eu":
        members = eu_countries
    
    # Create selections for member countries
    if c_group != "none":     
        i = 0
        for country in countries:
            if country in members:
                lb.select_set(i, last=None)
            i += 1
    return c_group

# command for when submit button selected
def submit():
    # read everything into the arguments dictionary
    argdict = init_argdict()
    argdict["fdate"] = date1.get()
    argdict["tdate"] = date2.get()
    argdict["rate"] = cmd_rate()
    argdict["operation"] = cmd_operation()
    argdict["measure"] = cmd_measure()
    if check_graph.get() == 1:
        argdict["graph"] = True
    i = 0
    while i < len(lb.curselection()):
        argdict["countries"].append(countries[lb.curselection()[i]])
        i += 1
    if debug_mode:
        print(argdict)
    # run it
    run_covid19(argdict)

# command for when clear button selected
def clear():
    if debug_mode:
        print("Clearing...")
    e1.delete (0, len(e1.get()))
    e2.delete (0, len(e2.get()))
    b_rate.select()
    b_operation.select()
    b_measure.select()
    b_country_group.select()
    cb.deselect()
    lb.select_clear(0, last=END)

# Creating main tkinter window 
window = Tk()
window.geometry("700x400")
window.title('Covid-19 Data Analyser')

# Variables for collecting inputs
opt_rate = StringVar()
opt_operation = StringVar()
opt_measure = StringVar()
opt_country_group = StringVar()
date1 = StringVar()
date2 = StringVar()
check_graph = IntVar()

# Create the menu bar
create_menubar(window)

# add the entry fields
Label(window, text='Enter date (start)', justify=LEFT).grid(column=0, row=0, sticky=N+W)
e1=Entry(window,justify=LEFT, textvariable=date1)
e1.grid(column=1, row=0, sticky=N+W)
Label(window, text='Enter date (end)', justify=LEFT).grid(column=0, row=1, sticky=N+W)
e2=Entry(window,justify=LEFT, textvariable=date2)
e2.grid(column=1, row=1, sticky=N+W)

# add a countries listbox
lb = add_listbox(window)

# add the radio buttons
Label(window, text='Enter a selection choice:').grid(column=0, row=2)
b_operation = add_radio(window, operation, cmd_operation, opt_operation, 0, 3)
b_measure = add_radio(window, measure, cmd_measure, opt_measure, 1, 3)
b_rate = add_radio(window, rate, cmd_rate, opt_rate, 2, 3)
b_country_group = add_radio(window, country_group, cmd_country_group, opt_country_group, 5, 0)

# add a check button
Label(window, text='Select if you want a graph:', justify=LEFT).grid(column=0, row=7, sticky=N+W)
cb = Checkbutton(window, text = "Graph", variable=check_graph, justify=LEFT)
cb.grid(column=0, row=8, sticky=W)

# add the buttons
Label(window, text='', justify=LEFT).grid(column=0, row=9, sticky=N+W)
add_buttons(window)
Label(window, text='', justify=LEFT).grid(column=0, row=11, sticky=N+W)

# run it
window.mainloop() 