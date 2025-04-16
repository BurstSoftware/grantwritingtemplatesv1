import streamlit as st
import pandas as pd
from datetime import datetime

# Streamlit app configuration
st.set_page_config(page_title="Minnesota Business Grant Eligibility Checker", layout="wide")

# Header
st.title("Minnesota Business Grant Eligibility Checker")
st.markdown("""
This tool helps you assess potential eligibility for business grants in Minnesota as of April 15, 2025. 
Enter your business details below to see how you align with common grant criteria. Note: This is a general guide—specific grants may vary.
""")

# Sidebar for navigation
st.sidebar.header("Navigation")
sections = ["Business Location", "Ownership", "Business Size", "Time in Operation", "Industry", 
            "Economic Impact", "Financial Need", "Legal Status", "Use of Funds", "Matching Funds", 
            "Results"]
selected_section = st.sidebar.radio("Jump to Section", sections)

# Initialize session state to store user inputs
if "responses" not in st.session_state:
    st.session_state.responses = {}

# Helper function to save responses
def save_response(key, value):
    st.session_state.responses[key] = value

# Section 1: Business Location
if selected_section == "Business Location":
    st.header("1. Business Location")
    located_in_mn = st.selectbox("Is your business physically located in Minnesota?", 
                                 ["Yes", "No"], key="located_in_mn")
    save_response("located_in_mn", located_in_mn)
    
    if located_in_mn == "Yes":
        metro_counties = ["Anoka", "Carver", "Dakota", "Hennepin", "Ramsey", "Scott", "Washington"]
        county = st.text_input("Enter your county (e.g., Hennepin, Olmsted, Cass)", key="county")
        save_response("county", county)
        
        distressed_area = st.selectbox("Is your business in a distressed area (e.g., high poverty, population loss)?", 
                                       ["Yes", "No", "Unsure"], key="distressed_area")
        save_response("distressed_area", distressed_area)

# Section 2: Ownership
if selected_section == "Ownership":
    st.header("2. Ownership")
    ownership_types = st.multiselect("Select applicable ownership categories (51%+ ownership):", 
                                     ["Minority-Owned (BIPOC)", "Women-Owned", "Veteran-Owned", 
                                      "Disability-Owned", "LGBTQ+-Owned", "Immigrant/Refugee-Owned", "None"],
                                     key="ownership_types")
    save_response("ownership_types", ownership_types)
    
    resident = st.selectbox("Is at least one majority owner a Minnesota resident?", 
                            ["Yes", "No"], key="resident")
    save_response("resident", resident)

# Section 3: Business Size
if selected_section == "Business Size":
    st.header("3. Business Size")
    employees = st.number_input("Number of full-time equivalent (FTE) employees (part-time prorated):", 
                                min_value=0, step=1, key="employees")
    save_response("employees", employees)
    
    revenue = st.number_input("Annual gross revenue ($):", min_value=0.0, step=1000.0, key="revenue")
    save_response("revenue", revenue)
    
    legal_structure = st.selectbox("Legal structure:", 
                                   ["Sole Proprietorship", "LLC", "S-Corp", "C-Corp", "Partnership", "Cooperative", "Other"],
                                   key="legal_structure")
    save_response("legal_structure", legal_structure)

# Section 4: Time in Operation
if selected_section == "Time in Operation":
    st.header("4. Time in Operation")
    start_date = st.date_input("Business start date:", value=datetime(2025, 4, 15), 
                               min_value=datetime(1900, 1, 1), max_value=datetime(2025, 4, 15), key="start_date")
    years_operational = (datetime(2025, 4, 15) - start_date).days / 365.25
    save_response("years_operational", years_operational)
    st.write(f"Years operational: {years_operational:.1f}")

# Section 5: Industry
if selected_section == "Industry":
    st.header("5. Industry")
    industry = st.selectbox("Primary industry:", 
                            ["Manufacturing", "Technology", "Agriculture", "Tourism", "Childcare", "Housing", 
                             "Healthcare", "Retail", "Real Estate", "Other"], key="industry")
    save_response("industry", industry)

# Section 6: Economic Impact
if selected_section == "Economic Impact":
    st.header("6. Economic Impact")
    jobs_created = st.number_input("Jobs to be created within 2–3 years:", min_value=0, step=1, key="jobs_created")
    save_response("jobs_created", jobs_created)
    
    wage = st.number_input("Average hourly wage for new jobs ($):", min_value=0.0, step=0.5, key="wage")
    save_response("wage", wage)
    
    community_benefit = st.multiselect("Community benefits (select all that apply):", 
                                       ["Revitalizing distressed area", "Serving underserved populations", 
                                        "Rural economic growth", "Sustainability (e.g., energy efficiency)", "None"],
                                       key="community_benefit")
    save_response("community_benefit", community_benefit)

# Section 7: Financial Need
if selected_section == "Financial Need":
    st.header("7. Financial Need")
    capital_access = st.selectbox("Have you been denied loans or struggled to access capital?", 
                                  ["Yes", "No", "Not Applicable"], key="capital_access")
    save_response("capital_access", capital_access)
    
    hardship = st.selectbox("Has your business faced financial hardship (e.g., revenue loss) in the past year?", 
                            ["Yes", "No"], key="hardship")
    save_response("hardship", hardship)
    
    prior_funding = st.number_input("Total state/federal relief received since 2020 ($):", 
                                    min_value=0.0, step=1000.0, key="prior_funding")
    save_response("prior_funding", prior_funding)

# Section 8: Legal Status
if selected_section == "Legal Status":
    st.header("8. Legal Status")
    good_standing = st.selectbox("Is your business in good standing with the MN Secretary of State and tax authorities?", 
                                 ["Yes", "No"], key="good_standing")
    save_response("good_standing", good_standing)
    
    compliance = st.selectbox("Are you compliant with all relevant regulations (e.g., labor, environmental)?", 
                              ["Yes", "No", "Unsure"], key="compliance")
    save_response("compliance", compliance)

# Section 9: Use of Funds
if selected_section == "Use of Funds":
    st.header("9. Use of Funds")
    use_of_funds = st.multiselect("Planned use of grant funds (select all that apply):", 
                                  ["Capital (e.g., equipment, construction)", "Operational (e.g., payroll, rent)", 
                                   "R&D (e.g., prototyping)", "Training", "Marketing (innovation-related)", "Other"],
                                  key="use_of_funds")
    save_response("use_of_funds", use_of_funds)

# Section 10: Matching Funds
if selected_section == "Matching Funds":
    st.header("10. Matching Funds")
    match_available = st.selectbox("Can you provide matching funds (e.g., cash, loans, in-kind)?", 
                                   ["Yes", "No", "Partial"], key="match_available")
    save_response("match_available", match_available)
    
    if match_available in ["Yes", "Partial"]:
        match_amount = st.number_input("Amount of matching funds available ($):", min_value=0.0, step=1000.0, key="match_amount")
        save_response("match_amount", match_amount)

# Section 11: Results
if selected_section == "Results":
    st.header("Eligibility Assessment Results")
    if st.button("Generate Results"):
        responses = st.session_state.responses
        feedback = []

        # Location Check
        if responses.get("located_in_mn") != "Yes":
            feedback.append("❌ Your business must be located in Minnesota to qualify for most grants.")
        else:
            metro_counties = ["Anoka", "Carver", "Dakota", "Hennepin", "Ramsey", "Scott", "Washington"]
            county = responses.get("county", "").lower()
            if any(c.lower() in county for c in metro_counties):
                feedback.append("✅ Located in the Twin Cities metro; some rural-focused grants may not apply.")
            else:
                feedback.append("✅ Located in Greater Minnesota; eligible for rural-focused grants.")
            if responses.get("distressed_area") == "Yes":
                feedback.append("✅ Distressed area location may boost eligibility for equity-focused grants (e.g., PROMISE Act).")

        # Ownership Check
        ownership = responses.get("ownership_types", [])
        if "None" not in ownership and ownership:
            feedback.append(f"✅ {', '.join(ownership)} status may qualify you for targeted grants (e.g., Emerging Entrepreneur).")
        if responses.get("resident") == "Yes":
            feedback.append("✅ MN resident owner meets residency criteria.")

        # Size Check
        employees = responses.get("employees", 0)
        revenue = responses.get("revenue", 0)
        if employees < 50:
            feedback.append(f"✅ {employees} FTEs qualifies as a small business for most grants.")
        if revenue < 1000000:
            feedback.append(f"✅ ${revenue:,.2f} revenue is below common thresholds (e.g., $1M).")

        # Time in Operation Check
        years = responses.get("years_operational", 0)
        if years >= 2:
            feedback.append(f"✅ {years:.1f} years operational meets minimums for established business grants.")
        elif years < 10:
            feedback.append(f"✅ {years:.1f} years operational aligns with startup/innovation grants.")

        # Industry Check
        industry = responses.get("industry", "")
        priority_industries = ["Manufacturing", "Technology", "Agriculture", "Tourism", "Childcare", "Housing", "Healthcare"]
        if industry in priority_industries:
            feedback.append(f"✅ {industry} is a priority sector for many grants.")

        # Economic Impact Check
        jobs = responses.get("jobs_created", 0)
        wage = responses.get("wage", 0)
        if jobs >= 2:
            feedback.append(f"✅ {jobs} jobs created meets minimums for job-focused grants.")
        if wage >= 20:
            feedback.append(f"✅ ${wage}/hour exceeds typical wage thresholds.")

        # Financial Need Check
        if responses.get("capital_access") == "Yes" or responses.get("hardship") == "Yes":
            feedback.append("✅ Demonstrated financial need may strengthen your application.")
        if responses.get("prior_funding", 0) <= 10000:
            feedback.append("✅ Limited prior funding aligns with some grant restrictions.")

        # Legal Status Check
        if responses.get("good_standing") == "Yes" and responses.get("compliance") in ["Yes", "Unsure"]:
            feedback.append("✅ Legal compliance meets basic eligibility.")

        # Use of Funds Check
        uses = responses.get("use_of_funds", [])
        if uses:
            feedback.append(f"✅ Planned uses ({', '.join(uses)}) align with common allowable expenses.")

        # Matching Funds Check
        if responses.get("match_available") in ["Yes", "Partial"]:
            feedback.append(f"✅ Matching funds availability enhances competitiveness.")

        # Display Results
        st.subheader("Summary")
        if feedback:
            for item in feedback:
                st.write(item)
            st.write("**Next Steps**: Review specific grant guidelines (e.g., MN DEED, Launch Minnesota) to confirm eligibility and apply.")
        else:
            st.write("Please complete all sections to see your results.")

# Footer
st.markdown("---")
st.write("Built with ❤️ by Grok 3 (xAI) | Current Date: April 15, 2025")
