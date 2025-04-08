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
        image = Image.open("chandu photo.jpg")  # Make sure this is in the same folder
    except FileNotFoundError:
        try:
            image = Image.open("assets/default.jpg")
        except FileNotFoundError:
            image = Image.new('RGB', (200, 200), color='gray')
            draw = ImageDraw.Draw(image)
            draw.text((50, 90), "No Image", fill="white")

    st.set_page_config(page_title="Chandu's Portfolio", page_icon="💼", layout="wide")

    # CSS for dark theme
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

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(image, width=200)

    with col2:    
        st.markdown('<div class="title-box">', unsafe_allow_html=True)
        st.title("👨‍💻 Chandu Yaramala")
        st.subheader("🎓 Fresher | ☁️ Azure & AWS Cloud | 🚀 DevOps Enthusiast")

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
    st.header("🙋‍♂️ About Me")
    st.write("""
    Passionate and highly motivated Cloud & DevOps fresher 🌟 with hands-on experience in tools like Azure, AWS, Docker, Git, and Terraform.
    Looking to contribute and grow 🌱 in a dynamic cloud environment ☁️.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Education
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("🎓 Education")
    st.write("""
    - 📘 **Prakasam Engineering College**, AP  
      B.Tech | CGPA: 7.0 (2020 - 2024)

    - 📗 **Narayana Junior College**, AP  
      Intermediate | GPA: 8.6 (2018 - 2020)

    - 📕 **Samskruti High School**, AP  
      SSC | GPA: 8.8 (2017 - 2018)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Skills
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("🛠️ Cloud & DevOps Skills")
    st.write("""
    - ☁️ **Cloud:** Azure, AWS (EC2, IAM, VPC, S3, ELB, NAT Gateway)  
    - 🔧 **DevOps Tools:** Git, GitHub, Docker, CI/CD, Terraform  
    - 🧠 **Azure Services:** Blob Storage, VM, ACR, Azure SQL, App Gateway  
    - 🛡️ **AWS Services:** EC2, VPC, IAM, Security Groups  
    - ⚙️ **IaC & Automation:** Terraform Modules, Shell Script  
    - 📦 **Containers:** Docker, ACR, ECR
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Projects
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("📁 Projects")
    st.write("""
    1. 🧱 **3-Tier Architecture using NSG**  
       Built secure 3-tier architecture in Azure (Web, App, DB) with traffic filtering. 🔐

    2. 🌐 **Secure VPC Architecture using NAT Gateway**  
       Deployed secure infrastructure using AWS VPC, NAT Gateway, route tables, EC2. 🛡️
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Links
    st.markdown('<div class="link-box">', unsafe_allow_html=True)
    st.markdown("🔗 [🌐 GitHub](https://github.com/Chanduyanamala68)", unsafe_allow_html=True)
    st.markdown("🔗 [🔗 LinkedIn](https://www.linkedin.com/in/chandu-yanamala-73455a356/)", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.write("📞 Let's connect! Feel free to reach out for collaboration or opportunities.")
    st.markdown("<p style='font-size: small;'>✨ Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    print("Required modules are missing. Please run: pip install streamlit pillow")
