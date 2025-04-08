# To run: streamlit run chandu_portfolio.py
# Required: pip install streamlit pillow

import streamlit as st
from PIL import Image

# ----- Load Image -----
try:
    image = Image.open("chandu_photo.jpg")
except FileNotFoundError:
    image = Image.new("RGB", (200, 200), color="gray")

# ----- Page Config -----
st.set_page_config(page_title="Chandu's DevOps Portfolio", page_icon="🛠️", layout="wide")

# ----- Custom CSS -----
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
    .link-box {
        background-color: #2a2d36;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.3);
        margin-top: 10px;
        text-align: center;
    }
    .link-box a {
        color: #4fc3f7;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Optional DevOps background banner
try:
    bg_image = Image.open("assets/devops_bg.jpg")
    st.image(bg_image, use_column_width=True)
except FileNotFoundError:
    st.warning("DevOps background image not found. Skipping banner.")


# ----- Header -----
col1, col2 = st.columns([1, 2])
with col1:
    st.image(image, width=200)
with col2:
    st.markdown('<div class="title-box">', unsafe_allow_html=True)
    st.title("Chandu Yaramala")
    st.subheader("Fresher | Azure & AWS Cloud | DevOps Enthusiast")
    st.markdown("""
        <p>📧 Email: chanduyanamala68@gmail.com<br>
        📞 Phone: 8142331266<br>
        💻 GitHub: <a href='https://github.com/Chanduyanamala68' target='_blank'>Chanduyanamala68</a><br>
        🔗 LinkedIn: <a href='https://www.linkedin.com/in/chandu-yanamala-3b12a334a' target='_blank'>Chandu Yaramala</a></p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----- About Me -----
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.header("About Me")
st.write("""
Passionate and highly motivated Cloud & DevOps fresher with hands-on experience in tools like Azure, AWS, Docker, Git, and Terraform.
Looking to contribute and grow in a dynamic cloud environment.
""")
st.markdown('</div>', unsafe_allow_html=True)

# ----- Education -----
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.header("Education")
st.write("""
- 🎓 **Prakasam Engineering College**, AP  
  B.Tech | CGPA: 7.0 (2020 - 2024)

- 🏫 **Narayana Junior College**, AP  
  Intermediate | GPA: 8.6 (2018 - 2020)

- 📚 **Samskruti High School**, AP  
  SSC | GPA: 8.8 (2017 - 2018)
""")
st.markdown('</div>', unsafe_allow_html=True)

# ----- Skills -----
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.header("Skills")
st.write("""
- ☁️ **Cloud**: Azure, AWS (EC2, IAM, VPC, S3, ELB, NAT Gateway)  
- 🛠️ **DevOps Tools**: Git, GitHub, Docker, CI/CD, Terraform  
- 🔐 **Security**: NSG, IAM, Key Vault  
- 📦 **Containers**: Docker, ACR, ECR  
- 🔁 **IaC & Automation**: Terraform Modules, Shell Script  
- 📊 **Monitoring & Storage**: Azure Monitor, Blob, Azure SQL  
""")
st.markdown('</div>', unsafe_allow_html=True)

# ----- Projects -----
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.header("Projects")
st.write("""
1. 🔧 **3-Tier Architecture using NSG (Azure)**  
   Deployed Web-App-DB tiers with secure access control using NSG & routing.

2. 🌐 **Secure AWS VPC with NAT Gateway**  
   Created a secure AWS environment with private/public subnets, EC2, NAT Gateway, route tables.

3. 📦 **CI/CD Pipeline with GitHub Actions**  
   Built a basic CI/CD flow using GitHub Actions to deploy Dockerized app on Azure VM.
""")
st.markdown('</div>', unsafe_allow_html=True)

# ----- Footer -----
st.markdown('<div class="link-box">', unsafe_allow_html=True)
st.markdown("[🌐 GitHub](https://github.com/Chanduyanamala68)", unsafe_allow_html=True)
st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/chandu-yanamala-3b12a334a/)", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.write("Let's connect! Open to cloud, DevOps, and automation opportunities.")
st.markdown("<p style='font-size: small;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
