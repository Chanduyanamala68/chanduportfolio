import streamlit as st
from PIL import Image

# ----- Page Config -----
st.set_page_config(page_title="Chandu Portfolio", page_icon="🌐", layout="wide")

# ----- Sidebar -----
with st.sidebar:
    image = Image.open("assets/profile.jpg")
    st.image(image, width=200)
    
    st.title("Chandu")
    st.subheader("💼 DevOps & Cloud Enthusiast")

    st.markdown("---")
    st.markdown("📧 Email: chandudevops@example.com")
    st.markdown("🌐 [LinkedIn](https://www.linkedin.com/in/chandu-devops)")
    st.markdown("🐙 [GitHub](https://github.com/chandudevops)")
    st.markdown("📄 [Resume](https://link-to-resume.com)")

# ----- Main Page -----
st.title("👋 Hello, I'm Chandu!")
st.write("Recent graduate and passionate DevOps learner with hands-on experience in Azure, AWS, Docker, Terraform, and Kubernetes. Looking forward to starting my career in cloud and DevOps engineering.")

# ----- Skills -----
st.markdown("## 🚀 Skills")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Cloud Platforms:**")
    st.write("- Azure (VMs, NSG, Blob, ACR)")
    st.write("- AWS (EC2, VPC, S3, IAM)")

    st.markdown("**Infrastructure as Code:**")
    st.write("- Terraform")

    st.markdown("**Version Control:**")
    st.write("- Git & GitHub")

with col2:
    st.markdown("**Containerization:**")
    st.write("- Docker")
    st.write("- Kubernetes (Basics)")

    st.markdown("**CI/CD:**")
    st.write("- GitHub Actions (Basic)")

# ----- Projects -----
st.markdown("## 🧪 Projects")

st.markdown("### 📌 3-Tier Architecture using Azure NSG")
st.write("- Created a secure web-app using Azure NSG to control inbound/outbound traffic between Web, App, and DB tiers.")

st.markdown("### 📌 AWS VPC with NAT Gateway")
st.write("- Built a secure VPC setup with public and private subnets and configured NAT gateway to allow outbound internet from private subnet.")

# ----- Contact -----
st.markdown("## 📬 Contact Me")
contact_form = """
<form action="https://formsubmit.co/YOUR-EMAIL@domain.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required><br><br>
     <input type="email" name="email" placeholder="Your email" required><br><br>
     <textarea name="message" placeholder="Your message here" rows="5" required></textarea><br><br>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
