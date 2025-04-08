# NOTE: This script requires Streamlit and Pillow to run.
# To install: pip install streamlit pillow

try:
    import streamlit as st
except ModuleNotFoundError:
    print("Streamlit not installed. Run 'pip install streamlit'")
    st = None

try:
    from PIL import Image, ImageDraw
except ModuleNotFoundError:
    print("Pillow not installed. Run 'pip install pillow'")
    Image = None
    ImageDraw = None

if st and Image:
    # Load profile photo
    try:
        image = Image.open("chandu photo.jpg")
    except FileNotFoundError:
        try:
            image = Image.open("assets/default.jpg")
        except FileNotFoundError:
            image = Image.new('RGB', (200, 200), color='gray')
            draw = ImageDraw.Draw(image)
            draw.text((50, 90), "No Image", fill="white")

    st.set_page_config(page_title="DevOps Portfolio | Chandu", page_icon="⚙️", layout="wide")

    # Custom CSS for DevOps feel
    st.markdown("""
        <style>
        body {
            background-color: #0f1117;
            color: white;
        }
        .title-box {
            background-color: #1f232b;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.6);
            margin-bottom: 20px;
        }
        .section-box {
            background-color: #1a1d24;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(255,255,255,0.04);
            margin-bottom: 20px;
        }
        .link-box {
            background-color: #2b2f38;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 3px 6px rgba(0,0,0,0.3);
            margin-top: 10px;
            text-align: center;
        }
        .link-box a {
            color: #00d1ff;
            text-decoration: none;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(image, width=200)

    with col2:    
        st.markdown('<div class="title-box">', unsafe_allow_html=True)
        st.title("⚙️ Chandu Yaramala")
        st.subheader("DevOps Engineer | Azure & AWS | CI/CD | IaC | Containers")

        st.markdown("""
            <p>
            📧 <strong>Email:</strong> chanduyanamala68@gmail.com<br>
            📞 <strong>Phone:</strong> 8142331266<br>
            🐙 <strong>GitHub:</strong> <a href='https://github.com/Chanduyanamala68' target='_blank'>github.com/Chanduyanamala68</a><br>
            🔗 <strong>LinkedIn:</strong> <a href='https://www.linkedin.com/in/chandu-yanamala-73455a356/' target='_blank'>linkedin.com/in/chandu-yanamala</a>
            </p>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # About Me
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("👨‍💻 About Me")
    st.write("""
    I'm a DevOps enthusiast who enjoys automating everything, optimizing infrastructure, and solving real-world deployment problems.
    Skilled in Azure & AWS cloud, CI/CD pipelines, container orchestration, and infrastructure as code.
    Always learning, always building 🚀
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Education
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("🎓 Education")
    st.write("""
    - **Prakasam Engineering College**, AP  
      B.Tech | CGPA: 7.0 (2020 - 2024)

    - **Narayana Junior College**, AP  
      Intermediate | GPA: 8.6 (2018 - 2020)

    - **Samskruti High School**, AP  
      SSC | GPA: 8.8 (2017 - 2018)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Skills
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("🛠️ DevOps Toolset")
    st.write("""
    - ☁️ **Cloud:** Azure, AWS (EC2, IAM, VPC, S3, ELB, NAT Gateway)  
    - 🔧 **Tools:** Git, GitHub, Docker, Terraform, Azure CLI, Bash  
    - 📦 **Containers:** Docker, Azure Container Registry (ACR), AWS ECR  
    - ⚙️ **CI/CD:** GitHub Actions, Azure DevOps  
    - 📄 **IaC:** Terraform Modules, State Management, Variables  
    - 🔐 **Security:** NSG, IAM Roles, Security Groups  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Projects
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("🚀 Projects")
    st.write("""
    1. **3-Tier Azure Architecture with NSG 🔐**  
       Implemented secure 3-tier application architecture using Azure resources like VMs, NSG, and load balancer.

    2. **AWS VPC Design with NAT Gateway 🌐**  
       Created isolated private/public subnets with secure outbound access via NAT, EC2, route tables.

    3. **CI/CD Pipeline with GitHub Actions ⚙️**  
       Built automated deployment pipeline to Dockerize and push updates to cloud environment.

    4. **Terraform IaC for Azure Infrastructure 📄**  
       Provisioned complete infrastructure using reusable modules for VM, Storage, and Networking.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Links
    st.markdown('<div class="link-box">', unsafe_allow_html=True)
    st.markdown("🐙 [GitHub](https://github.com/Chanduyanamala68)", unsafe_allow_html=True)
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/chandu-yanamala-73455a356/)", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.write("📬 Let's collaborate! I'm open to DevOps internships or junior engineer opportunities.")
    st.markdown("<p style='font-size: small;'>🛠️ Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    print("Required modules are missing. Please run: pip install streamlit pillow")
