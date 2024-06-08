
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\py_code\pbo_uas\guiii\main_logbook\view_logbook\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def viewlgbk():
    ViewLogbook()
#window = Tk()

#window.geometry("1005x623")
#window.configure(bg = "#303030")

class ViewLogbook(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(bg="#313131")
        self.canvas = Canvas(
            self,
            bg ="#313131",
            height = 666,
            width = 1099,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            15.0,
            47.0,
            990.0,
            539.0,
            fill="#D9D9D9",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("inptlgbk"),
            activebackground="#313131",
            relief="flat"
        )
        button_1.place(
            x=401.0,
            y=560.0,
            width=203.0,
            height=57.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_1 = self.canvas.create_image(
            502.0,
            27.0,
            image=self.image_image_1
        )
        

#window.resizable(False, False)
#window.mainloop()