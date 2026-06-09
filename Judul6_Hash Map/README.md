Tujuan: Program ini memungkinkan pengguna untuk menambah data, mencari data, menghapus data, dan menampilkan isi hash table

Source Code:
<img width="1616" height="5878" alt="code TA judul 6" src="https://github.com/user-attachments/assets/522e90e4-ba22-4ec3-b3a0-6a90c6959c27" />

1.	 Membuat kelas untuk menyimpan status setiap slot pada hash table.
2.	Menandakan slot masih kosong dan belum pernah digunakan.
3.	Menandakan slot sedang berisi data.
4.	Menandakan data pada slot telah dihapus.
5.	
6.	
7.	Membuat kelas Entry yang digunakan sebagai elemen penyimpan data pada hash table.
8.	Konstruktor kelas Entry yang dijalankan saat objek dibuat.
9.	Menginisialisasi value dengan nilai kosong.
10.	Mengatur status nilai slot sebagai EMPTY.
11.	Mengatur status awal slot sebagai EMPTY.
12.	
13.
14.	Membuat kelas HashMap menggunakan metode Open Addressing.
15.	Konstruktor kelas HashMap dengan ukuran default 10.
16.	= Menyimpan ukuran hash table.
17.	Membuat list berisi objek Entry sebanyak ukuran hash table.
18.	
19.	Mendefinisikan fungsi hash.
20.	Menghasilkan indeks hash dan memastikan hasil selalu positif.
21.	
22.	Fungsi untuk menambahkan data ke hash table.
23.	Menghitung indeks awal berdasarkan key.
24.	Menyimpan posisi pertama yang berstatus DELETED.
25.	
26.	Melakukan probing sebanyak ukuran tabel.
27.	Menghitung indeks saat probing linear.
28.	
29.	→ Memeriksa apakah slot sedang terisi.
30.	Memeriksa apakah key sudah ada.
31.	Memperbarui value jika key ditemukan.
32.	Mengembalikan nilai True karena update berhasil.
33.	
34.	Memeriksa apakah slot pernah dihapus.
35.	Memastikan belum ada slot DELETED yang tersimpan.
36.	Menyimpan posisi slot DELETED pertama.
37.	
38.	Jika slot EMPTY ditemukan.
39.	Memeriksa apakah ada slot DELETED sebelumnya.
40.	Menggunakan slot DELETED tersebut.
41.	
42.	Menyimpan key.
43.	Menyimpan value.
44.	 Mengubah status slot menjadi OCCUPIED.
45.	Menandakan data berhasil ditambahkan.
46.	
47.	Jika tidak ditemukan slot kosong tetapi ada slot DELETED.
48.	Menyimpan key pada slot DELETED.
49.	 Menyimpan value pada slot DELETED.
50.	Mengubah status menjadi OCCUPIED.
51.	Menandakan penyisipan berhasil.
52.	
53.	Menandakan hash table penuh.
54.	
55.	Fungsi untuk mencari data berdasarkan key.
56.	Menghitung indeks awal key.
57.	
58.	Melakukan pencarian dengan linear probing.
59.	Menghitung indeks pencarian.
60.	
61.	Jika menemukan slot kosong.
62.	Data tidak ditemukan.
63.	
64.	Memeriksa apakah slot terisi.
65.	Memastikan key sama dengan yang dicari.
66.	Mengembalikan objek Entry yang ditemukan.
67.	
68.	Data tidak ditemukan setelah seluruh probing dilakukan.
69.	
70.	Fungsi untuk menghapus data berdasarkan key.
71.	eMencari data yang akan dihapus.
72.	
73.	Jika data tidak ditemukan.
74.	Mengembalikan False.
75.	
76.	Mengubah status slot menjadi DELETED.
77.	Menandakan data berhasil dihapus.
78.	
79.	Fungsi untuk menampilkan isi hash table.
80.	Menampilkan judul output.
81.	
82.	Melakukan perulangan seluruh indeks.
83.	Menampilkan nomor indeks.
84.	
85.	Jika slot kosong.
86.	Menampilkan EMPTY.
87.	
88.	Jika slot telah dihapus.
89.	Menampilkan DELETED.
90.	
91.	Jika slot berisi data.
92.	Menampilkan key dan value.
93.	
94.	
95.	 Fungsi utama program.
96.	Membuat objek HashMap.
97.	
98.	Perulangan menu hingga pengguna keluar.
99.	Menampilkan judul menu.
100.	Menampilkan menu tambah data.
101.	Menampilkan menu cari data.
102.	Menampilkan menu hapus data.
103.	Menampilkan menu tampil data.
104.	Menampilkan menu keluar.
105.	
106.	Meminta input pilihan pengguna
107.	
108.	Jika memilih tambah data.
109.	Meminta key.
110.	Meminta value.
111.	
112.	Menambahkan data ke hash table.
113. Menampilkan pesan berhasil.
114.	Jika gagal.
115.	Menampilkan pesan tabel penuh.
116.	
117.	Jika memilih cari data.
118.	Meminta key yang dicari.
119.	
120.	Melakukan pencarian.
121.	
122.	Jika data ditemukan.
123.	Key = {hasil.key}, Value = {hasil.value}") → Menampilkan data.
124.	Jika tidak ditemukan.
125.	print("Data tidak ditemukan.") → Menampilkan pesan tidak ditemukan.
126.	
127.	Jika memilih hapus data.
128.	Meminta key yang akan dihapus.
129.	
130.	Menghapus data.
131.	Menampilkan pesan berhasil.
132.	Jika gagal.
133.	Menampilkan pesan gagal.
134.	
135.	Jika memilih tampilkan hash table.
136.	Menampilkan isi hash table.
137.	
138.	Jika memilih keluar.
139.	Menampilkan pesan program selesai.
140.	Menghentikan perulangan.
141.	
142.	Jika pilihan tidak sesuai.
143.	Menampilkan pesan kesalahan.
144.	
145.	
146.	Memastikan file dijalankan sebagai program utama.
147.	Memanggil fungsi utama program.

Pilihan Menu:
<img width="264" height="147" alt="Screenshot 2026-06-09 210411" src="https://github.com/user-attachments/assets/202e41e4-de8f-4ff1-81e8-ce9d3bf9c5c9" />

inputan 1:
<img width="234" height="102" alt="Screenshot 2026-06-09 210421" src="https://github.com/user-attachments/assets/95690678-2a06-44a6-a4cd-dff98a336191" />
<img width="225" height="99" alt="Screenshot 2026-06-09 210436" src="https://github.com/user-attachments/assets/b019de2f-5b2a-4b10-9ac9-bfb4bf055719" />

inputan 2:
<img width="364" height="78" alt="Screenshot 2026-06-09 210453" src="https://github.com/user-attachments/assets/89aa7a6f-36c4-4ac0-933b-b90b072fb74a" />

inputan 3:
<img width="318" height="72" alt="Screenshot 2026-06-09 210504" src="https://github.com/user-attachments/assets/3ecc3796-1b1e-4266-8442-1a2c70785301" />
<img width="316" height="68" alt="Screenshot 2026-06-09 210514" src="https://github.com/user-attachments/assets/1cb4d1ce-015b-40d8-9b2f-45d9a86da619" />

inputan 4:
<img width="223" height="286" alt="Screenshot 2026-06-09 210528" src="https://github.com/user-attachments/assets/f8d02321-923a-468e-8b93-62a8f0656e83" />

inputan 5:
<img width="415" height="187" alt="Screenshot 2026-06-09 210538" src="https://github.com/user-attachments/assets/e1956f24-1b99-471b-89a1-2f2f8411fc23" />



link youtube:
