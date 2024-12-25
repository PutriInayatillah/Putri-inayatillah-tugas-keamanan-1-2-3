# Putri-inayatillah-tugas-keamanan-1-2-3

1. Nama Tugas: Aplikasi Caesar Cipher dengan GUI

Isi Tugas: Aplikasi ini digunakan untuk melakukan enkripsi dan dekripsi teks menggunakan metode Caesar Cipher. Metode ini bekerja dengan cara mengganti setiap huruf dalam teks dengan huruf lain yang berada pada jarak tertentu (shift) dalam urutan alfabet. Pengguna dapat memasukkan teks yang ingin dienkripsi atau didekripsi, memberikan nilai pergeseran (shift), dan mendapatkan hasilnya melalui antarmuka grafis yang mudah digunakan.

Cara Menjalankan:

Simpan kode Python ini ke file dengan ekstensi .py (misalnya caesar_cipher_gui.py).
Pastikan Python sudah terinstal di komputer Anda.
Buka terminal atau command prompt, lalu jalankan file dengan perintah:
bash
Copy code
python caesar_cipher_gui.py
Setelah program berjalan, akan muncul jendela GUI.
Untuk Enkripsi:

Masukkan teks yang ingin dienkripsi di kolom Masukkan Plaintext.
Isi nilai shift (pergeseran) di kolom Pergeseran Kunci (Shift).
Klik tombol Enkripsi untuk melihat hasil enkripsi yang muncul di kolom Hasil Enkripsi.
Untuk Dekripsi:

Masukkan teks yang sudah dienkripsi (ciphertext) di kolom Masukkan Ciphertext.
Isi nilai shift (pergeseran) di kolom Pergeseran Kunci (Shift).
Klik tombol Dekripsi untuk melihat hasil dekripsi yang muncul di kolom Hasil Dekripsi.

2. Nama Tugas: Aplikasi Enkripsi dan Dekripsi DES dengan GUI

Data Encryption Standard (DES) adalah salah satu algoritma enkripsi simetrik yang digunakan untuk mengamankan data dengan cara mengubahnya menjadi format yang tidak dapat dibaca tanpa kunci khusus. DES bekerja dengan menggunakan satu kunci untuk proses enkripsi (mengubah data asli menjadi data terenkripsi) dan dekripsi (mengembalikan data terenkripsi ke bentuk aslinya).
Isi Tugas:
Aplikasi ini menggunakan metode Data Encryption Standard (DES) untuk melakukan enkripsi dan dekripsi teks. Dengan aplikasi ini :
Mengubah teks biasa (Plain Text) menjadi teks terenkripsi (Encrypted Text).
Mengembalikan teks terenkripsi menjadi teks aslinya.
Setelah program dijalankan, akan muncul jendela GUI dengan beberapa kolom input:

Plain Text: Masukkan teks asli yang akan dienkripsi.
Key (8 karakter): Masukkan kunci yang panjangnya tepat 8 karakter.
Encrypted Text: Menampilkan hasil enkripsi teks.
Decrypted Text: Menampilkan hasil dekripsi dari teks terenkripsi.
Klik tombol Encrypt untuk mengenkripsi teks, atau tombol Decrypt untuk mendekripsi teks yang sudah terenkripsi.

Jika ada error atau kesalahan input (misalnya, panjang kunci tidak 8 karakter), akan muncul pesan peringatan atau error.

3. Nama tugas : Steganografi
Steganografi adalah teknik yang digunakan untuk menyembunyikan pesan atau informasi dalam bentuk lain, seperti gambar, suara, atau video, sehingga informasi tersebut tidak dapat terdeteksi oleh orang yang tidak mengetahui caranya. Berbeda dengan enkripsi yang mengubah bentuk pesan agar tidak bisa dibaca tanpa kunci, steganografi menyembunyikan pesan dalam media lain dengan cara yang tidak mencurigakan.

Contohnya, sebuah pesan teks bisa disembunyikan dalam gambar dengan memanfaatkan piksel yang hampir tidak terlihat oleh mata manusia. Steganografi ini banyak digunakan dalam berbagai bidang, termasuk komunikasi aman, pengamanan data, dan bahkan dalam dunia digital untuk perlindungan hak cipta.

Di dalam aplikasi Steganography Tool ini, kita menggunakan teknik steganografi untuk menyembunyikan pesan dalam gambar. Program ini memungkinkan pengguna untuk:

Menyembunyikan pesan: Memasukkan teks ke dalam gambar (seperti foto) dan menyimpannya.
Mengambil pesan tersembunyi: Membaca pesan yang sudah disembunyikan dalam gambar tersebut.
Dengan kata lain, steganografi di sini membuat pesan yang disembunyikan dalam gambar menjadi tidak terlihat dan hanya bisa diambil jika kita tahu cara untuk mengekstrak pesan tersebut.
