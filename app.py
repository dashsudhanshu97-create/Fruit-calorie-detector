import streamlit as st
from PIL import Image
from utils.detector import detect_fruits
from utils.calorie import calculate_calories

st.title("🍎 Fruit Calorie Detector")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    # detect fruits
    count = detect_fruits(image)

    if not count:
        st.warning("No fruits detected ❌")
    else:
        st.success(f"Detected Fruits: {dict(count)}")

        # calculate calories
        total, details = calculate_calories(count)

        st.subheader("Calories Breakdown 🍽️")
        for fruit, cal in details.items():
            st.write(f"{fruit} → {cal} kcal")

        st.subheader(f"🔥 Total Calories: {total} kcal")