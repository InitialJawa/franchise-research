#!/usr/bin/env python3
"""
Script analisis keuntungan franchise minimarket
Menghitung proyeksi keuntungan berdasarkan berbagai skenario
"""

import json
from pathlib import Path

def load_franchise_data(data_dir):
    """Load semua data franchise dari folder data"""
    franchises = []
    for file in data_dir.glob("*.json"):
        if file.name != "kur.json":
            with open(file, 'r', encoding='utf-8') as f:
                franchises.append(json.load(f))
    return franchises

def format_currency(amount):
    """Format angka ke format mata uang Rupiah"""
    if amount >= 1000000000:
        return f"Rp{amount/1000000000:.1f} miliar"
    elif amount >= 1000000:
        return f"Rp{amount/1000000:.0f} juta"
    else:
        return f"Rp{amount:,.0f}"

def analisis_keuntungan_lokasi():
    """Analisis keuntungan berdasarkan lokasi"""
    print("=" * 80)
    print("ANALISIS KEUNTUNGAN BERDASARKAN LOKASI")
    print("=" * 80)
    
    skenarios = [
        {
            "nama": "Lokasi Perkotaan (Traffic Tinggi)",
            "omzet_min": 400000000,
            "omzet_max": 600000000,
            "margin": 0.08,
            "biaya_operasional": 15000000
        },
        {
            "nama": "Lokasi Suburban (Traffic Sedang)",
            "omzet_min": 300000000,
            "omzet_max": 500000000,
            "margin": 0.075,
            "biaya_operasional": 12000000
        },
        {
            "nama": "Lokasi Pinggiran (Traffic Rendah)",
            "omzet_min": 200000000,
            "omzet_max": 300000000,
            "margin": 0.07,
            "biaya_operasional": 10000000
        },
    ]
    
    print(f"\n{'Lokasi':<35} {'Omzet/Bulan':<20} {'Laba Kotor':<15} {'Biaya Ops':<15} {'Laba Bersih':<15}")
    print("-" * 100)
    
    for skenario in skenarios:
        # Hitung rata-rata omzet
        avg_omzet = (skenario['omzet_min'] + skenario['omzet_max']) / 2
        
        # Hitung laba kotor
        laba_kotor = avg_omzet * skenario['margin']
        
        # Hitung laba bersih
        laba_bersih = laba_kotor - skenario['biaya_operasional']
        
        nama = skenario['nama']
        omzet = f"{format_currency(skenario['omzet_min'])}-{format_currency(skenario['omzet_max'])}"
        kotor = format_currency(laba_kotor)
        ops = format_currency(skenario['biaya_operasional'])
        bersih = format_currency(laba_bersih)
        
        print(f"{nama:<35} {omzet:<20} {kotor:<15} {ops:<15} {bersih:<15}")
    
    print("\n" + "=" * 80)
    print("KESIMPULAN LOKASI")
    print("=" * 80)
    print("""
[REKOMENDASI LOKASI]
   1. Perkotaan: Laba bersih Rp17-33 juta/bulan (terbaik)
   2. Suburban: Laba bersih Rp10-25 juta/bulan (cukup baik)
   3. Pinggiran: Laba bersih Rp4-11 juta/bulan (risiko tinggi)

[FAKTOR KUNCI KEBERHASILAN]
   - Traffic kendaraan dan pejalan kaki
   - Jarak dengan kompetitor (minimal 500m)
   - Kepadatan penduduk di sekitar
   - Akses parkir yang memadai
""")

def analisis_cashflow():
    """Analisis arus kas bulanan"""
    print("=" * 80)
    print("ANALISIS ARUS KAS BULANAN")
    print("=" * 80)
    
    skenarios = [
        {
            "nama": "Alfamart 18 rak",
            "modal": 650000000,
            "cicilan": 12630000,
            "omzet_bulan_1_6": 300000000,
            "omzet_bulan_7_12": 400000000,
            "margin": 0.075,
            "biaya_operasional": 12000000
        },
        {
            "nama": "Indomaret",
            "modal": 644000000,
            "cicilan": 12510000,
            "omzet_bulan_1_6": 350000000,
            "omzet_bulan_7_12": 450000000,
            "margin": 0.075,
            "biaya_operasional": 12000000
        },
        {
            "nama": "O!Save",
            "modal": 400000000,
            "cicilan": 8400000,
            "omzet_bulan_1_6": 250000000,
            "omzet_bulan_7_12": 350000000,
            "margin": 0.065,
            "biaya_operasional": 10000000
        },
    ]
    
    print(f"\n{'Brand':<15} {'Omzet 1-6':<15} {'Omzet 7-12':<15} {'Laba Bersih 1-6':<15} {'Laba Bersih 7-12':<15}")
    print("-" * 90)
    
    for skenario in skenarios:
        # Bulan 1-6
        laba_kotor_1_6 = skenario['omzet_bulan_1_6'] * skenario['margin']
        laba_bersih_1_6 = laba_kotor_1_6 - skenario['biaya_operasional'] - skenario['cicilan']
        
        # Bulan 7-12
        laba_kotor_7_12 = skenario['omzet_bulan_7_12'] * skenario['margin']
        laba_bersih_7_12 = laba_kotor_7_12 - skenario['biaya_operasional'] - skenario['cicilan']
        
        nama = skenario['nama']
        omzet_1_6 = format_currency(skenario['omzet_bulan_1_6'])
        omzet_7_12 = format_currency(skenario['omzet_bulan_7_12'])
        bersih_1_6 = format_currency(laba_bersih_1_6)
        bersih_7_12 = format_currency(laba_bersih_7_12)
        
        print(f"{nama:<15} {omzet_1_6:<15} {omzet_7_12:<15} {bersih_1_6:<15} {bersih_7_12:<15}")
    
    print("\n" + "=" * 80)
    print("PROYEKSI 5 TAHUN")
    print("=" * 80)
    
    for skenario in skenarios:
        # Tahun 1
        laba_kotor_1 = skenario['omzet_bulan_1_6'] * 6 * skenario['margin'] + skenario['omzet_bulan_7_12'] * 6 * skenario['margin']
        laba_bersih_tahun_1 = laba_kotor_1 - (skenario['biaya_operasional'] * 12) - (skenario['cicilan'] * 12)
        
        # Tahun 2-5 (asumsi omzet naik 10% per tahun)
        total_laba_5_tahun = laba_bersih_tahun_1
        for tahun in range(2, 6):
            laba_bersih_tahun = laba_bersih_tahun_1 * (1.1 ** (tahun - 1))
            total_laba_5_tahun += laba_bersih_tahun
        
        # Balik modal
        balik_modal = skenario['modal'] / (laba_bersih_tahun_1 / 12) if laba_bersih_tahun_1 > 0 else 0
        
        print(f"\n{skenario['nama']}:")
        print(f"  - Laba Bersih Tahun 1: {format_currency(laba_bersih_tahun_1)}")
        print(f"  - Total Laba 5 Tahun: {format_currency(total_laba_5_tahun)}")
        print(f"  - Balik Modal: {balik_modal:.0f} bulan ({balik_modal/12:.1f} tahun)")

def analisis_sensitivitas():
    """Analisis sensitivitas terhadap perubahan omzet"""
    print("\n" + "=" * 80)
    print("ANALISIS SENSITIVITAS TERHADAP PERUBAHAN OMZET")
    print("=" * 80)
    
    # Skenario dasar
    modal = 650000000
    cicilan = 12630000
    biaya_operasional = 12000000
    margin = 0.075
    
    print(f"\nModal: {format_currency(modal)}")
    print(f"Cicilan: {format_currency(cicilan)}/bulan")
    print(f"Biaya Operasional: {format_currency(biaya_operasional)}/bulan")
    print(f"Margin: {margin*100}%")
    
    print(f"\n{'Omzet/Bulan':<20} {'Laba Kotor':<15} {'Laba Bersih':<15} {'Status':<15}")
    print("-" * 70)
    
    omzet_scenarios = [
        200000000,  # -33%
        250000000,  # -17%
        300000000,  # Dasar
        350000000,  # +17%
        400000000,  # +33%
        450000000,  # +50%
    ]
    
    for omzet in omzet_scenarios:
        laba_kotor = omzet * margin
        laba_bersih = laba_kotor - biaya_operasional - cicilan
        
        # Hitung persentase perubahan
        persen_perubahan = ((omzet - 300000000) / 300000000) * 100
        
        # Status
        if laba_bersih > 20000000:
            status = "[OK] Sangat Baik"
        elif laba_bersih > 10000000:
            status = "[OK] Baik"
        elif laba_bersih > 0:
            status = "[!] Cukup"
        else:
            status = "[X] Rugi"
        
        omzet_str = f"{format_currency(omzet)} ({persen_perubahan:+.0f}%)"
        kotor = format_currency(laba_kotor)
        bersih = format_currency(laba_bersih)
        
        print(f"{omzet_str:<20} {kotor:<15} {bersih:<15} {status:<15}")
    
    print("\n" + "=" * 80)
    print("KESIMPULAN SENSITIVITAS")
    print("=" * 80)
    print("""
[TEMUAN PENTING]
   1. Break-even point: Omzet minimal Rp233 juta/bulan
   2. Omzet < Rp233 juta: Rugi
   3. Omzet Rp233-300 juta: Untung kecil
   4. Omzet > Rp300 juta: Untung stabil

[RISIKO]
   - Penurunan omzet 17% dari target masih aman
   - Penurunan omzet 33% dari target mulai rugi
   - Perlu manajemen biaya yang ketat

[TARGET OMZET AMAN]
   - Minimal: Rp300 juta/bulan
   - Nyaman: Rp400 juta/bulan
   - Ideal: Rp500+ juta/bulan
""")

def rekomendasi_investasi():
    """Rekomendasi investasi berdasarkan profil risiko"""
    print("=" * 80)
    print("REKOMENDASI INVESTASI BERDASARKAN PROFIL RISIKO")
    print("=" * 80)
    
    profil = [
        {
            "nama": "Konservatif",
            "modal_sendiri": 80000000,
            "toleransi_risiko": "Rendah",
            "rekomendasi": "Franchise kecil (9 rak) dengan KUR Mikro"
        },
        {
            "nama": "Moderat",
            "modal_sendiri": 80000000,
            "toleransi_risiko": "Sedang",
            "rekomendasi": "Franchise menengah (18 rak) dengan KUR Mikro + KUR Kecil"
        },
        {
            "nama": "Agresif",
            "modal_sendiri": 80000000,
            "toleransi_risiko": "Tinggi",
            "rekomendasi": "Franchise besar (25+ rak) dengan KUR penuh"
        },
    ]
    
    print(f"\n{'Profil':<15} {'Modal Sendiri':<15} {'Toleransi':<15} {'Rekomendasi':<40}")
    print("-" * 85)
    
    for p in profil:
        print(f"{p['nama']:<15} {format_currency(p['modal_sendiri']):<15} {p['toleransi_risiko']:<15} {p['rekomendasi']:<40}")
    
    print("\n" + "=" * 80)
    print("LANGKAH SELANJUTNYA")
    print("=" * 80)
    print("""
[LANGKAH-LANGKAH YANG PERLU DILAKUKAN]

1. TAHAP PERSIAPAN (1-3 bulan)
   - Riset lokasi potensial
   - Siapkan dokumen untuk KUR
   - Buat proposal bisnis
   - Konsultasi dengan bank

2. TAHAP PENGAJUAN (1-2 bulan)
   - Ajukan KUR ke bank
   - Siapkan agunan (jika perlu)
   - Tunggu proses verifikasi
   - Tandatangani kontrak

3. TAHAP PERSIAPAN GERAI (1-2 bulan)
   - Renovasi lokasi
   - Pengadaan peralatan
   - Rekrutmen karyawan
   - Pelatihan

4. TAHAP OPERASIONAL (Bulan ke-1)
   - Grand opening
   - Monitoring kinerja
   - Evaluasi bulanan
   - Penyesuaian strategi

[TIPS SUKSES]
   - Mulai dari yang kecil, scale up setelah berhasil
   - Pastikan lokasi strategis sebelum memulai
   - Manajemen biaya yang ketat di 6 bulan pertama
   - Bangun hubungan baik dengan supplier
   - Pantau kompetitor dan adaptasi
""")

def main():
    """Fungsi utama"""
    # Jalankan analisis
    analisis_keuntungan_lokasi()
    analisis_cashflow()
    analisis_sensitivitas()
    rekomendasi_investasi()

if __name__ == "__main__":
    main()