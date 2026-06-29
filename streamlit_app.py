import streamlit as st

st.title("🎯 My Life Dashboard")

# --- Finance Section (Upgraded) ---
st.subheader("💰 Money Wisdom")

# Initialize a list to hold expenses in the session
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# Input for new expense
expense_name = st.text_input("What did you buy?")
amount = st.number_input("Amount (₹):", min_value=0)
category = st.selectbox("Type:", ["Need", "Want", "Waste"])

if st.button("Add Expense"):
    if amount > 0:
        st.session_state.expenses.append({"item": expense_name, "amount": amount, "type": category})
        st.success(f"Added {expense_name}")
    else:
        st.warning("Please enter an amount greater than 0.")

# Show the list
if st.session_state.expenses:
    st.write("### Today's Expenses:")
    total = 0
    for i, exp in enumerate(st.session_state.expenses):
        st.write(f"{i+1}. {exp['item']} - ₹{exp['amount']} ({exp['type']})")
        total += exp['amount']
    st.write(f"**Total Spent: ₹{total}**")
    
    # Warning for Waste
    waste_total = sum(e['amount'] for e in st.session_state.expenses if e['type'] == "Waste")
    if waste_total > 0:
        st.error(f"⚠️ You have spent ₹{waste_total} on 'Waste' today. Stop and think!")
        
