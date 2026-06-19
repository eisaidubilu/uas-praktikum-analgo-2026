# Pipeline Simulasi Optimasi Rute Last-Mile Delivery

## Anggota Kelompok
1. Syaikha Habibtiana Widi Sukamto - 140810240025
2. Fitri Sahwalia - 140810240031
3. Syifa Azzahra - 140810240041
4. Aisha Kinasih Susanto - 140810240047

## Latar Belakang
Perusahaan ekspedisi lokal saat ini menghadapi dilema efisiensi operasional pada pengantaran rute terakhir (Last-Mile Delivery). Sistem yang berjalan saat ini menggunakan algoritma heuristik dasar yang pengerjaannya sangat cepat dan hemat biaya server, namun rute yang dihasilkan sering kali sub-optimal (memutar) sehingga boros Bahan Bakar Minyak (BBM). Di sisi lain, manajemen berencana memperbarui sistem ke algoritma eksak tingkat lanjut demi rute yang absolut efisien, tetapi algoritma ini memakan waktu komputasi eksponensial yang berisiko melonjakkan tagihan Cloud Server dengan sistem *Pay-as-you-go*. Oleh karena itu, diperlukan sebuah pipeline simulasi untuk membandingkan kedua arsitektur algoritma ini guna menentukan skenario ekonomi mana yang paling menguntungkan secara finansial bagi perusahaan.

## Tujuan
1. Membangun pipeline simulasi komputasi untuk membandingkan performa Algoritma A (Heuristik/Greedy) dan Algoritma B (Eksak/Backtracking).
2. Menganalisis Total Cost of Ownership (TCO) yang menggabungkan Biaya BBM dinamis dan Biaya Komputasi Cloud Server.
3. Menentukan titik impas (*Break-Even Point*) ekonomi dan memberikan rekomendasi keputusan bisnis yang tepat dalam kondisi Skenario Subsidi maupun Skenario Krisis.

## Manfaat
1. **Bagi Perusahaan**: Membantu manajemen mengambil keputusan berbasis data (*data-driven decision*) dalam memilih arsitektur perangkat lunak yang paling hemat biaya sesuai kondisi harga BBM di pasar.
2. **Bagi Operasional**: Mengoptimalkan pengeluaran tak terduga akibat perubahan beban paket yang memengaruhi efisiensi konsumsi bensin kurir di lapangan.
3. **Bagi Tim Pengembang**: Menghasilkan sistem perangkat lunak yang modular, terstruktur, dan mudah dikembangkan untuk pemodelan distribusi logistik yang lebih kompleks.

## Fungsi Setiap File
1. **`data/dataset.json`**: Berfungsi sebagai berkas masukan eksternal (database tiruan) yang menyimpan parameter dinamis seperti data harga bensin skenario, daftar nama lokasi, berat paket tiap pelanggan, serta matriks ketetanggaan jarak fisik antar-titik rute.
2. **`src/data_parser.py`**: Berfungsi sebagai modul pembaca file (*data parser*) bawaan Python tanpa library pihak ketiga yang bertugas menerjemahkan teks mentah JSON ke dalam struktur data Graf berbobot (Matriks Ketetanggaan) di dalam program.
3. **`src/main.py`**: Berfungsi sebagai pusat kendali program (kerangka interface CLI) yang memvalidasi argumen skenario terminal, mengoordinasikan pemuatan data, serta menampilkan visualisasi hasil komparasi rute, waktu eksekusi presisi, dan nilai TCO akhir.
4. **`.gitignore`**: Berfungsi sebagai file konfigurasi untuk menyaring dan memastikan file sampah otomatis atau cache lokal komputer (seperti folder `__pycache__`) tidak ikut terunggah mengotori repositori GitHub.

## Cara Menjalankan Program

### Prasyarat
- posisi Terminal/Command Line berada di direktori utama proyek (`uas-praktikum-analgo-2026`).

### Langkah Eksekusi
Jalankan program utama di Terminal dengan menyertakan argumen skenario pilihan Anda:

1. **Skenario Subsidi (Harga BBM murah Rp 5.000/liter)**
   ```bash
   python src/main.py --scenario subsidy

2. **Skenario Cricis (Harga BBM mahal Rp 20.000/liter)**
 ```bash
   python src/main.py --scenario crisis
   ```

### Pemilihan Algoritma
Algoritma heuristik yang dipilih adalah Greedy (Nearest Neighbor) karena memiliki waktu eksekusi yang sangat cepat dengan kompleksitas yang rendah, sehingga cocok digunakan pada sistem operasional harian yang membutuhkan respons instan.
Algoritma eksak yang dipilih adalah Backtracking dengan DFS dan Pruning karena mampu menjamin solusi rute paling optimal secara global. Namun, algoritma ini memiliki biaya komputasi yang jauh lebih tinggi sehingga hanya cocok digunakan pada kondisi tertentu.

### Analisis Kompleksitas (Big-O)

## Algoritma Greedy (Nearest Neighbor)

1. Kompleksitas Waktu: O(n²)
Algoritma Greedy menggunakan satu perulangan utama untuk mengunjungi seluruh lokasi pelanggan sebanyak n−1 kali. Pada setiap iterasi, algoritma melakukan pencarian tetangga terdekat dengan menelusuri seluruh lokasi yang belum dikunjungi. Dengan demikian, terdapat dua perulangan bersarang yang menghasilkan kompleksitas waktu sebesar:
O(n × n) = O(n²)
2. Kompleksitas Ruang: O(n)
Algoritma menyimpan beberapa struktur data tambahan, yaitu visited berukuran n, route berukuran n+1. Ada variabel bantu seperti current_node, nearest_node, dan min_distance.
Karena penggunaan memori bertambah secara linear terhadap jumlah lokasi, maka kompleksitas ruangnya adalah O(n).

## Algoritma Exact (Backtracking + DFS + Pruning)

1. Kompleksitas Waktu: O(n!)
Algoritma Exact menggunakan pendekatan rekursif (Depth First Search) untuk mengeksplorasi seluruh kemungkinan rute yang dapat dibentuk. Pada kasus terburuk, seluruh permutasi lokasi harus diperiksa. Jumlah kemungkinan rute yang dievaluasi adalah (n − 1)!. Karena pertumbuhannya bersifat faktorial, kompleksitas waktunya dinyatakan sebagai O(n!). Meskipun teknik pruning digunakan untuk memangkas cabang yang tidak mungkin menghasilkan solusi lebih baik, kompleksitas terburuknya tetap bersifat faktorial.
2. Kompleksitas Ruang: O(n)
Penggunaan memori berasal dari visited berukuran n, route berukuran n, dan stack rekursi DFS dengan kedalaman maksimum n. Karena kebutuhan memori bertambah secara linear terhadap jumlah lokasi, maka kompleksitas ruangnya adalah O(n)

### Summary
Berdasarkan hasil simulasi pada dua kondisi ekonomi, algoritma Greedy memiliki Total Cost of Ownership (TCO) yang lebih rendah dibandingkan algoritma Exact. Hal ini disebabkan karena algoritma Greedy memiliki waktu eksekusi yang sangat cepat sehingga biaya komputasi server yang dihasilkan jauh lebih kecil. Meskipun algoritma Exact mampu menghasilkan rute yang lebih optimal dan sedikit menghemat biaya bahan bakar, penghematan tersebut belum mampu mengimbangi tingginya biaya komputasi yang dibutuhkan.
Pada skenario Subsidi (Rp5.000/liter) maupun Krisis (Rp20.000/liter), algoritma Greedy tetap menjadi pilihan yang lebih ekonomis untuk digunakan. Berdasarkan analisis Break-Even, algoritma Exact baru mulai menguntungkan ketika harga bensin berada pada kisaran belasan juta Rupiah per liter. 
Oleh karena itu, keputusan bisnis yang direkomendasikan adalah tetap menggunakan algoritma Greedy pada kondisi operasional normal. Algoritma Exact hanya layak dipertimbangkan apabila terjadi kenaikan harga bahan bakar yang sangat ekstrem atau ketika perusahaan memiliki kebutuhan optimasi rute yang jauh lebih tinggi dibandingkan biaya komputasi yang harus dikeluarkan.