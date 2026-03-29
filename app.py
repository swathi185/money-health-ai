import streamlit as st

st.set_page_config(page_title="AI Money Health Score", layout="centered")

st.title("💰 AI Money Health Score")
st.write("A 5-minute financial checkup for middle-class Indians")

st.divider()

# -------------------------
# USER INPUTS
# -------------------------

st.header("👤 Basic Details")

age = st.number_input("Your Age", min_value=18, max_value=70, value=25)

monthly_income = st.number_input(
    "Monthly Income (₹)",
    min_value=0,
    placeholder="Enter your monthly income"
)

monthly_expenses = st.number_input(
    "Monthly Expenses (₹)",
    min_value=0,
    placeholder="Enter your monthly expenses"
)

st.divider()

st.header("🏦 Financial Information")

emergency_savings = st.number_input(
    "Emergency Savings Available (₹)",
    min_value=0,
    placeholder="Savings you can use in emergency"
)

has_health_insurance = st.selectbox(
    "Do you have Health Insurance?",
    ["No", "Yes"]
)

has_term_insurance = st.selectbox(
    "Do you have Term Life Insurance?",
    ["No", "Yes"]
)

monthly_sip = st.number_input(
    "Monthly Investment / SIP (₹)",
    min_value=0,
    placeholder="Amount you invest monthly"
)

monthly_emi = st.number_input(
    "Total Monthly EMI (₹)",
    min_value=0,
    placeholder="Loan EMI if any"
)

uses_tax_saving = st.selectbox(
    "Do you invest in tax-saving options (80C / NPS)?",
    ["No", "Yes"]
)

started_retirement = st.selectbox(
    "Have you started investing for retirement?",
    ["No", "Yes"]
)

st.divider()

# -------------------------
# SCORING LOGIC
# -------------------------

score = 0
details = []

# 1. Emergency Preparedness (15)
if monthly_expenses > 0 and emergency_savings >= monthly_expenses * 3:
    score += 15
    details.append("✅ Emergency fund is adequate")
else:
    details.append("❌ Emergency fund is insufficient")

# 2. Insurance Coverage (15)
if has_health_insurance == "Yes" and has_term_insurance == "Yes":
    score += 15
    details.append("✅ Insurance coverage is good")
else:
    details.append("❌ Insurance coverage needs improvement")

# 3. Investment Discipline (20)
if monthly_income > 0 and monthly_sip >= monthly_income * 0.2:
    score += 20
    details.append("✅ Strong investment habit")
elif monthly_sip > 0:
    score += 10
    details.append("⚠️ Moderate investment habit")
else:
    details.append("❌ No regular investments")

# 4. Debt Health (15)
if monthly_income > 0 and monthly_emi <= monthly_income * 0.3:
    score += 15
    details.append("✅ Debt level is healthy")
else:
    details.append("❌ Debt burden is high")

# 5. Tax Awareness (15)
if uses_tax_saving == "Yes":
    score += 15
    details.append("✅ Using tax-saving instruments")
else:
    details.append("❌ Not using tax benefits effectively")

# 6. Retirement Readiness (20)
if started_retirement == "Yes":
    score += 20
    details.append("✅ Retirement planning started")
else:
    details.append("❌ Retirement planning not started")

# -------------------------
# RESULTS
# -------------------------

st.header("📊 Your Money Health Result")

st.metric("Money Health Score", f"{score} / 100")

if score >= 80:
    st.success("🌟 Excellent financial health")
elif score >= 60:
    st.info("🙂 Good, but can be improved")
elif score >= 40:
    st.warning("⚠️ Needs attention")
else:
    st.error("🚨 Financial health is weak")

st.divider()

st.subheader("🔍 Detailed Analysis")
for d in details:
    st.write(d)

st.divider()

# -------------------------
# ACTIONABLE SUGGESTIONS
# -------------------------

st.subheader("🛠️ Personalized Suggestions")

if emergency_savings < monthly_expenses * 3:
    st.write("• Build an emergency fund of at least **3 months of expenses**")

if has_health_insurance == "No":
    st.write("• Buy **health insurance** to protect against medical costs")

if has_term_insurance == "No":
    st.write("• Consider **term life insurance** for family protection")

if monthly_income > 0 and monthly_sip < monthly_income * 0.2:
    st.write("• Try investing at least **20% of income** regularly")

if monthly_emi > monthly_income * 0.3 and monthly_income > 0:
    st.write("• Reduce loan burden; keep EMI below **30% of income**")

if uses_tax_saving == "No":
    st.write("• Use **80C / NPS** to save tax and invest smartly")

if started_retirement == "No":
    st.write("• Start retirement investing early for long-term security")

st.divider()

st.caption(
    "⚠️ This is an educational advisory tool, not financial or legal advice."
)
