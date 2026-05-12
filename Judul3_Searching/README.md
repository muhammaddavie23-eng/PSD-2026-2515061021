Judul Program : mencari nomor kursi bioskop menggunakan Binary Search

Tujuan dari program pencarian nomor kursi bioskop menggunakan Binary Search adalah untuk mempermudah dan mempercepat proses pencarian nomor kursi tertentu dalam daftar kursi yang sudah terurut. Program ini membantu pengguna menemukan posisi kursi yang dicari secara efisien tanpa harus memeriksa satu per satu. Selain itu, program ini bertujuan untuk menerapkan algoritma Binary Search dalam situasi sehari-hari, sehingga proses pencarian data menjadi lebih cepat, akurat, dan efisien terutama ketika jumlah data yang dicari cukup banyak.


code source:
<img width="1356" height="1812" alt="yang bener" src="https://github.com/user-attachments/assets/6c278f45-501d-4427-96c8-581d82ea45a4" />

1.	membuat fungsi pencarian bernama Binary Search untuk mencari nomor kursi tertentu pada daftar data yang sudah terurut. 
2.	Fungsi menerima tiga parameter yaitu daftar data, jumlah data, dan nomor kursi yang dicari. 
3.	Variabel batas kiri dibuat dengan nilai awal indeks pertama. 
4.	Variabel batas kanan dibuat dengan nilai indeks terakhir dari daftar. 
5.	
6.	Variabel posisi dibuat untuk menyimpan hasil pencarian. Nilai awalnya menandakan data belum ditemukan. 
7.	Program menjalankan perulangan selama batas kiri masih kurang dari atau sama dengan batas kanan. 
8.	Program menghitung posisi tengah dari daftar data. 
9.	
10.	Program menampilkan nomor kursi yang sedang diperiksa pada posisi tengah. 
11.	Program memeriksa apakah nomor kursi di tengah sama dengan nomor yang dicari. 
12.	Jika sama, posisi kursi disimpan. 
13.	Pencarian dihentikan karena data sudah ditemukan. 
14.	Jika nomor kursi di tengah lebih kecil dari nomor yang dicari, maka pencarian dilanjutkan ke bagian kanan. 
15.	Program menampilkan pesan bahwa pencarian bergerak ke kanan. 
16.	Batas kiri dipindahkan ke posisi setelah titik tengah. 
17.	Jika nomor kursi di tengah lebih besar dari nomor yang dicari, maka pencarian dilanjutkan ke bagian kiri. 
18.	Program menampilkan pesan bahwa pencarian bergerak ke kiri. 
19.	
20.	Batas kanan dipindahkan ke posisi sebelum titik tengah. 
21.	
22.	
23.	Setelah proses selesai, fungsi mengembalikan posisi data yang ditemukan. 
24.	Program kemudian membuat fungsi utama untuk menjalankan seluruh proses. 
25.	
26.	Program membuat daftar nomor kursi bioskop yang sudah terurut. 
27.	Program menampilkan daftar nomor kursi ke layar. 
28.	
29.	Pengguna diminta memasukkan nomor kursi yang ingin dicari. 
30.	
31.	Program menjalankan fungsi Binary Search untuk mencari nomor kursi tersebut. 
32.	
33.	Hasil pencarian disimpan ke dalam variabel hasil. 
34.	Program memeriksa apakah nomor kursi ditemukan. 
35.	Jika ditemukan, program menampilkan nomor kursi beserta posisi indeksnya. 
36.	Jika tidak ditemukan, program menampilkan pesan bahwa nomor kursi tidak ada. 
37.	
38.	
39.	Program memeriksa apakah file dijalankan secara langsung. 
40.	Jika dijalankan langsung, maka fungsi utama akan dieksekusi. 
Program selesai setelah hasil pencarian ditampilkan kepada pengguna. 



Output:
<img width="327" height="45" alt="Screenshot 2026-05-12 110043" src="https://github.com/user-attachments/assets/9f8c7873-b5e2-42d4-84b8-fa882338929e" />

<img width="356" height="154" alt="Screenshot 2026-05-12 110100" src="https://github.com/user-attachments/assets/6445dd9f-ad38-4efd-8b7a-77d3e911fb08" />



