# Analisis Persediaan dan Penentuan Pemesanan Ulang Barang Gudang untuk Mendukung Distribusi Logistik

Program berbasis antarmuka teks (*command line*) yang dikembangkan dengan bahasa Python untuk menganalisis stok barang gudang, menentukan barang yang perlu dipesan ulang, dan mensimulasikan pembelian barang. Penentuan pemesanan ulang menggunakan pendekatan **titik pemesanan ulang (*reorder point*)**.

---

## Daftar Isi

1. [Latar Belakang](#latar-belakang)
2. [Tujuan](#tujuan)
3. [Fitur Utama](#fitur-utama)
4. [Metodologi](#metodologi)
5. [Struktur Repositori](#struktur-repositori)
6. [Persyaratan Sistem](#persyaratan-sistem)
7. [Cara Menjalankan Program](#cara-menjalankan-program)
8. [Panduan Penggunaan](#panduan-penggunaan)
9. [Format Data](#format-data)
10. [Keterbatasan](#keterbatasan)
11. [Tim Pengembang](#tim-pengembang)

---

## Latar Belakang

Kelancaran distribusi logistik sangat bergantung pada ketersediaan barang di gudang. Stok yang terlalu sedikit menyebabkan keterlambatan pengiriman, sedangkan pemesanan ulang yang terlambat menambah risiko kehabisan barang. Program ini membantu pengelola gudang memantau stok, mengetahui barang yang sudah mencapai batas pemesanan ulang, dan melihat jumlah serta waktu tunggu (*lead time*) pemesanannya.

## Tujuan

- Menampilkan data persediaan barang gudang beserta statusnya.
- Menentukan barang yang perlu dipesan ulang berdasarkan batas pemesanan (*reorder point*).
- Memberikan rekomendasi jumlah pesanan dan lead time untuk tiap barang.
- Mensimulasikan pembelian barang beserta pembaruan stok sementara.
- Menyajikan laporan persediaan dan riwayat pembelian.

## Fitur Utama

| No | Fitur | Keterangan |
|----|-------|------------|
| 1 | Data Persediaan | Menampilkan SKU, nama barang, gudang, stok, batas pemesanan, dan status. |
| 2 | Analisis Stok | Ringkasan jumlah barang, stok aman, barang perlu dipesan, dan total stok. |
| 3 | Rekomendasi Pemesanan | Daftar barang yang perlu dipesan beserta jumlah pesan dan lead time. |
| 4 | Simulasi Pembelian Barang | Simulasi pembelian dengan validasi stok, jumlah, tanggal, alamat, dan metode pengiriman (darat, laut, udara). |
| 5 | Laporan dan Riwayat | Laporan persediaan, stok sementara setelah simulasi, dan riwayat pembelian. |
| 6 | Cari Barang | Pencarian berdasarkan SKU atau nama barang. |

Program dilindungi *login* sederhana sebelum menu utama ditampilkan.

## Metodologi

### Penentuan Status Barang

Status setiap barang ditentukan dengan membandingkan stok saat ini dengan batas pemesanan ulang.

| Kondisi | Status |
|---------|--------|
| `opening_on_hand` ≤ `reorder_point` | **Perlu pesan** |
| `opening_on_hand` > `reorder_point` | **Aman** |

### Simulasi Pembelian

Simulasi mengurangi stok sementara (hanya di memori, tidak mengubah berkas CSV). Pembelian ditolak apabila:

- SKU tidak ditemukan,
- stok barang sudah habis,
- jumlah pembelian kurang dari atau sama dengan 0, atau bukan angka,
- jumlah pembelian melebihi stok tersedia,
- format tanggal tidak sesuai (`DD-MM-YYYY`),
- alamat pengiriman kosong,
- metode pengiriman tidak valid.

## Struktur Repositori

```
.
├── CODING MENU 1-2.py   # Menu 1 (Data Persediaan) dan Menu 2 (Analisis Stok)
├── CODING MENU 3-4.py   # Menu 3 (Rekomendasi Pemesanan) dan Menu 4 (Simulasi Pembelian)
├── CODING MENU 5-6.py   # Menu 5 (Laporan dan Riwayat) dan Menu 6 (Cari Barang)
├── stok_item.csv        # Data persediaan barang
└── README.md            # Dokumentasi
```

## Persyaratan Sistem

- Python versi 3.6 atau yang lebih baru.
- Tidak memerlukan pustaka tambahan (hanya pustaka standar: `csv` dan `datetime`).

## Cara Menjalankan Program

1. Kloning repositori:

   ```
   git clone https://github.com/muhammadrakhachandra7-wq/Analisis-Persediaan-dan-Penentuan-Pemesanan-Ulang-Barang-Gudang-untuk-Mendukung-Distribusi-Logistik.git
   cd Analisis-Persediaan-dan-Penentuan-Pemesanan-Ulang-Barang-Gudang-untuk-Mendukung-Distribusi-Logistik
   ```

   > Sesuaikan alamat di atas dengan URL repositori yang tampil di tombol **Code** pada GitHub.

2. Jalankan salah satu berkas program:

   ```
   python "CODING MENU 1-2.py"
   ```

   Pada sebagian sistem, gunakan perintah `python3`.

> **Catatan:** Jalankan program dari dalam folder repositori agar `stok_item.csv` dapat terbaca.

## Panduan Penggunaan

1. **Login.** Masukkan *username* dan *password* yang telah ditentukan di dalam program.
2. **Pilih menu** sesuai nomor yang tampil pada Menu Utama.
3. Tekan **Enter** untuk kembali ke menu setelah hasil ditampilkan.
4. Pilih **0** untuk keluar dari program.

Setiap berkas program menampilkan menu sesuai pasangannya:

| Berkas | Menu yang tersedia |
|--------|--------------------|
| `CODING MENU 1-2.py` | 1. Data Persediaan, 2. Analisis Stok |
| `CODING MENU 3-4.py` | 3. Rekomendasi Pemesanan, 4. Simulasi Pembelian Barang |
| `CODING MENU 5-6.py` | 5. Laporan dan Riwayat, 6. Cari Barang |

## Format Data

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

Contoh:

```
id,warehouse_id,sku,product_name,opening_on_hand,counted_at,reorder_point,reorder_qty,lead_time_days
1,1,SKU-428373,Bluetooth Speaker,236,2024-08-31 13:52:30,94,120,5
```

## Keterbatasan

- Data disimpan dalam berkas CSV sehingga belum sesuai untuk penggunaan skala besar atau serentak oleh banyak pengguna.
- *Username* dan *password* ditulis langsung di dalam kode dan belum dienkripsi. Program ini ditujukan untuk pembelajaran.
- Hasil simulasi pembelian hanya tersimpan selama program berjalan dan tidak mengubah `stok_item.csv`.
- Karena program dipisah menjadi tiga berkas, riwayat pembelian pada `CODING MENU 5-6.py` tidak memuat transaksi dari `CODING MENU 3-4.py`.
- Penentuan pemesanan hanya memakai batas pemesanan ulang dan belum mempertimbangkan pola permintaan.

## Tim Pengembang

**Kelompok [...]**

| No | Nama | NIM |
|----|------|-----|
| 1 | [Nama] | [NIM] |
| 2 | [Nama] | [NIM] |
| 3 | [Nama] | [NIM] |
