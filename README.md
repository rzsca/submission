# Dashboard Analisis Kualitas Udara di Wilayah Guanyuan dan Huairou
Dashboard ini dirancang untuk menganalisis kualitas udara di dua wilayah, Guanyuan dan Huairou. Menggunakan data yang relevan, dashboard ini memberikan wawasan mendalam tentang faktor-faktor yang memengaruhi kualitas udara dan membandingkan tingkat polusi antara kedua daerah.

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
git clone https://github.com/rzsca/submission.git
cd submission
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```
