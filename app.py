import tkinter as tk
from pytube import YouTube
from PIL import Image, ImageTk

class Gui:
    def __init__(self, master) -> None:
        self.master = master
        self.master.geometry('700x300')
        self.master.title('Mi descargadar de videos de YouTube')
        
        # Imagen tortuguita
        """self.img = tk.PhotoImage(file='Tortuguita.png')
        self.label = tk.Label(self.master, image=self.img)
        self.label.pack()"""
        # Image aun no es compatible con TK asi que lo teneme que convertir
        self.img = Image.open('./Tortuguita.png') 
        self.img = self.img.resize((300,200))
        
        # Frame imagen 
        self.frame_img = tk.Frame(self.master)
        self.frame_img.place(x=0, y=0)
        self.frame_img.config(bg='red', width=300, height=200)

        # ahora si es compatible usando el ImageTk
        self.img_tk = ImageTk.PhotoImage(self.img)
        # operaciones basicas, .resize((x,y), Image.ANTIALIAS) esto retorna una imagen 
        # por cierto esos cambios que se hacen se lo hace antes de que sean ImageTk
        # .rotate(x) donde x es en grados y de igual forma retorna una imagen 
        self.lbl_img = tk.Label(self.frame_img, image=self.img_tk)
        self.lbl_img.pack()

        # Frame info
        self.frame_info = tk.Frame(self.master)
        self.frame_info.place(x=301,y=0)
        self.frame_info.config(bg='yellow', width=400, height=200)

        self.lbl_url = tk.Label(self.frame_info, text='Ingrese la Url:', font=('Arial', 12), width=10)
        self.lbl_url.place(x=5,y=5)
        
        self.txt_url = tk.Entry(self.frame_info, width=40)
        self.txt_url.place(x=110,y=5)

        

if __name__ == '__main__':
    root = tk.Tk()
    my_gui = Gui(root)

    root.mainloop()
