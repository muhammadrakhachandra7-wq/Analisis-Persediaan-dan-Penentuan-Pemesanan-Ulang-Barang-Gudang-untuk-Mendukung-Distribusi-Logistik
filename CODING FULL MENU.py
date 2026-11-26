import csv
from datetime import datetime

FILE = "stok_item.csv"
RIWAYAT = []
STOK_SEMENTARA = {}


def baca_data():
    try:
        with open(FILE, newline="", encoding="utf-8-sig") as f:
            data = list(csv.DictReader(f))

        wajib = ["id", "warehouse_id", "sku", "product_name",
                 "opening_on_hand", "counted_at", "reorder_point",
                 "reorder_qty", "lead_time_days"]

        if not data or not all(k in data[0] for k in wajib):
            print("Format CSV tidak sesuai.")
            return []

        for x in data:
            for k in ["opening_on_hand", "reorder_point",
                      "reorder_qty", "lead_time_days"]:
                x[k] = int(x[k])

            STOK_SEMENTARA[x["sku"]] = x["opening_on_hand"]

        return data

    except FileNotFoundError:
        print("File stok_item.csv tidak ditemukan.")
        return []
    except (ValueError, KeyError):
        print("Data CSV tidak valid.")
        return []


def status(x):
    stok = STOK_SEMENTARA[x["sku"]]
    return "Perlu pesan" if stok <= x["reorder_point"] else "Aman"


def tampil(data, sementara=False):
    if not data:
        print("Data tidak tersedia.")
        return

    print("-" * 90)
    print(f"{'SKU':<15}{'Nama Barang':<28}{'Gudang':<10}{'Stok':<10}{'Batas':<10}{'Status'}")
    print("-" * 90)

    for x in data:
        stok = STOK_SEMENTARA[x["sku"]]
        print(f"{x['sku']:<15}{x['product_name'][:26]:<28}{x['warehouse_id']:<10}{stok:<10}{x['reorder_point']:<10}{status(x)}")

    print("-" * 90)


def cari(data):
    kata = input("Masukkan SKU atau nama barang: ").lower()

    hasil = [
        x for x in data
        if kata in x["sku"].lower()
        or kata in x["product_name"].lower()
    ]

    tampil(hasil) if hasil else print("Barang tidak ditemukan.")


def analisis(data):
    aman = [x for x in data if status(x) == "Aman"]
    pesan = [x for x in data if status(x) == "Perlu pesan"]

    print("Jumlah barang:", len(data))
    print("Stok aman:", len(aman))
    print("Perlu pesan ulang:", len(pesan))
    print("Total stok:", sum(STOK_SEMENTARA[x["sku"]] for x in data))

    print("\nBarang perlu dipesan:")
    tampil(pesan)


def rekomendasi(data):
    hasil = [x for x in data if status(x) == "Perlu pesan"]

    if not hasil:
        print("Tidak ada barang yang perlu dipesan.")
        return

    for x in hasil:
        print(f"{x['sku']} - {x['product_name']} | "
              f"Pesan: {x['reorder_qty']} unit | "
              f"Lead time: {x['lead_time_days']} hari")


def simulasi(data):
    print("\nSIMULASI PEMBELIAN BARANG")
    tampil(data, sementara=True)

    sku = input("\nMasukkan SKU barang: ").strip().lower()

    x = next((i for i in data if i["sku"].lower() == sku), None)

    if not x:
        print("Barang tidak ditemukan.")
        return

    stok = STOK_SEMENTARA[x["sku"]]

    if stok <= 0:
        print("Pembelian ditolak. Stok barang sudah habis.")
        return

    try:
        jumlah = int(input("Masukkan jumlah pembelian: "))

        if jumlah <= 0:
            print("Jumlah pembelian harus lebih dari 0.")
            return

        if jumlah > stok:
            print("Pembelian ditolak. Stok tidak mencukupi.")
            print("Stok tersedia:", stok, "unit")
            return

    except ValueError:
        print("Jumlah pembelian harus berupa angka.")
        return

    tanggal = input("Tanggal pembelian (DD-MM-YYYY): ")

    try:
        tanggal = datetime.strptime(tanggal, "%d-%m-%Y").strftime("%d-%m-%Y")
    except ValueError:
        print("Format tanggal salah.")
        return

    alamat = input("Alamat pengiriman: ").strip()

    if not alamat:
        print("Alamat tidak boleh kosong.")
        return

    print("\n1. Darat")
    print("2. Laut")
    print("3. Udara")

    metode = {
        "1": "Darat",
        "2": "Laut",
        "3": "Udara"
    }.get(input("Pilih metode pengiriman: "))

    if not metode:
        print("Metode pengiriman tidak valid.")
        return

    akhir = stok - jumlah
    STOK_SEMENTARA[x["sku"]] = akhir

    transaksi = {
        "tanggal": tanggal,
        "sku": x["sku"],
        "nama": x["product_name"],
        "jumlah": jumlah,
        "stok_awal": stok,
        "stok_akhir": akhir,
        "alamat": alamat,
        "metode": metode
    }

    RIWAYAT.append(transaksi)

    print("\nPEMBELIAN BERHASIL")
    print("Tanggal:", tanggal)
    print("Barang:", x["product_name"])
    print("Jumlah dibeli:", jumlah, "unit")
    print("Stok sebelum pembelian:", stok)
    print("Sisa stok simulasi:", akhir)
    print("Status stok:", status(x))
    print("Alamat pengiriman:", alamat)
    print("Metode pengiriman:", metode)


def laporan(data):
    print("\nLAPORAN PERSEDIAAN")
    analisis(data)

    print("\nSTOK SEMENTARA SETELAH SIMULASI")
    tampil(data, sementara=True)

    print("\nRIWAYAT PEMBELIAN")
    print("Jumlah transaksi:", len(RIWAYAT))

    if not RIWAYAT:
        print("Belum ada transaksi.")
        return

    for r in RIWAYAT:
        print(f"{r['tanggal']} | {r['sku']} | {r['nama']} | "
              f"{r['jumlah']} unit | Sisa: {r['stok_akhir']} unit | "
              f"{r['metode']}")


def main():
    print("SISTEM PERSEDIAAN BARANG GUDANG")

    if input("Username: ") != "admin" or input("Password: ") != "admin123":
        print("Login gagal.")
        return

    data = baca_data()

    if not data:
        return

    while True:
        print("\n===== MENU UTAMA =====")
        print("1. Data Persediaan")
        print("2. Analisis Stok")
        print("3. Rekomendasi Pemesanan")
        print("4. Simulasi Pembelian Barang")
        print("5. Laporan dan Riwayat")
        print("6. Cari Barang")
        print("0. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tampil(data)

        elif pilih == "2":
            analisis(data)

        elif pilih == "3":
            rekomendasi(data)

        elif pilih == "4":
            simulasi(data)

        elif pilih == "5":
            laporan(data)

        elif pilih == "6":
            cari(data)

        elif pilih == "0":
            print("Terima kasih.")
            break

        else:
            print("Pilihan tidak valid.")

        input("\nTekan Enter untuk kembali...")


main()