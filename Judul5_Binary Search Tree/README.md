Judul Program: Sistem Data Barang Toko

Tujuan dari program ini adalah untuk membantu pengelolaan data barang pada sebuah toko dengan menggunakan struktur data Binary Search Tree (BST). Program dibuat agar proses penyimpanan dan pencarian barang menjadi lebih cepat dan teratur berdasarkan kode barang

Source code
<img width="1510" height="5650" alt="code tugas akhir" src="https://github.com/user-attachments/assets/f085c404-53d3-421e-857b-a2f012c164d1" />


1.  mendefinisikan class Node untuk membuat node pada Binary Search Tree.
   
2 mendefinisikan constructor __init__ pada class Node.

3 menyimpan nilai key ke atribut self.key.

4 menyimpan nama barang ke atribut self.nama_barang.

5 mengatur child kiri bernilai None.

6 mengatur child kanan bernilai None.

7

8

9 mendefinisikan class BSTBarang.

10 mendefinisikan constructor class BSTBarang.

11 membuat root awal bernilai None.

12

13 mendefinisikan fungsi insert_node untuk memasukkan node baru.

14 memeriksa apakah root kosong.

15 membuat node baru jika root kosong.

16

17 memeriksa apakah key lebih kecil dari root.key.

18 memasukkan node ke subtree kiri.

19 memeriksa apakah key lebih besar dari root.key.

20 memasukkan node ke subtree kanan.

21

22 mengembalikan root setelah proses insert selesai.

23

24 mendefinisikan fungsi insert.

25 memanggil fungsi insert_node mulai dari root utama.

26

27 mendefinisikan fungsi search_node.

28 memeriksa apakah root kosong.

29 mengembalikan None jika data tidak ditemukan.

30

31 memeriksa apakah key sama dengan root.key.

32 mengembalikan root jika data ditemukan.

33

34 memeriksa apakah key lebih kecil dari root.key.

35 mencari data pada subtree kiri.

36

37 mencari data pada subtree kanan.

38

39 mendefinisikan fungsi search.

40 memanggil fungsi search_node mulai dari root utama.

41

42 mendefinisikan fungsi inorder.

43 memeriksa apakah root kosong.

44 menghentikan fungsi jika root kosong.

45

46 memanggil traversal inorder pada subtree kiri.

47 menampilkan kode barang dan nama barang.

48 memanggil traversal inorder pada subtree kanan.

49

50 mendefinisikan fungsi find_min.

51 memeriksa apakah root kosong.

52 mengembalikan None jika tree kosong.

53

54 menyimpan root ke variabel current.

55 melakukan perulangan selama child kiri masih ada.

56 berpindah ke node kiri berikutnya.

57

58 mengembalikan node dengan nilai terkecil.

59

60 mendefinisikan fungsi find_max.

61 memeriksa apakah root kosong.

62 mengembalikan None jika tree kosong.

63

64 menyimpan root ke variabel current.

65 melakukan perulangan selama child kanan masih ada.

66 berpindah ke node kanan berikutnya.

67

68 mengembalikan node dengan nilai terbesar.

69

70 mendefinisikan fungsi count_nodes.

71 memeriksa apakah root kosong.

72 mengembalikan nilai 0 jika tree kosong.

73

74 menghitung jumlah node secara rekursif.

75

76 mendefinisikan fungsi utama main.

77 membuat objek BST bernama toko.

78 membuat variabel pilih dengan nilai awal 0.

79

80 melakukan perulangan selama pilihan tidak sama dengan 6.

81 menampilkan judul program.

82 menampilkan menu tambah barang.

83 menampilkan menu cari barang.

84 menampilkan menu tampilkan semua barang.

85 menampilkan menu barang dengan kode terkecil.

86 menampilkan menu jumlah barang.

87 menampilkan menu keluar.

88

89 memulai blok try.

90 menerima input pilihan menu dari user.

91 menangkap error jika input bukan angka.

92 menampilkan pesan input tidak valid.

93 melanjutkan perulangan menu.

94

95 memeriksa apakah user memilih menu 1.

96 memulai blok try untuk input barang.

97 menerima input kode barang.

98 menerima input nama barang.

99

100 memasukkan data barang ke BST.

101 menampilkan pesan barang berhasil ditambahkan.

102

103 menangkap error jika input salah.

104 menampilkan pesan input tidak valid.

105 memeriksa apakah user memilih menu 2.

106 memulai blok try untuk pencarian barang.

107 menerima input kode barang yang dicari.

108

109 mencari barang pada BST.

110

111 memeriksa apakah hasil pencarian ditemukan.

112 menampilkan nama barang jika ditemukan.

113 memeriksa kondisi selain ditemukan.

114 menampilkan pesan barang tidak ditemukan.

115

116 menangkap error jika input salah.

117 menampilkan pesan input tidak valid.

118

119 memeriksa apakah user memilih menu 3.

120 menampilkan tulisan daftar barang.

121 menampilkan seluruh data barang secara inorder.

122

123 memeriksa apakah user memilih menu 4.

124 mencari node dengan nilai minimum.

125 memeriksa apakah hasil ditemukan.

126 menampilkan barang dengan kode terkecil.

127 memeriksa kondisi selain ditemukan.

128 menampilkan pesan data kosong.

129

130 memeriksa apakah user memilih menu 5.

131 menampilkan jumlah seluruh barang.

132

133 memeriksa apakah user memilih menu 6.

134 menampilkan pesan program selesai.

135

136 menangani pilihan menu yang tidak tersedia.

137 menampilkan pesan pilihan tidak valid.

138

139

140 memeriksa apakah file dijalankan langsung.

141 menjalankan fungsi main().


link youtube:https://youtu.be/J5NOIa_DE9k](https://youtu.be/O6Ql8er8fZw
