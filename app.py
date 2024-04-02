import tkinter as tk
from pytube import YouTube
from PIL import Image, ImageTk

class Gui:
    def __init__(self, master) -> None:
        self.master = master
        self.master.geometry('1000x700')
        self.master.title('Mi descargadar de videos de YouTube')
        
        # Imagen tortuguita
        """self.img = tk.PhotoImage(file='Tortuguita.png')
        self.label = tk.Label(self.master, image=self.img)
        self.label.pack()"""
        


if __name__ == '__main__':
    root = tk.Tk()
    my_gui = Gui(root)

    root.mainloop()
