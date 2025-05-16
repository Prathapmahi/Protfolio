import streamlit as st
from config import *

# Page config
st.set_page_config(
    page_title=f"{PERSONAL_INFO['name']} - Portfolio",
    page_icon="📊",
    layout="wide"
)

# Custom CSS with enhanced fonts and navigation button styles
st.markdown(f"""
<style>
    html, body, [class*="css"]  {{
        font-family: '{FONTS['body_text']}', sans-serif;
        font-size: 18px;
    }}
    .main-header {{
        font-family: '{FONTS['main_header']}';
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(120deg, #2196F3, #00BCD4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .sub-header {{
        font-family: '{FONTS['sub_header']}';
        font-size: 2.2rem;
        font-weight: 600;
        margin-top: 2rem;
        color: #2c3e50;
        border-bottom: 3px solid #2196F3;
        padding-bottom: 0.5rem;
        width: fit-content;
    }}
    .project-card {{
        background: white;
        padding: 1.8rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
    }}
    .project-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    }}
    .skill-tag {{
        background: #2196F3;
        color: white;
        padding: 0.6rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        display: inline-block;
    }}
    button[kind="secondary"] {{
        background-color: #ffffff !important;
        border: 2px solid #2196F3 !important;
        color: #2196F3 !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 0.6rem 1.5rem !important;
    }}
    button[kind="secondary"]:hover {{
        background-color: #2196F3 !important;
        color: #fff !important;
    }}
</style>
""", unsafe_allow_html=True)

# Section Renderers
def home():
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(f"""
            <div class="main-header">Hi, I'm {PERSONAL_INFO['name']}</div>
            <h3 style='color:#1a1a1a'>{PERSONAL_INFO['title']}</h3>
            <p style='line-height: 1.6'>{PERSONAL_INFO['about']}</p>
        """, unsafe_allow_html=True)
    with col2:
        st.image("prathap_photo.jpg", use_container_width=True)

def experience():
    st.markdown("<div class='sub-header'>Work Experience</div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='project-card'>
        <h4>{EXPERIENCE['position']} at {EXPERIENCE['company']} ({EXPERIENCE['duration']})</h4>
        <p><strong>Location:</strong> {EXPERIENCE['location']}</p>
        <ul>
            {''.join([f"<li>{item}</li>" for item in EXPERIENCE['responsibilities']])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

def achievements():
    st.markdown("<div class='sub-header'>Achievements</div>", unsafe_allow_html=True)
    for achievement in ACHIEVEMENTS['achievements']:
        st.markdown(f"<div class='project-card'>{achievement}</div>", unsafe_allow_html=True)

def education():
    st.markdown("<div class='sub-header'>Education</div>", unsafe_allow_html=True)
    for level, details in EDUCATION.items():
        st.markdown(f"""
        <div class='project-card'>
            <h4>{level}</h4>
            <p>{details['degree'] if 'degree' in details else ''}</p>
            <p>{details['institution']} ({details['duration']})</p>
            <p><strong>Score:</strong> {details['score']}</p>
        </div>
        """, unsafe_allow_html=True)

def skills():
    st.markdown("<div class='sub-header'>Skills</div>", unsafe_allow_html=True)
    for category, skill_list in SKILLS.items():
        st.markdown(f"### {category}")
        st.markdown(" ".join([f"<span class='skill-tag'>{skill}</span>" for skill in skill_list]), unsafe_allow_html=True)
    st.markdown("### Intermediate Knowledge")
    st.markdown(" ".join([f"<span class='skill-tag'>{skill}</span>" for skill in INTERMEDIATE_KNOWLEDGE]), unsafe_allow_html=True)

def projects():
    st.markdown("<div class='sub-header'>Projects</div>", unsafe_allow_html=True)
    for project in PROJECTS:
        st.markdown(f"""
        <div class='project-card'>
            <h4>{project['title']}</h4>
            <p>{project['description']}</p>
            <p><strong>Technologies:</strong> {', '.join(project['technologies'])}</p>
        </div>
        """, unsafe_allow_html=True)

def nav():
    sections = ["Home", "Experience", "Achievements", "Education", "Skills", "Projects"]
    cols = st.columns(len(sections))
    clicked = None
    for i, section in enumerate(sections):
        if cols[i].button(section):
            clicked = section
    return clicked or "Home"

def main():
    st.markdown("<div style='margin-top: -2rem;'>", unsafe_allow_html=True)
    section = nav()
    st.markdown("</div>", unsafe_allow_html=True)

    if section == "Home":
        home()
    elif section == "Experience":
        experience()
    elif section == "Achievements":
        achievements()
    elif section == "Education":
        education()
    elif section == "Skills":
        skills()
    elif section == "Projects":
        projects()

if __name__ == '__main__':
    main()
