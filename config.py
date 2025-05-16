# config.py

# Font settings for different sections
FONTS = {
    "main_header": "Poppins",
    "sub_header": "Roboto",
    "body_text": "Inter",
    "code_font": "JetBrains Mono"
}

# Color scheme
COLORS = {
    "primary": "#2196F3",
    "secondary": "#00BCD4",
    "text": "#2c3e50",
    "background": "#f8f9fa",
    "card": "#ffffff",
    "highlight": "#1a73e8"
}

# Personal Information
PERSONAL_INFO = {
    "name": "Prathap Elumalai",
    "title": "AI/ML Engineer",
    "location": "1/112, North St, Kallakurichi",
    "email": "prathapsinghe2003@gmail.com",
    "phone": "+91 9344139449",
    "about": """I am a highly motivated and detail-oriented AI and Machine Learning graduate with a strong foundation in data analytics, predictive modeling, and algorithm development. Passionate about solving real-world challenges through data-driven insights, I thrive in dynamic environments that foster innovation and continuous learning. With hands-on experience in machine learning frameworks, data visualization, and automation, I am eager to contribute my expertise to impactful projects. I aim to bridge the gap between theoretical knowledge and practical applications, driving meaningful AI and data science advancements.""",
    "social_links": {
        "github": "https://github.com/Prathap-Elumalai/Prathap",
        "linkedin": "https://www.linkedin.com/in/prathap-elumalai-8abaa3250"
    }
}

# Educational Background
EDUCATION = {
    "Bachelor of Technology": {
        "degree": "B.Tech in Artificial Intelligence and Machine Learning",
        "institution": "Sri Shakthi Institute of Engineering and Technology",
        "location": "Coimbatore, Tamil Nadu",
        "duration": "Oct 2021 – May 2025",
        "score": "CGPA: 8.00",
        "key_courses": [
            "Machine Learning",
            "Deep Learning",
            "Data Structures",
            "Database Management",
            "Computer Vision"
        ]
    },
    "HSC": {
        "institution": "Model Higher Secondary School",
        "location": "G. Ariyur",
        "duration": "2020 - 2021",
        "score": "74%",
        "stream": "Computer Science"
    },
    "SSLC": {
        "institution": "Model Higher Secondary School",
        "location": "G. Ariyur",
        "duration": "2018 - 2019",
        "score": "68.8%"
    }
}

SKILLS = {
    "Programming Languages": ["Python"],
    "Data Visualization": ["Matplotlib", "Microsoft Power BI"],
    "Machine Learning": ["Linear Regression", "KNN", "K-means", "Random Forest"],
    "Data Analysis": ["Pandas", "NumPy"],
    "Database": ["MySQL"],
    "Tools": ["Git", "Jupyter Notebook", "Google Colab", "VS Code"],
    "Cloud Computing": ["Microsoft Azure services (Basic)"],
    "Data Integration": ["SSIS", "Talend"]
}

INTERMEDIATE_KNOWLEDGE = [
    "Big Data",
    "NLP (Natural Language Processing)",
    "Deep Learning",
    "Generative AI"
]

PROJECTS = [
    {
        "title": "Natural Language Chat with MySQL using Python",
        "description": "Built an innovative model that converts natural language user input into SQL queries, executes them in MySQL, and returns results in a conversational format.",
        "technologies": ["Python", "Natural Language Toolkit (NLTK)", "MySQL"]
    },
    {
        "title": "One-Shot Face Stylization",
        "description": "Implemented an advanced technique for transferring artistic styles from a single reference image onto facial photographs while preserving facial features and identity.",
        "technologies": ["PyTorch", "OpenCV", "Python"]
    },
    {
        "title": "Meat Freshness Analysis using CNN and Deep Learning",
        "description": "Created a CNN to classify meat freshness based on visual features, enhancing food quality assurance.",
        "technologies": ["TensorFlow", "Keras", "Python", "Google Colab"]
    },
    {
        "title": "Credit Card Score Prediction",
        "description": "Developed statistical models to predict an individual's creditworthiness based on financial factors.",
        "technologies": ["Python", "Scikit-learn", "Pandas", "NumPy"]
    },
    {
        "title": "Prime Video Dashboard using Power BI",
        "description": "Designed a Power BI dashboard to visualize real-time metrics and analytics for Prime Video, aiding data-driven decisions.",
        "technologies": ["Power BI", "Python", "Pandas"]
    }
]

EXPERIENCE = {
    "company": "Klodev Company",
    "position": "AI/ML Engineer",
    "location": "Coimbatore",
    "duration": "July 2024 – Present",
    "responsibilities": [
        "Designed and fine-tuned LLM-based agents for address parsing, NL-to-SQL conversion, and search pipelines",
        "Built scalable data workflows using PySpark and Databricks for high-volume ETL and inference tasks",
        "Integrated Playwright, LangChain, and Gemini API to automate user workflows and RAG pipelines"
    ]
}

ACHIEVEMENTS = {
    "achievements": [
        "Improved address segmentation accuracy from 92% to 95% using BERT and Gemini API integration",
        "Implemented RLHF pipeline (DPO) to enhance model reliability and push predictive accuracy to 93%",
        "Reduced SQL errors by 40% and increased query adoption via a Gemini-powered NL-to-SQL interface deployed with Streamlit"
    ]
}
