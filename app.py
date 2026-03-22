import streamlit as st

# ---------------- TITLE ----------------
st.title("Money Health Score - India")
st.write("Enter your details to check your money health")

# ---------------- INPUTS (EMPTY BY DEFAULT) ----------------
age = st.text_input("Enter your age")
income = st.text_input("Monthly income (₹)")
expenses = st.text_input("Monthly expenses (₹)")
savings = st.text_input("Current savings (₹)")
loans = st.text_input("Total loans (₹)")

# ---------------- BUTTON ----------------
clicked = st.button("Check My Money Health")

# ---------------- LOGIC ----------------
if clicked:
    try:
        age = int(age)
        income = float(income)
        expenses = float(expenses)
        savings = float(savings)
        loans = float(loans)

        score = 100

        if expenses > income:
            score -= 30

        if savings < income * 0.2:
            score -= 20

        if savings < expenses * 3:
            score -= 25

        if loans > income * 0.4:
            score -= 25

        if score < 0:
            score = 0

        # ---------------- OUTPUT ----------------
        st.subheader(f"Your Money Health Score: {score}/100")

        if score >= 70:
            st.success("You are financially healthy 👍")
        elif score >= 40:
            st.warning("Your finances are average. Improvement needed ⚠️")
        else:
            st.error("Your financial health needs urgent attention ❌")

        # ---------------- AI ADVISOR ----------------
        st.markdown("### AI Money Advisor 🧠")

        advice = []

        if expenses > income:
            advice.append("Your expenses are higher than your income. Start by cutting unnecessary monthly spending.")

        if savings < income * 0.2:
            advice.append("You are saving less than 20% of your income. Try to increase savings gradually.")

        if savings < expenses * 3:
            advice.append("You do not have an emergency fund. Aim to save at least 3 months of expenses.")

        if loans > income * 0.4:
            advice.append("Your loan burden is high compared to your income. Avoid taking new loans and focus on repayment.")

        if not advice:
            advice.append("Great job! Your financial habits are healthy. Stay consistent.")

        for tip in advice:
            st.write("•", tip)

    except ValueError:
        st.error("⚠️ Please enter valid numeric values in all fields")