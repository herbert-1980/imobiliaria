import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def baixar_video():
    video_url = url_entry.get()
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        if video:
            video.download()
            messagebox.showinfo("Download Completo", "O vídeo foi baixado com sucesso!")
        else:
            messagebox.showerror("Erro", "Não foi possível encontrar uma representação de vídeo disponível para download.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante o download: {str(e)}")

# Configuração da janela principal
root = tk.Tk()
root.title("Herbert Software")

# Configuração dos widgets
url_label = tk.Label(root, text="URL do Vídeo:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

baixar_button = tk.Button(root, text="Baixar Vídeo", command=baixar_video)
baixar_button.pack(pady=5)

# Execução da interface
root.mainloop()
