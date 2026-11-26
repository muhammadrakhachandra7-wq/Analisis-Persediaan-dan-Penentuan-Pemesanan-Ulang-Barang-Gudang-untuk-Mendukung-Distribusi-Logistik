Analisis Persediaan dan Penentuan Pemesanan Ulang Barang Gudang untuk Mendukung Distribusi Logistik

Program berbasis Python dengan antarmuka teks (command line) untuk menganalisis persediaan barang gudang, menentukan kebutuhan pemesanan ulang menggunakan metode Reorder Point (ROP), serta melakukan simulasi pembelian barang guna mendukung kelancaran distribusi logistik.

Daftar Isi

1. "Deskripsi Proyek" (#deskripsi-proyek)
2. "Fitur Utama" (#fitur-utama)
3. "Teknologi yang Digunakan" (#teknologi-yang-digunakan)
4. "Struktur Repositori" (#struktur-repositori)
5. "Persyaratan Sistem" (#persyaratan-sistem)
6. "Instalasi" (#instalasi)
7. "Cara Menjalankan Program" (#cara-menjalankan-program)
8. "Panduan Penggunaan" (#panduan-penggunaan)
9. "Dataset" (#dataset)
10. "Metodologi" (#metodologi)
11. "Pengujian Program" (#pengujian-program)
12. "Keterbatasan Program" (#keterbatasan-program)
13. "Tim Pengembang" (#tim-pengembang)

1. Deskripsi Proyek

Kelancaran distribusi logistik sangat bergantung pada ketersediaan barang di gudang. Stok yang terlalu sedikit dapat menyebabkan keterlambatan pengiriman, sedangkan keterlambatan pemesanan ulang meningkatkan risiko kehabisan barang.

Program ini dikembangkan untuk membantu pengelola gudang dalam memantau persediaan, mengidentifikasi barang yang telah mencapai batas pemesanan ulang, memberikan rekomendasi jumlah pemesanan, serta mengetahui waktu tunggu (lead time) setiap barang.

2. Fitur Utama

Program menyediakan enam fitur pengelolaan persediaan dan satu fitur navigasi untuk mengakhiri program.

Menu| Fitur| Deskripsi
1| Data Persediaan| Menampilkan SKU, nama barang, gudang, stok, batas pemesanan, dan status persediaan.
2| Analisis Stok| Menampilkan jumlah barang, stok aman, barang yang perlu dipesan, dan total stok.
3| Rekomendasi Pemesanan| Menampilkan barang yang perlu dipesan beserta jumlah pemesanan dan lead time.
4| Simulasi Pembelian Barang| Mensimulasikan pembelian dengan validasi stok, jumlah, tanggal, alamat, dan metode pengiriman.
5| Laporan dan Riwayat| Menampilkan laporan persediaan, stok sementara, dan riwayat pembelian.
6| Cari Barang| Mencari barang berdasarkan SKU atau nama barang.
0| Keluar| Mengakhiri program dan menampilkan pesan terima kasih.

Program juga dilengkapi sistem login sederhana sebelum pengguna dapat mengakses menu utama.

3. Teknologi yang Digunakan

Teknologi dan pustaka yang digunakan dalam pengembangan program meliputi:

Teknologi| Fungsi
Python| Bahasa pemrograman utama.
CSV| Membaca dan mengelola dataset persediaan barang.
Datetime| Memvalidasi dan mengolah tanggal pembelian.
Command Line Interface (CLI)| Menyediakan antarmuka interaksi berbasis teks.

4. Struktur Repositori

Struktur berkas dalam repositori proyek adalah sebagai berikut:

.
├── CODING MENU 1-2.py
├── CODING MENU 3-4.py
├── CODING MENU 5-6.py
├── stok_item.csv
└── README.md

Keterangan:

- "CODING MENU 1-2.py": Program Data Persediaan dan Analisis Stok.
- "CODING MENU 3-4.py": Program Rekomendasi Pemesanan dan Simulasi Pembelian Barang.
- "CODING MENU 5-6.py": Program Laporan dan Riwayat serta Pencarian Barang.
- "stok_item.csv": Dataset persediaan barang.
- "README.md": Dokumentasi proyek.

5. Persyaratan Sistem

Persyaratan untuk menjalankan program:

- Python versi 3.6 atau lebih baru.
- Sistem operasi yang mendukung Python.
- Dataset "stok_item.csv".
- Pustaka standar Python, yaitu "csv" dan "datetime".

Tidak diperlukan instalasi pustaka eksternal tambahan.

6. Instalasi

Kloning repositori dari GitHub menggunakan perintah berikut:

git clone https://github.com/muhammadrakhachandra7-wq/Analisis-Persediaan-dan-Penentuan-Pemesanan-Ulang-Barang-Gudang-untuk-Mendukung-Distribusi-Logistik.git

Setelah proses kloning selesai, masuk ke direktori proyek:

cd Analisis-Persediaan-dan-Penentuan-Pemesanan-Ulang-Barang-Gudang-untuk-Mendukung-Distribusi-Logistik

Pastikan seluruh berkas program dan dataset berada dalam direktori yang sama.

7. Cara Menjalankan Program

Jalankan program menggunakan perintah berikut:

python "CODING MENU 1-2.py"

Pada beberapa sistem, perintah "python3" dapat digunakan sebagai pengganti "python".

Catatan: Program harus dijalankan dari dalam direktori repositori agar berkas "stok_item.csv" dapat ditemukan.

8. Panduan Penggunaan

Berikut tahapan penggunaan program:

1. Login: Masukkan username dan password yang telah ditentukan dalam kode program.
2. Pilih Menu: Masukkan nomor menu sesuai fitur yang ingin digunakan.
3. Ikuti Instruksi: Masukkan data yang diminta oleh program sesuai fitur yang dipilih.
4. Kembali ke Menu: Tekan Enter setelah proses selesai untuk kembali ke menu utama.
5. Keluar: Pilih menu 0 untuk mengakhiri program.

Daftar Menu

Nomor| Nama Menu
1| Data Persediaan
2| Analisis Stok
3| Rekomendasi Pemesanan
4| Simulasi Pembelian Barang
5| Laporan dan Riwayat
6| Cari Barang
0| Keluar

9. Dataset

Dataset disimpan dalam berkas "stok_item.csv" yang berisi informasi persediaan barang gudang.

Struktur Kolom Dataset

Kolom| Keterangan
"id"| Nomor identitas data.
"warehouse_id"| Kode gudang.
"sku"| Kode unik barang.
"product_name"| Nama barang.
"opening_on_hand"| Jumlah stok awal dalam bilangan bulat.
"counted_at"| Waktu pencatatan stok.
"reorder_point"| Batas stok untuk melakukan pemesanan ulang.
"reorder_qty"| Jumlah barang yang direkomendasikan untuk dipesan.
"lead_time_days"| Waktu tunggu pemesanan dalam hari.

Contoh Dataset

id,warehouse_id,sku,product_name,opening_on_hand,counted_at,reorder_point,reorder_qty,lead_time_days
1,1,SKU-428373,Bluetooth Speaker,236,2024-08-31 13:52:30,94,120,5

10. Metodologi

Penentuan Status Persediaan

Penentuan status barang dilakukan dengan membandingkan jumlah stok awal ("opening_on_hand") dengan batas pemesanan ulang ("reorder_point").

Kondisi| Status
"opening_on_hand" ≤ "reorder_point"| Perlu pesan
"opening_on_hand" > "reorder_point"| Aman

Rekomendasi Pemesanan

Barang yang memiliki jumlah stok kurang dari atau sama dengan batas pemesanan ulang akan dimasukkan ke dalam daftar rekomendasi pemesanan. Rekomendasi menampilkan jumlah barang yang perlu dipesan ("reorder_qty") dan waktu tunggu pemesanan ("lead_time_days").

Simulasi Pembelian

Simulasi pembelian dilakukan dengan mengurangi stok sementara berdasarkan jumlah pembelian yang dimasukkan pengguna. Proses pembelian dilengkapi beberapa validasi:

- SKU barang harus tersedia dalam dataset.
- Stok barang harus lebih dari nol.
- Jumlah pembelian harus berupa angka positif.
- Jumlah pembelian tidak boleh melebihi stok tersedia.
- Format tanggal harus sesuai ("DD-MM-YYYY").
- Alamat pengiriman tidak boleh kosong.
- Metode pengiriman harus dipilih dari pilihan yang tersedia, yaitu darat, laut, atau udara.

Catatan: Simulasi pembelian hanya memperbarui stok sementara selama program berjalan dan tidak mengubah dataset asli.

11. Pengujian Program

Pengujian dilakukan untuk memastikan setiap fitur berjalan sesuai dengan fungsi yang telah ditentukan. Pengujian mencakup beberapa kondisi berikut:

- Data normal dan lengkap untuk memastikan fungsi utama berjalan dengan benar.
- Data batas untuk menguji kondisi pada nilai ambang pemesanan ulang.
- Dataset kosong atau hanya berisi header.
- Data tidak valid, seperti nilai numerik yang berisi teks atau jumlah pembelian di luar ketentuan.
- Pengujian regresi untuk memastikan perbaikan program tidak menimbulkan kembali kesalahan yang sebelumnya ditemukan.

Hasil pengujian digunakan untuk mengevaluasi ketepatan proses pembacaan data, analisis stok, rekomendasi pemesanan, simulasi pembelian, dan penyajian laporan.

12. Keterbatasan Program

Beberapa keterbatasan yang terdapat dalam program ini adalah:

- Data persediaan disimpan dalam berkas CSV sehingga belum mendukung pengelolaan data secara bersamaan oleh banyak pengguna.
- Username dan password ditulis langsung dalam kode program dan belum menggunakan sistem enkripsi.
- Hasil simulasi pembelian hanya tersimpan selama program berjalan dan tidak mengubah berkas "stok_item.csv".
- Karena program dibagi menjadi tiga berkas terpisah, riwayat pembelian pada "CODING MENU 5-6.py" tidak memuat transaksi dari "CODING MENU 3-4.py".
- Penentuan pemesanan ulang hanya menggunakan batas reorder point dan belum mempertimbangkan perubahan pola permintaan barang.

13. Tim Pengembang

Proyek ini dikembangkan oleh:

No.| Nama| NIM
1| Muhammad Rakha Chandra| 2610932016
2| Adib Fawwaz Ramadhan| 2610932044
3| Dzaky Rinanda Pratama| 2610933006
4| Sayyid Bayhaqi Dinata| 2610933002

---

Proyek ini dikembangkan sebagai bagian dari pembelajaran pemrograman Python dalam penerapan analisis persediaan dan pengelolaan distribusi logistik.
