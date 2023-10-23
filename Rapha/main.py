import customtkinter
from tkinter import Listbox, Scrollbar, filedialog
from pytube import YouTube

def update_status(message):
    Lconclusão.delete(0, 'end')  # Clear previous status
    Lconclusão.insert(customtkinter.END, message)

def download_video():
    url = EURL.get()
    update_status(f'Iniciando o download de vídeo da URL: {url}')
    
    try:
        yt = YouTube(url)
        ys = yt.streams.get_highest_resolution()

        output_path = filedialog.askdirectory()
        if output_path:
            ys.download(output_path=output_path, filename_prefix='MP4 - ')
            update_status('Conclusão Download de Vídeo')
            update_status(f'Concluido: {output_path}')
        else:
            update_status('Operação de download de vídeo cancelada pelo usuário')
    except Exception as e:
        update_status(f'Erro: {str(e)}')

def download_audio():
    url = EURL.get()
    update_status(f'Iniciando o download do audio da URL: {url}')
    
    try:
        yt = YouTube(url)
        audio_streams = yt.streams.filter(only_audio=True)
        if audio_streams:
            for stream in audio_streams:
                update_status(f'Iniciando o download do Áudio da URL: {url}')

                output_path = filedialog.askdirectory()
                if output_path:
                    stream.download(output_path=output_path, filename_prefix='MP3 - ')
                    update_status(f'Conclusão do Download de Áudio: {stream.mime_type}')
                    update_status(f'Concluido: {output_path}')
                else:
                    update_status(f'Operação de download de áudio cancelada pelo usuário')
                return
        else:
            update_status(f'Erro: Não foi possível encontrar um fluxo de áudio.')
    except Exception as e:
        update_status(f'Erro: {str(e)}')

def limpar():
    EURL.delete(0, 'end')
    Lconclusão.delete(0, 'end')

janela = customtkinter.CTk()
janela.geometry('400x150+100+100')  # Adjust the window height to accommodate the larger textbox
janela.resizable(width=False, height=False)
janela.title('Youtuber Download')

Lautor = customtkinter.CTkLabel(janela, text='Cole abaixo o link do YouTube')
Lautor.place(x=100, y=0)

EURL = customtkinter.CTkEntry(janela, width=390, placeholder_text='Cole aqui a sua URL:')
EURL.place(x=5, y=25)

BMP3 = customtkinter.CTkButton(janela, text='Download Vídeo (MP4)', width=40, command=download_video, text_color='#000000')
BMP3.place(x=10, y=60)
BMP4 = customtkinter.CTkButton(janela, text='Download Áudio (MP3)', width=40, command=download_audio, text_color='#000000')
BMP4.place(x=160, y=60)
BLimpar = customtkinter.CTkButton(janela, text='Limpar', width=40, command=limpar, text_color='#000000')
BLimpar.place(x=310, y=60)

Lconclusão = Listbox(janela, width=53, height=2, font=('arial', 12))  # Adjust the height to 2
Lconclusão.place(x=10, y=100)  # Adjust the position

scrollbar = Scrollbar(janela, orient="vertical")
scrollbar.config(command=Lconclusão.yview)
scrollbar.place(x=465, y=100, height=60)  # Adjust the position and height
Lconclusão.config(yscrollcommand=scrollbar.set)

janela.mainloop()




