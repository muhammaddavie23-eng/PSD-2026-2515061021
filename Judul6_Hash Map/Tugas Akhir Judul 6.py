class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True

            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i

            else:
                if first_deleted != -1:
                    i = first_deleted

                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True

        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True

        return False

    def search(self, key):
        idx = self.hash_function(key)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.EMPTY:
                return None

            if (self.table[i].state == SlotState.OCCUPIED and
                    self.table[i].key == key):
                return self.table[i]

        return None

    def remove_key(self, key):
        entry = self.search(key)

        if entry is None:
            return False

        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\n=== ISI HASH TABLE ===")

        for i in range(self.SIZE):
            print(f"Index {i}: ", end="")

            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")

            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")

            else:
                print(f"({self.table[i].key}, {self.table[i].value})")


def main():
    hashmap = HashMapOpenAddressing()

    while True:
        print("\n===== MENU HASH MAP =====")
        print("1. Tambah Data")
        print("2. Cari Data")
        print("3. Hapus Data")
        print("4. Tampilkan Hash Table")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            key = int(input("Masukkan Key : "))
            value = int(input("Masukkan Value : "))

            if hashmap.insert(key, value):
                print("Data berhasil disimpan.")
            else:
                print("Hash Table penuh!")

        elif pilihan == "2":
            key = int(input("Masukkan Key yang dicari: "))

            hasil = hashmap.search(key)

            if hasil:
                print(f"Data ditemukan -> Key = {hasil.key}, Value = {hasil.value}")
            else:
                print("Data tidak ditemukan.")

        elif pilihan == "3":
            key = int(input("Masukkan Key yang akan dihapus: "))

            if hashmap.remove_key(key):
                print("Data berhasil dihapus.")
            else:
                print("Data tidak ditemukan.")

        elif pilihan == "4":
            hashmap.display()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()