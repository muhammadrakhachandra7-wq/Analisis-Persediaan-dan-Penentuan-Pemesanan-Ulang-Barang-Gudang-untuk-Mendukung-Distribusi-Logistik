# Analisis Persediaan dan Penentuan Pemesanan Ulang Barang Gudang untuk Mendukung Distribusi Logistik

Program Python berbasis terminal untuk menganalisis stok barang gudang dan menentukan kapan barang perlu dipesan ulang.

## Fitur

1. **Data Persediaan**: menampilkan seluruh stok barang beserta statusnya.
2. **Analisis Stok**: ringkasan jumlah barang, stok aman, dan barang yang perlu dipesan.
3. **Rekomendasi Pemesanan**: daftar barang yang perlu dipesan, jumlah pesan, dan lead time.
4. **Simulasi Pembelian Barang**: simulasi pembelian dengan validasi stok, tanggal, alamat, dan metode pengiriman.
5. **Laporan dan Riwayat**: laporan persediaan dan riwayat pembelian.
6. **Cari Barang**: pencarian berdasarkan SKU atau nama barang.

## Struktur File

| File | Isi |
|---|---|
| `CODING MENU 1-2.py` | Menu 1 dan 2 |
| `CODING MENU 3-4.py` | Menu 3 dan 4 |
| `CODING MENU 5-6.py` | Menu 5 dan 6 |
| `stok_item.csv` | Data stok barang |

## Cara Menjalankan

1. Pastikan Python 3 sudah terpasang.
2. Simpan semua file dalam satu folder.
3. Jalankan di terminal:

```bash
python "CODING MENU 1-2.py"
```

## Format Data (`stok_item.csv`)

Kolom: `id`, `warehouse_id`, `sku`, `product_name`, `opening_on_hand`, `counted_at`, `reorder_point`, `reorder_qty`, `lead_time_days`.

Barang dianggap **perlu dipesan** jika `opening_on_hand` kurang dari atau sama dengan `reorder_point`.
