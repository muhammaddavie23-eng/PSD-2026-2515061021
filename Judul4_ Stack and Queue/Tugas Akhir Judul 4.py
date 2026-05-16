class StackArray:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Riwayat penuh")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"Buku '{x}' berhasil ditambahkan")

    def pop(self):
        if self.is_empty():
            print("Riwayat kosong")
            return
        print(f"Buku '{self.st[self.top_idx]}' dihapus dari riwayat")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Riwayat kosong")
            return
        print(f"Buku terakhir dibaca: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Riwayat kosong")
            return
        print("\nRiwayat Buku (terbaru ke lama):")
        for i in range(self.top_idx, -1, -1):
            print("-", self.st[i])


def main():
    riwayat = StackArray()
    pilih = 0

    while pilih != 5:
        print("\n=== PROGRAM RIWAYAT BUKU ===")
        print("1. Tambah Buku")
        print("2. Hapus Buku Terakhir")
        print("3. Lihat Buku Terakhir")
        print("4. Tampilkan Semua Riwayat")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            judul = input("Masukkan judul buku: ")
            riwayat.push(judul)

        elif pilih == 2:
            riwayat.pop()

        elif pilih == 3:
            riwayat.peek()

        elif pilih == 4:
            riwayat.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()