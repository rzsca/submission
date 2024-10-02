import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
sns.set(style='dark')

# Judul dashboard
st.title("Dashboard Analisis Kualitas Udara di Wilayah Guanyuan dan Huairou")

# Memuat Dataset
guanyuan_df = pd.read_csv('https://raw.githubusercontent.com/marceloreis/HTI/c8688fc517972e373d7c1df3a8d82b2a2468131f/PRSA_Data_20130301-20170228/PRSA_Data_Guanyuan_20130301-20170228.csv')
huairou_df = pd.read_csv('https://raw.githubusercontent.com/marceloreis/HTI/c8688fc517972e373d7c1df3a8d82b2a2468131f/PRSA_Data_20130301-20170228/PRSA_Data_Huairou_20130301-20170228.csv')

# Data Cleaning
def clean_data(df):
    df = df.drop(["No"], axis=1)
    if 'wd' in df.columns:
        df.wd.fillna(value=df.wd.mode()[0], inplace=True)
    kolom_handle = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']
    df[kolom_handle] = df[kolom_handle].fillna(df[kolom_handle].mean())
    return df

guanyuan_df = clean_data(guanyuan_df)
huairou_df = clean_data(huairou_df)

# Expander untuk dataset
with st.expander("Tampilkan Dataset"):
    show_guanyuan = st.checkbox("Dataset Guanyuan")
    show_huairou = st.checkbox("Dataset Huairou")
    
    if show_guanyuan:
        st.subheader("Dataset Guanyuan")
        st.write(guanyuan_df)

    if show_huairou:
        st.subheader("Dataset Huairou")
        st.write(huairou_df)

# Rata-rata Polutan
guanyuan_avg = guanyuan_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].mean()
huairou_avg = huairou_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].mean()

# Interactive Bar Chart Comparison
st.subheader("Perbandingan Rata-rata Kualitas Udara")

# Create a DataFrame for Plotly
avg_df = pd.DataFrame({
    'Indicators': ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'],
    'Guanyuan': guanyuan_avg.values,
    'Huairou': huairou_avg.values
})

# Create Plotly bar chart
fig = go.Figure()
fig.add_trace(go.Bar(x=avg_df['Indicators'], y=avg_df['Guanyuan'], name='Guanyuan', marker_color='blue'))
fig.add_trace(go.Bar(x=avg_df['Indicators'], y=avg_df['Huairou'], name='Huairou', marker_color='orange'))

# Update layout
fig.update_layout(
    title='Perbandingan Rata-rata Kualitas Udara',
    xaxis_title='Indikator',
    yaxis_title='Konsentrasi',
    barmode='group',
    template='plotly_dark'
)

# Display Plotly chart
st.plotly_chart(fig)


# Tab Scatter plots yang memvisualisasikan korelasi antara polutan dan curah hujan
st.subheader("Pengaruh Curah Hujan terhadap Konsentrasi Polutan di Guanyuan")
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
tab_labels = [f"{pollutant}" for pollutant in pollutants]
tabs = st.tabs(tab_labels)

for i, pollutant in enumerate(pollutants):
    with tabs[i]:
        fig = px.scatter(guanyuan_df, x='RAIN', y=pollutant,
                         title=f'Pengaruh Curah Hujan terhadap {pollutant}',
                         labels={'RAIN': 'Curah Hujan (RAIN)', pollutant: f'Konsentrasi {pollutant}'})
        st.plotly_chart(fig)



# Kesimpulan
st.subheader("Kesimpulan")
st.write("""
- Curah hujan pada wilayah Guanyuan memiliki efek penurunan kecil terhadap sebagian polutan seperti PM2.5, PM10, SO2, NO2, dan CO, namun penurunan tersebut tidak signifikan. Polutan seperti CO memiliki tingkat konsentrasi yang tinggi, sehingga curah hujan tidak cukup untuk mengurangi polusi. Adapun sebaliknya pada O3 mengalami peningkatan konsentrasi saat curah hujan terjadi.

- Kualitas udara di Guanyuan lebih buruk dibandingkan dengan Huairou, terutama dalam PM2.5, PM10, SO2, NO2, dan CO yang dimana semuanya lebih tinggi di Guanyuan.
""")
