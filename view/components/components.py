from tkinter import *
import tkinter.ttk as ttk

class LabelAndEntry:
    def __init__(self, window, text, x, y, distance=80, data_type="str", state=None):
        Label(window, text=text).place(x=x, y=y)

        match data_type:
            case "str":
                self.variable = StringVar()
            case "int":
                self.variable = IntVar()
            case "float":
                self.variable = DoubleVar()
            case _:
                self.variable = StringVar()

        Entry(window, textvariable=self.variable, state=state).place(x=x + distance, y=y)

class Table:
    def __init__(self, window, headings, widths, x, y):
        columns = list(range(len(headings)))
        self.table = ttk.Treeview(window, columns=columns, show="headings")

        for i in columns:
            self.table.heading(i, text=headings[i])
            self.table.column(i, width=widths[i])

        self.table.place(x=x, y=y)

    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

    def show_data(self, data_list):
        self.clear_table()
        for item in data_list:
            self.table.insert("", END, values=item.to_tuple())
