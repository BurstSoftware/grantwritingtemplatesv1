import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Federal Business Grant Eligibility Checker", layout="wide")

st.title("Federal Business Grant Eligibility Checker")
st.markdown("""
This tool assesses your eligibility for federal business grants as of April 15, 2025. 
Enter details below to evaluate alignment with common federal criteria (e.g., SBIR/STTR, USDA RBDG).
""")

# Sidebar
st.sidebar.header("Navigation")
sections = ["Location", "Ownership", "Size", "Time", "Industry", "Impact", "Financial", 
            "Legal", "Funds", "Matching", "Results"]
selected_section = st.sidebar.radio("Jump to Section", sections)

# Session state
if "responses" not in st.session_state:
    st.session_state.responses = {}

def save_response(key, value):
    st.session_state.responses[key] = value

# Section 1: Location
if selected_section == "Location":
    st.header("1. Business Location")
    us_located = st.selectbox("Is your business located in the U.S. or its territories?", ["Yes", "No"], key="us_located")
    save_response("us_located", us_located)
    if us_located == "Yes":
        rural = st.selectbox("Is it in a rural area (<50,000 population)?", ["Yes", "No", "Unsure"], key="rural")
        save_response("rural", rural)
        distressed = st.selectbox("Is it in an economically distressed area?", ["Yes", "No", "Unsure"], key="distressed")
        save_response("distressed", distressed)

# Section 2: Ownership
if selected_section == "Ownership":
    st.header("2. Ownership")
    ownership = st.multiselect("Ownership categories (51%+):", 
                              ["Minority-Owned", "Women-Owned", "Veteran-Owned", "Disadvantaged (8(a))", "None"], 
                              key="ownership")
    save_response("ownership", ownership)
    citizenship = st.selectbox("Are principal owners U.S. citizens or permanent residents?", ["Yes", "No"], key="citizenship")
    save_response("citizenship", citizenship)

# Section 3: Size
if selected_section == "Size":
    st.header("3. Business Size")
    employees = st.number_input("FTE employees:", min_value=0, step=1, key="employees")
    save_response("employees", employees)
    revenue = st.number_input("Annual revenue ($):", min_value=0.0, step=1000.0, key="revenue")
    save_response("revenue", revenue)

# Section 4: Time
if selected_section == "Time":
    st.header("4. Time in Operation")
    start_date = st.date_input("Start date:", max_value=datetime(2025, 4, 15), key="start_date")
    years = (datetime(2025, 4, 15) - start_date).days / 365.25
    save_response("years", years)
    st.write(f"Years operational: {years:.1f}")

# Section 5: Industry
if selected_section == "Industry":
    st.header("5. Industry")
    industry = st.selectbox("Primary industry:", 
                            ["Technology/R&D", "Agriculture", "Manufacturing", "Infrastructure", "Energy", "Other"], 
                            key="industry")
    save_response("industry", industry)

# Section 6: Impact
if selected_section == "Impact":
    st.header("6. Economic Impact")
    jobs = st.number_input("Jobs to create:", min_value=0, step=1, key="jobs")
    save_response("jobs", jobs)
    wage = st.number_input("Average wage ($/hour):", min_value=0.0, step=0.5, key="wage")
    save_response("wage", wage)

# Section 7: Financial
if selected_section == "Financial":
    st.header("7. Financial Need")
    need = st.selectbox("Struggled with capital access or hardship?", ["Yes", "No"], key="need")
    save_response("need", need)
    prior = st.number_input("Prior federal funding ($):", min_value=0.0, step=1000.0, key="prior")
    save_response("prior", prior)

# Section 8: Legal
if selected_section == "Legal":
    st.header("8. Legal Status")
    standing = st.selectbox("Registered and compliant (e.g., SAM.gov)?", ["Yes", "No"], key="standing")
    save_response("standing", standing)

# Section 9: Funds
if selected_section == "Funds":
    st.header("9. Use of Funds")
    uses = st.multiselect("Planned uses:", 
                          ["Capital", "R&D", "Operational", "Training"], key="uses")
    save_response("uses", uses)

# Section 10: Matching
if selected_section == "Matching":
    st.header("10. Matching Funds")
    match = st.selectbox("Can you provide matching funds?", ["Yes", "No", "Partial"], key="match")
    save_response("match", match)
    if match in ["Yes", "Partial"]:
        match_amount = st.number_input("Match amount ($):", min_value=0.0, step=1000.0, key="match_amount")
        save_response("match_amount", match_amount)

# Section 11: Results
if selected_section == "Results":
    st.header("Results")
    if st.button("Generate Results"):
        responses = st.session_state.responses
        feedback = []

        if responses.get("us_located") == "Yes":
            feedback.append("✅ U.S.-based; meets basic eligibility.")
            if responses.get("rural") == "Yes":
                feedback.append("✅ Rural location aligns with USDA grants.")
            if responses.get("distressed") == "Yes":
                feedback.append("✅ Distressed area boosts EDA eligibility.")

        ownership = responses.get("ownership", [])
        if "None" not in ownership and ownership:
            feedback.append(f"✅ {', '.join(ownership)} may qualify for SBA or MBDA grants.")
        if responses.get("citizenship") == "Yes":
            feedback.append("✅ Citizenship/residency meets requirements.")

        employees = responses.get("employees", 0)
        if employees < 500:
            feedback.append(f"✅ {employees} employees fits SBA small business size.")

        years = responses.get("years", 0)
        if years >= 1:
            feedback.append(f"✅ {years:.1f} years meets operational minimums.")
        if years < 10:
            feedback.append("✅ Eligible for early-stage grants (e.g., SBIR).")

        industry = responses.get("industry", "")
        if industry != "Other":
            feedback.append(f"✅ {industry} aligns with federal priorities.")

        jobs = responses.get("jobs", 0)
        if jobs >= 1:
            feedback.append(f"✅ {jobs} jobs meets impact thresholds.")

        if responses.get("need") == "Yes":
            feedback.append("✅ Financial need strengthens application.")

        if responses.get("standing") == "Yes":
            feedback.append("✅ Legal compliance confirmed.")

        if responses.get("uses", []):
            feedback.append(f"✅ Uses ({', '.join(responses['uses'])}) are allowable.")

        if responses.get("match") in ["Yes", "Partial"]:
            feedback.append("✅ Matching funds enhance competitiveness.")

        st.subheader("Summary")
        for item in feedback:
            st.write(item)
        st.write("**Next Steps**: Check Grants.gov or agency sites (e.g., SBA, USDA) for specific opportunities.")

st.markdown("---")
st.write("Built by Grok 3 (xAI) | Date: April 15, 2025")
