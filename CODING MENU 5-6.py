import csv

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
    return "Perlu pesan" if x["opening_on_hand"] <= x["reorder_point"] else "Aman"


def tampil(data, sementara=False):
    if not data:
        print("Data tidak tersedia.")
        return

    print("-" * 90)
    print(f"{'SKU':<15}{'Nama Barang':<28}{'Gudang':<10}{'Stok':<10}{'Batas':<10}{'Status'}")
    print("-" * 90)

    for x in data:
        stok = STOK_SEMENTARA[x["sku"]] if sementara else x["opening_on_hand"]
        print(f"{x['sku']:<15}{x['product_name'][:26]:<28}{x['warehouse_id']:<10}{stok:<10}{x['reorder_point']:<10}{status(x)}")

    print("-" * 90)


def analisis(data):
    aman = [x for x in data if status(x) == "Aman"]
    pesan = [x for x in data if status(x) == "Perlu pesan"]

    print("Jumlah barang:", len(data))
    print("Stok aman:", len(aman))
    print("Perlu pesan ulang:", len(pesan))
    print("Total stok:", sum(x["opening_on_hand"] for x in data))

    print("\nBarang perlu dipesan:")
    tampil(pesan)


def cari(data):
    kata = input("Masukkan SKU atau nama barang: ").lower()

    hasil = [
        x for x in data
        if kata in x["sku"].lower()
        or kata in x["product_name"].lower()
    ]

    tampil(hasil) if hasil else print("Barang tidak ditemukan.")


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
        print("5. Laporan dan Riwayat")
        print("6. Cari Barang")
        print("0. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "5":
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