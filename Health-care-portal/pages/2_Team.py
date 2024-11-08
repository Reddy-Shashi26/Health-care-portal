import streamlit as st


# Set page configuration
st.set_page_config(
    page_title="Team - Healthcare Portal",
    page_icon="🏥",
    layout="wide"
)

# Header
st.markdown("""
    <div style='background-color: #ffffff; padding: 1rem; border-bottom: 2px solid #1e4b7a;'>
        <h1 style='color: #1e4b7a; text-align: center;'>Our Team</h1>
    </div>
""", unsafe_allow_html=True)

# Leadership Team
st.header("Leadership Team")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("Health-care-portal/data/pics/abhishek.png", caption="Rai Abhishek")
    st.subheader("Rai Abhishek")
    st.write("Team Leader")
    st.write("Code Deploying")

with col2:
    st.image("Health-care-portal/data/pics/shashi.jpg", caption="M Shashi Vardhan Reddy")
    st.subheader("M Shashi Vardhan Reddy")
    st.write("Team Member")
    st.write("Web Developer/Code Deployer")

with col3:
    st.image("Health-care-portal/data/pics/Revanth.jpg", caption="Nagidi Revanth")
    st.subheader("Nagidi Revanth")
    st.write("Team Member")
    st.write("Designer")

with col4:
    st.image("Health-care-portal/data/pics/Raki.jpg", caption="G Rakesh")
    st.subheader("G Rakesh")
    st.write("Team Member")
    st.write("Researcher")

# Departments
st.header("Our Skills")
departments = {
    "Python": "For Deploying",
    "AI": "Creating AI Models",
    "Websites": "Creating Dynanics sites",
    "Mobile Apps": "Integrating API",
    "Machine Learning": "Creating Models",
    "Deep Learning": "Creating Models"
}

col1, col2 = st.columns(2)
for i, (dept, desc) in enumerate(departments.items()):
    with col1 if i % 2 == 0 else col2:
        st.subheader(dept)
        st.write(desc)

