import streamlit as st
from PIL import Image

# Load your profile image safely
try:
    image = Image.open("assets/profile.jpg")
except FileNotFoundError:
    image = Image.open("https://via.placeholder.com/150")  # Placeholder if local image fails

# Set page config
st.set_page_config(page_title="Chandu's Portfolio", page_icon=":briefcase:", layout="wide")

# Custom CSS styles for dark mode and boxes
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .title-box {
        background-color: #1e2128;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        margin-bottom: 20px;
    }
    .section-box {
        background-color: #1c1f26;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(255,255,255,0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Main content layout
col1, col2 = st.columns([1, 2])

with col1:
    st.image(image, width=200)

with col2:
    st.markdown('<div class="title-box">', unsafe_allow_html=True)
    st.title("Chandu Yaramala")
    st.subheader("Fresher | Azure & AWS Cloud | DevOps Enthusiast")
    st.markdown("<p>Email: your_email@example.com | GitHub: github.com/yourprofile</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# About section
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.header("About Me")
st.write("""
I'm a passionate and highly motivated Cloud & DevOps fresher with hands-on experience in tools like Azure, AWS, Docker, Git, and Terraform. Seeking opportunities to contribute and grow in a dynamic cloud environment.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Skills section
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.header("Cloud & DevOps Skills")
st.write("""
- **Cloud Platforms:** Azure, AWS (EC2, IAM, VPC, S3, ELB, NAT Gateway)
- **DevOps Tools:** Git, GitHub, CI/CD, Docker, Terraform
- **Azure Services:** Blob Storage, Virtual Machines, ACR, Azure SQL, Networking, Application Gateway, Site Recovery
- **AWS Services:** EC2, IAM, VPC, Security Groups, NACLs, Load Balancers
- **Security & Recovery:** Azure Security Center, Recovery Vault, Availability Zones
""")
st.markdown('</div>', unsafe_allow_html=True)

# Projects section
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.header("Projects")
st.write("""
1. **Multi-Cloud Deployment using Terraform**  
   Automated infrastructure deployment on both AWS and Azure using Terraform scripts.

2. **CI/CD with GitHub Actions**  
   Built and deployed containerized applications using GitHub Actions and Docker.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.write("Let's connect! Feel free to reach out for collaboration or opportunities.")
st.markdown("<p style='font-size: small;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
