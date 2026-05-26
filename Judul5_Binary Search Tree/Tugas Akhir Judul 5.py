class Node:
    def __init__(self, key, nama_barang):
        self.key = key
        self.nama_barang = nama_barang
        self.left = None
        self.right = None


class BSTBarang:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key, nama_barang):
        if root is None:
            return Node(key, nama_barang)

        if key < root.key:
            root.left = self.insert_node(root.left, key, nama_barang)
        elif key > root.key:
            root.right = self.insert_node(root.right, key, nama_barang)

        return root

    def insert(self, key, nama_barang):
        self.root = self.insert_node(self.root, key, nama_barang)

    def search_node(self, root, key):
        if root is None:
            return None

        if root.key == key:
            return root

        if key < root.key:
            return self.search_node(root.left, key)

        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(f"Kode: {root.key} | Barang: {root.nama_barang}")
        self.inorder(root.right)

    def find_min(self, root):
        if root is None:
            return None

        current = root
        while current.left is not None:
            current = current.left

        return current

    def find_max(self, root):
        if root is None:
            return None

        current = root
        while current.right is not None:
            current = current.right

        return current

    def count_nodes(self, root):
        if root is None:
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)


def main():
    toko = BSTBarang()
    pilih = 0

    while pilih != 6:
        print("\n=== SISTEM DATA BARANG TOKO ===")
        print("1. Tambah Barang")
        print("2. Cari Barang")
        print("3. Tampilkan Semua Barang")
        print("4. Barang dengan Kode Terkecil")
        print("5. Jumlah Barang")
        print("6. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                kode = int(input("Masukkan kode barang: "))
                nama = input("Masukkan nama barang: ")

                toko.insert(kode, nama)
                print("Barang berhasil ditambahkan")

            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            try:
                kode = int(input("Masukkan kode barang yang dicari: "))

                hasil = toko.search(kode)

                if hasil:
                    print(f"Barang ditemukan: {hasil.nama_barang}")
                else:
                    print("Barang tidak ditemukan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            print("\nDaftar Barang:")
            toko.inorder(toko.root)

        elif pilih == 4:
            hasil = toko.find_min(toko.root)
            if hasil:
                print(f"Barang dengan kode terkecil: {hasil.nama_barang}")
            else:
                print("Data kosong")

        elif pilih == 5:
            print(f"Jumlah barang: {toko.count_nodes(toko.root)}")

        elif pilih == 6:
            print("Program selesai")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()