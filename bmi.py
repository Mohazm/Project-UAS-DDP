from tkinter import *
from tkinter import messagebox

def reset():
    height.delete(0, 'end')
    weight.delete(0, 'end')
    name_entry.delete(0, 'end')

def bmi_cal():
    kg = int(weight.get())
    m = int(height.get()) / 100
    bmi = kg / m ** 2
    bmi = round(bmi, 1)
    bmi_index_over18(bmi)

def bmi_index_over18(bmi):
    name = name_entry.get()
    if bmi < 18.5:
        messagebox.showinfo('BMI', f'{name}, Anda di bawah Rata - Rata berat badan ')
    elif (bmi > 18.5) and (bmi < 25.9):
        messagebox.showinfo('BMI', f'{name},Berat badan anda normal')
    elif (bmi > 25.9) and (bmi < 35.9):
        messagebox.showinfo('BMI',f'{name}, Anda Kelebihan Berat badan',)
    elif bmi > 35.9:
        messagebox.showinfo('BMI', f'{name}, Anda mengalami obesitas!')
    else:
        messagebox.showerror('BMI', 'Ada kesalahan!')

def info():
    messagebox.showinfo('Info', ' Anda bisa mencari berat badan ideal dengan memasukkan tinggi badan dan berat badan.')

root = Tk()
root.title("Body Mass Index Calculator")

gambar = PhotoImage(file="D:/Project-VSCode/Python/Semester1-DPP/UAS/mbi.png")
lbl = Label(image=gambar).pack()

var = IntVar()

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)

name_label = Label(frame, text="Masukkan nama anda             :")
name_label.grid(row=2, column=1)
name_entry = Entry(frame)
name_entry.grid(row=2, column=2, pady=5)

height_label = Label(frame, text="Masukkan tinggi badan anda :")
height_label.grid(row=3, column=1)
weight_label = Label(frame, text="Masukkan berat badan anda  :")
weight_label.grid(row=4, column=1)

height = Entry(frame)
height.grid(row=3, column=2, pady=5)
weight = Entry(frame)
weight.grid(row=4, column=2, pady=5)

frame3 = Frame(frame)
frame3.grid(row=5, column=3, pady=10)

calculate_b = Button(frame3, text="Hitung", command=bmi_cal)
calculate_b.pack(side=LEFT)

reset_b = Button(frame3, text="Reset", command=reset)
reset_b.pack(side=RIGHT)

info_b = Button(frame3, text="info", command=info)
info_b.pack(side=RIGHT)

root.mainloop()