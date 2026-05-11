def binary_search(arr, n, target):
    l = 0
    r = n - 1
    pos = -1

    while l <= r:
        m = l + (r - l) // 2
        print(f"Cek data tengah: {arr[m]}")

        if arr[m] == target:
            pos = m
            break
        elif arr[m] < target:
            print("Mencari harga lebih besar")
            l = m + 1
        else:
            print("Mencari harga lebih kecil")
            r = m - 1

    return pos


def main():
    harga_produk = [2000, 5000, 7000, 10000, 15000, 20000, 25000, 30000]

    print("Daftar harga produk:")
    print(harga_produk)

    target = int(input("Masukkan harga produk yang dicari: "))

    hasil = binary_search(harga_produk, len(harga_produk), target)

    if hasil != -1:
        print(f"Harga Rp{target} ditemukan pada indeks ke-{hasil}")
    else:
        print("Harga produk tidak ditemukan")


if __name__ == "__main__":
    main()