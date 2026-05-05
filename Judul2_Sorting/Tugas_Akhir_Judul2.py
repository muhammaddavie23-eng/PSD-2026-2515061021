def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j]["umur"] > temp["umur"]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def main():
    try:
        n = int(input("Masukkan jumlah orang: "))
        if n <= 0:
            print("Jumlah harus lebih dari 0!")
            return
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan data (nama dan umur):")
    for i in range(n):
        nama = input(f"  Nama orang ke-{i+1}: ")
        while True:
            try:
                umur = int(input(f"  Umur {nama}: "))
                if umur < 0:
                    print("  Umur tidak boleh negatif!")
                    continue
                break
            except ValueError:
                print("  Input tidak valid, masukkan angka!")
        arr.append({"nama": nama, "umur": umur})

    print("\nData sebelum diurutkan:")
    for i, orang in enumerate(arr):
        print(f"  {i+1}. {orang['nama']} - {orang['umur']} tahun")

    insertion_sort(arr, n)

    print("\nData setelah diurutkan (termuda ke tertua):")
    for i, orang in enumerate(arr):
        print(f"  {i+1}. {orang['nama']} - {orang['umur']} tahun")

if __name__ == "__main__":
    main()