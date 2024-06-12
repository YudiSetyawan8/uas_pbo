
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkPDFViewer import tkPDFViewer as pdf
import chardet
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Toplevel
from tkinter.ttk import Treeview
import controller as db_controller

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
    def __init__(self, parent, user_npm, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.user_npm =  user_npm
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

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_3 = self.canvas.create_image(
            62.0,
            582.0,
            image=self.image_image_3
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
            x=780.0,
            y=555.0,
            width=203.0,
            height=57.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            activebackground="#313131",
            relief="flat"
        )
        button_3.place(
            x=104.0,
            y=553.0,
            width=94.0,
            height=60.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            activebackground="#313131",
            relief="flat"
        )
        button_4.place(
            x=310.0,
            y=553.0,
            width=94.0,
            height=60.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            activebackground="#313131",
            relief="flat"
        )
        button_5.place(
            x=207.0,
            y=555.0,
            width=94.0,
            height=60.0
        )
        self.columns = {
            "id_detail": ["id_detail", 164],
            "npm": ["npm", 164],
            "tanggal": ["npm", 164],
            "konsultasi_pembimbing": ["tanggal", 164],
            "status_validasi": ["status_validasi", 163],
            "file_skripsi": ["file_skripsi", 164],
        }
        self.treeview = Treeview(
            self,
            columns=list(self.columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
            # ="#FFFFFF",
            # fg="#5E95FF",
            # font=("Montserrat Bold", 18 * -1)
        )

        for idx, txt in self.columns.items():
            self.treeview.heading(idx, text=txt[0])
            # Set the column widths
            self.treeview.column(idx, width=txt[1])

        self.treeview.place(x=15.0, y=44.0, width=983.0, height=494.0)
        self.handle_refresh()
        self.treeview.bind("<ButtonRelease-1>", self.on_treeview_click)

    def handle_refresh(self):
        self.treeview.delete(*self.treeview.get_children())
        self.room_data = db_controller.view_bimbingan(self.user_npm)

        for row in self.room_data:
            if isinstance(row[5], bytes):
                detected_encoding = self.detect_encoding(row[5])
                if detected_encoding:
                    try:
                        row = list(row)
                        row[5] = row[5].decode(detected_encoding)
                    except UnicodeDecodeError as e:
                        # Log the decoding error
                        logging.error(f"Error decoding BLOB data: {e}")
                        row = list(row)  # Convert to list to modify
                        row[5] = "Decoding Error"
                        row = tuple(row)  # Convert back to tuple
                else:
                    row = list(row)  # Convert to list to modify
                    row[5] = "Unknown Encoding"
                    row = tuple(row)  # Convert back to tuple
            self.treeview.insert("", "end", values=row)


    def detect_encoding(self, blob_data):
        result = chardet.detect(blob_data)
        return result['encoding']        

    def on_treeview_click(self, event):
        selected_item = self.treeview.selection()
        if not selected_item:
            return

        item = self.treeview.item(selected_item)
        values = item['values']

        # Assuming 'progress_skripsi' is the 10th column (index 9)
        file_skripsi = values[5]

        # Open the PDF file if progress_skripsi contains the path or filename
        if file_skripsi:
            self.open_pdf(file_skripsi)


    def open_pdf(self, pdf_path):
        pdf_window = Toplevel(self)
        pdf_window.title("PDF Viewer")
        pdf_window.geometry("800x600")

        pdf_viewer = pdf.ShowPdf()
        pdf_display = pdf_viewer.pdf_view(pdf_window, pdf_location=pdf_path, width=100, height=100)
        pdf_display.pack(expand=True, fill='both')       





#window.resizable(False, False)
#window.mainloop()
