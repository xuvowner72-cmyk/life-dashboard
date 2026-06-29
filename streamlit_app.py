import streamlit as st

st.title("🎯 My Life Dashboard")

# Initialize Memory
if 'sleep_val' not in st.session_state: st.session_state.sleep_val = 5.0
if 'learn_val' not in st.session_state: st.session_state.learn_val = 0.0
if 'focus_val' not in st.session_state: st.session_state.focus_val = "Average"
if 'expenses' not in st.session_state: st.session_state.expenses = []

# Sleep & Learning (Unchanged)
st.subheader("🌙 Sleep & Timetable")
st.session_state.sleep_val = st.slider("How was your sleep quality?", 1.0, 10.0, st.session_state.sleep_val)

st.subheader("🧠 Learning & Focus")
st.session_state.learn_val = st.slider("Hours spent in Deep Learning:", 0.0, 12.0, st.session_state.learn_val)
st.session_state.focus_val = st.radio("How was your focus today?", ["Distracted", "Average", "High"], 
                                      index=["Distracted", "Average", "High"].index(st.session_state.focus_val))

# --- Money Wisdom (Updated with Delete) ---
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
    total = 0
    # Use columns to create a delete button for each row
    for i, exp in enumerate(st.session_state.expenses):
        col1, col2 = st.columns([3, 1])
        col1.write(f"{exp['item']}: ₹{exp['amount']} ({exp['type']})")
        if col2.button("Delete", key=f"del_{i}"):
            del st.session_state.expenses[i]
            st.rerun() # Refresh the page to remove the item
        total += exp['amount']
    
    st.write(f"**Total Spent: ₹{total}**")
    
