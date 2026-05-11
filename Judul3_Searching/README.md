Judul Program : mencari nomor kursi bioskop menggunakan Binary Search

Tujuan dari program pencarian nomor kursi bioskop menggunakan Binary Search adalah untuk mempermudah dan mempercepat proses pencarian nomor kursi tertentu dalam daftar kursi yang sudah terurut. Program ini membantu pengguna menemukan posisi kursi yang dicari secara efisien tanpa harus memeriksa satu per satu. Selain itu, program ini bertujuan untuk menerapkan algoritma Binary Search dalam situasi sehari-hari, sehingga proses pencarian data menjadi lebih cepat, akurat, dan efisien terutama ketika jumlah data yang dicari cukup banyak.

code source:
<img width="1418" height="1812" alt="code tugas akhir 3png" src="https://github.com/user-attachments/assets/c6bc4144-2f74-43ad-a37d-3a6f4fcf5cb4" />

1. Program dimulai dengan membuat fungsi pencarian Binary Search yang bertugas mencari data tertentu dalam daftar. 
2.Variabel batas kiri dibuat untuk menandai awal pencarian. 
3. Variabel batas kanan dibuat untuk menandai akhir pencarian. 
4. Variabel posisi diatur dengan nilai awal yang menandakan data belum ditemukan. 
5.
6.Program menjalankan perulangan selama batas kiri masih lebih kecil atau sama dengan batas kanan. 
7.Program menghitung posisi tengah dari data. 
8.Nilai pada posisi tengah ditampilkan agar pengguna bisa melihat proses pencarian.
9.
10.Program membandingkan nilai tengah dengan data yang dicari. 
11.Jika sama, posisi data disimpan. 
12.Pencarian dihentikan karena data sudah ditemukan. 
13.Jika nilai tengah lebih kecil dari data yang dicari, berarti pencarian dilanjutkan ke bagian kanan. 
14.Program menampilkan pesan bahwa pencarian bergeser ke kanan. 
15.Batas kiri diperbarui ke posisi setelah titik tengah. 
16.Jika nilai tengah lebih besar dari data yang dicari, pencarian dilanjutkan ke bagian kiri. 
17.Program menampilkan pesan bahwa pencarian bergeser ke kiri. 
18.Batas kanan diperbarui ke posisi sebelum titik tengah.
19. 
20.Setelah pencarian selesai, program mengembalikan hasil posisi data.
21.
22.
23.Program kemudian menjalankan fungsi utama. 
24. Daftar nomor kursi bioskop dibuat dan disimpan.
25.  
26.Daftar kursi ditampilkan ke layar. 
27.Pengguna diminta memasukkan nomor kursi yang ingin dicari.
28. 
29.Program memanggil fungsi Binary Search untuk mencari nomor kursi tersebut.
30. 
31.Program memeriksa hasil pencarian.
32.
33.Jika ditemukan, program menampilkan posisi kursi. 
34.Jika tidak ditemukan, program menampilkan pesan bahwa kursi tidak ada.
35.
36.
37.
38.
39.
40.
