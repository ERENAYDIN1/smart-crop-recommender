# Mahsül Öneri Sistemi

Toprak ve iklim verilerine göre en uygun mahsülün yetiştirilmesini öneren çok sınıflı makine öğrenmesi projesi. 2200 örnekten oluşan Crop Recommendation Dataset üzerinde 5 farklı algoritma karşılaştırılmış, en iyi model tarım temalı özel bir Streamlit arayüzüyle canlıya alınmıştır.

---

## Özellikler

**Makine Öğrenmesi**
- 7 girdi değişkeni: N, P, K, sıcaklık, nem, pH, yağış
- 22 mahsül sınıfı arasından tahmin
- 5 algoritma karşılaştırması: Random Forest, Decision Tree, KNN, SVM, Gradient Boosting
- %60 eğitim / %20 doğrulama / %20 test — stratified bölme
- SHAP ile model açıklaması

**Web Arayüzü**
- Tarım temalı özel CSS tasarım (koyu yeşil + toprak tonları)
- 3 kolonlu girdi formu: Toprak Besinleri / İklim Koşulları / Toprak Özellikleri
- pH'a göre dinamik toprak durumu göstergesi
- Sonuçlar modal pencerede gösterilir:
  - Önerilen mahsülün Türkçe adı, emojisi ve güven oranı
  - İlk 3 adayın gradient olasılık çubukları
  - Kullanılan parametrelerin özet tablosu
- 22 mahsülün tamamı için Türkçe isim ve emoji eşlemesi
- Sidebar: NPK, pH ve yağış referans rehberleri

---

## Kurulum

```bash
pip install --prefer-binary -r requirements.txt
```

> Python başlatıcıları bozuksa: `python -m pip install --prefer-binary -r requirements.txt`

---

## Çalıştırma

```bash
streamlit run app.py
```

> Başlatıcı sorunu yaşıyorsanız: `python -m streamlit run app.py`

Uygulama tarayıcıda `http://localhost:8501` adresinde açılır.

---

## Kullanım

1. Sayfadaki 3 kolonlu formu doldurun:
   - **Toprak Besinleri:** Azot (N), Fosfor (P), Potasyum (K)
   - **İklim Koşulları:** Sıcaklık, Nem, Yağış
   - **Toprak Özellikleri:** pH değeri
2. **Mahsül Analizi Yap** butonuna tıklayın
3. Açılan modal pencerede sonucu inceleyin:
   - Önerilen mahsül ve güven oranı
   - Alternatif en olası 3 aday
   - Girilen parametrelerin özeti

> **Güven oranı nedir?** Modelin 22 sınıfa dağıttığı olasılık içinden en yüksek payı alan mahsülün yüzdesidir. Mutlak doğruluk garantisi değil, modelin emin olma derecesini gösterir. Düşük çıkması (örn. %28), girilen koşulların birden fazla mahsüle eşit ölçüde uyduğu anlamına gelir.

---

## Proje Yapısı

```
smart-crop-recommender/
├── data/
│   └── Crop_recommendation.csv      # 2200 örnek, 7 özellik, 22 sınıf
├── models/
│   ├── best_model.pkl               # Eğitilmiş en iyi model
│   ├── scaler.pkl                   # StandardScaler
│   ├── label_encoder.pkl            # LabelEncoder (22 sınıf)
│   └── feature_names.pkl            # Özellik isimleri
├── analiz_ve_modelleme.ipynb        # Veri ön işleme, özellik seçimi, modelleme, değerlendirme
├── app.py                           # Streamlit uygulaması
├── requirements.txt                 # Python bağımlılıkları
└── README.md
```

---

## Notebook (analiz_ve_modelleme.ipynb)

Modelleri sıfırdan eğitmek için notebook'u sırayla çalıştırın. Tamamlandığında model dosyaları `models/` klasörüne otomatik kaydedilir.

| Adım | İçerik |
|------|--------|
| Görev 1 | IQR yöntemiyle aykırı değer tespiti ve temizleme |
| Görev 2 | Pearson, ANOVA F-testi, Mutual Information, Random Forest önem skoru ile özellik seçimi |
| Görev 3 | 5 algoritma eğitimi, stratified %60/%20/%20 bölme, karışıklık matrisleri |
| Görev 4 | Accuracy / Precision / Recall, ROC analizi, SHAP açıklaması |

---

## Veri Seti

| Özellik | Açıklama | Birim |
|---------|----------|-------|
| N | Azot içeriği | kg/ha |
| P | Fosfor içeriği | kg/ha |
| K | Potasyum içeriği | kg/ha |
| temperature | Ortalama sıcaklık | °C |
| humidity | Bağıl nem | % |
| ph | Toprak pH değeri | 0–14 |
| rainfall | Yıllık yağış | mm |
| label | Önerilen mahsül (hedef) | 22 sınıf |

---

## Gereksinimler

- Python 3.9+
- Paketler: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `streamlit`, `joblib`, `shap`, `scipy`
