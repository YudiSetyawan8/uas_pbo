
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\py_code\pbo_uas\guiii\main_bimbingan_mahasiswa\bimbingan_mahasiswa\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def bimbingansiswa():
    BimbinganMahasiswa()
#window = Tk()

#window.geometry("1005x623")
#window.configure(bg = "#313131")

class BimbinganMahasiswa(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.canvas = Canvas(
            self,
            bg = "#313131",
            height = 666,
            width = 1099,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("Image_3.png"))
        
        image_1 = self.canvas.create_image(
            502.0,
            19.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            499.0,
            291.0,
            image=self.image_image_2
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("mdlsis"),
            activebackground="#313131",
            relief="flat"
        )
        button_1.place(
            x=401.0,
            y=548.0,
            width=203.0,
            height=57.0
        )

#window.resizable(False, False)
#window.mainloop()