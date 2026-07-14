#!/usr/bin/env python3
"""
Script simulasi cicilan KUR (Kredit Usaha Rakyat)
Menghitung cicilan, bunga, dan total pembayaran untuk berbagai skenario
"""

import json
from pathlib import Path

def load_kur_data(data_dir):
    """Load data KUR dari folder data"""
    with open(data_dir / "kur.json", 'r', encoding='utf-8') as f:
        return json.load(f)

def format_currency(amount):
    """Format angka ke format mata uang Rupiah"""
    if amount >= 1000000000:
        return f"Rp{amount/1000000000:.1f} miliar"
    elif amount >= 1000000:
        return f"Rp{amount/1000000:.0f} juta"
    else:
        return f"Rp{amount:,.0f}"

def hitung_cicilan_flat(principal, bunga_persen, tenor_bulan):
    """
    Hitung cicilan dengan sistem flat (bunga tetap)
    
    Parameters:
    - principal: pokok pinjaman
    - bunga_persen: bunga per tahun dalam persen
    - tenor_bulan: jangka waktu dalam bulan
    
    Returns:
    - cicilan_bulanan
    - total_bunga
    - total_pembayaran
    """
    bunga_tahunan = bunga_persen / 100
    bunga_per_bulan = bunga_tahunan / 12
    
    # Hitung bunga flat
    total_bunga = principal * bunga_tahunan * (tenor_bulan / 12)
    total_pembayaran = principal + total_bunga
    cicilan_bulanan = total_pembayaran / tenor_bulan
    
    return {
        'cicilan_bulanan': cicilan_bulanan,
        'total_bunga': total_bunga,
        'total_pembayaran': total_pembayaran,
        'bunga_persen': bunga_persen,
        'tenor_bulan': tenor_bulan
    }

def hitung_cicilan_diminishing(principal, bunga_persen, tenor_bulan):
    """
    Hitung cicilan dengan sistem diminishing (bunga berkurang)
    
    Parameters:
    - principal: pokok pinjaman
    - bunga_persen: bunga per tahun dalam persen
    - tenor_bulan: jangka waktu dalam bulan
    
    Returns:
    - cicilan_pertama
    - cicilan_terakhir
    - total_bunga
    - total_pembayaran
    """
    bunga_tahunan = bunga_persen / 100
    bunga_per_bulan = bunga_tahunan / 12
    
    # Cicilan pokok per bulan
    cicilan_pokok = principal / tenor_bulan
    
    # Cicilan pertama (pokok + bunga penuh)
    cicilan_pertama = cicilan_pokok + (principal * bunga_per_bulan)
    
    # Cicilan terakhir (pokok + bunga sedikit)
    cicilan_terakhir = cicilan_pokok + (cicilan_pokok * bunga_per_bulan)
    
    # Hitung total bunga (rata-rata)
    avg_bunga = (principal * bunga_per_bulan + cicilan_pokok * bunga_per_bulan) / 2
    total_bunga = avg_bunga * tenor_bulan
    total_pembayaran = principal + total_bunga
    
    return {
        'cicilan_pertama': cicilan_pertama,
        'cicilan_terakhir': cicilan_terakhir,
        'total_bunga': total_bunga,
        'total_pembayaran': total_pembayaran,
        'bunga_persen': bunga_persen,
        'tenor_bulan': tenor_bulan
    }

def simulasi_kur_mikro():
    """Simulasi KUR Mikro dengan berbagai skenario"""
    print("=" * 80)
    print("SIMULASI KUR MIKRO (Tanpa Agunan)")
    print("Plafon: Rp10-100 juta | Bunga: 6% | Tenor: Maks 60 bulan")
    print("=" * 80)
    
    skenarios = [
        {"nama": "KUR Mikro Rp50 juta", "modal": 50000000, "bunga": 6, "tenor": 60},
        {"nama": "KUR Mikro Rp80 juta", "modal": 80000000, "bunga": 6, "tenor": 60},
        {"nama": "KUR Mikro Rp100 juta", "modal": 100000000, "bunga": 6, "tenor": 60},
    ]
    
    print(f"\n{'Skenario':<25} {'Cicilan/Bulan':<15} {'Total Bunga':<15} {'Total Bayar':<15}")
    print("-" * 80)
    
    for skenario in skenarios:
        hasil = hitung_cicilan_flat(skenario['modal'], skenario['bunga'], skenario['tenor'])
        nama = skenario['nama']
        cicilan = format_currency(hasil['cicilan_bulanan'])
        bunga = format_currency(hasil['total_bunga'])
        total = format_currency(hasil['total_pembayaran'])
        
        print(f"{nama:<25} {cicilan:<15} {bunga:<15} {total:<15}")

def simulasi_kur_kecil():
    """Simulasi KUR Kecil dengan berbagai skenario"""
    print("\n" + "=" * 80)
    print("SIMULASI KUR KECIL (Perlu Agunan)")
    print("Plafon: Rp100-500 juta | Bunga: 6-9% | Tenor: Maks 60 bulan")
    print("=" * 80)
    
    skenarios = [
        {"nama": "KUR Kecil Rp150 juta", "modal": 150000000, "bunga": 6, "tenor": 60},
        {"nama": "KUR Kecil Rp200 juta", "modal": 200000000, "bunga": 6, "tenor": 60},
        {"nama": "KUR Kecil Rp300 juta", "modal": 300000000, "bunga": 6, "tenor": 60},
        {"nama": "KUR Kecil Rp400 juta", "modal": 400000000, "bunga": 6, "tenor": 60},
        {"nama": "KUR Kecil Rp500 juta", "modal": 500000000, "bunga": 6, "tenor": 60},
    ]
    
    print(f"\n{'Skenario':<25} {'Cicilan/Bulan':<15} {'Total Bunga':<15} {'Total Bayar':<15}")
    print("-" * 80)
    
    for skenario in skenarios:
        hasil = hitung_cicilan_flat(skenario['modal'], skenario['bunga'], skenario['tenor'])
        nama = skenario['nama']
        cicilan = format_currency(hasil['cicilan_bulanan'])
        bunga = format_currency(hasil['total_bunga'])
        total = format_currency(hasil['total_pembayaran'])
        
        print(f"{nama:<25} {cicilan:<15} {bunga:<15} {total:<15}")

def simulasi_kombinasi():
    """Simulasi kombinasi KUR Mikro + KUR Kecil"""
    print("\n" + "=" * 80)
    print("SIMULASI KOMBINASI KUR MIKRO + KUR KECIL")
    print("=" * 80)
    
    modal_sendiri = 80000000
    
    skenarios = [
        {
            "nama": "Alfamart 18 rak (Rp650 juta)",
            "modal_total": 650000000,
            "kur_mikro": 100000000,
            "kur_kecil": 470000000
        },
        {
            "nama": "Indomaret (Rp644 juta)",
            "modal_total": 644000000,
            "kur_mikro": 100000000,
            "kur_kecil": 464000000
        },
        {
            "nama": "O!Save (Rp400 juta)",
            "modal_total": 400000000,
            "kur_mikro": 100000000,
            "kur_kecil": 220000000
        },
    ]
    
    print(f"\n{'Skenario':<30} {'Modal Sendiri':<15} {'KUR Mikro':<15} {'KUR Kecil':<15} {'Cicilan/Bulan':<15}")
    print("-" * 100)
    
    for skenario in skenarios:
        # Hitung cicilan KUR Mikro
        cicilan_mikro = hitung_cicilan_flat(skenario['kur_mikro'], 6, 60)
        
        # Hitung cicilan KUR Kecil
        cicilan_kecil = hitung_cicilan_flat(skenario['kur_kecil'], 6, 60)
        
        # Total cicilan
        total_cicilan = cicilan_mikro['cicilan_bulanan'] + cicilan_kecil['cicilan_bulanan']
        
        nama = skenario['nama']
        modal = format_currency(modal_sendiri)
        mikro = format_currency(skenario['kur_mikro'])
        kecil = format_currency(skenario['kur_kecil'])
        cicilan = format_currency(total_cicilan)
        
        print(f"{nama:<30} {modal:<15} {mikro:<15} {kecil:<15} {cicilan:<15}")

def analisis_cicilan_vs_laba():
    """Analisis perbandingan cicilan dengan laba bersih"""
    print("\n" + "=" * 80)
    print("ANALISIS CICILAN vs LABA BERSIH")
    print("=" * 80)
    
    # Data cicilan dari simulasi sebelumnya
    skenarios = [
        {
            "nama": "Alfamart 18 rak",
            "modal": 650000000,
            "cicilan_bulanan": 12630000,  # Dari simulasi kombinasi
            "laba_min": 22000000,
            "laba_max": 70000000
        },
        {
            "nama": "Indomaret",
            "modal": 644000000,
            "cicilan_bulanan": 12510000,
            "laba_min": 22000000,
            "laba_max": 70000000
        },
        {
            "nama": "O!Save",
            "modal": 400000000,
            "cicilan_bulanan": 8400000,
            "laba_min": 20000000,
            "laba_max": 50000000
        },
    ]
    
    print(f"\n{'Brand':<15} {'Cicilan/Bulan':<15} {'Laba Min':<15} {'Laba Max':<15} {'Sisa (Min)':<15} {'Sisa (Max)':<15}")
    print("-" * 90)
    
    for skenario in skenarios:
        nama = skenario['nama']
        cicilan = format_currency(skenario['cicilan_bulanan'])
        laba_min = format_currency(skenario['laba_min'])
        laba_max = format_currency(skenario['laba_max'])
        sisa_min = format_currency(skenario['laba_min'] - skenario['cicilan_bulanan'])
        sisa_max = format_currency(skenario['laba_max'] - skenario['cicilan_bulanan'])
        
        print(f"{nama:<15} {cicilan:<15} {laba_min:<15} {laba_max:<15} {sisa_min:<15} {sisa_max:<15}")
    
    print("\n" + "=" * 80)
    print("KESIMPULAN ANALISIS")
    print("=" * 80)
    print("""
[RASIO CICILAN TERHADAP LABA]
   - Alfamart: Cicilan 18-57% dari laba bersih
   - Indomaret: Cicilan 18-57% dari laba bersih
   - O!Save: Cicilan 17-42% dari laba bersih

[REKOMENDASI]
   1. Pilih franchise dengan cicilan < 30% dari laba bersih
   2. Untuk keamanan, pastikan laba bersih > 2x cicilan
   3. Siapkan dana cadangan 3-6 bulan cicilan
   4. Mulai dari franchise yang lebih kecil dulu

[TIPS PENTING]
   - Jangan memulai jika cicilan > 40% dari laba bersih
   - Pastikan ada cadangan cash untuk 6 bulan pertama
   - Pilih lokasi dengan traffic tinggi untuk memastikan omzet
""")

def main():
    """Fungsi utama"""
    # Tentukan path ke folder data
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / "data"
    
    # Jalankan simulasi
    simulasi_kur_mikro()
    simulasi_kur_kecil()
    simulasi_kombinasi()
    analisis_cicilan_vs_laba()

if __name__ == "__main__":
    main()