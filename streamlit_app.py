import streamlit as st

st.set_page_config(page_title="My Life Dashboard", layout="centered")

st.title("🎯 My Life Dashboard")

# 1. Sleep Tracking
st.subheader("🌙 Sleep & Timetable")
sleep_quality = st.select_slider("How was your sleep quality?", options=["Bad", "Okay", "Good", "Great"])
wake_time = st.time_input("What time did you wake up?")

# 2. Focus/Learning & Reflection
st.subheader("🧠 Learning & Focus")
learning_hours = st.slider("Hours spent in Deep Learning:", 0.0, 8.0, 0.0)
focus_score = st.radio("How was your focus today?", ["Distracted", "Average", "High"])

# --- NEW: Daily Reflection ---
st.info("💡 Reflection: What is the ONE big thing you learned today?")
daily_reflection = st.text_area("Write it down here to lock it in your memory:")

# 3. Finance (The "Careless" Fix)
st.subheader("💰 Money Wisdom")
expense_type = st.selectbox("Did you spend money on:", ["Need", "Want", "Waste"])
if expense_type == "Waste":
    st.warning("⚠️ Take a breath! Ask yourself: 'Will this matter in 30 days?'")
amount = st.number_input("Amount spent (₹):", min_value=0)

# 4. Save
if st.button("Save Daily Progress"):
    if daily_reflection:
        st.success("Entry saved! Great work keeping your focus.")
    else:
        st.warning("Don't forget to add your reflection before saving!")
      
