
import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment
import os

def change_speed(file_path, speed):
    audio = AudioSegment.from_file(file_path)
    changed_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * speed)
    }).set_frame_rate(audio.frame_rate)
    output_path = os.path.splitext(file_path)[0] + f"_speed_{speed}.mp3"
    changed_audio.export(output_path, format="mp3")
    return output_path

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path)

def convert():
    file_path = entry_file.get()
    try:
        speed = float(entry_speed.get())
        output = change_speed(file_path, speed)
        messagebox.showinfo("Hoàn tất", f"Đã lưu file mới:\n{output}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

app = tk.Tk()
app.title("Tăng/Giảm Tốc Độ Nhạc")
app.geometry("400x180")

tk.Label(app, text="Chọn file nhạc:").pack()
entry_file = tk.Entry(app, width=50)
entry_file.pack()
tk.Button(app, text="Chọn File", command=browse_file).pack(pady=5)

tk.Label(app, text="Tốc độ (vd: 1.2 hoặc 0.8):").pack()
entry_speed = tk.Entry(app)
entry_speed.insert(0, "1.2")
entry_speed.pack()

tk.Button(app, text="Xử lý", command=convert).pack(pady=10)

app.mainloop()
