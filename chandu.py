from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Portfolio data (could be loaded from a file or database)
    personal_info = {
        "name": "YANAMALA CHANDU",
        "title": "Engineering Student | Cloud Technologies | Network Security",
        "contact": {
            "email": "chanduyanamala68@gmail.com",
            "linkedin": "...",
            "phone": "+91...",
            "location": "Hyderabad, Telangana"
        },
        "summary": "Passionate about cloud technologies...",
    }
    education_data = [
        {"institution": "Prakasam...", "degree": "B.Tech", ...},
        {"institution": "Narayana...", "degree": "Intermediate", ...}
    ]
    skills_data = {
        "Cloud Platforms": ["Azure", "AWS"],
        # ...
    }
    projects_data = [
        {"title": "3-Tier NSG", "description": "...", "tech": "..."},
        # ...
    ]
    certifications_data = [
        {"name": "MULTI CLOUD DEVOPS", "issuer": "V-Cube"},
        # ...
    ]

    return render_template(
        "index.html",
        personal=personal_info,
        education=education_data,
        skills=skills_data,
        projects=projects_data,
        certs=certifications_data
    )

if __name__ == "__main__":
    app.run(debug=True)