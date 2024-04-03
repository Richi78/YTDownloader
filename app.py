import tkinter as tk
from pytube import YouTube
from PIL import Image, ImageTk
from pytube import Playlist
from tkinter import filedialog as fd
from tkinter import messagebox as mb 
import os 

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
        self.frame_info.place(x=302,y=0)
        self.frame_info.config(width=400, height=200) #bg='yellow', 

        self.lbl_url = tk.Label(self.frame_info, text='Ingrese la Url: ', font=('Arial', 12))
        self.lbl_url.grid(row=0, column=0, sticky='w', padx=10)
        
        self.txt_url = tk.Entry(self.frame_info, width=40)
        self.txt_url.grid(row=0, column=1)

        self.lbl_path = tk.Label(self.frame_info, text='Ruta de destino: ', font=('Arial', 12))
        self.lbl_path.grid(row=1, sticky='w', padx=10)

        self.btn_ruta = tk.Button(self.frame_info, text='Buscar', command=self.getPath)
        self.btn_ruta.grid(row=1, column=1, sticky='w')

        self.btn_dwn = tk.Button(self.frame_info, text='Descargar', command=self.download_video)
        self.btn_dwn.grid(row=2, column=0, columnspan=2)

    def verificar_tipo_url(self):
        url = self.txt_url.get()
        try:
            yt = YouTube(url)
            return yt
        except:
            try:
                pl = Playlist(url)
                return pl
            except:
                return "Url no reconocida"

    def download_video(self) -> None:
        my_object = self.verificar_tipo_url()
        if isinstance(my_object, YouTube): 
            try:
                self.download_YouTube(my_object)
                mb.showinfo(title='Bien!', message='Descarga finalizada.')
            except Exception as e:
                mb.showerror(title='Descarga fallida', message=f'Se produjo un error {str(e)}')

        elif isinstance(my_object, Playlist):
            youTube_list = my_object.videos
            self.path = os.path.join(self.path, my_object.title)
            os.makedirs(name=self.path, exist_ok=True)
            for element in youTube_list:
                try:
                    self.download_YouTube(element)
                except Exception as e:
                    mb.showerror(title='Descarga fallida', message=f'Se produjo un error {str(e)}')
            mb.showinfo(title='Bien!', message='Descarga finalizada.')
        else:
            mb.showerror(title='Descarga fallida', 
                        message='La URL o la ruta de destino proporcionada no es valida.')

    def download_YouTube(self, my_object):
        vid = my_object.streams.get_highest_resolution()
        print(f'[+] Se esta descargando el video: {my_object.title}')
        output_path = vid.download(output_path=self.path, timeout=10, max_retries=1, skip_existing=True)
        #print(output_path)
        
    def getPath(self) -> None:
        self.path = fd.askdirectory(initialdir='./', title='Ruta donde se va guardar la descarga')
        
if __name__ == '__main__':
    root = tk.Tk()
    my_gui = Gui(root)
    root.mainloop()