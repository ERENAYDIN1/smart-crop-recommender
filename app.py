import streamlit as st
import numpy as np
import joblib
import pandas as pd
import os

st.set_page_config(
    page_title="Mahsül Öneri Sistemi",
    page_icon="🌾",
    layout="centered"
)

MODEL_PATH   = "models/best_model.pkl"
SCALER_PATH  = "models/scaler.pkl"
ENCODER_PATH = "models/label_encoder.pkl"
FEATS_PATH   = "models/feature_names.pkl"

@st.cache_resource
def load_artifacts():
    model   = joblib.load(MODEL_PATH)
    scaler  = joblib.load(SCALER_PATH)
    encoder = joblib.load(ENCODER_PATH)
    feats   = joblib.load(FEATS_PATH)
    return model, scaler, encoder, feats

def check_models():
    return all(os.path.exists(p) for p in [MODEL_PATH, SCALER_PATH, ENCODER_PATH, FEATS_PATH])

st.title("🌾 Mahsül Öneri Sistemi")
st.markdown(
    "Toprak ve iklim verilerinizi girerek **hangi mahsülün yetiştirilmesi gerektiğini** öğrenin."
)
st.divider()

if not check_models():
    st.error(
        "Model dosyaları bulunamadı. Lütfen önce `analiz_ve_modelleme.ipynb` "
        "notebook'unu çalıştırarak modeli eğitin ve kaydedin."
    )
    st.stop()

model, scaler, encoder, feature_names = load_artifacts()

st.subheader("📋 Toprak & İklim Değerleri")

col1, col2 = st.columns(2)

with col1:
    N = st.number_input(
        "Azot (N) – kg/ha", min_value=0, max_value=200, value=50, step=1,
        help="Topraktaki azot miktarı"
    )
    P = st.number_input(
        "Fosfor (P) – kg/ha", min_value=0, max_value=200, value=50, step=1,
        help="Topraktaki fosfor miktarı"
    )
    K = st.number_input(
        "Potasyum (K) – kg/ha", min_value=0, max_value=210, value=50, step=1,
        help="Topraktaki potasyum miktarı"
    )
    temperature = st.number_input(
        "Sıcaklık (°C)", min_value=0.0, max_value=55.0, value=25.0, step=0.1,
        help="Ortalama yıllık sıcaklık"
    )

with col2:
    humidity = st.number_input(
        "Nem (%)", min_value=0.0, max_value=100.0, value=70.0, step=0.1,
        help="Bağıl nem oranı"
    )
    ph = st.number_input(
        "pH", min_value=0.0, max_value=14.0, value=6.5, step=0.01,
        help="Toprak pH değeri (0-14)"
    )
    rainfall = st.number_input(
        "Yağış (mm)", min_value=0.0, max_value=3000.0, value=200.0, step=1.0,
        help="Yıllık toplam yağış miktarı"
    )

st.divider()

if st.button("🔍 Mahsül Öner", use_container_width=True, type="primary"):
    input_values = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    input_scaled = scaler.transform(input_values)

    prediction_enc = model.predict(input_scaled)[0]
    prediction_label = encoder.inverse_transform([prediction_enc])[0]

    probabilities = model.predict_proba(input_scaled)[0]
    top3_idx = np.argsort(probabilities)[::-1][:3]
    top3_labels = encoder.inverse_transform(top3_idx)
    top3_probs  = probabilities[top3_idx]

    st.success(f"### 🌱 Önerilen Mahsül: **{prediction_label.upper()}**")

    st.subheader("📊 Olasılık Dağılımı (İlk 3)")
    prob_df = pd.DataFrame({
        "Mahsül": top3_labels,
        "Olasılık (%)": (top3_probs * 100).round(2)
    })
    st.bar_chart(prob_df.set_index("Mahsül"))
    st.dataframe(prob_df, use_container_width=True)

    with st.expander("🔎 Girilen Değerler"):
        input_df = pd.DataFrame(
            [[N, P, K, temperature, humidity, ph, rainfall]],
            columns=["N (kg/ha)", "P (kg/ha)", "K (kg/ha)",
                     "Sıcaklık (°C)", "Nem (%)", "pH", "Yağış (mm)"]
        )
        st.dataframe(input_df, use_container_width=True)

st.divider()
st.caption(
    "Bu uygulama Crop Recommendation Dataset üzerinde eğitilmiş bir makine öğrenmesi "
    "modeli kullanmaktadır. Tahminler yalnızca rehber niteliğindedir."
)
