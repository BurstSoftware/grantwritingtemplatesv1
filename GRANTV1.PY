import streamlit as st
import pandas as pd
import base64

# Initialize a dictionary to hold all inputs
all_inputs = {}

# Function to save input data
def save_input_data(section, input_data):
    all_inputs[section] = input_data

# Function to collect inputs into a DataFrame
def collect_inputs():
    df = pd.DataFrame(list(all_inputs.items()), columns=['Section', 'Input'])
    return df

# Helper function to generate a CSV download link
def get_table_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="grant_data.csv">Download CSV File</a>'
    return href

# Streamlit app code where inputs are collected
st.title('Grant Writing Template v1')

# Grant source selection and entity type
grant_options = [
    "Family Foundations",
    "Independent Private Foundations",
    "Federated Funds",
    "Corporate Foundations",
    "Community Foundations",
    "Financial Institutions",
    "Federal Grants",
    "State Grants",
    "Local Grants"
]
selected_grants = st.multiselect("Select grant sources:", grant_options)
save_input_data("Grant Source and Entity Type", ", ".join(selected_grants))

entity_type = st.selectbox("Select your entity type:", ["Non-profit entity", "For-profit entity"])
save_input_data("Entity Type", entity_type)

# Adjusted all st.text_area components to have a consistent height of 100 for uniformity
grant_outline = st.text_area("Grant Outline (topic, outline, sub-header, sub-sub header)", height=100)
save_input_data("Grant Outline", grant_outline)

material_organization = st.text_area("Before you start filling in the outline (organize the material you have available)", height=100)
save_input_data("Material Organization", material_organization)

program_title = st.text_input("Program Title")
save_input_data("Program Title", program_title)

executive_summary = st.text_area("Executive Summary", height=100)
save_input_data("Executive Summary", executive_summary)

organization_description = st.text_area("Description and Background of the Organization", height=100)
save_input_data("Organization Description", organization_description)

program_statement_need = st.text_area("Program Statement and Need for the Program", height=100)
save_input_data("Program Statement Need", program_statement_need)

program_description = st.text_area("Program Description", height=100)
save_input_data("Program Description", program_description)

goals_description = st.text_area("Goals Description", height=100)
save_input_data("Goals Description", goals_description)

program_activities = st.text_area("Program Activities", height=100)
save_input_data("Program Activities", program_activities)

timeline = st.text_area("Timeline", height=100)
save_input_data("Timeline", timeline)

staff = st.text_area("Staff", height=100)
save_input_data("Staff", staff)

evaluation = st.text_area("Evaluation", height=100)
save_input_data("Evaluation", evaluation)

budget = st.text_area("Budget", height=100)
save_input_data("Budget", budget)

budget_narrative = st.text_area("Summary", height=100)
save_input_data("Summary", budget_narrative)

# After collecting all inputs, convert them to a DataFrame
df_inputs = collect_inputs()

# Display the download link
st.markdown(get_table_download_link(df_inputs), unsafe_allow_html=True)
