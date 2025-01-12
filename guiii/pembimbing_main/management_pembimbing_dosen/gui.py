
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
#from guiii.pembimbing_main.modul_pembimbing_dosen.gui import ModulPembimbingDosen
#from guiii.pembimbing_main.main_mng import MainMNG
#from guiii.management_pembimbing_dosen.main_mng import navigate


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\py_code\pbo_uas\guiii\pembimbing_main\management_pembimbing_dosen\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#def nav():
    #MainMNG


#window = Tk()

#window.geometry("1005x623")
#window.configure(bg = "#313131")
def managementpembimbingdosen():
    ManagementPembimbingDosen()


class ManagementPembimbingDosen(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(bg="#313131")
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
        self.image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            502.0,
            292.0,
            image=self.image_1
        )

        self.image_image_2 = PhotoImage(file=relative_to_assets("Image_3.png"))
        image_2 = self.canvas.create_image(
            502.0,
            19.0,
            image=self.image_image_2
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("mdl"),
            activebackground="#313131",
            relief="flat"
        )
        button_1.place(
            x=401.0,
            y=557.0,
            width=203.0,
            height=57.0
        )

        #self.windows = {
            #"mdl": ModulPembimbingDosen(self)
        #}

    #def nav(self, caller, name):
        # Place the sidebar on respective button
        # Hide all screens
        #for window in self.windows.values():
            #window.place_forget()

        # Set ucrrent Window
        #self.current_window = self.windows.get(name)

        # Show the screen of the button pressed
        #self.windows[name].place(x=101, y=34, width=1099.0, height=666.0)
        #if self.current_window:
            #self.current_window.place(x=101, y=34, width=1099.0, height=666.0)
            #self.current_window.tkraise()
        #else:
            #print(f"Window with name {name} not found")  # Debug statement

     


#window.resizable(False, False)
#window.mainloop()
