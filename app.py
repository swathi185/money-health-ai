import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Money Health AI",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("💰 Money Health Score – India")
st.caption("An AI-powered personal finance mentor for everyday Indians")
st.info("⌨️ Tip: Use TAB to move between fields")

st.divider()

# ---------------- FORM ----------------
with st.form("money_form"):

    st.subheader("👤 User Information")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")

    with col2:
        income = st.text_input("Monthly Income (₹)")

    with col3:
        expenses = st.text_input("Monthly Expenses (₹)")

    st.subheader("💼 Financial Status")
    col4, col5 = st.columns(2)

    with col4:
        savings = st.text_input("Savings (₹)")

    with col5:
        loans = st.text_input("Loans (₹)")

    st.subheader("🎯 Goals & Life Events")
    col6, col7 = st.columns(2)

    with col6:
        life_event = st.selectbox(
            "Upcoming Life Event",
            ["None", "Bonus", "Marriage", "New Baby"]
        )

    with col7:
        retirement_age = st.number_input(
            "Target Retirement Age",
            min_value=40,
            max_value=65,
            value=60
        )

    submitted = st.form_submit_button("📊 Check My Money Health")

# ---------------- LOGIC ----------------
if submitted:
    try:
        age = int(age)
        income = float(income)
        expenses = float(expenses)
        savings = float(savings)
        loans = float(loans)

        # -------- SCORE --------
        score = 100

        if expenses > income:
            score -= 30
        if savings < income * 0.2:
            score -= 20
        if savings < expenses * 3:
            score -= 25
        if loans > income * 0.4:
            score -= 25

        score = max(score, 0)

        # -------- RESULT --------
        st.divider()
        st.subheader("📈 Your Money Health Result")
        st.metric("Money Health Score", f"{score} / 100")

        if score >= 70:
            st.success("You are financially healthy 👍")
        elif score >= 40:
            st.warning("Your financial health is average ⚠️")
        else:
            st.error("Your financial health needs urgent attention ❌")

        # -------- AI INSIGHTS --------
        st.subheader("🧠 AI Insights")

        issues = []

        if expenses > income:
            issues.append("High expenses compared to income")
        if savings < income * 0.2:
            issues.append("Low savings rate")
        if savings < expenses * 3:
            issues.append("No emergency fund")
        if loans > income * 0.4:
            issues.append("High loan burden")

        if not issues:
            st.info("No major issues detected. Keep maintaining your habits.")
        else:
            for issue in issues:
                st.warning(issue)

        # -------- HOW TO DO IT (MOST IMPORTANT) --------
        st.subheader("🛠️ How to Improve – Action Plan")

        steps = []

        if expenses > income:
            steps.append(
                "📌 Track expenses for 30 days and cut at least 10–20% from non-essential spending (food delivery, subscriptions, impulse buys)."
            )

        if savings < income * 0.2:
            steps.append(
                "📌 Follow the 50-30-20 rule: 50% needs, 30% wants, 20% savings. Start by auto-transferring savings on salary day."
            )

        if savings < expenses * 3:
            steps.append(
                "📌 Build an emergency fund equal to 3 months of expenses by saving a fixed amount every month in a liquid fund or savings account."
            )

        if loans > income * 0.4:
            steps.append(
                "📌 Prioritize closing high-interest loans first (credit cards, personal loans) before starting new investments."
            )

        if not steps:
            steps.append(
                "📌 Continue investing regularly and review your finances every 6 months."
            )

        for step in steps:
            st.write(step)

        # -------- LIFE EVENT ADVISOR --------
        if life_event != "None":
            st.subheader("🎉 Life Event Guidance")

            if life_event == "Bonus":
                st.info(
                    "How to use bonus: "
                    "50% invest (mutual funds / PPF), "
                    "30% save for goals, "
                    "20% spend guilt-free."
                )

            elif life_event == "Marriage":
                st.info(
                    "How to prepare for marriage: "
                    "Create joint budget, increase emergency fund, "
                    "review health & life insurance."
                )

            elif life_event == "New Baby":
                st.info(
                    "How to prepare for a baby: "
                    "Upgrade health insurance, "
                    "start education savings, "
                    "increase emergency fund."
                )

        # -------- FIRE READINESS --------
        st.subheader("🔥 FIRE (Early Retirement) Guidance")

        if retirement_age < 50:
            st.warning(
                "How to achieve early retirement: "
                "Save aggressively (30–40% income), "
                "focus on equity investments, "
                "avoid lifestyle inflation."
            )
        elif retirement_age <= 60:
            st.success(
                "How to stay on track: "
                "Invest consistently, "
                "review asset allocation yearly, "
                "increase savings with income growth."
            )
        else:
            st.info(
                "How to plan comfortably: "
                "Maintain steady investments and control risk."
            )

    except ValueError:
        st.error("⚠️ Please enter valid numeric values in all input fields")
