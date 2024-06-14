import streamlit as st
import random

# Dummy user data
users = {
    "user1": {"password": "pass1", "balance": 1000},
    "user2": {"password": "pass2", "balance": 2000}
}

# Dummy transaction data
transactions = [
    {"user": "user1", "amount": 100, "category": ""},
    {"user": "user1", "amount": 50, "category": ""},
    {"user": "user2", "amount": 200, "category": ""},
    {"user": "user2", "amount": 150, "category": ""}
]

# Dummy machine learning model for transaction categorization
def categorize_transaction(transaction):
    categories = ["Shopping", "Food", "Travel", "Utilities"]
    return random.choice(categories)

# User authentication
def authenticate(username, password):
    if username in users and users[username]["password"] == password:
        return True
    else:
        return False

# Transaction history retrieval
def get_transactions(username):
    return [t for t in transactions if t["user"] == username]

# Make a transaction
def make_transaction(username, amount):
    if username in users:
        users[username]["balance"] -= amount
        transactions.append({"user": username, "amount": amount, "category": categorize_transaction({"user": username, "amount": amount})})
        return True
    else:
        return False

# Streamlit app
def main():
    st.title("Banking Application")

    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.success("Authentication successful.")

            st.subheader("Transaction History:")
            for transaction in get_transactions(username):
                st.write(transaction)

            transaction_amount = st.number_input("Enter the transaction amount", value=0.0, step=0.01)
            if st.button("Make Transaction"):
                if transaction_amount > 0:
                    if make_transaction(username, transaction_amount):
                        st.success(f"Transaction of {transaction_amount} successful.")
                        st.write("Updated Balance:", users[username]["balance"])
                    else:
                        st.error("Transaction failed.")
                else:
                    st.error("Invalid transaction amount.")
        else:
            st.error("Authentication failed.")

if __name__ == "__main__":
    main()