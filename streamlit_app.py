import streamlit as st
from datetime import datetime, timedelta, time

st.title("🎯 My Life Dashboard")

# Initialize Memory
if 'sleep_val' not in st.session_state: st.session_state.sleep_val = 5.0
if 'learn_val' not in st.session_state: st.session_state.learn_val = 0.0
if 'focus_val' not in st.session_state: st.session_state.focus_val = "Average"
if 'expenses' not in st.session_state: st.session_state.expenses = []

# --- Sleep & Timetable (New Logic) ---
st.subheader("🌙 Sleep & Timetable")
st.session_state.sleep_val = st.slider("How was your sleep quality?", 1.0, 10.0, st.session_state.sleep_val)

# Bedtime selector (defaults to 10:00 PM)
bedtime = st.time_input("What time do you plan to go to sleep?", time(22, 0))

# Calculate Wake up time (+ 6 hours)
# We convert time to a datetime object, add 6 hours, then convert back to time
dummy_date = datetime.combine(datetime.today(), bedtime)
wakeup_time = (dummy_date + timedelta(hours=6)).time()

st.write(f"### ⏰ If you sleep at {bedtime.strftime('%I:%M %p')}, you should wake up at: **{wakeup_time.strftime('%I:%M %p')}**")

# --- Learning & Focus ---
st.subheader("🧠 Learning & Focus")
st.session_state.learn_val = st.slider("Hours spent in Deep Learning:", 0.0, 12.0, st.session_state.learn_val)
st.session_state.focus_val = st.radio("How was your focus today?", ["Distracted", "Average", "High"], 
                                      index=["Distracted", "Average", "High"].index(st.session_state.focus_val))

# --- Money Wisdom ---
st.subheader("💰 Money Wisdom")
expense_name = st.text_input("What did you buy?")
amount = st.number_input("Amount (₹):", min_value=0)
category = st.selectbox("Type:", ["Need", "Want", "Waste"])

if st.button("Add Expense"):
    if amount > 0:
        st.session_state.expenses.append({"item": expense_name, "amount": amount, "type": category})
        st.success(f"Added {expense_name}")

if st.session_state.expenses:
    st.write("### Today's Expenses:")
    for i, exp in enumerate(st.session_state.expenses):
        col1, col2 = st.columns([3, 1])
        col1.write(f"{exp['item']}: ₹{exp['amount']} ({exp['type']})")
        if col2.button("Delete", key=f"del_{i}"):
            del st.session_state.expenses[i]
            st.rerun()
    total = sum(exp['amount'] for exp in st.session_state.expenses)
    st.write(f"**Total Spent: ₹{total}**")
  
