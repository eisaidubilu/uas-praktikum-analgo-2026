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

