from tkinter import *
root = Tk()
root.title("Sales Tuple")
root.geometry("900x500")
root.configure(background="light blue")

month = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
         "October", "November", "December") 

profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

heading = Label(root, text = "Maximum & Minimum Sales Months")
Labelmonth = Label(root, text = "Months- " + str(month))
Labelprofits = Label(root, text = "Profits- " + str(profits))

maxmonth = Label(root)
minmonth = Label(root)

def profitmax():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    print(max_profit_index)
    max_profit_month = month[max_profit_index]
    maxmonth["text"] = "A maximum profit of " + str(max_profit) + " was recorded in the month of " + str(max_profit_month)

def profitmin():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    print(min_profit_index)
    min_profit_month = month[min_profit_index]
    minmonth["text"] = "A minimum profit of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month)

btnmax = Button(root, text = "Show max profitable Month- ", command = profitmax, bg = "blue", fg = "white")
btnmin = Button(root, text = "Show min profitable Month- ", command = profitmin, bg = "red", fg = "black")

heading.place(relx = 0.5, rely = 0.1, anchor=CENTER)

Labelmonth.place(relx = 0.5, rely = 0.2, anchor=CENTER)
Labelprofits.place(relx = 0.5, rely = 0.3, anchor=CENTER)

btnmax.place(relx = 0.5, rely = 0.4, anchor=CENTER)
maxmonth.place(relx = 0.5, rely = 0.5, anchor=CENTER)

btnmin.place(relx = 0.5, rely = 0.6, anchor=CENTER)
minmonth.place(relx = 0.5, rely = 0.7, anchor=CENTER)

root.mainloop()