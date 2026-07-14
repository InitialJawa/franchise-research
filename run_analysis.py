#!/usr/bin/env python3
"""
Script utama untuk menjalankan semua analisis franchise
Menjalankan semua script analisis secara berurutan
"""

import subprocess
import sys
from pathlib import Path

def run_script(script_path, description):
    """Jalankan script Python"""
    print(f"\n{'='*80}")
    print(f"MENJALANKAN: {description}")
    print(f"{'='*80}\n")
    
    try:
        # Jalankan script
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        # Tampilkan output
        print(result.stdout)
        
        # Tampilkan error jika ada
        if result.stderr:
            print(f"\nERROR:\n{result.stderr}")
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"Error menjalankan script: {e}")
        return False

def main():
    """Fungsi utama"""
    # Tentukan path ke folder scripts
    script_dir = Path(__file__).parent
    scripts = [
        ("scripts/compare_franchise.py", "Perbandingan Franchise"),
        ("scripts/simulasi_kur.py", "Simulasi Cicilan KUR"),
        ("scripts/analisis_keuntungan.py", "Analisis Keuntungan"),
    ]
    
    print("=" * 80)
    print("FRANCHISE MINIMARKET RESEARCH - ANALISIS LENGKAP")
    print("=" * 80)
    
    success_count = 0
    total_count = len(scripts)
    
    for script_path, description in scripts:
        full_path = script_dir / script_path
        if full_path.exists():
            if run_script(full_path, description):
                success_count += 1
        else:
            print(f"\nScript tidak ditemukan: {full_path}")
    
    print("\n" + "=" * 80)
    print("RINGKASAN EKSEKUSI")
    print("=" * 80)
    print(f"\nBerhasil: {success_count}/{total_count} script")
    
    if success_count == total_count:
        print("\n[OK] Semua analisis berhasil dijalankan!")
        print("\n[DATA] Hasil analisis tersimpan di:")
        print("   - data/alfamart.json")
        print("   - data/indomaret.json")
        print("   - data/osave.json")
        print("   - data/alfamidi.json")
        print("   - data/kur.json")
        print("   - notes/pipo_hargiyanto.md")
        print("   - notes/lokasi.md")
        print("   - docs/syarat_kur.md")
        print("   - docs/tips_franchise.md")
        print("   - docs/referensi.md")
        print("\n[SCRIPT] Script analisis tersimpan di:")
        print("   - scripts/compare_franchise.py")
        print("   - scripts/simulasi_kur.py")
        print("   - scripts/analisis_keuntungan.py")
        print("\n[TIPS] Untuk menjalankan script individual:")
        print("   python scripts/compare_franchise.py")
        print("   python scripts/simulasi_kur.py")
        print("   python scripts/analisis_keuntungan.py")
    else:
        print("\n[WARNING] Beberapa script gagal dijalankan")
        print("   Periksa error di atas untuk detail")

if __name__ == "__main__":
    main()