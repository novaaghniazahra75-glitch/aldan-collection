from datetime import datetime

# ==============================
# IDENTITAS TOKO
# ==============================
nama_toko = "ALDAN COLLECTION"

# ==============================
# DATA BARANG 
# ==============================
barang_list = [
    {"id": 1, "nama": "Celana Oro", "stok": 20, "harga": 45000},
    {"id": 2, "nama": "Celana Cutbray", "stok": 15, "harga": 45000},
    {"id": 3, "nama": "Celana Etta", "stok": 10, "harga": 45000},
    {"id": 4, "nama": "Kemeja Salur Merah", "stok": 12, "harga": 40000},
    {"id": 5, "nama": "Kemeja Salur Pink", "stok": 8, "harga": 40000},
]

riwayat_transaksi = []

# ==============================
# UTILITAS
# ==============================
def clear():
    print("\n" * 1)

def pause():
    input("\nTekan ENTER untuk melanjutkan...")

def header(judul):
    clear()
    waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print("=" * 60)
    print(nama_toko.center(60))
    print(waktu.center(60))
    print("=" * 60)
    print(judul.center(60))
    print("=" * 60)

def cari_barang_by_id(id_barang):
    for b in barang_list:
        if b["id"] == id_barang:
            return b
    return None

# ==============================
# LOGIN
# ==============================
def login():
    username = "admin"
    password = "admin"

    for _ in range(3):
        clear()
        print("LOGIN SISTEM PERSEDIAAN".center(60))
        print("-" * 60)
        u = input("Username : ")
        p = input("Password : ")

        if u == username and p == password:
            print("\nLogin berhasil!")
            pause()
            return True

        print("Login gagal!")
        pause()

    return False

# ==============================
# CRUD BARANG
# ==============================
def tambah_barang():
    while True:
        header("TAMBAH BARANG")
        id_barang = int(input("ID Barang   : "))
        nama = input("Nama Barang : ")
        stok = int(input("Stok        : "))
        harga = int(input("Harga       : "))

        barang_list.append({
            "id": id_barang,
            "nama": nama,
            "stok": stok,
            "harga": harga
        })

        print("Barang berhasil ditambahkan.")
        
        pilih = input("Tambah barang lagi? (y/n): ").lower()
        if pilih != 'y':
            break
    
    pause()

def tampil_barang():
    header("DAFTAR BARANG")

    if not barang_list:
        print("Data barang kosong.")
        pause()
        return

    per_halaman = 3
    total_halaman = (len(barang_list) + per_halaman - 1) // per_halaman
    halaman = 1

    while True:
        clear()
        print("DAFTAR BARANG".center(60))
        print("-" * 60)
        print("No | ID | Nama Barang           | Stok | Harga")
        print("-" * 60)

        awal = (halaman - 1) * per_halaman
        akhir = awal + per_halaman

        for i, b in enumerate(barang_list[awal:akhir], start=awal + 1):
            print(f"{i:<3}| {b['id']:<3}| {b['nama']:<22}| {b['stok']:<5}| {b['harga']}")

        print("-" * 60)
        print(f"Halaman {halaman} dari {total_halaman}")
        print("[N] Next | [P] Prev | [Q] Keluar")

        pilih = input("Pilih: ").lower()

        if pilih == "n" and halaman < total_halaman:
            halaman += 1
        elif pilih == "p" and halaman > 1:
            halaman -= 1
        elif pilih == "q":
            break

def update_barang():
    while True:
        header("UPDATE BARANG")
        id_barang = int(input("Masukkan ID Barang: "))

        b = cari_barang_by_id(id_barang)
        if b:
            b["nama"] = input("Nama Baru  : ")
            b["stok"] = int(input("Stok Baru  : "))
            b["harga"] = int(input("Harga Baru : "))
            print("Data berhasil diupdate.")
        else:
            print("Barang tidak ditemukan.")
        
        pilih = input("Update barang lagi? (y/n): ").lower()
        if pilih != 'y':
            break
    
    pause()

def hapus_barang():
    while True:
        header("HAPUS BARANG")
        id_barang = int(input("Masukkan ID Barang: "))

        b = cari_barang_by_id(id_barang)
        if b:
            barang_list.remove(b)
            print("Barang berhasil dihapus.")
        else:
            print("Barang tidak ditemukan.")
        
        pilih = input("Hapus barang lagi? (y/n): ").lower()
        if pilih != 'y':
            break
    
    pause()

# ==============================
# BARANG MASUK & KELUAR
# ==============================
def barang_masuk():
    while True:
        header("BARANG MASUK")
        id_barang = int(input("ID Barang     : "))
        jumlah = int(input("Jumlah Masuk  : "))

        b = cari_barang_by_id(id_barang)
        if b:
            b["stok"] += jumlah
            riwayat_transaksi.append({
                "waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                "nama": b["nama"],
                "jenis": "MASUK",
                "jumlah": jumlah
            })
            print("Stok berhasil ditambahkan.")
        else:
            print("Barang tidak ditemukan.")
        
        pilih = input("Tambah barang masuk lagi? (y/n): ").lower()
        if pilih != 'y':
            break
    
    pause()

def barang_keluar():
    while True:
        header("BARANG KELUAR")
        id_barang = int(input("ID Barang      : "))
        jumlah = int(input("Jumlah Keluar  : "))

        b = cari_barang_by_id(id_barang)
        if b:
            if jumlah <= b["stok"]:
                b["stok"] -= jumlah
                riwayat_transaksi.append({
                    "waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                    "nama": b["nama"],
                    "jenis": "KELUAR",
                    "jumlah": jumlah
                })
                print("Stok berhasil dikurangi.")
            else:
                print("Stok tidak mencukupi.")
        else:
            print("Barang tidak ditemukan.")
        
        pilih = input("Tambah barang keluar lagi? (y/n): ").lower()
        if pilih != 'y':
            break
    
    pause()

# ==============================
# LAPORAN
# ==============================
def laporan_riwayat():
    while True:
        header("RIWAYAT TRANSAKSI")

        if not riwayat_transaksi:
            print("Belum ada transaksi.")
        else:
            # Pisahkan transaksi MASUK dan KELUAR
            masuk = [r for r in riwayat_transaksi if r['jenis'] == 'MASUK']
            keluar = [r for r in riwayat_transaksi if r['jenis'] == 'KELUAR']
            
            # Sorting berdasarkan jumlah descending untuk MASUK
            masuk_sorted = sorted(masuk, key=lambda x: x['jumlah'], reverse=True)
            # Sorting berdasarkan jumlah descending untuk KELUAR
            keluar_sorted = sorted(keluar, key=lambda x: x['jumlah'], reverse=True)
            
            # Hitung total
            total_masuk = sum(r['jumlah'] for r in masuk)
            total_keluar = sum(r['jumlah'] for r in keluar)
            
            # Tampilkan dalam satu tabel
            print("-" * 70)
            print("Waktu               | Nama Barang        | Jenis  | Jumlah")
            print("-" * 70)
            
            # Bagian MASUK
            for r in masuk_sorted:
                print(f"{r['waktu']:<20}| {r['nama']:<18}| {r['jenis']:<6}| {r['jumlah']}")
            
            # Pemisah
            print("-" * 70)
            
            # Bagian KELUAR
            for r in keluar_sorted:
                print(f"{r['waktu']:<20}| {r['nama']:<18}| {r['jenis']:<6}| {r['jumlah']}")
            
            # Total
            print("-" * 70)
            print(f"{'TOTAL MASUK':<46}| {total_masuk}")
            print(f"{'TOTAL KELUAR':<46}| {total_keluar}")

        pilih = input("Lihat laporan lagi? (y/n): ").lower()
        if pilih != 'y':
            break
    
    pause()

# ==============================
# MENU
# ==============================
def menu():
    while True:
        header("SISTEM PERSEDIAAN PRODUK FASHION WANITA")
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Barang Masuk")
        print("6. Barang Keluar")
        print("7. Laporan Riwayat")
        print("0. Keluar")

        pilih = input("Pilih Menu: ")

        if pilih == "1":
            tambah_barang()
        elif pilih == "2":
            tampil_barang()
        elif pilih == "3":
            update_barang()
        elif pilih == "4":
            hapus_barang()
        elif pilih == "5":
            barang_masuk()
        elif pilih == "6":
            barang_keluar()
        elif pilih == "7":
            laporan_riwayat()
        elif pilih == "0":
            break

# ==============================
# MAIN PROGRAM
# ==============================
if login():
    menu()
else:
    print("Akses ditolak.")
