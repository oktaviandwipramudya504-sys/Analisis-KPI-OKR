import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Advanced KPI Dashboard", layout="wide")
st.title("🚀 Advanced KPI & OKR Analytics")

# Load Data
df = pd.read_csv('kpi_data.csv')
df['persentase'] = (df['realisasi'] / df['target']) * 100

# 1. Menambahkan Metrik Ringkasan (KPI Cards)
col1, col2, col3 = st.columns(3)
total_at_risk = len(df[df['persentase'] < 90])
avg_performance = df['persentase'].mean()

col1.metric("Rata-rata Kinerja", f"{avg_performance:.1f}%")
col2.metric("Indikator Perlu Perhatian", total_at_risk)
col3.metric("Departemen Aktif", len(df['departemen'].unique()))

st.divider()

# 2. Visualisasi dengan Logika Warna
fig = px.bar(df, x='key_result', y='persentase', color='persentase',
             color_continuous_scale=['red', 'yellow', 'green'],
             range_color=[70, 100],
             title="Analisis Kinerja Terperinci")
fig.add_hline(y=90, line_dash="dash", line_color="black")
st.plotly_chart(fig, use_container_width=True)

# 3. Intelligent Insights Module
st.subheader("💡 Rekomendasi Tindakan (AI-Generated)")
for index, row in df.iterrows():
    if row['persentase'] < 90:
        st.error(f"⚠️ {row['key_result']} ({row['departemen']}) di bawah target! Rekomendasi: Audit strategi operasional segera.")
    elif row['persentase'] > 110:
        st.warning(f"📈 {row['key_result']} ({row['departemen']}) melampaui target. Rekomendasi: Evaluasi apakah target terlalu rendah.")