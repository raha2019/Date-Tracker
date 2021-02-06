import tkinter as tk
from tkinter import ttk
from tkcalendar import *

from datetime import datetime

def calculateDateDifference(*args):
    try:  
        date = datetime.strptime(cal.get_date(), "%m/%d/%y").date()
        currentDate = datetime.now().date()
        if date < currentDate:
            delta = currentDate - date
            daysRemain.config(text="Days in the past: " + str(delta.days))
        elif date > currentDate:
            delta = date - currentDate
            daysRemain.config(text="Days Remaining: " + str(delta.days))
    except ValueError:
        pass




root = tk.Tk()
root.title("Date Tracker")
root.geometry("300x200")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

daysRemain = ttk.Label(frame, text="")
daysRemain.pack()

cal = Calendar(root, selectmode="day", year=2021, month=2, day=3)
cal.pack(pady=20)

button1 = ttk.Button(frame, text="Calculate", command=calculateDateDifference)

button1.pack()

root.mainloop()
