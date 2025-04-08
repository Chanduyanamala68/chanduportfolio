import streamlit as st
from PIL import Image

# ----- Page Config -----
st.set_page_config(page_title="Chandu | DevOps Engineer", page_icon="💼", layout="wide")

# ----- Header -----
st.title("👨‍💻 Chandu Yanamala")
st.subheader("🚀 Aspiring DevOps & Cloud Engineer | Multi-Cloud | Automation Enthusiast")

st.write("📍 Hyderabad, India | 📧 chanduyanamala68@gmail.com | 📞 +91 8142331266")
st.write("[🔗 LinkedIn](https://www.linkedin.com/in/chandu-yanamala-3b12a334a/) | [📄 Download Resume](https://your-resume-link.com)")

st.markdown("---")

# ----- Profile Summary -----
st.header("📝 About Me")
st.write("""
Hello! I'm Chandu, a passionate DevOps enthusiast eager to kickstart my career in cloud engineering.  
I specialize in building and automating scalable cloud infrastructure using Azure, AWS, Docker, and Terraform.  
My strength lies in continuous learning, problem-solving, and collaborating on impactful cloud solutions.
""")

# ----- Highlights -----
st.header("🌟 Highlights")
st.markdown("""
- 🛠️ Hands-on with **multi-cloud platforms**: Azure & AWS  
- ⚙️ Worked on **end-to-end DevOps pipelines** using GitHub Actions & Azure DevOps  
- 🧠 Quick learner, passionate about **automation, scripting, and CI/CD**  
- 👨‍💼 Actively seeking opportunities as **DevOps Engineer | Cloud Engineer | Site Reliability Engineer**
""")

# ----- Skills -----
st.header("🧰 Skills")

col1, col2 = st.columns(2)

with col1:
    st.subheader("☁️ Cloud & Infrastructure")
    st.markdown("""
    - Microsoft Azure: VMs, Blob, ACR, SQL, AD, NSG, App Gateway  
    - AWS: EC2, VPC, IAM, EFS, EKS, Load Balancer, Security Groups, Lambda  
    - Terraform: Infrastructure as Code  
    - Git, GitHub, Azure Repos
    """)

with col2:
    st.subheader("🔧 DevOps & Tools")
    st.markdown("""
    - Docker & Docker Swarm  
    - Kubernetes (Basics)  
    - CI/CD: GitHub Actions, Azure Pipelines  
    - Maven | Jenkins (Basic knowledge)  
    - Monitoring: CloudWatch, Azure Monitor  
    - Scripting: YAML, Shell
    """)

# ----- Projects -----
st.header("🚀 Projects")

st.subheader("🔐 3-Tier Architecture on Azure using NSG")
st.markdown("""
- Designed secure 3-tier structure with NSG for each layer  
- Controlled traffic between Web, App, and DB tiers  
- Improved isolation, performance, and compliance
""")

st.subheader("🌐 AWS VPC with NAT Gateway")
st.markdown("""
- Created VPC with public and private subnets  
- Deployed NAT Gateway for secure internet access to private instances  
- Configured route tables and security groups for best practices
""")

# ----- Achievements -----
st.header("🏆 Achievements")
st.markdown("""
- 🏅 Completed **Multi-Cloud DevOps Certification** from VCube  
- 🧪 Built live projects showcasing real-world DevOps scenarios  
- 👨‍💻 Actively contribute to GitHub & stay updated on DevOps trends
""")

# ----- Testimonials -----
st.header("💬 Testimonials")
st.markdown("""
> *"Chandu shows excellent initiative and eagerness to learn cloud technologies. A quick problem solver."*  
– Instructor, VCube Software Solutions

> *"Impressive dedication towards automation and infrastructure design."*  
– Project Mentor
""")

# ----- Education -----
st.header("🎓 Education")

st.markdown("""
**B.Tech in Electronics & Communication Engineering**  
Prakasam Engineering College – 2024 | CGPA: 7.0

**Intermediate (MPC)**  
Narayana Junior College – 2020 | GPA: 8.6

**SSC**  
Samskruti High School – 2018 | GPA: 8.8
""")

# ----- Resume & Contact -----
st.header("📄 Resume & Contact")
st.markdown("""
- 📄 [Download My Resume](https://your-resume-link.com)  
- 📧 Email: chanduyanamala68@gmail.com  
- 📞 Phone: +91 8142331266  
- 🌐 LinkedIn: [chandu-yanamala](https://www.linkedin.com/in/chandu-yanamala-3b12a334a/)
""")

st.markdown("---")
st.write("🤝 Open to Full-Time/Fresher Roles | Let's collaborate and grow together!")

