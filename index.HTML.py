import streamlit as st
from PIL import Image

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Chandu's Portfolio", page_icon=":wave:", layout="wide")

# ---- HEADER SECTION ----
st.title("Hi, I'm Chandu :wave:")
st.subheader("Azure | AWS | DevOps | Cloud Engineer")
st.write("I’m a passionate Cloud and DevOps enthusiast, ready to contribute and learn in a dynamic IT environment.")

# ---- PROFILE IMAGE ----
# You can replace 'profile.png' with your image file
# image = Image.open("profile.png")
# st.image(image, width=150)

# ---- SOCIAL LINKS ----
st.write("📫 Connect with me:")
st.markdown("""
- [LinkedIn](https://www.linkedin.com/in/chandu-yanamala-73455aa356/)
- [GitHub](https://github.com/your-github)
- [Email](mailto:your.email@example.com)
""")

# ---- SKILLS SECTION ----
st.header("💡 Skills")
st.write("""
- **Cloud:** Microsoft Azure, AWS  
- **DevOps Tools:** Docker, Kubernetes, Git, Terraform, Maven  
- **CI/CD:** GitHub Actions, Azure Pipelines  
- **Other:** Linux, Networking, Active Directory, Virtual Machines
""")

# ---- PROJECTS SECTION ----
st.header("🛠 Projects")
st.write("Here are a few projects I've worked on:")
st.markdown("""
- 🔹 **3-Tier Architecture using NSG** (Azure)
- 🔹 **VPC Architecture using NAT Gateway** (AWS)
- 🔹 **CI/CD Pipeline with GitHub Actions & Terraform**
- 🔹 **Kubernetes Deployment on AWS EKS**
""")

# ---- EDUCATION SECTION ----
st.header("🎓 Education")
st.write("""
- **B.Tech in Electronics and Communication Engineering**  
  Prakasam Engineering College
""")

# ---- FOOTER ----
st.write("---")
st.write("💬 *Feel free to reach out for collaborations, projects or job opportunities!*")
