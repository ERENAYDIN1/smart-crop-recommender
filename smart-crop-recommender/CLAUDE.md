# Mahsül Öneri Sistemi – Makine Öğrenmesi Projesi

Toprak ve iklim verilerine göre en uygun mahsülün yetiştirilmesini öngören çok sınıflı sınıflandırma projesi.

---

## Görevler

**Görev 1 – Veri Ön İşleme**
- IQR yöntemiyle aykırı değer tespiti ve temizleme
- Veri seti seçimi gerekçelendirildi

**Görev 2 – Özellik Seçimi**
- StandardScaler ile normalizasyon
- 4 farklı yöntem: Pearson Korelasyon, ANOVA F-testi, Mutual Information, Random Forest Önemi

**Görev 3 – Modelleme**
- 5 algoritma: Random Forest, Decision Tree, KNN, SVM, Gradient Boosting
- %60 eğitim / %20 doğrulama / %20 test ayrımı (stratified)
- Tüm modeller için karışıklık matrisi

**Görev 4 – Model Değerlendirme**
- Accuracy / Precision / Recall (eğitim + doğrulama + test)
- ROC analizi (eğitim + doğrulama)
- Recall analizi (eğitim + doğrulama)
- SHAP ile kara kutu model açıklaması
- Streamlit ile canlıya alma

---

## Proje Yapısı

```
Crop_Project/
├── data/
│   └── Crop_recommendation.csv      # 2200 örnek, 7 özellik, 22 mahsül sınıfı
├── models/
│   ├── best_model.pkl               # Eğitilmiş en iyi model (~2.7 MB)
│   ├── scaler.pkl                   # StandardScaler
│   ├── label_encoder.pkl            # LabelEncoder (22 sınıf)
│   └── feature_names.pkl            # Özellik isim listesi
├── analiz_ve_modelleme.ipynb        # Ana notebook – Görev 1-4
├── app.py                           # Streamlit uygulaması
├── requirements.txt                 # Python bağımlılıkları
├── .gitignore
└── CLAUDE.md
```

---

## Veri Seti

| Özellik | Açıklama |
|---|---|
| N | Azot içeriği (kg/ha) |
| P | Fosfor içeriği (kg/ha) |
| K | Potasyum içeriği (kg/ha) |
| temperature | Ortalama sıcaklık (°C) |
| humidity | Bağıl nem (%) |
| ph | Toprak pH değeri (0–14) |
| rainfall | Yıllık yağış (mm) |
| label | Önerilen mahsül – 22 sınıf (hedef) |

---

## Çalıştırma

```bash
# Bağımlılıkları yükle
pip install --prefer-binary -r requirements.txt

# Streamlit uygulamasını başlat
streamlit run app.py
```

Notebook yeniden çalıştırılmak istenirse `analiz_ve_modelleme.ipynb` açılıp tüm hücreler sırayla çalıştırılır. Model dosyaları `models/` klasörüne otomatik kaydedilir.

---

## Proje Durumu

✅ Veri ön işleme tamamlandı  
✅ Özellik seçimi tamamlandı (4 yöntem)  
✅ 5 model eğitildi ve değerlendirildi  
✅ Model dosyaları kaydedildi  
✅ Streamlit uygulaması çalışıyor  
