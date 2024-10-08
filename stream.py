import streamlit as st

# Title of the app
st.title("Message Generator")

# Input form for gathering information
with st.form("email_form"):
    recipient_name = st.text_input("Recipient's Name")
    role_name = st.text_input("Role Name")
    company_name = st.text_input("Company Name")
    job_id = st.text_input("Job ID (optional)")
    
    # Submit button
    submitted = st.form_submit_button("Generate ")

# The email template
if submitted:
    portfolio_link = "https://myweblol.my.canva.site/unnati-singh"
    
    email_template = f"""
    Dear {recipient_name},

    I hope you're doing well. I’m Unnati Singh, a final-year student at IIT Ropar, and I recently came across an opening for {role_name} at {company_name} (Job ID: {job_id if job_id else 'N/A'}). Given my experience as a Community Manager at Saras AI and a Techno-Economic Analyst at Greenshift Energy Pvt. Ltd., along with proficiency in product management, data analysis, Python, SQL, Power BI, Excel, and Canva, I believe I would be a strong fit for the role.

    I’ve attached my resume for reference, and you can also view my portfolio at {portfolio_link}. I’d be grateful if you could consider referring me. Please let me know if you need any further information.

    Thank you for your time and support.

    Best regards,
    Unnati Singh
    """
    
    # Display the generated message
    st.text_area("Generated message", email_template, height=300)
    
    # Button to copy to clipboard
    st.write("Copy the message above and send it!")
