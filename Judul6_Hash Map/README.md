
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
10.	Mengatur status awal slot sebagai EMPTY.
11.	
12.	
13.	Membuat kelas HashMap menggunakan metode Open Addressing.
14.	Konstruktor kelas HashMap dengan ukuran default 10.
15.	= Menyimpan ukuran hash table.
16.	Membuat list berisi objek Entry sebanyak ukuran hash table.
17.	
18.	Mendefinisikan fungsi hash.
19.	Menghasilkan indeks hash dan memastikan hasil selalu positif.
20.	
21.	Fungsi untuk menambahkan data ke hash table.
22.	Menghitung indeks awal berdasarkan key.
23.	Menyimpan posisi pertama yang berstatus DELETED.
24.	
25.	Melakukan probing sebanyak ukuran tabel.
26.	Menghitung indeks saat probing linear.
27.	
28.	→ Memeriksa apakah slot sedang terisi.
29.	Memeriksa apakah key sudah ada.
30.	Memperbarui value jika key ditemukan.
31.	Mengembalikan nilai True karena update berhasil.
32.	
33.	Memeriksa apakah slot pernah dihapus.
34.	Memastikan belum ada slot DELETED yang tersimpan.
35.	Menyimpan posisi slot DELETED pertama.
36.	
37.	Jika slot EMPTY ditemukan.
38.	Memeriksa apakah ada slot DELETED sebelumnya.
39.	Menggunakan slot DELETED tersebut.
40.	
41.	Menyimpan key.
42.	Menyimpan value.
43.	 Mengubah status slot menjadi OCCUPIED.
44.	Menandakan data berhasil ditambahkan.
45.	
46.	Jika tidak ditemukan slot kosong tetapi ada slot DELETED.
47.	Menyimpan key pada slot DELETED.
48.	 Menyimpan value pada slot DELETED.
49.	Mengubah status menjadi OCCUPIED.
50.	Menandakan penyisipan berhasil.
51.	
52.	Menandakan hash table penuh.
53.	
54.	Fungsi untuk mencari data berdasarkan key.
55.	Menghitung indeks awal key.
56.	
57.	Melakukan pencarian dengan linear probing.
58.	Menghitung indeks pencarian.
59.	
60.	Jika menemukan slot kosong.
61.	Data tidak ditemukan.
62.	
63.	Memeriksa apakah slot terisi.
64.	Memastikan key sama dengan yang dicari.
65.	Mengembalikan objek Entry yang ditemukan.
66.	
67.	Data tidak ditemukan setelah seluruh probing dilakukan.
68.	
69.	Fungsi untuk menghapus data berdasarkan key.
70.	eMencari data yang akan dihapus.
71.	
72.	Jika data tidak ditemukan.
73.	Mengembalikan False.
74.	
75.	Mengubah status slot menjadi DELETED.
76.	Menandakan data berhasil dihapus.
77.	
78.	Fungsi untuk menampilkan isi hash table.
79.	Menampilkan judul output.
80.	
81.	Melakukan perulangan seluruh indeks.
82.	Menampilkan nomor indeks.
83.	
84.	Jika slot kosong.
85.	Menampilkan EMPTY.
86.	
87.	Jika slot telah dihapus.
88.	Menampilkan DELETED.
89.	
90.	Jika slot berisi data.
91.	Menampilkan key dan value.
92.	
93.	
94.	 Fungsi utama program.
95.	Membuat objek HashMap.
96.	
97.	Perulangan menu hingga pengguna keluar.
98.	Menampilkan judul menu.
99.	Menampilkan menu tambah data.
100.	Menampilkan menu cari data.
101.	Menampilkan menu hapus data.
102.	Menampilkan menu tampil data.
103.	Menampilkan menu keluar.
104.	
105.	Meminta input pilihan pengguna
106.	
107.	Jika memilih tambah data.
108.	Meminta key.
109.	Meminta value.
110.	
111.	Menambahkan data ke hash table.
112. Menampilkan pesan berhasil.
113.	Jika gagal.
114.	Menampilkan pesan tabel penuh.
115.	
116.	Jika memilih cari data.
117.	Meminta key yang dicari.
118.	
119.	Melakukan pencarian.
120.	
121.	Jika data ditemukan.
122.	Key = {hasil.key}, Value = {hasil.value}") → Menampilkan data.
123.	Jika tidak ditemukan.
124.	print("Data tidak ditemukan.") → Menampilkan pesan tidak ditemukan.
125.	
126.	Jika memilih hapus data.
127.	Meminta key yang akan dihapus.
128.	
129.	Menghapus data.
130.	Menampilkan pesan berhasil.
131.	Jika gagal.
132.	Menampilkan pesan gagal.
133.	
134.	Jika memilih tampilkan hash table.
135.	Menampilkan isi hash table.
136.	
137.	Jika memilih keluar.
138.	Menampilkan pesan program selesai.
139.	Menghentikan perulangan.
140.	
141.	Jika pilihan tidak sesuai.
142.	Menampilkan pesan kesalahan.
143.	
144.	
145.	Memastikan file dijalankan sebagai program utama.
146.	Memanggil fungsi utama program.

link youtube:
