"""import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--len", help="Lenght of the board", type=int, default=20)
parser.add_argument("--color", help="Color style", type=str, default="Smooth")
parser.add_argument("--algo", help="Astar or Dijkstra", type=str, default="A*")
parser.add_argument("--diag", help="Unauthorize Diagonals", type=bool, default=True)

args = parser.parse_args()
"""
import tkinter as tk
from tkinter import ttk


class Args:
    def __init__(self):
        self.algo = None
        self.len = None
        self.diag = None
        self.color = None
        # self.load()

    def load(self):
        args = self.__getArgs()
        try:
            self.algo = args["algo"]
            self.len = int(args["len"])
            self.diag = args["diag"] == "Yes"
            self.color = args["color"]
        except:
            self.load()

    def __getArgs(self):
        args = {}

        def runApp():
            app = tk.Tk()
            app.geometry("190x300")
            app.title("Args Form")

            ################## algorithm ##################

            label_1 = tk.Label(app, text="Choose your algorithm")
            label_1.grid(column=0, row=0)

            algo_combobox = ttk.Combobox(
                app, values=["A*", "Dijkstra"], state="readonly"
            )
            algo_combobox.grid(column=0, row=1)
            algo_combobox.current(0)

            ################## lenght ##################

            label_2 = tk.Label(app, text="Size of the grid")
            label_2.grid(column=0, row=2)

            lenght_entry = ttk.Entry(app)
            lenght_entry.insert(tk.END, "20")
            lenght_entry.grid(column=0, row=3)

            ################## diagonals ##################

            label_3 = tk.Label(app, text="Authorize diagonals ?")
            label_3.grid(column=0, row=4)

            diag_combobox = ttk.Combobox(app, values=["Yes", "No"], state="readonly")
            diag_combobox.grid(column=0, row=5)
            diag_combobox.current(0)

            ################## colors ##################

            label_4 = tk.Label(app, text="Style")
            label_4.grid(column=0, row=6)

            color_combobox = ttk.Combobox(
                app, values=["Smooth", "Strong"], state="readonly"
            )
            color_combobox.grid(column=0, row=7)
            color_combobox.current(0)

            ################## validation ##################
            def callBackFunc():
                args["algo"] = algo_combobox.get()
                args["len"] = int(lenght_entry.get())
                args["diag"] = diag_combobox.get()
                args["color"] = color_combobox.get()
                app.destroy()

            validate_button = ttk.Button(app, text="Run !", command=callBackFunc)
            validate_button.grid(column=0, row=8)

            app.mainloop()

        runApp()

        return args

    def __str__(self):
        return f"algo: {self.algo}, len: {self.len}, diag: {self.diag}, color: {self.color}"


args = Args()
# print(args)

