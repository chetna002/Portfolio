import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# --- Page config (set before anything else) ---
st.set_page_config(page_title="Chetna Saini", page_icon="💼", layout="wide")

# --- Custom Background CSS ---
st.markdown("""
<style>
.stApp {
    background: #ffecd2; /* soft gradient */
    color: #333333;
}
/* Headings color fix */
h1, h2, h3, h4, h5, h6 {
    color: #333333 !important;
}
p, li {
    color: #333333;
/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: #fcb69f; /* light cream for sidebar */
    width: 320px !important;   /* increase sidebar width */
}


}

}
/* Card styling for About section */
.card {
    background-color: rgba(255,255,255,0.8);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    margin: 20px 10px;
}
</style>
""", unsafe_allow_html=True)

# --- Function to make circular image ---
def make_circle_image(img):
    img = img.convert("RGBA")
    size = img.size
    mask = Image.new('L', size, 0)
    draw = Image.new('L', size, 255)
    mask.paste(draw, (0, 0))
    output = Image.new('RGBA', size, (0, 0, 0, 0))
    output.paste(img, (0, 0), mask)
    return output

# --- Function to convert PIL image to base64 ---
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# --- Load and prepare image ---
image = Image.open("image.jpeg")
circular_image = make_circle_image(image)
image_base64 = image_to_base64(circular_image)

# --- Sidebar navigation ---
menu = ["About", "Skills", "Projects", "Certificates", "Education", "Contact"]
choice = st.sidebar.selectbox("📂 Explore", menu)

# --- Social icons ---
linkedin_icon = "https://cdn-icons-png.flaticon.com/512/174/174857.png"
github_icon = "https://cdn-icons-png.flaticon.com/512/733/733553.png"
email_icon = "https://cdn-icons-png.flaticon.com/512/561/561127.png"

# ===== About Section =====
# ===== About Section =====
if choice == "About":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2], vertical_alignment="center")

    # --- Profile Image ---
    with col1:
        st.markdown(
            f'<img src="data:image/png;base64,{image_base64}" width="300" '
            'style="border-radius:50%; box-shadow:0px 4px 15px rgba(0,0,0,0.2);">',
            unsafe_allow_html=True
        )

    # --- Name & Subtitle ---
    with col2:
        # Stylish Gradient Name
        st.markdown("""
<h1 style='
    font-size:55px;
    font-weight:bold;
    color:#ff7e5f; /* <-- Change color here */
    font-family: "Georgia", serif;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
'>
    Chetna Saini
</h1>
""", unsafe_allow_html=True)


        # Custom Subtitle
        st.markdown("""
        <p style='
            font-size:26px;
            color:#444444;
            font-family: "Trebuchet MS", sans-serif;
            margin-top:-10px;
        '>
            Data Scientist | Data Analyst | Machine Learning Enthusiast
        </p>
        """, unsafe_allow_html=True)

        # About Me Text
        st.markdown("""
<p style='
    font-size:18px;  /* Increase this for bigger text */
    color:#333333;
    line-height:1.6;
    font-family: "Trebuchet MS", sans-serif;
'>
    I love exploring the stories hidden in data and turning them into solutions that matter.
    Whether it’s building a machine learning model, uncovering trends through analysis, or
    crafting visuals that make insights click, I enjoy bridging the gap between raw numbers
    and real-world impact. My work blends curiosity, analytical thinking, and a passion for
    continuous learning in the evolving world of data science.
</p>
""", unsafe_allow_html=True)
        # Social Icons
        st.markdown(
            f"""<a href="https://www.linkedin.com/in/chetna-saini" target="_blank">
                    <img src="{linkedin_icon}" width="45" style="margin-right:10px;"></a>
                 <a href="https://github.com/chetna002" target="_blank">
                    <img src="{github_icon}" width="45" style="margin-right:10px;"></a>
                 <a href="mailto:chetnasaini002@gmail.com">
                    <img src="{email_icon}" width="45"></a>""",
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)


# ===== Skills Section =====
elif choice == "Skills":
    st.markdown("""
    <h1 style='font-size:36px; font-weight:bold; color:#333333;'>
        💡 Skills
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size:20px; line-height:1.8; color:#333333;'>
    <b>Programming:</b> Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, TensorFlow, NLTK), SQL<br>
    <b>Tools:</b> Tableau, Power BI, Excel, Jupyter Notebook, GitHub, Streamlit<br>
    <b>Machine Learning:</b> NLP, Predictive Modeling, Classification, Regression, Time Series Analysis<br>
    <b>Soft Skills:</b> Problem-solving, Communication, Teamwork
    </p>
    """, unsafe_allow_html=True)

# ===== Projects Section =====
elif choice == "Projects":
    st.markdown("<h1 style='font-size:36px;'>📂 Projects</h1>", unsafe_allow_html=True)

    projects = [
        {
            
        "title": "Intelligent Spam Ham Detector System",
        "desc": "Built an NLP-powered email classification system to detect spam and ham messages using deep learning models.",
        "link":"https://intelligentspamham-detector-system-c36fxk8ajousbjsjyjqrhr.streamlit.app/"
    },
        {
            "title": "Road Accidents Analysis",
            "desc": "Analyzed road accident data to uncover trends, high-risk locations, and key contributing factors using data visualization.",
            "link": "https://github.com/chetna002/Road-Accident"
        },
        {
            "title": "Movie Recommendation System",
        "desc": "Developed a recommendation engine that suggests movies based on user preferences using collaborative filtering techniques.",
        "link": "https://movie-recommendation-system-ggagluh2fnkgqdawihfgxl.streamlit.app/"
        },
        {
            "title": "HR Analytics Dashboard",
            "desc": "Created an interactive dashboard to visualize HR data, track key metrics, and identify employee attrition trends.",
            "link": "https://github.com/chetna002/HR-Analytics-Dashboard"
        },
        {
            "title": "NEET 2024 Spam Analysis",
            "desc": "Analyzed online communications related to NEET 2024 to detect spam content using Natural Language Processing, text preprocessing, and classification models.",
            "link": "https://github.com/chetna002/NEET-2024-Spam-Analysis"
        },
        {
            "title": "Climate Change Modeling",
            "desc": "Performed sentiment analysis on NASA climate dataset by cleaning and preprocessing text data, applying sentiment intensity analysis, and training a TF-IDF-based machine learning model to classify sentiment trends in climate-related discussions.",
            "link": "https://github.com/chetna002/Climate-Change-Modeling"
        },
        {
            "title": "iPhone Review Using NLP",
            "desc": "Analyzed iPhone customer reviews using Natural Language Processing to extract insights, determine sentiment polarity, and identify key factors influencing user satisfaction.",
            "link": "https://github.com/chetna002/IPhone-Review-Using-NLP"
        },
        {
            "title": "Face-Mask Detection using CNN",
            "desc": "Built a CNN-based deep learning model to detect face mask compliance in real time using image processing and computer vision techniques.",
            "link": "https://github.com/chetna002/Face-Mask-Detection-Using-CNN"
        },
        {
            "title": "Uber Data Analysis",
            "desc": "Performed exploratory data analysis on Uber trip data to identify ride patterns, peak demand hours, and key factors affecting trip frequency and duration.",
            "link": "https://github.com/chetna002/Uber-Data-Analysis"
        },
        {
            "title": "Tele-customer-Churn-Analysis",
            "desc": "Conducted data analysis on telecom customer records to identify churn patterns, uncover key factors influencing customer retention, and build predictive models to reduce attrition.",
            "link": "https://github.com/chetna002/-Telco-Customer-Churn-Analysis"
        }
        
    ]

    for i, project in enumerate(projects, start=1):
        st.markdown(
            f"<p style='font-size:18px;'><b>{i}. <a href='{project['link']}' target='_blank' "
            f"style='color:#ff5733; text-decoration:none;'>{project['title']}</a></b> — {project['desc']}</p>",
            unsafe_allow_html=True
        )



# ===== Certificates Section =====
elif choice == "Certificates":
    st.markdown("""
    <h2 style='font-size:32px; font-weight:bold; color:#4b0082;'>
        📜 Certificates
    </h2>
    <ul style='font-size:20px;'>
        <li> Data Scientist and Artificial Intelligence  – Eagletfly Solutions</li>
        <li>AI Tools & ChatGPT Workshop – Be10x</li>
    </ul>
    """, unsafe_allow_html=True)

    #st.write("- **Advanced SQL for Data Analysis** – DataCamp")
    #st.write("- **Tableau Desktop Specialist** – Tableau")

# ===== Education Section =====
elif choice == "Education":
    st.markdown("""
    <h2 style='font-size:32px; font-weight:bold; color:#4b0082;'>
        🎓 Education
    </h2>
    <ul style='font-size:20px;'>
        <li>Bachelor’s Of Computer Application – Maharaja Agrasen Himalayan Garhwal University (2021-2024)</li>
        <li>  Arts – South Point Public School (2019-2020)</li>
    </ul>
    """, unsafe_allow_html=True)


# ===== Contact Section =====
elif choice == "Contact":
    st.markdown("""
    <h2 style='font-size:35px; font-weight:bold; color:#4b0082;'>
        📞 Contact Me
    </h2>
    <p style='font-size:30px;'>
        📧 Email: chetnasaini002@gmail.com
    </p>
    <p style='font-size:30px; '>
        📱 Phone: +91-7206832013
    </p>
    <p style='font-size:30px; '>
        🔗 <a href='https://www.linkedin.com/in/chetna-saini' target='_blank'>LinkedIn</a>
    </p>
    <p style='font-size:30px; '>
        💻 <a href='https://github.com/chetna002' target='_blank'>GitHub</a>
    </p>
    """, unsafe_allow_html=True)

