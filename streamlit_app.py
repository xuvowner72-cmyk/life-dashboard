import streamlit as st

st.title("🎯 My Life Dashboard")

# Initialize session state variables if they don't exist
if 'sleep' not in st.session_state: st.session_state.sleep = 5.0
if 'learning' not in st.session_state: st.session_state.learning = 0.0
if 'expenses' not in st.session_state: st.session_state.expenses = []

# --- Sleep & Timetable ---
st.subheader("🌙 Sleep & Timetable")
st.session_state.sleep = st.slider("How was your sleep quality?", 1.0, 10.0, st.session_state.sleep)

# --- Learning & Focus ---
st.subheader("🧠 Learning & Focus")
st.session_state.learning = st.slider("Hours spent in Deep Learning:", 0.0, 12.0, st.session_state.learning)

# --- Finance Section ---
st.subheader("💰 Money Wisdom")
expense_name = st.text_input("What did you buy?")
amount = st.number_input("Amount (₹):", min_value=0)
category = st.selectbox("Type:", ["Need", "Want", "Waste"])

if st.button("Add Expense"):
    if amount > 0:
        st.session_state.expenses.append({"item": expense_name, "amount": amount, "type": category})
        st.success(f"Added {expense_name}")

# Show the list and total
if st.session_state.expenses:
    st.write("### Today's Expenses:")
    total = 0
    for exp in st.session_state.expenses:
        st.write(f"- {exp['item']}: ₹{exp['amount']} ({exp['type']})")
        total += exp['amount']
    st.write(f"**Total Spent: ₹{total}**")
    
