# Klasifikasi Kelayakan Pemberian Kredit Komputer Menggunakan Naive Bayes
## 🧩 Tahapan - Tahapan dalam Pembuatan Model 🧩
### 1. Mengimport library
Langkah pertama adalah mengimpor pustaka/library Python yang diperlukan untuk menjalankan program. Adapun library yang dibutuhkan :
- `pandas` untuk membaca dan mengelola data  
- `sklearn` untuk machine learning  
- `matplotlib` dan `seaborn` untuk visualisasi  
- `numpy` untuk perhitungan matematis  

### 2. Pengumpulan Data 
Pada tahap kedua tentunya kita membutuhkan sebuah data yang akan diproses. Adapun data yang dipakai biasanya dalam bentuk file `.csv`. File ini dibaca dan dimasukkan ke dalam struktur DataFrame dari pustaka `pandas`, untuk memudahkan dalam analisis, eksplorasi, dan manipulasi data. Data yang dipakai pada pembuatan model ini berisi : 
- Age  : Tua, Paruh Baya, Muda
- Income : Rendah, Sedang, Tinggi
- Student : Ya atau Tidak
- Credit_Rating : Baik atau Buruk
- Buys_Computer : Target (1 = Layak, 0 = Tidak Layak)
  
### 3. Pra-Pemrosesan Data
Sebelum data digunakan untuk pelatihan model data diproses dengan :
- Label Encoding : Karena model naive bayes hanya bisa membaca angka, maka semua data teks kita ubah jadi angka.
- Memisahkan Fitur dan Target : - X = Fitur (Age, Income, Student, Credit_Rating) - Y = Target/Output yang ingin di prediksi (Buys_Computer)
  
### 4. Membagi Data (Training dan Testing)
Data dibagi menjadi dua bagian :
- Training (80%) : untuk melatih model
- Testing (20%) : untuk menguji performa model

  Tujuannya untuk menghindari overfitting dan mengetahui performa model pada data baru.
### 5. Pembuatan dan Pelatihan Model
- Karena menggunakan naive bayes, maka GaussianNB cocok untuk membuat data numerik hasil encoding.
-  Model dibuat menggunakan GaussianNB, lalu dilatih menggunakan **.fit(X_train, y_train)**
### 6.Prediksi
Setelah model dilatih, selanjutnya model digunakan untuk memprediksi pada data testing, apakah masuk kategori layak (1) atau tidak layak (2). Model diprediksi menggunakan **.predict(X_test)**

### 7. Evaluasi Model
Terakhir, kita cek seberapa bagus model dengan melihat :
- Akurasi : berapa persen prediksi yang benar
- Confusion Matrix : Menunjukan jumlah diprediksi apakah layak (1) dan tidak layak (0) tiap kategori
- Classification Report : Agar lebih detail bisa dilihat juga precision, recall, sama f1-score

  



