import tkinter as tk
from tkinter import messagebox

# Fungsi untuk enkripsi Caesar Cipher
def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

# Fungsi untuk dekripsi Caesar Cipher
def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

# Fungsi untuk proses enkripsi
def proses_enkripsi():
    try:
        shift = int(entry_shift_enkripsi.get())
        plaintext = entry_plaintext_enkripsi.get("1.0", tk.END).strip()
        if plaintext:
            result = caesar_cipher_encrypt(plaintext, shift)
            entry_hasil_enkripsi.delete("1.0", tk.END)
            entry_hasil_enkripsi.insert(tk.END, result)
        else:
            messagebox.showerror("Error", "Masukkan plaintext untuk enkripsi")
    except ValueError:
        messagebox.showerror("Error", "Kunci harus berupa angka")

# Fungsi untuk proses dekripsi
def proses_dekripsi():
    try:
        shift = int(entry_shift_dekripsi.get())
        ciphertext = entry_plaintext_dekripsi.get("1.0", tk.END).strip()
        if ciphertext:
            result = caesar_cipher_decrypt(ciphertext, shift)
            entry_hasil_dekripsi.delete("1.0", tk.END)
            entry_hasil_dekripsi.insert(tk.END, result)
        else:
            messagebox.showerror("Error", "Masukkan ciphertext untuk dekripsi")
    except ValueError:
        messagebox.showerror("Error", "Kunci harus berupa angka")

# Fungsi untuk menghapus teks di semua entri
def hapus():
    entry_plaintext_enkripsi.delete("1.0", tk.END)
    entry_hasil_enkripsi.delete("1.0", tk.END)
    entry_shift_enkripsi.delete(0, tk.END)
    entry_plaintext_dekripsi.delete("1.0", tk.END)
    entry_hasil_dekripsi.delete("1.0", tk.END)
    entry_shift_dekripsi.delete(0, tk.END)

# Inisialisasi window Tkinter
root = tk.Tk()
root.title("Aplikasi Enkripsi dan Dekripsi Caesar Cipher")
root.geometry("900x600")
root.configure(bg="#d9eaf7")

# Label judul utama
tk.Label(root, text="Caesar Cipher", font=("Arial", 28, "bold"), bg="#d9eaf7", fg="#003f7f").pack(pady=20)

# Frame utama
frame_main = tk.Frame(root, bg="#d9eaf7")
frame_main.pack(fill="both", expand=True, padx=20, pady=20)

# Fungsi untuk membuat frame enkripsi dan dekripsi
def create_cipher_frame(parent, title, input_label, shift_label, output_label, button_text, button_command):
    frame = tk.LabelFrame(parent, text=title, font=("Arial", 16, "bold"), bg="#ffffff", fg="#003f7f", padx=20, pady=20, bd=2, relief=tk.RIDGE)
    frame.configure(highlightbackground="#b8d3ef", highlightcolor="#b8d3ef", highlightthickness=1)

    tk.Label(frame, text=input_label, bg="#ffffff", fg="#003f7f", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=(0, 10))
    input_text = tk.Text(frame, height=5, width=40, font=("Arial", 11), relief=tk.FLAT, bd=1)
    input_text.grid(row=1, column=0, pady=(0, 10))
    input_text.configure(borderwidth=2, relief=tk.GROOVE)

    tk.Label(frame, text=shift_label, bg="#ffffff", fg="#003f7f", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=(0, 10))
    shift_entry = tk.Entry(frame, width=15, font=("Arial", 11), relief=tk.FLAT, bd=1)
    shift_entry.grid(row=3, column=0, sticky="w", pady=(0, 10))
    shift_entry.configure(borderwidth=2, relief=tk.GROOVE)

    tk.Label(frame, text=output_label, bg="#ffffff", fg="#003f7f", font=("Arial", 12)).grid(row=4, column=0, sticky="w", pady=(0, 10))
    output_text = tk.Text(frame, height=5, width=40, font=("Arial", 11), relief=tk.FLAT, bd=1)
    output_text.grid(row=5, column=0, pady=(0, 10))
    output_text.configure(borderwidth=2, relief=tk.GROOVE)

    button = tk.Button(frame, text=button_text, command=button_command, font=("Arial", 12, "bold"), width=15, bg="#0056b3", fg="#ffffff", relief=tk.FLAT, bd=0)
    button.grid(row=6, column=0, pady=(10, 0))
    button.configure(borderwidth=2, relief=tk.GROOVE)

    return frame, input_text, shift_entry, output_text

# Frame Enkripsi
enkripsi_frame, entry_plaintext_enkripsi, entry_shift_enkripsi, entry_hasil_enkripsi = create_cipher_frame(
    frame_main,
    "Enkripsi",
    "Masukkan Plaintext:",
    "Pergeseran Kunci (Shift):",
    "Hasil Enkripsi:",
    "Enkripsi",
    proses_enkripsi
)
enkripsi_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

# Frame Dekripsi
dekripsi_frame, entry_plaintext_dekripsi, entry_shift_dekripsi, entry_hasil_dekripsi = create_cipher_frame(
    frame_main,
    "Dekripsi",
    "Masukkan Ciphertext:",
    "Pergeseran Kunci (Shift):",
    "Hasil Dekripsi:",
    "Dekripsi",
    proses_dekripsi
)
dekripsi_frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

# Tombol Hapus dan Keluar
frame_buttons = tk.Frame(root, bg="#d9eaf7")
frame_buttons.pack(pady=20)

btn_hapus = tk.Button(frame_buttons, text="Hapus", command=hapus, font=("Arial", 12, "bold"), width=12, bg="#007bff", fg="#ffffff", relief=tk.FLAT, bd=0)
btn_hapus.grid(row=0, column=0, padx=10)
btn_hapus.configure(borderwidth=2, relief=tk.GROOVE)

btn_keluar = tk.Button(frame_buttons, text="Keluar", command=root.quit, font=("Arial", 12, "bold"), width=12, bg="#dc3545", fg="#ffffff", relief=tk.FLAT, bd=0)
btn_keluar.grid(row=0, column=1, padx=10)
btn_keluar.configure(borderwidth=2, relief=tk.GROOVE)

# Mengatur grid utama
frame_main.grid_rowconfigure(0, weight=1)
frame_main.grid_columnconfigure(0, weight=1)
frame_main.grid_columnconfigure(1, weight=1)

# Menjalankan aplikasi
root.mainloop()
