import streamlit as st
from io import StringIO

# Initialize session state variables if not already done
if 'resume' not in st.session_state:
    st.session_state.resume = None
if 'job_description' not in st.session_state:
    st.session_state.job_description = ""
if 'page' not in st.session_state:
    st.session_state.page = "Home"

def upload_resume():
    st.sidebar.subheader("Upload Resume")
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf", "docx", "txt"])
    if uploaded_file is not None:
        st.session_state.resume = uploaded_file
        st.sidebar.text("Resume uploaded successfully.")

def upload_job_description():
    st.sidebar.subheader("Upload Job Description")
    job_desc = st.sidebar.text_area("Job Description", value=st.session_state.job_description, height=150, key="job_desc_area")
    st.session_state.job_description = job_desc

def Home_page():
    st.title("Welcome to Resume Analysis & Tailoring App")
    st.write("""
        This application helps you to analyze and tailor your resume for specific job descriptions.
        Follow these steps to get started:
        1. **Upload your resume**: Use the sidebar to upload your resume file. Supported formats are PDF, DOCX, and TXT.
        2. **Enter the job description**: Input the job description in the sidebar. This will be used to tailor your resume.
        3. **Navigate through the pages**: Use the buttons to move between pages and perform various actions like viewing parsed resume, evaluating matching with the job, and tailoring your resume.
    """)
    st.image("https://via.placeholder.com/700x300.png?text=Resume+Analysis+%26+Tailoring+App", use_column_width=True)

    cols = st.columns([2, 7, 1])
    with cols[0]:
        if st.button("Get Started"):
            st.session_state.page = "View Parsed Result"
    with cols[2]:
        if st.button("Help"):
            st.session_state.page = "Help"

def view_parsed_result():
    st.header("View Parsed Result")
    if st.session_state.resume:
        st.write(f"Resume file: {st.session_state.resume.name}")
        if st.session_state.resume.type == "text/plain":
            resume_text = st.session_state.resume.getvalue().decode("utf-8")
            st.text_area("Parsed Resume Content", resume_text, height=300, key="parsed_resume_content")
    else:
        st.warning("Please upload a resume file in the sidebar.")
    cols = st.columns([2, 7, 1])
    # with cols[0]:
    #     if st.button("Home"):
    #         st.session_state.page = "Home"
    with cols[2]:
        if st.button("Next"):
            st.session_state.page = "Evaluate Matching with a Job"

def evaluate_matching():
    st.header("Evaluate Matching with a Job")
    if st.session_state.resume and st.session_state.job_description:
        st.write("Job Description:")
        st.text_area("Job Description", st.session_state.job_description, height=150, key="eval_job_desc_area")
        st.write("Resume Matching Analysis would be displayed here.")
    else:
        st.warning("Please upload both resume and job description.")
    cols = st.columns([2, 7, 1])
    with cols[0]:
        if st.button("Previous"):
            st.session_state.page = "View Parsed Result"
    with cols[2]:
        if st.button("Next"):
            st.session_state.page = "Tailor Resume"

def tailor_resume():
    st.header("Tailor Resume")
    if st.session_state.resume:
        st.write("Resume:")
        if st.session_state.resume.type == "text/plain":
            resume_text = st.session_state.resume.getvalue().decode("utf-8")
            st.text_area("Resume Content", resume_text, height=300, key="tailor_resume_content")
        st.write("Customize your resume for the job description.")
    else:
        st.warning("Please upload a resume file in the sidebar.")
    cols = st.columns([2, 7, 1])
    with cols[0]:
        if st.button("Previous"):
            st.session_state.page = "Evaluate Matching with a Job"
    # with cols[2]:
    #     if st.button("Next"):
    #         st.session_state.page = "Help"

def help_page():
    st.header("Help")
    st.write("""
        This application helps you to analyze and tailor your resume for specific job descriptions. 
        Follow these steps:
        1. Upload your resume in the sidebar.
        2. Enter the job description in the sidebar.
        3. Navigate through the pages to view the parsed resume, evaluate the match with the job, and tailor your resume.
    """)
    st.subheader("Frequently Asked Questions (FAQs)")
    st.write("""
        **1. What file formats are supported for resume upload?**
        - The application supports PDF, DOCX, and TXT formats.

        **2. How do I input the job description?**
        - Use the text area in the sidebar to input the job description.

        **3. Can I navigate back to previous pages?**
        - Yes, each page has "Previous" and "Next" buttons to navigate between pages.

        **4. How is the resume parsed and analyzed?**
        - The application parses the uploaded resume and displays the content. It also evaluates the matching between the resume and the job description.

        **5. How can I tailor my resume to the job description?**
        - Use the "Tailor Resume" page to customize your resume content based on the job description.
    """)
    # cols = st.columns([2, 7, 1])
    # with cols[0]:
    #     if st.button("Previous"):
    #         st.session_state.page = "Tailor Resume"
    # with cols[2]:
    #     if st.button("Home"):
    #         st.session_state.page = "Home"

def main():
    # Set page config
    st.set_page_config(
        page_title="Resume Analysis & Tailoring",
        page_icon=":clipboard:"  # You can use emoji shortcodes for icons
    )

    st.sidebar.title("Resume Analysis & Tailoring")
    pages = {
        "Home": Home_page,
        "View Parsed Result": view_parsed_result,
        "Evaluate Matching with a Job": evaluate_matching,
        "Tailor Resume": tailor_resume,
        "Help": help_page
    }

    upload_resume()
    upload_job_description()
    
    # Sidebar for page navigation
    page = st.sidebar.radio("Go to", options=list(pages.keys()), index=list(pages.keys()).index(st.session_state.page))
    st.session_state.page = page
    
    # Render the selected page
    pages[st.session_state.page]()

if __name__ == "__main__":
    main()
