import streamlit as st
from PIL import Image

# ----- Page Config -----
st.set_page_config(page_title="Chandu | DevOps Engineer", page_icon="🚀", layout="wide")

# ----- Header Section -----
st.title("👨‍💻 Chandu Yanamala")
st.subheader("Fresher DevOps Engineer | Cloud | Automation | Azure | AWS")

st.write("📍 Hyderabad, Telangana")
st.write("📧 chanduyanamala68@gmail.com | 📞 +91 8142331266")
st.write("[🔗 LinkedIn](https://www.linkedin.com/in/chandu-yanamala-3b12a334a/)")

st.markdown("---")

# ----- Summary -----
st.header("📝 Summary")
st.write("""
Passionate and certified in Multi-Cloud DevOps with hands-on experience in Azure, AWS, Git, Docker, Kubernetes, and Terraform.
Skilled in building secure, scalable infrastructures and eager to contribute to a high-performing DevOps team.
""")

# ----- Skills -----
st.header("⚙️ Skills")

cloud_cols = st.columns(2)

with cloud_cols[0]:
    st.subheader("☁️ Cloud Platforms & Services")
    st.markdown("""
    - **Azure**: AD, VMs, Blob, Container Registry, SQL, Networking, Site Recovery  
    - **AWS**: EC2, VPC, IAM, LB, SGs, NACLs, NAT Gateway, EKS, EFS, Lambda  
    """)

with cloud_cols[1]:
    st.subheader("🛠️ DevOps Tools")
    st.markdown("""
    - **Tools**: Git, GitHub, Docker, Terraform, Azure DevOps  
    - **CI/CD**: GitHub Actions, Azure Pipelines  
    - **Security**: Cloud Security, IAM, Secrets Management  
    - **Build Tool**: Maven  
    """)

# ----- Projects -----
st.header("💻 Projects")

st.subheader("🔐 3-Tier Architecture using NSG (Azure)")
st.markdown("""
- Designed a secure 3-tier cloud structure using Azure Network Security Groups (NSGs)
- Managed inbound/outbound rules to secure Web, App, and DB layers
- Improved performance and security by 40%
""")

st.subheader("🛡️ Secure VPC with NAT Gateway (AWS)")
st.markdown("""
- Created VPC with public/private subnets
- Deployed NAT Gateway to allow secure outbound internet for private EC2 instances
- Managed routing and security groups for safe architecture
""")

# ----- Education -----
st.header("🎓 Education")
st.markdown("""
**Bachelor of Technology (ECE)**  
Prakasam Engineering College, Andhra Pradesh  
*08/2020 - 05/2024 | CGPA: 7.0*

**Intermediate**  
Narayana Junior College, Andhra Pradesh  
*08/2018 - 05/2020 | GPA: 8.6*

**High School**  
Samskruti High School, Andhra Pradesh  
*06/2017 - 05/2018 | GPA: 8.8*
""")

# ----- Certification -----
st.header("📜 Certification")
st.write("✅ Multi-Cloud DevOps - VCube Software Solutions")

# ----- Footer -----
st.markdown("---")
st.write("🧠 Let's connect and build something great!")

