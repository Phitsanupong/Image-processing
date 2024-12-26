import mahotas
import skimage.color
import scipy
import os
import App3
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Label, filedialog
from PIL import ImageTk, Image
from tkinter import font



def open_file():
    global total, passed, rejected
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        #App3.orcodeall(file_path,ax)
        ax.clear()  
        file_name = os.path.basename(file_path)
        ax.set_title("Orange Quality Analysis : {}".format(file_name))  # ตั้งชื่อ title
        ax.set_xlabel("X ")            # ตั้งชื่อแกน X
        ax.set_ylabel("Y ")            # ตั้งชื่อแกน Y
        total, passed, rejected = App3.orcodeall(file_path, ax,total,passed,rejected)
        total_label.config(text=f"จำนวนส้มทั้งหมด: {total}")
        pass_label.config(text=f"จำนวนส้มที่ดี: {passed}")
        reject_label.config(text=f"จำนวนส้มที่เสีย: {rejected}")
        canvas.draw()

def exit_program():
    root.destroy()
        
# สร้างหน้าต่าง tkinter


root = tk.Tk()
root.title("Orange Quality Sorting Algorithm Based on An Image Processing Method")
fig, ax = plt.subplots()

# สร้าง Label สำหรับแสดงภาพ
frame = tk.Frame(root)

label = tk.Label(text= "ระบบคัดแยกส้มด้วยการประมวลผลภาพ")
label.config(font=("mm",32))
label.pack(pady=10)

button_font = font.Font(family='Helvetica', size=30, weight='bold')  

# สร้างปุ่มเพื่อเลือกรูปภาพ
button_1 = tk.Button(root, text="Open",bg="#4267B2",fg="white",activebackground="#365899",activeforeground="white",relief="flat",bd=0,padx=30,pady=15,command=open_file)
button_1.pack(pady=10)

canvas = FigureCanvasTkAgg(fig, master= frame)
canvas.get_tk_widget().pack()
frame.pack()

total=0
passed=0 
rejected=0

# สร้าง Label สำหรับแสดงจำนวนการใช้งาน
total_label = tk.Label(root, text="จำนวนส้มทั้งหมด: 0", font=("Helvetica", 15))
total_label.pack(padx=5)
pass_label = tk.Label(root, text="จำนวนส้มที่ดี: 0", font=("Helvetica", 15))
pass_label.pack(padx=5)
reject_label = tk.Label(root, text="จำนวนส้มที่เสีย: 0", font=("Helvetica", 15))
reject_label.pack(padx=5)


exit_button = tk.Button(root, text="Exit",bg="#4267B2",fg="white",activebackground="#365899",activeforeground="white",relief="flat",bd=0,padx=30,pady=15, command=exit_program)
exit_button.pack(pady=10)



# รัน main loop ของ tkinter

root.geometry("1250x800+250+90")
root.mainloop()
