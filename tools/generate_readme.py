from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "README.md"

PROFILE = {
    "name": "Mohit Sharma",
    "tagline": "Student by degree. Developer by passion. Builder by choice.",
    "github": "https://github.com/mohit-sharma-001",
    "linkedin": "https://www.linkedin.com/in/mohit-sharma-7487b83ab",
    "email": "mohitsharma084400@gmail.com",
    "college": "Uttarakhand Technical University",
    "year": "2nd Year CSE",
    "location": "Dehradun, Uttarakhand, India",
    "status": "Open to Opportunities",
    "quote": "Consistency beats talent when talent doesn't work consistently."
}

ROLES = [
    "Student Developer",
    "Open Source Enthusiast",
    "Project Builder"
]

CURRENT_FOCUS = [
    "Building production-ready software",
    "Open Source Contributions",
    "Full Stack Development",
    "Writing clean and maintainable code"
]

LANGUAGES = [
    "HTML",
    "CSS",
    "JavaScript",
    "Python",
    "Java",
    "C",
    "SQLite"
]

FRAMEWORKS = [
    "React",
    "Next.js",
    "Vite",
    "Flask"
]

TOOLS = [
    "Git",
    "GitHub",
    "VS Code",
    "Render",
    "Netlify",
    "npm",
    "SQLite"
]


def badge(label, color="24292e"):
    return (
        f"https://img.shields.io/badge/"
        f"{label.replace(' ', '%20')}-{color}"
        f"?style=for-the-badge"
    )


def generate():

    md = f"""# Hi, I'm {PROFILE['name']} 👋

> **{PROFILE['tagline']}**

<p align="center">
<img src="assets/portrait_animated.svg" width="260">
</p>

<p align="center">
<img src="assets/terminal.svg" width="820">
</p>

---

## 👨‍💻 About Me

Passionate Computer Science student focused on building real-world software,
contributing to open source, and continuously improving through hands-on
projects.

- 🎓 {PROFILE['college']}
- 📚 {PROFILE['year']}
- 📍 {PROFILE['location']}
- 💼 {PROFILE['status']}

---

## 🚀 Roles

"""

    for role in ROLES:
        md += f"- {role}\n"

    md += "\n---\n\n## 🎯 Current Focus\n\n"

    for item in CURRENT_FOCUS:
        md += f"- {item}\n"

    md += "\n---\n\n## 💻 Languages\n\n"

    for item in LANGUAGES:
        md += f"![{item}]({badge(item)}) "

    md += "\n\n---\n\n## ⚙️ Frameworks\n\n"

    for item in FRAMEWORKS:
        md += f"![{item}]({badge(item)}) "

    md += "\n\n---\n\n## 🛠 Tools\n\n"

    for item in TOOLS:
        md += f"![{item}]({badge(item)}) "

    md += f"""

---

## 🌐 Connect

- GitHub: {PROFILE['github']}
- LinkedIn: {PROFILE['linkedin']}
- Email: {PROFILE['email']}

---

> "{PROFILE['quote']}"

"""

    OUTPUT.write_text(md, encoding="utf-8")

    print("=" * 60)
    print("README Generated")
    print(OUTPUT)
    print("=" * 60)


if __name__ == "__main__":
    generate()