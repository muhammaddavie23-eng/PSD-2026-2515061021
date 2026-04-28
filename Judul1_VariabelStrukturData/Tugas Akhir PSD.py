def menu():
    print("\n=== SISTEM MANAJEMEN TOKO ===")
    print("1. Tampilkan Semua Barang")
    print("2. Tambah / Update Barang")
    print("3. Transaksi Penjualan")
    print("4. Lihat Total Pendapatan")
    print("0. Keluar")

def main():
    nama_barang = []
    harga_barang = []
    stok_barang = []
    total_pendapatan = 0

    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilih menu: "))
        except ValueError:
            print("Masukkan angka yang benar!")
            continue

        if choice == 1:
            print("\n=== DAFTAR BARANG ===")
            if len(nama_barang) == 0:
                print("Belum ada data barang.")
            else:
                print(f"{'No':<5}{'Nama':<15}{'Harga':<10}{'Stok':<10}")
                print("-" * 40)
                for i in range(len(nama_barang)):
                    print(f"{i+1:<5}{nama_barang[i]:<15}{harga_barang[i]:<10}{stok_barang[i]:<10}")

        elif choice == 2:
            print("\n=== TAMBAH / UPDATE BARANG ===")
            nama = input("Masukkan nama barang: ")

            if nama in nama_barang:
                index = nama_barang.index(nama)
                print("Barang sudah ada, update data.")
            else:
                nama_barang.append(nama)
                harga_barang.append(0)
                stok_barang.append(0)
                index = len(nama_barang) - 1

            try:
                harga = int(input("Masukkan harga: "))
                stok = int(input("Masukkan stok: "))
                harga_barang[index] = harga
                stok_barang[index] = stok
            except ValueError:
                print("Input harus angka!")

        elif choice == 3:
            print("\n=== TRANSAKSI PENJUALAN ===")
            if len(nama_barang) == 0:
                print("Belum ada barang.")
                continue

            for i in range(len(nama_barang)):
                print(f"{i+1}. {nama_barang[i]} (Stok: {stok_barang[i]})")

            try:
                pilih = int(input("Pilih barang: ")) - 1
                jumlah = int(input("Jumlah beli: "))

                if jumlah <= stok_barang[pilih]:
                    total = jumlah * harga_barang[pilih]
                    stok_barang[pilih] -= jumlah
                    total_pendapatan += total
                    print(f"Total bayar: {total}")
                else:
                    print("Stok tidak cukup!")
            except:
                print("Input salah!")

        elif choice == 4:
            print(f"\nTotal Pendapatan: {total_pendapatan}")

        elif choice == 0:
            running = False
            print("Program selesai.")

        else:
            print("Menu tidak tersedia.")

if __name__ == "__main__":
    main()