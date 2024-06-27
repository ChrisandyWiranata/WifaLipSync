import platform
from tkinter import filedialog
from customtkinter import *
import shutil
import subprocess
import threading
from gtts import gTTS
import os

# App configuration
app = CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 800
window_height = 500
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
app.title("Wifa Lip-Sync")
app.resizable(False, False)

# Global variable
audio_file_path = ""
video_file_path = ""


# Initialize functions
def upload_audio():
    global audio_file_path
    audio_file_path = filedialog.askopenfilename(filetypes=[("Audio Files", ".wav;.mp3")])
    if audio_file_path:
        audio_status_label.configure(text="Audio has been selected")
    print("Audio file directory:", audio_file_path)

def upload_video():
    global video_file_path
    video_file_path = filedialog.askopenfilename(filetypes=[("Video File", "*.mp4")])
    if video_file_path:
        video_status_label.configure(text="Video has been selected")
    print("Video file directory:", video_file_path)

def run_process():
    global audio_file_path, video_file_path

    selectedMenu = menu.get()
    if selectedMenu == 'Video and Audio':
        if audio_file_path and video_file_path:
            app.config(cursor="watch") 
            process_status_label.configure(text="Loading...")

            def process():
                try: 
                    destination_folder = os.getcwd()
                    destination_folder_video = os.path.join(destination_folder, "input_video")
                    destination_folder_audio = os.path.join(destination_folder, "input_audio")
            
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)

                    video_filename = os.path.basename(video_file_path)
                    audio_filename = os.path.basename(audio_file_path)

                    shutil.copy(video_file_path, os.path.join(destination_folder_video, video_filename))
                    shutil.copy(video_file_path, os.path.join(destination_folder_audio, audio_filename))

                    print("Video has been copied to:", destination_folder_video)
                    print("Audio has been copied to:", destination_folder_audio)
                    print("Running process...")

                    output_video_path = os.path.join(os.getcwd(), "results", "result_voice.mp4")

                    subprocess.call(["python", "inference.py", "--checkpoint_path", "checkpoints/wav2lip.pth", "--face", os.path.join(destination_folder_video, video_filename), "--audio", os.path.join(destination_folder_audio, audio_filename)])

                    process_status_label.configure(text="Finished")

                    if platform.system() == 'Windows':
                        os.startfile(output_video_path)

                finally:
                    app.config(cursor="") 
                    process_status_label.configure(text="Finished")

            threading.Thread(target=process, daemon=True).start()
    elif selectedMenu == 'Video and Text':
        processTextToAudio()
        if video_file_path:
            app.config(cursor="watch") 
            process_status_label.configure(text="Loading...")

            def process():
                try: 
                    destination_folder = os.getcwd()
                    destination_folder_video = os.path.join(destination_folder, "input_video")
                    destination_folder_audio = os.path.join(destination_folder, "input_audio")
            
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)

                    video_filename = os.path.basename(video_file_path)
                    audio_filename = "text_audio.mp3"

                    shutil.copy(video_file_path, os.path.join(destination_folder_video, video_filename))

                    print("Video has been copied to:", destination_folder_video)
                    print("Running process...")

                    output_video_path = os.path.join(os.getcwd(), "results", "result_voice.mp4")

                    subprocess.call(["python", "inference.py", "--checkpoint_path", "checkpoints/wav2lip.pth", "--face", os.path.join(destination_folder_video, video_filename), "--audio", os.path.join(destination_folder_audio, audio_filename)])

                    process_status_label.configure(text="Finished")

                    if platform.system() == 'Windows':
                        os.startfile(output_video_path)

                finally:
                    app.config(cursor="") 
                    process_status_label.configure(text="Finished")

            threading.Thread(target=process, daemon=True).start()

def processTextToAudio():
    language = ''
    valueLanguage = languageMenu.get()
    if valueLanguage == "English":
        language = 'en'
    elif valueLanguage == 'Indonesian':
        language = 'id'
    elif valueLanguage == 'Mandarin':
        language = 'zh-cn'
    elif valueLanguage == 'Japanese':
        language = 'ja'

    if entryText.get():
        input_audio_dir = os.path.join(os.getcwd(), 'input_audio')
        audio_file = os.path.join(input_audio_dir, "text_audio.mp3")
        
        obj = gTTS(text=entryText.get(), lang=language)
        obj.save(audio_file)

def changeView(value):
    if value == "Video and Audio":
        audio_frame.grid()
        input_text_frame.grid_remove()
    else:
        audio_frame.grid_remove()
        input_text_frame.grid()


# Create menu
menu = CTkOptionMenu(app, values=['Video and Audio', 'Video and Text'], command=changeView)
menu.pack(pady=10)

# Upper frame design
upper_frame_child_font = ("DefaultFont", 12, "italic")

upper_frame = CTkFrame(master=app, fg_color="transparent")
upper_frame.pack(fill="x", pady=20, padx=20)

input_text_frame = CTkFrame(master=upper_frame, corner_radius=10)
input_text_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 25))

audio_frame = CTkFrame(master=upper_frame, corner_radius=10)
audio_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 25))

video_frame = CTkFrame(master=upper_frame, corner_radius=10)
video_frame.grid(row=0, column=1, sticky="nsew", padx=(0, 25))

process_frame = CTkFrame(master=upper_frame, corner_radius=10)
process_frame.grid(row=0, column=2, sticky="nsew")

upper_frame.grid_columnconfigure(0, weight=1)
upper_frame.grid_columnconfigure(1, weight=1)
upper_frame.grid_columnconfigure(2, weight=1)

# Input Text
languageMenu = CTkOptionMenu(master=input_text_frame, values=['English', 'Indonesian', 'Mandarin', 'Japanese'])
languageMenu.pack(pady=10)
entryText = CTkEntry(master=input_text_frame, font=('Poppins', 12))
entryText.pack(pady=10)
labelText = CTkLabel(master=input_text_frame, text='Enter some words ', font=upper_frame_child_font)
labelText.pack()

# Audio
upload_audio_button = CTkButton(master=audio_frame, text="Upload Audio", command=upload_audio)
upload_audio_button.pack(pady=10)

audio_status_label = CTkLabel(master=audio_frame, text="No audio selected", font=upper_frame_child_font)
audio_status_label.pack()

# Video
upload_video_button = CTkButton(master=video_frame, text="Upload Video", command=upload_video)
upload_video_button.pack(pady=10)

video_status_label = CTkLabel(master=video_frame, text="No video selected", font=upper_frame_child_font)
video_status_label.pack()

# Process to generate video
process_button = CTkButton(master=process_frame, text="Process Files", command=run_process)
process_button.pack(pady=10)

process_status_label = CTkLabel(master=process_frame, text="Waiting for files", font=upper_frame_child_font)
process_status_label.pack()

# Membuat scrollable frame
scrollable_frame = CTkScrollableFrame(app)
scrollable_frame.pack(fill="both", expand=True)

# Bottom frame design
group_name_font = ("DefaultFont", 25, "bold")
project_description_font = ("DefaultFont", 15, "normal")
group_member_font = ("DefaultFont", 10, "bold")

bottom_frame = CTkFrame(master=scrollable_frame)
bottom_frame.pack(fill="both", expand=True, padx=20, pady=20)

group_name_label = CTkLabel(master=bottom_frame, text="Wifa Lip-Sync", font=group_name_font, anchor="center")
group_name_label.pack(anchor='w', padx=20, pady=(20,0), fill='x')

project_description_label = CTkLabel(master=bottom_frame, text="Program AI Lip-Syncing Audio Ke Video", font=project_description_font, anchor="center")
project_description_label.pack(anchor='w', padx=20, pady=(0,10), fill='x')

def create_label(master, text, is_bold=False):
    font_style = ("DefaultFont", 11, "bold" if is_bold else "normal")
    label = CTkLabel(master=master, text=text, font=font_style, wraplength=window_width - 100, justify='left', anchor="w")
    label.pack(anchor='w', padx=20, pady=(1, 1), fill='x')
    return label

create_label(bottom_frame, "1. Pastikan audio merupakan file dengan ekstensi .wav dan video merupakan file dengan ektensi .mp4 (Jikalau audio berbentuk mp3, mp4a, OPUS, ataupun bentuk lainnya, mohon konversi terlebih dahulu ke bentuk .wav)")
create_label(bottom_frame, "2. Mohon perhatikan bahwa semakin tinggi durasi serta ukuran dari audio maupun video yang ingin di proses, maka waktu pengerjaannya akan semakin lama sesuai dengan kapasitas performa laptop / komputer pengguna. Untuk hasil yang lebih maksimal, usahakan durasi audio dan video sama panjangnya.")
create_label(bottom_frame, "3. Rekomendasi kami mengenai durasi audio dan video adalah 10 detik secara maksimal, dengan size untuk audio sekitar 1.5 mb dan 2.5 mb untuk video. Namun tetap kami tidak menutup jika ingin memproses lebih dari rekomendasi kami, tentunya kembali ke poin nomor dua.")
create_label(bottom_frame, "4. Berdasarkan pengalaman kami, untuk memproses audio dan video selama 5 detik dengan ukuran masing-masing sebesar 500 KB dan 1 MB, butuh swaktu kurang lebih 5 menit.")
create_label(bottom_frame, "5. Setelah mengklik button proses, maka label dibawah proses akan berubah menjadi \"Loading...\" dan cursor akan berbentuk circular progress, selagi dua hal ini masih berlansung, mohon tunggu sampai pengerjaan selesai.")
create_label(bottom_frame, "6. Jika pengerjaan telah selesai, maka label dibawah proses akan bertuliskan \"Finished\" dan dan cursor akan kembali normal serta video akan langsung terputar secara otomatis.")
create_label(bottom_frame, "7. Hasil output video juga akan tercopy secara otomatis ke WifaLipSync/results. Dokumentasi lebih lanjut silahkan membaca dari README.txt. Terimakasih atas perhatiannya!")

group_member_label = CTkLabel(master=bottom_frame, text="By: Fahim - Chrisandy - Jhonsen - Kent - Kevin", font=group_member_font, anchor="center")
group_member_label.pack(anchor='w', padx=20, pady=(0,10), fill='x')

app.mainloop()