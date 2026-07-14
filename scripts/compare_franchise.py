#!/usr/bin/env python3
"""
Script untuk membandingkan franchise minimarket
Analisis perbandingan Alfamart, Indomaret, O!Save, dan Alfamidi
"""

import json
import os
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

def compare_franchises(franchises):
    """Bandingkan franchise berdasarkan berbagai kriteria"""
    print("=" * 80)
    print("PERBANDINGAN FRANCHISE MINIMARKET")
    print("=" * 80)
    
    # Header tabel
    print(f"\n{'Brand':<15} {'Modal Awal':<20} {'Franchise Fee':<15} {'Royalti':<10} {'Target Omzet':<20}")
    print("-" * 80)
    
    for franchise in franchises:
        nama = franchise['nama']
        tipe_gerai = franchise['tipe_gerai'][0]  # Ambil tipe pertama
        modal = format_currency(tipe_gerai['total_modal'])
        fee = format_currency(franchise['biaya_franchise']['franchise_fee']) if isinstance(franchise['biaya_franchise']['franchise_fee'], int) else franchise['biaya_franchise']['franchise_fee']
        royalti = franchise['biaya_franchise']['royalti']
        omzet = franchise['keuntungan']['omzet_bulanan']
        
        print(f"{nama:<15} {modal:<20} {fee:<15} {royalti:<10} {omzet:<20}")
    
    print("\n" + "=" * 80)
    print("ANALISIS KEUNTUNGAN PER FRANCHISE")
    print("=" * 80)
    
    for franchise in franchises:
        nama = franchise['nama']
        keuntungan = franchise['keuntungan']
        
        print(f"\n{nama}:")
        print(f"  - Omzet Bulanan: {keuntungan['omzet_bulanan']}")
        print(f"  - Laba Bersih: {keuntungan['laba_bersih']}")
        print(f"  - Margin: {keuntungan['margin']}")
        print(f"  - Balik Modal: {keuntungan['balik_modal']}")
        
        print(f"\n  Resiko:")
        for resiko in franchise['resiko']:
            print(f"    • {resiko}")

def calculate_roi(franchise):
    """Hitung ROI untuk setiap franchise"""
    tipe_gerai = franchise['tipe_gerai'][0]
    modal = tipe_gerai['total_modal']
    
    # Ambil rata-rata laba bersih
    laba_text = franchise['keuntungan']['laba_bersih']
    # Parse laba bersih (contoh: "Rp22-70 juta/bulan")
    if '-' in laba_text:
        min_laba, max_laba = laba_text.replace('Rp', '').replace(' juta/bulan', '').split('-')
        avg_laba = (float(min_laba) + float(max_laba)) / 2 * 1000000
    else:
        avg_laba = 50000000  # Default 50 juta
    
    # Hitung ROI tahunan
    roi_tahunan = (avg_laba * 12 / modal) * 100
    
    return {
        'modal': modal,
        'laba_bulanan': avg_laba,
        'roi_tahunan': roi_tahunan,
        'balik_modal_bulan': modal / avg_laba if avg_laba > 0 else 0
    }

def show_roi_comparison(franchises):
    """Tampilkan perbandingan ROI"""
    print("\n" + "=" * 80)
    print("PERBANDINGAN ROI (Return on Investment)")
    print("=" * 80)
    
    print(f"\n{'Brand':<15} {'Modal Awal':<15} {'Laba/Bulan':<15} {'ROI Tahunan':<12} {'Balik Modal':<15}")
    print("-" * 80)
    
    roi_data = []
    for franchise in franchises:
        roi = calculate_roi(franchise)
        nama = franchise['nama']
        modal = format_currency(roi['modal'])
        laba = format_currency(roi['laba_bulanan'])
        roi_tahun = f"{roi['roi_tahunan']:.1f}%"
        balik_modal = f"{roi['balik_modal_bulan']:.0f} bulan"
        
        print(f"{nama:<15} {modal:<15} {laba:<15} {roi_tahun:<12} {balik_modal:<15}")
        roi_data.append({
            'nama': nama,
            'roi_tahunan': roi['roi_tahunan'],
            'balik_modal_bulan': roi['balik_modal_bulan']
        })
    
    # Rekomendasi berdasarkan ROI
    print("\n" + "=" * 80)
    print("REKOMENDASI BERDASARKAN ROI")
    print("=" * 80)
    
    # Cari franchise dengan ROI tertinggi
    best_roi = max(roi_data, key=lambda x: x['roi_tahunan'])
    fastest_payback = min(roi_data, key=lambda x: x['balik_modal_bulan'])
    
    print(f"\n[ROI TERTINGGI] {best_roi['nama']} ({best_roi['roi_tahunan']:.1f}%/tahun)")
    print(f"[BALIK MODAL TERCEPAT] {fastest_payback['nama']} ({fastest_payback['balik_modal_bulan']:.0f} bulan)")

def show_financing_scenarios(franchises):
    """Tampilkan skenario pembiayaan untuk setiap franchise"""
    print("\n" + "=" * 80)
    print("SKENARIO PEMBIAYAAN DENGAN KUR")
    print("=" * 80)
    
    modal_sendiri = 80000000  # Rp80 juta
    
    for franchise in franchises:
        nama = franchise['nama']
        tipe_gerai = franchise['tipe_gerai'][0]
        total_modal = tipe_gerai['total_modal']
        
        print(f"\n{nama} (Modal: {format_currency(total_modal)}):")
        
        # Opsi 1: Modal sendiri + KUR Mikro
        kur_mikro_1 = min(100000000, total_modal - modal_sendiri)
        if kur_mikro_1 > 0:
            cicilan_1 = kur_mikro_1 * (1 + 0.06 * 5) / 60  # Bunga 6% flat, tenor 60 bulan
            print(f"  Opsi 1: Modal sendiri {format_currency(modal_sendiri)} + KUR Mikro {format_currency(kur_mikro_1)}")
            print(f"           Cicilan/bulan: {format_currency(cicilan_1)}")
        
        # Opsi 2: Modal sendiri + KUR Mikro + KUR Kecil
        kur_kecil_2 = max(0, total_modal - modal_sendiri - 100000000)
        if kur_kecil_2 > 0 and kur_kecil_2 <= 500000000:
            cicilan_mikro = 100000000 * (1 + 0.06 * 5) / 60
            cicilan_kecil = kur_kecil_2 * (1 + 0.06 * 5) / 60
            total_cicilan = cicilan_mikro + cicilan_kecil
            print(f"  Opsi 2: Modal sendiri {format_currency(modal_sendiri)} + KUR Mikro Rp100 juta + KUR Kecil {format_currency(kur_kecil_2)}")
            print(f"           Cicilan/bulan: {format_currency(total_cicilan)}")
        
        # Opsi 3: 100% dari bank
        if total_modal <= 600000000:  # Maks KUR Rp600 juta
            cicilan_full = total_modal * (1 + 0.06 * 5) / 60
            print(f"  Opsi 3: 100% dari bank (KUR Rp100 juta + KUR Kecil {format_currency(total_modal - 100000000)})")
            print(f"           Cicilan/bulan: {format_currency(cicilan_full)}")

def main():
    """Fungsi utama"""
    # Tentukan path ke folder data
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / "data"
    
    # Load data franchise
    franchises = load_franchise_data(data_dir)
    
    # Tampilkan perbandingan
    compare_franchises(franchises)
    
    # Tampilkan perbandingan ROI
    show_roi_comparison(franchises)
    
    # Tampilkan skenario pembiayaan
    show_financing_scenarios(franchises)
    
    print("\n" + "=" * 80)
    print("KESIMPULAN")
    print("=" * 80)
    print("""
Berdasarkan analisis:
1. Alfamart dan Indomaret memiliki track record terbaik dengan balik modal 2-3 tahun
2. O!Save lebih murah namun belum ada data balik modal yang jelas
3. Alfamidi membutuhkan modal lebih besar namun potensi keuntungan lebih tinggi

Dengan modal sendiri Rp80 juta:
- Bisa memulai dengan KUR Mikro (tanpa agunan) untuk franchise kecil
- Untuk franchise lebih besar, perlu KUR Kecil (perlu agunan)

Rekomendasi:
- Mulai dengan Alfamart atau Indomaret tipe kecil (18 rak)
- Gunakan kombinasi modal sendiri + KUR
- Pastikan lokasi strategis sebelum memulai
""")

if __name__ == "__main__":
    main()