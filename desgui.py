import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

def decrypt(encrypted_text, key):
    des = DES.new(key, DES.MODE_ECB)
    decoded_encrypted_text = base64.b64decode(encrypted_text)
    decrypted_text = des.decrypt(decoded_encrypted_text).decode('utf-8')
    return decrypted_text.rstrip()

def process_encryption():
    plain_text = entry_plain.get("1.0", tk.END).strip()
    key_input = entry_key.get().strip()

    if len(key_input) != 8:
        messagebox.showerror("Error", "Key harus memiliki panjang 8 karakter")
        return

    if not plain_text:
        messagebox.showwarning("Warning", "Plain Text tidak boleh kosong")
        return

    try:
        key = key_input.encode('utf-8')
        encrypted = encrypt(plain_text, key)
        entry_encrypted.delete("1.0", tk.END)
        entry_encrypted.insert(tk.END, encrypted)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def process_decryption():
    encrypted_text = entry_encrypted.get("1.0", tk.END).strip()
    key_input = entry_key.get().strip()

    if len(key_input) != 8:
        messagebox.showerror("Error", "Key harus memiliki panjang 8 karakter")
        return

    if not encrypted_text:
        messagebox.showwarning("Warning", "Encrypted Text tidak boleh kosong")
        return

    try:
        key = key_input.encode('utf-8')
        decrypted = decrypt(encrypted_text, key)
        entry_decrypted.delete("1.0", tk.END)
        entry_decrypted.insert(tk.END, decrypted)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Membuat GUI
root = tk.Tk()
root.title("DES Encryption/Decryption")
root.geometry("900x600")
root.configure(bg="#f3f7fb")

# Warna tema
bg_color = "#f3f7fb"
primary_color = "#3b5998"
secondary_color = "#8b9dc3"
text_color = "#333333"

# Font utama
main_font = ("Calibri", 14)
header_font = ("Calibri", 18, "bold")

# Judul
title_label = tk.Label(root, text="DES Encryption/Decryption", font=("Calibri", 26, "bold"), bg=bg_color, fg=primary_color)
title_label.pack(pady=20)

# Frame utama
main_frame = tk.Frame(root, bg=bg_color)
main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Grid konfigurasi
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# Label dan Entry untuk Plain Text
label_plain = tk.Label(main_frame, text="Plain Text:", font=main_font, bg=bg_color, fg=text_color)
label_plain.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
entry_plain = tk.Text(main_frame, width=60, height=5, font=main_font, bg="white", fg=text_color, bd=2, relief="groove")
entry_plain.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Label dan Entry untuk Key
label_key = tk.Label(main_frame, text="Key (8 karakter):", font=main_font, bg=bg_color, fg=text_color)
label_key.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_key = tk.Entry(main_frame, width=30, font=main_font, bg="white", fg=text_color, bd=2, relief="groove")
entry_key.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Label dan Entry untuk Encrypted Text
label_encrypted = tk.Label(main_frame, text="Encrypted Text:", font=main_font, bg=bg_color, fg=text_color)
label_encrypted.grid(row=2, column=0, padx=10, pady=10, sticky="nw")
entry_encrypted = tk.Text(main_frame, width=60, height=5, font=main_font, bg="white", fg=text_color, bd=2, relief="groove")
entry_encrypted.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

# Label dan Entry untuk Decrypted Text
label_decrypted = tk.Label(main_frame, text="Decrypted Text:", font=main_font, bg=bg_color, fg=text_color)
label_decrypted.grid(row=3, column=0, padx=10, pady=10, sticky="nw")
entry_decrypted = tk.Text(main_frame, width=60, height=5, font=main_font, bg="white", fg=text_color, bd=2, relief="groove")
entry_decrypted.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

# Tombol untuk Enkripsi dan Dekripsi
btn_frame = tk.Frame(root, bg=bg_color)
btn_frame.pack(pady=20)

btn_encrypt = tk.Button(btn_frame, text="Encrypt", font=main_font, bg=primary_color, fg="white", width=15, command=process_encryption, relief="raised", bd=3)
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(btn_frame, text="Decrypt", font=main_font, bg=secondary_color, fg="white", width=15, command=process_decryption, relief="raised", bd=3)
btn_decrypt.grid(row=0, column=1, padx=10)

# Footer
footer_label = tk.Label(root, text="© 2024 DES Encryption/Decryption Tool", font=("Calibri", 12), bg=bg_color, fg=text_color)
footer_label.pack(side=tk.BOTTOM, pady=10)

# Menjalankan GUI
root.mainloop()
