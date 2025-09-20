import tkinter as tk
from tkinter import messagebox, font

def hitung_bunga_tunggal(modal, bunga, periode):
    return modal + (modal * bunga / 100 * periode)

def hitung_bunga_majemuk(modal, bunga, periode):
    return modal * ((1 + bunga / 100) ** periode)

def hitung():
    try:
        modal = float(entry_modal.get())
        bunga = float(entry_bunga.get())
        periode = int(entry_periode.get())
        mode = var_mode.get()
        if mode == "Tunggal":
            hasil = hitung_bunga_tunggal(modal, bunga, periode)
            messagebox.showinfo("Hasil", f"Total setelah {periode} bulan (Bunga Tunggal): {hasil:.2f}")
        else:
            hasil = hitung_bunga_majemuk(modal, bunga, periode)
            messagebox.showinfo("Hasil", f"Total setelah {periode} bulan (Bunga Majemuk): {hasil:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid!")

root = tk.Tk()
root.title("Kalkulator Bunga")
root.configure(bg="#f0f4f8")

default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=11)

frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove", padx=20, pady=20)
frame.pack(padx=30, pady=30)

tk.Label(frame, text="Modal Awal:", bg="#ffffff", font=("Segoe UI", 11)).grid(row=0, column=0, sticky="w", pady=5)
entry_modal = tk.Entry(frame, font=("Segoe UI", 11), width=20, bg="#d3d3d3")
entry_modal.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Bunga per bulan (%):", bg="#ffffff", font=("Segoe UI", 11)).grid(row=1, column=0, sticky="w", pady=5)
entry_bunga = tk.Entry(frame, font=("Segoe UI", 11), width=20, bg="#d3d3d3")
entry_bunga.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Periode (bulan):", bg="#ffffff", font=("Segoe UI", 11)).grid(row=2, column=0, sticky="w", pady=5)
entry_periode = tk.Entry(frame, font=("Segoe UI", 11), width=20, bg="#d3d3d3")
entry_periode.grid(row=2, column=1, pady=5)

var_mode = tk.StringVar(value="Tunggal")
tk.Radiobutton(frame, text="Bunga Tunggal", variable=var_mode, value="Tunggal", bg="#d3d3d3", font=("Segoe UI", 11)).grid(row=3, column=0, pady=10)
tk.Radiobutton(frame, text="Bunga Majemuk", variable=var_mode, value="Majemuk", bg="#d3d3d3", font=("Segoe UI", 11)).grid(row=3, column=1, pady=10)

tk.Button(frame, text="Hitung", command=hitung, bg="#4f8cff", fg="white", font=("Segoe UI", 11, "bold"), relief="raised", bd=2).grid(row=4, column=0, columnspan=2, pady=15, ipadx=10, ipady=2)

root.mainloop()
