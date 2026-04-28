Tugas Akhir Percobaan 1

Judul Program : Sistem Manajemen Toko

Program sistem manajemen toko ini dirancang untuk membantu pengguna mengelola operasional toko dengan cara yang lebih terorganisir dan efektif. Pengguna dapat secara sistematis mencatat informasi barang, seperti nama barang, harga, dan ketersediaan stok, menggunakan program ini. Pengguna dapat dengan mudah mengakses, melihat, dan mengubah informasi kapan pun diperlukan karena struktur data yang terorganisir dengan baik. Fungsi ini menghilangkan kebutuhan bagi manajer atau pemilik toko untuk mencatat data secara manual, yang rentan terhadap kesalahan,dan kehilangan data

Source Code
<img width="1834" height="3674" alt="Tugas akhir" src="https://github.com/user-attachments/assets/f5bd068b-35e8-4ffb-b44c-e039a1f9211b" />

1.Mendefinisikan fungsi bernama menu untuk membungkus kode yang menampilkan daftar pilihan.

2.Mencetak judul sistem ke layar dengan tambahan baris baru di awal agar tampilan lebih rapi.

3.Mencetak opsi pertama menu yang berfungsi untuk menampilkan seluruh data barang

4.Mencetak opsi kedua menu yang digunakan untuk menambah atau memperbarui data barang.

5.5Mencetak opsi ketiga menu yang digunakan untuk melakukan transaksi penjualan.

6.Mencetak opsi keempat menu yang digunakan untuk melihat total pendapatan toko.

7.Mencetak opsi nol sebagai pilihan untuk keluar dari program.

8.

9.Mendefinisikan fungsi utama bernama main yang menjadi tempat seluruh alur logika program dijalankan.

10.Membuat list kosong untuk menyimpan nama-nama barang yang ada di toko.

11.Membuat list kosong untuk menyimpan harga dari setiap barang.

12.Membuat list kosong untuk menyimpan jumlah stok dari setiap barang.

13.Membuat variabel untuk menyimpan total pendapatan yang diperoleh dari transaksi penjualan.

14.

15.Membuat variabel kontrol bernama running dengan nilai awal True sebagai penanda bahwa program akan terus berjalan.

16.Membuat perulangan while yang akan terus dieksekusi selama nilai running bernilai benar.

17.Memanggil fungsi menu untuk menampilkan pilihan menu kepada pengguna.

18.Menggunakan blok try untuk menangani kemungkinan kesalahan saat pengguna memasukkan pilihan menu.

19.Mengambil input dari pengguna untuk memilih menu dan mengubahnya menjadi tipe data integer.

20.Menggunakan except untuk menangkap kesalahan jika input bukan angka dan menampilkan pesan kesalahan.

21-22.Mencetak judul daftar barang yang akan ditampilkan.

23.

25-26.Memeriksa apakah data barang masih kosong dengan mengecek panjang list.

27.Menampilkan pesan bahwa belum ada data barang jika list masih kosong.

28.Menjalankan blok else jika data barang sudah tersedia.

29.Mencetak header tabel yang berisi nomor, nama barang, harga, dan stok dengan format rapi.

30Mencetak garis pemisah untuk memperjelas tampilan tabel.

31.Melakukan perulangan untuk menampilkan seluruh data barang satu per satu.

32.Mencetak setiap data barang berdasarkan index dengan format kolom yang rapi.

33.

34.Memeriksa apakah pengguna memilih menu kedua untuk menambah atau memperbarui barang.

35.Mencetak judul bagian input data barang.

36.Mengambil input nama barang dari pengguna.

37.

38.Memeriksa apakah nama barang sudah ada di dalam list.

39.Mengambil index barang jika sudah ada untuk dilakukan pembaruan data.

40.Menampilkan informasi bahwa data barang akan diperbarui.

41.Menjalankan blok else jika barang belum ada di dalam list.

42.Menambahkan nama barang baru ke dalam list nama barang.

43.Menambahkan nilai awal harga barang sebesar nol ke dalam list harga.

44.Menambahkan nilai awal stok barang sebesar nol ke dalam list stok.

45.Menentukan index dari barang yang baru saja ditambahkan.

46.

47.Menggunakan blok try untuk input harga dan stok agar aman dari kesalahan.
   
48.Mengambil input harga barang dari pengguna dan mengubahnya menjadi integer.

49.Mengambil input jumlah stok barang dari pengguna dan mengubahnya menjadi integer.

50.Menyimpan atau memperbarui nilai harga barang pada index yang sesuai.

51.Menyimpan atau memperbarui jumlah stok barang pada index yang sesuai.

52-53.Menggunakan except untuk menangani kesalahan input yang bukan angka.

54.

55.Memeriksa apakah pengguna memilih menu ketiga untuk melakukan transaksi penjualan.

56.Mencetak judul bagian transaksi penjualan.

57.Memeriksa apakah data barang masih kosong sebelum melakukan transaksi.

58.Menampilkan pesan bahwa belum ada barang jika data kosong lalu kembali ke menu.

59.Melakukan perulangan untuk menampilkan daftar barang beserta stoknya.

60.

61.Mengurangi stok barang sesuai jumlah yang dibeli.

62.Menambahkan hasil transaksi ke total pendapatan toko.

63.

64.Menjalankan sungsi Try

65.Mengambil input pilihan barang dari pengguna dan menyesuaikannya dengan index list.

66.Mengambil input jumlah barang yang ingin dibeli oleh pelanggan.

67.

68.Memeriksa apakah jumlah pembelian tidak melebihi stok yang tersedia.

69.Menghitung total harga berdasarkan jumlah beli dikalikan harga barang.

70.Mengurangi jumlah stok barang sesuai dengan jumlah yang dibeli.

71Menambahkan nilai transaksi ke dalam total pendapatan toko.

72.Menampilkan total pembayaran kepada pengguna.

73-74.Menampilkan pesan jika stok barang tidak mencukupi.

75-76.Menggunakan except untuk menangani kesalahan input saat transaksi.

77.

78.Memeriksa apakah pengguna memilih menu keempat untuk melihat pendapatan.

79.Menampilkan total pendapatan yang telah dikumpulkan dari seluruh transaksi.

80.

81.Memeriksa apakah pengguna memilih menu nol untuk keluar dari program.

82.Mengubah nilai running menjadi False agar perulangan berhenti.

83.Menampilkan pesan bahwa program telah selesai dijalankan.

84.

85-86.Menangani kondisi jika pengguna memasukkan pilihan menu yang tidak tersedia.

87.

88-89.Memastikan fungsi main dijalankan hanya ketika file program dieksekusi secara langsung




Output : Menu
<img width="299" height="171" alt="Screenshot 2026-04-28 204350" src="https://github.com/user-attachments/assets/7e91a37e-f5fa-4515-98b2-cfee58b0f445" />

Menu 1 (belum ada inputan)
<img width="299" height="234" alt="Screenshot 2026-04-28 204446" src="https://github.com/user-attachments/assets/39fdba9e-51bc-4fd9-93cb-13e232cf2447" />

Menu 2 (menambahkan barang)
<img width="287" height="102" alt="Screenshot 2026-04-28 204508" src="https://github.com/user-attachments/assets/c8e20696-37ba-4d92-a176-febeb2db9908" />

Menu 1 (setelah di beri inputan)
<img width="372" height="155" alt="Screenshot 2026-04-28 205517" src="https://github.com/user-attachments/assets/c2ed94b8-689e-48cb-af19-2fa886a4dfb5" />

Menu 3
<img width="282" height="132" alt="Screenshot 2026-04-28 204609" src="https://github.com/user-attachments/assets/2cd29959-0873-446a-9c5e-5e3614466cd9" />

Menu 4
<img width="264" height="71" alt="Screenshot 2026-04-28 204635" src="https://github.com/user-attachments/assets/b0e049b0-8749-4a88-8a67-ce376497e452" />

Menu 0
<img width="294" height="165" alt="Screenshot 2026-04-28 204653" src="https://github.com/user-attachments/assets/2ea12e30-1e34-45c7-aa73-f67c8872dfd5" />




