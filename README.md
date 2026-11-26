# Analisis Persediaan dan Penentuan Pemesanan Ulang Barang Gudang untuk Mendukung Distribusi Logistik

---

## 1. Project Title

Analisis Persediaan dan Penentuan Pemesanan Ulang Barang Gudang untuk Mendukung Distribusi Logistik

---

## 2. Description

Program berbasis antarmuka teks (*command line*) yang dikembangkan dengan bahasa Python untuk menganalisis stok barang gudang, menentukan barang yang perlu dipesan ulang, dan mensimulasikan pembelian barang. Penentuan pemesanan ulang menggunakan pendekatan **titik pemesanan ulang (*reorder point*)**.

Program membantu pengelola gudang memantau stok, mengetahui barang yang sudah mencapai batas pemesanan ulang, serta melihat jumlah dan waktu tunggu (*lead time*) pemesanannya, sehingga kelancaran distribusi logistik tetap terjaga.

---

## 3. Table of Contents

1. [Project Title](#1-project-title)
2. [Description](#2-description)
3. [Table of Contents](#3-table-of-contents)
4. [Features](#4-features)
5. [Technologies Used](#5-technologies-used)
6. [Project Structure](#6-project-structure)
7. [Requirements](#7-requirements)
8. [Installation](#8-installation)
9. [Usage](#9-usage)
10. [Dataset](#10-dataset)
11. [Methodology](#11-methodology)
12. [Limitations](#12-limitations)
13. [Contributors](#13-contributors)

---

## 4. Features

| Menu | Fitur | Keterangan |
|------|-------|------------|
| 1 | Data Persediaan | Menampilkan SKU, nama barang, gudang, stok, batas pemesanan, dan status. |
| 2 | Analisis Stok | Ringkasan jumlah barang, stok aman, barang perlu dipesan, dan total stok. |
| 3 | Rekomendasi Pemesanan | Daftar barang yang perlu dipesan beserta jumlah pesan dan lead time. |
| 4 | Simulasi Pembelian Barang | Simulasi pembelian dengan validasi stok, jumlah, tanggal, alamat, dan metode pengiriman (darat, laut, udara). |
| 5 | Laporan dan Riwayat | Laporan persediaan, stok setelah simulasi, dan riwayat pembelian. |
| 6 | Cari Barang | Pencarian berdasarkan SKU atau nama barang. |
| 0 | Keluar | Mengakhiri program. |

Program juga dilindungi *login* sederhana sebelum menu utama ditampilkan.

---

## 5. Technologies Used

- **Python 3**: bahasa pemrograman utama.
- **Modul `csv`**: membaca dataset persediaan.
- **Modul `datetime`**: validasi format tanggal pembelian.
- **Git dan GitHub**: pengelolaan versi dan penyimpanan kode.
- **Visual Studio Code**: editor kode.

---

## 6. Project Structure

```
.
├── CODING MENU 0.py     # Menu 0 (Keluar)
├── CODING MENU 1-2.py   # Menu 1 (Data Persediaan) dan Menu 2 (Analisis Stok)
├── CODING MENU 3-4.py   # Menu 3 (Rekomendasi Pemesanan) dan Menu 4 (Simulasi Pembelian)
├── CODING MENU 5-6.py   # Menu 5 (Laporan dan Riwayat) dan Menu 6 (Cari Barang)
├── stok_item.csv        # Dataset persediaan barang
└── README.md            # Dokumentasi
```

---

## 7. Requirements

- Python versi 3.6 atau yang lebih baru.
- Berkas `stok_item.csv` berada di folder yang sama dengan program.
- Git (opsional, untuk mengkloning repositori).
- Tidak memerlukan pustaka tambahan di luar pustaka standar Python.

---

## 8. Installation

1. Kloning repositori:

   ```
   git clone https://github.com/muhammadrakhachandra7-wq/Analisis-Persediaan-dan-Penentuan-Pemesanan-Ulang-Barang-Gudang-untuk-Mendukung-Distribusi-Logistik.git
   ```

2. Masuk ke folder proyek:

   ```
   cd Analisis-Persediaan-dan-Penentuan-Pemesanan-Ulang-Barang-Gudang-untuk-Mendukung-Distribusi-Logistik
   ```

Alternatif tanpa Git: klik tombol **Code > Download ZIP** di GitHub, lalu ekstrak.

---

## 9. Usage

1. Jalankan salah satu berkas program dari dalam folder proyek:

   ```
   python "CODING MENU 1-2.py"
   ```

   Pada sebagian sistem, gunakan perintah `python3`.

2. **Login** dengan *username* dan *password* yang telah ditentukan di dalam program.
3. **Pilih menu** sesuai nomor yang tampil pada Menu Utama.
4. Tekan **Enter** untuk kembali ke menu setelah hasil ditampilkan.
5. Pilih **0** untuk keluar dari program.

Menu yang tampil pada tiap berkas:

| Berkas | Menu yang tersedia |
|--------|--------------------|
| `CODING MENU 0.py` | 0. Keluar |
| `CODING MENU 1-2.py` | 1. Data Persediaan, 2. Analisis Stok |
| `CODING MENU 3-4.py` | 3. Rekomendasi Pemesanan, 4. Simulasi Pembelian Barang |
| `CODING MENU 5-6.py` | 5. Laporan dan Riwayat, 6. Cari Barang |

---

## 10. Dataset

Berkas `stok_item.csv` memiliki kolom berikut.

| Kolom | Keterangan |
|-------|------------|
| `id` | Nomor urut data. |
| `warehouse_id` | Kode gudang. |
| `sku` | Kode unik barang. |
| `product_name` | Nama barang. |
| `opening_on_hand` | Stok awal (bilangan bulat). |
| `counted_at` | Waktu pencatatan stok. |
| `reorder_point` | Batas stok untuk melakukan pemesanan ulang. |
| `reorder_qty` | Jumlah barang yang dipesan ulang. |
| `lead_time_days` | Waktu tunggu pemesanan (hari). |

Contoh data:

```
id,warehouse_id,sku,product_name,opening_on_hand,counted_at,reorder_point,reorder_qty,lead_time_days
1,1,SKU-428373,Bluetooth Speaker,236,2024-08-31 13:52:30,94,120,5
```

---

## 11. Methodology

### Penentuan Status Barang

Status ditentukan dengan membandingkan **stok saat ini** dengan batas pemesanan ulang. Stok saat ini awalnya sama dengan `opening_on_hand`, lalu berkurang setiap kali simulasi pembelian dilakukan, sehingga status ikut diperbarui.

| Kondisi | Status |
|---------|--------|
| stok saat ini ≤ `reorder_point` | **Perlu pesan** |
| stok saat ini > `reorder_point` | **Aman** |

### Simulasi Pembelian

Simulasi mengurangi stok sementara (hanya di memori, tidak mengubah berkas CSV) dan menampilkan status stok setelah pembelian. Pembelian ditolak apabila:

- SKU tidak ditemukan,
- stok barang sudah habis,
- jumlah pembelian kurang dari atau sama dengan 0, atau bukan angka,
- jumlah pembelian melebihi stok tersedia,
- format tanggal tidak sesuai (`DD-MM-YYYY`),
- alamat pengiriman kosong,
- metode pengiriman tidak valid.

---

## 12. Limitations

- Data disimpan dalam berkas CSV sehingga belum sesuai untuk penggunaan skala besar atau serentak oleh banyak pengguna.
- *Username* dan *password* ditulis langsung di dalam kode dan belum dienkripsi. Program ini ditujukan untuk pembelajaran.
- Hasil simulasi pembelian hanya tersimpan selama program berjalan dan tidak mengubah `stok_item.csv`.
- Karena program dipisah menjadi beberapa berkas, riwayat dan stok hasil simulasi tidak dibagikan antarberkas.
- Penentuan pemesanan hanya memakai batas pemesanan ulang dan belum mempertimbangkan pola permintaan.

---

## 13. Contributors

| No | Nama | NIM |
|----|------|-----|
| 1 | Muhammad Rakha Chandra | 2610932016 |
| 2 | Adib Fawwaz Ramadhan | 2610932044 |
| 3 | Dzaky Rinanda Pratama | 2610933006 |
| 4 | Sayyid Bayhaqi Dinata | 2610933002 |
