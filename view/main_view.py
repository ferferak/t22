from tkinter import *
from view.components.components import Table, LabelAndEntry

class MainView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")
        self.window.title("Financial Records")

        self.person_entry = LabelAndEntry(self.window, "Person:", 50, 50)
        self.type_entry = LabelAndEntry(self.window, "Type:", 50, 100)
        self.amount_entry = LabelAndEntry(self.window, "Amount:", 50, 150, data_type="float")
        self.date_entry = LabelAndEntry(self.window, "Date (YYYY-MM-DD):", 50, 200)
        self.time_entry = LabelAndEntry(self.window, "Time (HH:MM):", 50, 250)

        self.table = Table(self.window, ["ID", "Person", "Type", "Amount", "Date", "Time"], [50, 100, 80, 80, 100, 80], 50, 350)

        Button(self.window, text="Add", command=self.add_record).place(x=50, y=300)
        Button(self.window, text="Edit").place(x=150, y=300)
        Button(self.window, text="Remove").place(x=250, y=300)
        Button(self.window, text="Save").place(x=350, y=300)

    def add_record(self):
        pass

    def run(self):
        self.window.mainloop()
