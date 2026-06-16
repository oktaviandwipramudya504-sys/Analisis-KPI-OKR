import pandas as pd

# Kita baca file dengan mengabaikan header otomatis jika perlu
# 'sep' bisa diganti jadi ',' atau '\t' (tab) tergantung bagaimana file disimpan
try:
    df = pd.read_csv('kpi_data.csv')
    
    # Jika kolom tidak terdeteksi (semua jadi satu), kita bersihkan namanya
    df.columns = df.columns.str.strip()
    
    # Menghitung persentase secara manual
    df['persentase'] = (df['realisasi'] / df['target']) * 100
    
    print("--- Data yang Terbaca ---")
    print(df[['departemen', 'key_result', 'persentase']])
    
    # Filter yang "At Risk" (di bawah 90%)
    at_risk = df[df['persentase'] < 90]
    
    print("\n--- Perlu Perhatian (At Risk) ---")
    print(at_risk[['departemen', 'key_result', 'persentase']])

except Exception as e:
    print(f"Terjadi kesalahan: {e}")