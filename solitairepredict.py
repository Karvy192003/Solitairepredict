import streamlit as st  # ✅ This line is required!
import pandas as pd
from sklearn.linear_model import LinearRegression

# 🧾 Load your dataset
data = pd.read_csv("solitaire.csv")

# 🎯 Prepare features and target
X = data[['Carat', 'Cut', 'Clarity']]
y = data['Price_INR']

# 🔁 Train the model
model = LinearRegression()
model.fit(X, y)

# 👉 Page Title and Description
st.set_page_config(page_title="Diamond Estimator", layout="centered")
st.markdown("<h2>💠 Diamond Estimator: Craft Your Sparkle</h2>", unsafe_allow_html=True)
st.write("📊 Estimate your diamond's value based on precision-cut features.")

# 👉 Sidebar input sliders
st.sidebar.header("🛠️ Personalize Your Diamond")

carat = st.sidebar.slider("💎 Choose Carat Weight", min_value=0.25, max_value=1.0, value=0.5, step=0.05)

cut = st.sidebar.select_slider(
    "✨ Select Cut Quality (Brilliance Level)",
    options=[1, 2, 3],
    value=2,
    help="1 = Good, 2 = Very Good, 3 = Excellent"
)

clarity = st.sidebar.slider(
    "🔍 Choose Clarity Grade (Purity Scale)",
    min_value=1, max_value=5, value=3,
    help="1 = IF (Flawless), 5 = SI1 (Slight Inclusions)"
)

# 🚀 Predict price
if st.button("🔮 Predict My Diamond Price"):
    input_data = [[carat, cut, clarity]]
    prediction = model.predict(input_data)[0]
    prediction = round(prediction, 2)

    st.markdown(f"""
        <div style='text-align: center; margin-top: 30px; padding: 15px; border-radius: 12px;
                    background: linear-gradient(to right, #D3CCE3, #E9E4F0); color: #333;
                    font-size: 22px; font-weight: bold;'>
            ✅ Estimated Price: ₹ {prediction:,.2f} INR
        </div>
    """, unsafe_allow_html=True)
