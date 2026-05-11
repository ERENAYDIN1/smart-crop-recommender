# Mahsül Öneri Sistemi

Toprak ve iklim verilerine göre en uygun mahsülün yetiştirilmesini öneren çok sınıflı makine öğrenmesi projesi. 2200 örnekten oluşan Crop Recommendation Dataset üzerinde 5 farklı algoritma eğitilmiş, en iyi model Streamlit arayüzüyle canlıya alınmıştır.

## Özellikler

- 7 girdi değişkeni: N, P, K, sıcaklık, nem, pH, yağış
- 22 mahsül sınıfı arasından tahmin
- 5 algoritma karşılaştırması: Random Forest, Decision Tree, KNN, SVM, Gradient Boosting
- SHAP ile model açıklaması
- Streamlit web arayüzü

## Kurulum

```bash
pip install --prefer-binary -r requirements.txt
```

> Python başlatıcıları bozuksa `python -m pip install --prefer-binary -r requirements.txt` kullanın.

## Çalıştırma

```bash
streamlit run app.py
```

> Başlatıcı sorunu yaşıyorsanız: `python -m streamlit run app.py`

Uygulama tarayıcıda `http://localhost:8501` adresinde açılır.

## Kullanım

1. Sol panelden toprak ve iklim değerlerini girin (N, P, K, sıcaklık, nem, pH, yağış)
2. **Mahsül Öner** butonuna tıklayın
3. Önerilen mahsül ve ilk 3 adayın olasılık dağılımı görüntülenir

## Proje Yapısı

```
smart-crop-recommender/
├── data/
│   └── Crop_recommendation.csv      # 2200 örnek, 7 özellik, 22 sınıf
├── models/
│   ├── best_model.pkl               # Eğitilmiş en iyi model
│   ├── scaler.pkl                   # StandardScaler
│   ├── label_encoder.pkl            # LabelEncoder
│   └── feature_names.pkl            # Özellik isimleri
├── analiz_ve_modelleme.ipynb        # Veri ön işleme, özellik seçimi, modelleme
├── app.py                           # Streamlit uygulaması
├── requirements.txt
└── README.md
```

## Notebook (analiz_ve_modelleme.ipynb)

Modelleri sıfırdan eğitmek için notebook'u sırayla çalıştırın. Eğitim tamamlandığında model dosyaları `models/` klasörüne otomatik kaydedilir.

| Adım | İçerik |
|------|--------|
| Görev 1 | IQR yöntemiyle aykırı değer temizleme |
| Görev 2 | Pearson, ANOVA F-testi, Mutual Information, Random Forest önem skoru ile özellik seçimi |
| Görev 3 | 5 algoritma eğitimi, %60/%20/%20 stratified bölme, karışıklık matrisleri |
| Görev 4 | Accuracy/Precision/Recall, ROC analizi, SHAP açıklaması |

## Gereksinimler

- Python 3.9+
- Paketler: pandas, numpy, scikit-learn, matplotlib, seaborn, streamlit, joblib, shap, scipy
