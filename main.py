import csv
from collections import deque

FILE_NAME = "buku.csv"
antrian = deque()


# =========================
# INIT FILE CSV
# =========================
def init_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id_buku", "judul", "penulis", "stok"])
    except FileExistsError:
        pass


# =========================
# READ DATA
# =========================
def load_data():
    data = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["stok"] = int(row["stok"])
            data.append(row)

    return data


# =========================
# WRITE DATA
# =========================
def save_data(data):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id_buku", "judul", "penulis", "stok"])
        writer.writeheader()
        writer.writerows(data)


# =========================
# HASH MAP INDEX
# =========================
def index_data(data):
    return {b["id_buku"]: i for i, b in enumerate(data)}


# =========================
# CREATE
# =========================
def tambah_buku():
    data = load_data()

    buku = {
        "id_buku": input("ID Buku: "),
        "judul": input("Judul: "),
        "penulis": input("Penulis: "),
        "stok": int(input("Stok: "))
    }

    data.append(buku)
    save_data(data)

    print("✔ Buku berhasil ditambahkan")


# =========================
# READ
# =========================
def tampilkan_buku():
    data = load_data()

    print("\n=== DAFTAR BUKU ===")
    for b in data:
        print(f"{b['id_buku']} | {b['judul']} | {b['penulis']} | Stok: {b['stok']}")


# =========================
# SEARCH (HASH MAP)
# =========================
def cari_buku():
    data = load_data()
    index = index_data(data)

    id_cari = input("Masukkan ID buku: ")

    if id_cari in index:
        b = data[index[id_cari]]
        print(f"Ditemukan: {b['judul']} ({b['penulis']})")
    else:
        print("Buku tidak ditemukan")


# =========================
# UPDATE
# =========================
def update_buku():
    data = load_data()
    index = index_data(data)

    id_buku = input("ID buku yang diupdate: ")

    if id_buku in index:
        i = index[id_buku]

        data[i]["judul"] = input("Judul baru: ")
        data[i]["penulis"] = input("Penulis baru: ")
        data[i]["stok"] = int(input("Stok baru: "))

        save_data(data)
        print("✔ Data berhasil diupdate")
    else:
        print("Data tidak ditemukan")


# =========================
# DELETE
# =========================
def hapus_buku():
    data = load_data()
    index = index_data(data)

    id_buku = input("ID buku yang dihapus: ")

    if id_buku in index:
        data.pop(index[id_buku])
        save_data(data)
        print("✔ Buku berhasil dihapus")
    else:
        print("Data tidak ditemukan")


# =========================
# SORTING
# =========================
def urutkan_buku():
    data = load_data()

    print("\n1. Judul (A-Z)")
    print("2. Stok (terbanyak)")

    pilih = input("Pilih: ")

    if pilih == "1":
        data.sort(key=lambda x: x["judul"])
    elif pilih == "2":
        data.sort(key=lambda x: x["stok"], reverse=True)

    for b in data:
        print(b)


# =========================
# QUEUE PEMINJAMAN
# =========================
def pinjam_buku():
    nama = input("Nama peminjam: ")
    id_buku = input("ID buku: ")

    antrian.append((nama, id_buku))
    print("✔ Masuk antrian")


def proses_pinjam():
    if not antrian:
        print("Antrian kosong")
        return

    nama, buku = antrian.popleft()
    print(f"{nama} meminjam buku ID {buku}")


# =========================
# MENU UTAMA
# =========================
def menu():
    init_file()

    while True:
        print("""
========= PERPUSTAKAAN =========
1. Tambah Buku
2. Lihat Buku
3. Cari Buku
4. Urutkan Buku
5. Update Buku
6. Hapus Buku
7. Pinjam Buku 
8. Proses Pinjam
0. Keluar
""")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            tampilkan_buku()
        elif pilihan == "3":
            cari_buku()
        elif pilihan == "4":
            urutkan_buku()
        elif pilihan == "5":
            update_buku()
        elif pilihan == "6":
            hapus_buku()
        elif pilihan == "7":
            pinjam_buku()
        elif pilihan == "8":
            proses_pinjam()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid")


menu()
