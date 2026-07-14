# 📊 PERHITUNGAN YANG DILAKUKAN TIM ALFAMART
## Panduan Lengkap Evaluasi Lokasi & Simulasi Keuangan

---

## 📋 5 ASPEK YANG DIEVALUASI TIM SURVEYOR ALFAMART

Berdasarkan informasi resmi dari BFI Finance, tim surveyor Alfamart menilai **5 aspek utama**:

| No | Aspek | Bobot | Cara Pengukuran |
|----|-------|-------|-----------------|
| 1 | **Jumlah Penduduk** | Tinggi | Data BPS, Dukcapil, kepadatan area |
| 2 | **Daya Beli Masyarakat** | Tinggi | Pendapatan rata-rata, pengeluaran konsumen |
| 3 | **Traffic Kendaraan** | Tinggi | Hitung manual, Google Maps, Waze |
| 4 | **Kompetitor** | Sedang | Jarak Alfamart/Indomaret/minimarket lain |
| 5 | **Fasilitas Pendukung** | Sedang | Sekolah, RS, kantor, pasar, SPBU |

---

## 🔌 A. PERHITUNGAN LISTRIK

### Kebutuhan Listrik Alfamart:

| Komponen | Daya (Watt) | Jam/Hari | KWh/Hari |
|----------|-------------|----------|----------|
| **Lampu** | | | |
| - Lampu LED (30 titik) | 900W | 13 jam | 11.7 |
| **AC** | | | |
| - AC 2 PK (2 unit) | 3.200W | 12 jam | 38.4 |
| **Kulkas** | | | |
| - Show Case (4 unit) | 800W | 24 jam | 19.2 |
| - Freezer (2 unit) | 400W | 24 jam | 9.6 |
| **Kasir** | | | |
| - Komputer Kasir | 300W | 13 jam | 3.9 |
| - Printer Struk | 150W | 13 jam | 1.95 |
| - Scanner Barcode | 100W | 13 jam | 1.3 |
| **Lain-lain** | | | |
| - Pompa Air | 125W | 2 jam | 0.25 |
| - Sound System | 50W | 10 jam | 0.5 |
| - CCTV (8 channel) | 100W | 24 jam | 2.4 |
| **TOTAL** | **5.125W** | - | **89.2 KWh** |

### Perhitungan Biaya Listrik:

```
TARIF DASAR (R-1/TR 1300VA): Rp1.444,70/KWh
TARIF MIDDLE (R-2/TR 2200VA): Rp1.699,52/KWh
TARIF BESAR (R-3/TR 3500-5500VA): Rp1.699,52/KWh + Rp1.286,53/KWh

ESTIMASI BIAYA LISTRIK/BULAN:
- KWh/Hari: 89.2 KWh
- KWh/Bulan: 89.2 × 30 = 2.676 KWh
- Biaya @Rp1.700/KWh: Rp4.549.200
- Biaya @Rp2.000/KWh (termasuk abonemen): Rp5.352.000
- Biaya @Rp2.500/KWh (jam beban puncak): Rp6.690.000

REKOMENDASI: Rp5.000.000 - Rp7.000.000/bulan
```

### Tips Hemat Listrik:
1. Gunakan **AC Inverter** (hemat 30-40%)
2. Gunakan **LED** untuk semua lampu
3. Atur **suhu AC** di 24-26°C
4. Matikan AC di luar jam operasional
5. Gunakan **timer** untuk showcase

---

## 🚗 B. PERHITUNGAN TRAFFIC

### Cara Menghitung Traffic:

#### 1. **Manual Counting (Paling Akurat)**
```
WAKTU: 07.00-09.00 (2 jam) dan 16.00-18.00 (2 jam)
TEMPAT: Berdiri di depan lokasi target
CARA: Hitung setiap kendaraan yang lewat

TEMPLATE PENCATATAN:
┌─────────────┬─────────┬─────────┬─────────┬─────────┐
│ Waktu       │ Motor   │ Mobil   │ Truk    │ Total   │
├─────────────┼─────────┼─────────┼─────────┼─────────┤
│ 07.00-07.30 │ ____    │ ____    │ ____    │ ____    │
│ 07.30-08.00 │ ____    │ ____    │ ____    │ ____    │
│ 08.00-08.30 │ ____    │ ____    │ ____    │ ____    │
│ 08.30-09.00 │ ____    │ ____    │ ____    │ ____    │
│ 16.00-16.30 │ ____    │ ____    │ ____    │ ____    │
│ 16.30-17.00 │ ____    │ ____    │ ____    │ ____    │
│ 17.00-17.30 │ ____    │ ____    │ ____    │ ____    │
│ 17.30-18.00 │ ____    │ ____    │ ____    │ ____    │
├─────────────┼─────────┼─────────┼─────────┼─────────┤
│ TOTAL/HARI  │ ____    │ ____    │ ____    │ ____    │
└─────────────┴─────────┴─────────┴─────────┴─────────┘

ESTIMASI TRAFFIC 24 JAM:
- Jam Sibuk (4 jam): Total × 1.5
- Jam Normal (10 jam): Total × 1.0
- Jam Sepi (10 jam): Total × 0.3
```

#### 2. **Google Maps Traffic**
```
CARA AKSES:
1. Buka Google Maps
2. Cari lokasi target
3. Klik layer "Live Traffic"
4. Pilih waktu: Weekday jam 08.00 & 17.00
5. Catat warna: Merah (padat), Kuning (sedang), Hijau (lancar)

ESTIMASI:
- Merah: >50 kendaraan/menit
- Kuning: 20-50 kendaraan/menit
- Hijau: <20 kendaraan/menit
```

#### 3. **Waze Traffic**
```
CARA AKSES:
1. Buka Waze
2. Pilih lokasi
3. Lihat "Live Map"
4. Cek traffic real-time
```

### Rumus Estimasi Konversi:

```
TRAFFIC KENDARAAN/HARI: ____ kendaraan
× KONVERSI PEMBELI: 3-5% (minimarket)
= PENGUNJUNG/HARI: ____ orang
× NILAI TRANSAKSI RATA-RATA: Rp50.000-80.000
= OMZET ESTIMASI/HARI: Rp_______
× 30 HARI
= OMZET ESTIMASI/BULAN: Rp_______
```

---

## 🏪 C. PERHITUNGAN KOMPETITOR

### Template Analisis Kompetitor:

```
RADIUS ANALISIS: 2 KM dari lokasi target

1. ALFAMART TERDEKAT
   - Alamat: ______________
   - Jarak: ____ km
   - Rating Google: ____ bintang
   - Jam Operasional: ______________
   - Kekuatan: ______________
   - Kelemahan: ______________

2. INDOMARET TERDEKAT
   - Alamat: ______________
   - Jarak: ____ km
   - Rating Google: ____ bintang
   - Jam Operasional: ______________
   - Kekuatan: ______________
   - Kelemahan: ______________

3. MINIMARKET LAIN
   - Nama: ______________
   - Alamat: ______________
   - Jarak: ____ km
   - Kekuatan: ______________

4. PASAR TRADISIONAL
   - Nama: ______________
   - Jarak: ____ km
   - Jam Operasional: ______________
   - Keunggulan: ______________

TOTAL KOMPETITOR DALAM 2KM:
- Alfamart: ____ gerai
- Indomaret: ____ gerai
- Minimarket lain: ____ gerai
- Pasar tradisional: ____

SKOR KOMPETISI: ____/10
(10 = sangat kompetitif, 1 = sangat sedikit kompetitor)
```

---

## 💰 D. RINCIAN BIAYA OPERASIONAL BULANAN (OPEX)

### Data dari Scribd - Simulasi Opex Minimarket:

**TOTAL OPEX: Rp22.300.000/bulan**

| No | Komponen Biaya | Perkiraan (Rp) | Persentase |
|----|----------------|----------------|------------|
| 1 | **Gaji Karyawan (4 orang)** | | |
|   | - Kepala Toko | 4.000.000 | |
|   | - Kasir | 3.000.000 | |
|   | - Pramuniaga 1 | 2.500.000 | |
|   | - Pramuniaga 2 | 2.500.000 | |
|   | **Subtotal Gaji** | **12.000.000** | **54%** |
| 2 | **Sewa Toko** | 5.000.000 | **22%** |
| 3 | **Listrik** | 1.500.000 | **7%** |
| 4 | **Internet/Wifi** | 300.000 | **1%** |
| 5 | **Air PDAM** | 200.000 | **1%** |
| 6 | **Promosi/Marketing** | 500.000 | **2%** |
| 7 | **Perlengkapan ATK** | 100.000 | **0.4%** |
| 8 | **Biaya Administrasi** | 100.000 | **0.4%** |
| 9 | **Konsumsi Karyawan** | 500.000 | **2%** |
| 10 | **Perawatan/Rusak** | 300.000 | **1%** |
| 11 | **Pajak/Retribusi** | 500.000 | **2%** |
| 12 | **Lain-lain** | 1.300.000 | **6%** |
| | **TOTAL OPEX** | **22.300.000** | **100%** |

---

## 📊 E. SIMULASI KEUANGAN LENGKAP

### Studi Kasus: Alfamart Palembang - Sukarami

#### Asumsi Dasar:
| Komponen | Angka | Sumber |
|----------|-------|--------|
| Luas Area Sales | 120 m² | Formulir Alfamart |
| Tipe Gerai | 36 Rak | Estimasi |
| Omzet/Hari | Rp2.500.000 | Rata-rata minimarket |
| Omzet/Bulan | Rp75.000.000 | 30 hari |
| Laba Kotor | 10% | Standar minimarket |

#### Proyeksi Omzet (6 Bulan Pertama):

```
BULAN 1 (Grand Opening):
- Omzet: Rp50.000.000 (60% dari target)
- Laba Kotor (10%): Rp5.000.000
- OPEX: Rp22.300.000
- ROYALTI (0%): Rp0
- SISA: -Rp17.300.000 (RUGI)

BULAN 2:
- Omzet: Rp60.000.000 (80%)
- Laba Kotor: Rp6.000.000
- OPEX: Rp22.300.000
- ROYALTI (0%): Rp0
- SISA: -Rp16.300.000 (RUGI)

BULAN 3:
- Omzet: Rp70.000.000 (93%)
- Laba Kotor: Rp7.000.000
- OPEX: Rp22.300.000
- ROYALTI (0%): Rp0
- SISA: -Rp15.300.000 (RUGI)

BULAN 4:
- Omzet: Rp75.000.000 (100%)
- Laba Kotor: Rp7.500.000
- OPEX: Rp22.300.000
- ROYALTI (0%): Rp0
- SISA: -Rp14.800.000 (RUGI)

BULAN 5:
- Omzet: Rp80.000.000 (107%)
- Laba Kotor: Rp8.000.000
- OPEX: Rp22.300.000
- ROYALTI (0%): Rp0
- SISA: -Rp14.300.000 (RUGI)

BULAN 6:
- Omzet: Rp85.000.000 (113%)
- Laba Kotor: Rp8.500.000
- OPEX: Rp22.300.000
- ROYALTI (0%): Rp0
- SISA: -Rp13.800.000 (RUGI)
```

### Proyeksi Omzet (Bulan 7-12):

```
BULAN 7-12 (Stabil):
- Omzet: Rp100.000.000 - Rp150.000.000
- Laba Kotor (10%): Rp10.000.000 - Rp15.000.000
- OPEX: Rp22.300.000
- ROYALTI:
  - 0-150jt: 0% = Rp0
  - 150-175jt: 1% = Rp1.500.000
- SISA: -Rp12.300.000 s/d -Rp8.800.000 (RUGI)
```

---

## ⚠️ F. PERHITUNGAN YANG HARUS DILAKUKAN TIM ALFAMART

### Tahap 1: Evaluasi Lokasi (Sebelum Survey)

| No | Data yang Dikumpulkan | Sumber | Target |
|----|----------------------|--------|--------|
| 1 | Jumlah penduduk kecamatan | BPS/Dukcapil | >50.000 jiwa |
| 2 | Kepadatan penduduk | BPS | >3.000/km² |
| 3 | Pendapatan rata-rata | BPS | >Rp2.5 juta/bulan |
| 4 | Jarak ke Alfamart terdekat | Google Maps | >500 meter |
| 5 | Jarak ke Indomaret terdekat | Google Maps | >300 meter |
| 6 | Traffic kendaraan/hari | Manual count | >500 kendaraan |
| 7 | Luas tanah/bangunan | Survei | >150m² |
| 8 | Akses jalan | Survei | Jalan 2 mobil |
| 9 | Parkir kendaraan | Survei | Muat 10+ motor |
| 10 | Fasilitas pendukung | Google Maps | Dekat sekolah/RS |

### Tahap 2: Survei Lokasi (Saat Datang)

| No | Yang Diperiksa | Cara Cek | Kriteria |
|----|----------------|----------|----------|
| 1 | **Kondisi Bangunan** | Lihat langsung | Tidak rusak, siap renovasi |
| 2 | **Akses Listrik** | Cek meteran | Daya cukup (min 3.500VA) |
| 3 | **Akses Air** | Cek PDAM/toren | Ada air bersih |
| 4 | **Drainase** | Lihat saluran | Tidak banjir |
| 5 | **Parkir** | Ukur area | Muat 5-10 kendaraan |
| 6 | **Visibilitas** | Dari jalan | Terlihat jelas |
| 7 | **Keamanan** | Tanya warga | Aman, tidak rawan |
| 8 | **Lingkungan** | Lihat sekitar | Bersih, rapi |

### Tahap 3: Analisis Keuangan

| No | Item yang Dihitung | Rumus | Target |
|----|-------------------|-------|--------|
| 1 | **Omzet Estimasi** | Traffic × Konversi × Nilai Transaksi | >Rp75 juta/bulan |
| 2 | **Biaya Sewa** | Harga pasar | <10% omzet |
| 3 | **Biaya Listrik** | Daya × Jam × Tarif | <Rp7 juta/bulan |
| 4 | **Biaya Karyawan** | 4-5 orang × UMK | <Rp15 juta/bulan |
| 5 | **OPEX Total** | Semua biaya bulanan | <Rp25 juta/bulan |
| 6 | **Laba Bersih** | Omzet × Margin - OPEX | >Rp10 juta/bulan |
| 7 | **BEP** | Modal ÷ Laba Bersih | <18 bulan |
| 8 | **ROI** | (Laba/Tahun ÷ Modal) × 100 | >30%/tahun |

### Tahap 4: Proyeksi 5 Tahun

| Tahun | Omzet/Tahun | Laba Bersih | ROI | Akumulasi |
|-------|-------------|-------------|-----|-----------|
| 1 | Rp900 juta | Rp60 juta | 12% | Rp60 juta |
| 2 | Rp1.080 juta | Rp90 juta | 18% | Rp150 juta |
| 3 | Rp1.296 juta | Rp120 juta | 24% | Rp270 juta |
| 4 | Rp1.555 juta | Rp150 juta | 30% | Rp420 juta |
| 5 | Rp1.866 juta | Rp180 juta | 36% | Rp600 juta |

---

## 📋 G. FORMULIR EVALUASI LOKASI ALFAMART

```
FORMULIR EVALUASI LOKASI FRANCHISE ALFAMART

A. DATA UMUM LOKASI
Tanggal Survey: ______________
Nama Surveyor: ______________
Lokasi: ______________

B. DATA DEMOGRAFIS
1. Jumlah Penduduk Kecamatan: ______________ jiwa
2. Kepadatan Penduduk: ______________/km²
3. Rata-rata Pendapatan: Rp______________/bulan
4. Jumlah KK di Area: ______________

C. DATA TRAFFIC
1. Traffic Pagi (07-09): ______________ kendaraan
2. Traffic Sore (16-18): ______________ kendaraan
3. Total Estimasi/Hari: ______________ kendaraan
4. Komposisi: Motor ____% | Mobil ____% | Lain ____%

D. DATA KOMPETITOR
1. Alfamart Terdekat: ____ km
2. Indomaret Terdekat: ____ km
3. Minimarket Lain: ____ km
4. Pasar Tradisional: ____ km
5. Total Kompetitor dalam 2km: ____

E. DATA PROPERTI
1. Luas Tanah: ____ m²
2. Luas Bangunan: ____ m²
3. Luas Area Sales: ____ m²
4. Status: Milik Sendiri / Sewa
5. Harga Sewa: Rp______/bulan
6. Daya Listrik: _______VA
7. Akses Air: PDAM / Sumur / Toren

F. FASILITAS PENDUKUNG
1. Dekat Perumahan: Ya / Tidak (____ km)
2. Dekat Sekolah: Ya / Tidak (____ km)
3. Dekat RS/Klinik: Ya / Tidak (____ km)
4. Dekat Kantor: Ya / Tidak (____ km)
5. Dekat SPBU: Ya / Tidak (____ km)
6. Dekat Pasar: Ya / Tidak (____ km)

G. PROYEKSI KEUANGAN
1. Omzet Estimasi/Bulan: Rp______________
2. Biaya Sewa/Bulan: Rp______________
3. Biaya Listrik/Bulan: Rp______________
4. Biaya Karyawan/Bulan: Rp______________
5. OPEX Total/Bulan: Rp______________
6. Laba Bersih/Bulan: Rp______________
7. Estimasi BEP: ____________ bulan

H. REKOMENDASI
[ ] LAYAK - Submit ke Alfamart
[ ] TIDAK LAYAK - Cari lokasi lain
[ ] PERLU PERBAIKAN - ____________________________________

Tanda Tangan Surveyor: ______________
Tanggal: ______________
```

---

## 🔗 SUMBER DATA

| Kategori | Sumber | URL |
|----------|--------|-----|
| Opex Minimarket | Scribd | https://id.scribd.com/document/863202162 |
| Biaya Alfamart | CNBC Indonesia | https://www.cnbcindonesia.com/market/20250803 |
| Syarat Franchise | BFI Finance | https://www.bfi.co.id/en/blog/peluang-usaha-franchise-alfamart |
| Traffic | Google Maps | https://maps.google.com |
| Demografis | BPS | https://www.bps.go.id |

---

## Terakhir Diperbarui

14 Juli 2026
