import streamlit as st
import base64


class PortfolioData:
    """Contains all portfolio data and configuration"""
    
    def __init__(self):
        self.profile = {
                "name": "Hassan Yasser",
                "title": "Data Analyst & Business Intelligence Specialist",
                "subtitle": "Transforming raw data into business insights",
                "bio": "Data analyst with a background in engineering and a passion for business intelligence. Skilled in SQL, Power BI, Python and data visualization, with hands-on experience in e-commerce, HR analytics and operational dashboards.",
                "experience": [
                    {
                        "title": "From engineering to data analysis",
                        "description": "Leveraged my civil engineering and transportation background to apply statistical models and analytics, developing dashboards and reports to improve decision-making in traffic and operational projects."
                    },
                    {
                        "title": "Building real-world BI solutions",
                        "description": "Created Power BI dashboards for HR data, analyzed e-commerce markets (Amazon, Jumia) and built SQL-driven insights to support strategic decisions."
                    },
                    {
                        "title": "Expanding my expertise",
                        "description": "Learning Streamlit and advanced Python to convert data analyses into interactive apps while deepening my knowledge of machine learning and business intelligence."
                    }
                ],
                "contact": {
                    "email": "yasserhassen98@gmail.com",
                    "linkedin": "https://www.linkedin.com/in/hassan-yasser-2000hh/",
                    "github": "https://github.com/sonh2000",
                    "location": "10th Ramdan city, Egypt"
                }
            }
        
        self.portfolio_categories = {
                "Power BI Dashboards": {
                    "description": "Interactive business intelligence dashboards & KPI tracking",
                    "background": "linear-gradient(135deg, #F7931E 0%, #FFD200 100%)",
                    "icon": "📊"
                },
                "SQL & Database Analysis": {
                    "description": "Querying, reporting, and database optimization",
                    "background": "linear-gradient(135deg, #FF8C00 0%, #FFA500 100%)",
                    "icon": "🗄️"
                },
                "Web Scraping & Data Collection": {
                    "description": "Automated data extraction for market research & competitive analysis",
                    "background": "linear-gradient(135deg, #2E8B57 0%, #90EE90 100%)",
                    "icon": "🕷️"
                },
                "Python / Streamlit Apps": {
                    "description": "Lightweight web apps for data exploration & visualization",
                    "background": "linear-gradient(135deg, #3776AB 0%, #4B8BBE 100%)",
                    "icon": "🐍"
                },
                "ETL & Data Cleaning": {
                    "description": "Data pipeline creation, cleaning, and transformation",
                    "background": "linear-gradient(135deg, #1E90FF 0%, #87CEEB 100%)",
                    "icon": "🔄"
                }
            }

        
        self.projects = [
                {
                    "title": "E-commerce Market Analysis",
                    "category": "Power BI Dashboards",
                    "description": "Compared Amazon and Jumia mobile phone markets using SQL and Power BI, producing dashboards of pricing trends, market share, and KPIs.",
                    "technologies": ["Power BI", "SQL", "Python"],
                    "features": ["Market share KPIs", "Interactive filters", "Competitor benchmarking"],
                    "github_url": "https://github.com/sonh2000/E-commerce-Mobile-Phones-Market-Analysis/tree/main",
                    "demo_url": "",
                    "icon": "📊"
                },
                {
                    "title": "HR Analytics Dashboard",
                    "category": "Power BI Dashboards",
                    "description": "Analyzed employee attrition and performance metrics to support HR decision-making and workforce planning.",
                    "technologies": ["Power BI", "SQL"],
                    "features": ["Attrition trends", "Demographic breakdowns", "Custom visuals"],
                    "github_url": "https://github.com/sonh2000/-HR-Analytics-Employee-Attrition-Dashboard-Power-BI-Project-",
                    "demo_url": "",
                    "icon": "📊"
                },
                {
                    "title": "Chinook SQL Analysis",
                    "category": "SQL & Database Analysis",
                    "description": "SQL-driven analysis of the Chinook music database with sales, artist and customer KPIs, linked to Power BI dashboards.",
                    "technologies": ["SQL", "Power BI"],
                    "features": ["Sales by genre", "Customer lifetime value", "Revenue trends"],
                    "github_url": "https://github.com/sonh2000/chinook_analysis",
                    "demo_url": "",
                    "icon": "🗄️"
                },
                {
                    "title": "Web Scraping Pipeline",
                    "category": "Web Scraping & Data Collection",
                    "description": "Scraped e-commerce product data from multiple sites to compare prices and availability for market research.",
                    "technologies": ["Python", "BeautifulSoup", "Pandas"],
                    "features": ["Automated scraping", "Data cleaning", "Export to Excel/CSV"],
                    "github_url": "",
                    "demo_url": "",
                    "icon": "🕷️"
                },
                {
                    "title": "Streamlit Analytics App",
                    "category": "Python / Streamlit Apps",
                    "description": "Interactive Streamlit web app for exploring datasets and visualizing trends, with basic predictive analytics.",
                    "technologies": ["Python", "Streamlit", "Plotly", "Scikit-learn"],
                    "features": ["Data upload and preprocessing", "Interactive charts", "Basic ML predictions"],
                    "github_url": "",
                    "demo_url": "",
                    "icon": "🐍"
                },
                {
                    "title": "ETL Data Pipeline",
                    "category": "ETL & Data Cleaning",
                    "description": "Automated ETL pipeline to clean and transform multiple data sources for reporting and analysis.",
                    "technologies": ["Python", "Pandas", "SQL"],
                    "features": ["Automated data extraction", "Data transformation workflows", "Validation checks"],
                    "github_url": "",
                    "demo_url": "",
                    "icon": "🔄"
                }
            ]

        
        self.skills = [
                {
                    "category": "Data Analysis & Visualization",
                    "skills": ["SQL (PostgreSQL, MySQL)", "Power BI & DAX", "Excel (Advanced Formulas, Pivot Tables)", "Python (Pandas, NumPy, Matplotlib)"]
                },
                {
                    "category": "Business Intelligence & Reporting",
                    "skills": ["KPI Development", "Dashboard Design", "Data Cleaning & ETL", "Market & HR Analytics"]
                },
                {
                    "category": "Web Scraping & Automation",
                    "skills": ["BeautifulSoup", "Selenium", "Streamlit Apps "]
                }
            ]


class PortfolioRenderer:
    """Handles rendering of portfolio sections"""
    
    def __init__(self, data: PortfolioData):
        self.data = data
    
    def render_hero(self):
        image_path = "https://raw.githubusercontent.com/sonh2000/my-portfolio-app/bb3c2731c8cb5e29eeb5c461421d4a5f279c7631/cv_photo.jpg"
        
        col1, col2 = st.columns([1, 2])
        

        with col1:
             st.image(image_path, width=280)

        with col2:
            st.markdown(f"# {self.data.profile['name']}")
            st.markdown(f"### {self.data.profile['title']}")
            st.markdown(f"*{self.data.profile['subtitle']}*")
            
            st.markdown("---")
            st.markdown("## About Me")
            st.markdown(f"**{self.data.profile['bio']}**")

            
            for exp in self.data.profile['experience']:
                st.markdown(f"### {exp['title']}")
                st.markdown(exp['description'])
                st.markdown("")
    
    def render_portfolio_gallery(self):
        """Render portfolio category gallery"""
        st.markdown("# 💼 Portfolio Categories")
        
        # Count projects by category
        category_counts = {}
        for project in self.data.projects:
            category = project['category']
            category_counts[category] = category_counts.get(category, 0) + 1
        
        # Display categories in grid
        cols_per_row = 2
        categories_list = list(self.data.portfolio_categories.keys())
        
        for i in range(0, len(categories_list), cols_per_row):
            cols = st.columns(cols_per_row)
            
            for j, col in enumerate(cols):
                if i + j < len(categories_list):
                    category = categories_list[i + j]
                    category_info = self.data.portfolio_categories[category]
                    project_count = category_counts.get(category, 0)
                    
                    with col:
                        with st.container():
                            st.markdown(f"""
                            <div style="
                                background: {category_info['background']};
                                border-radius: 15px;
                                padding: 30px;
                                text-align: center;
                                color: white;
                                margin: 10px 0;
                                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                            ">
                                <div style="font-size: 3rem; margin-bottom: 1rem;">{category_info['icon']}</div>
                                <h3 style="margin: 0; font-weight: bold;">{category}</h3>
                                <p style="margin: 10px 0; font-size: 1.2rem;">{project_count} Projects</p>
                                <p style="margin: 0; opacity: 0.9;">{category_info['description']}</p>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            if st.button(f"View {category} Projects", key=f"btn_{category}"):
                                # All categories now go to project details page
                                st.session_state.loading = True
                                st.session_state.current_page = 'project'
                                st.session_state.selected_project = category.lower().replace(" ", "_")
                                st.rerun()
        
        # Show selected category projects
        
    
    def render_category_projects(self, selected_category):
        """Render projects for selected category"""
        st.markdown(f"## {selected_category} Projects")
        
        if st.button("← Back to Categories"):
            del st.session_state.selected_category
            st.rerun()
        
        filtered_projects = [p for p in self.data.projects if p['category'] == selected_category]
        
        if not filtered_projects:
            st.info(f"No projects found in {selected_category} category")
            return
            
        # Display projects in grid
        cols_per_row = 2
        for i in range(0, len(filtered_projects), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, col in enumerate(cols):
                if i + j < len(filtered_projects):
                    project = filtered_projects[i + j]
                    with col:
                        self.create_project_card(project)
    
    def create_project_card(self, project):
        """Create a project card"""
        technologies = " • ".join(project['technologies'])
        features = "\n".join([f"• {feature}" for feature in project['features']])
        
        with st.container():
            st.markdown(f"""
            <div style="
                border: 1px solid #e0e0e0;
                border-radius: 10px;
                padding: 20px;
                margin: 10px 0;
                background-color: white;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <div style="text-align: center; font-size: 4rem; margin-bottom: 1rem;">
                    {project['icon']}
                </div>
                <h3>{project['title']}</h3>
                <p><strong>Category:</strong> {project['category']}</p>
                <p>{project['description']}</p>
                <p><strong>Technologies:</strong> {technologies}</p>
            </div>  
            """, unsafe_allow_html=True)
            
            st.markdown("**Key Features:**")
            st.markdown(features)
            
            if project['github_url'] or project['demo_url']:
                col1, col2 = st.columns(2)
                if project['github_url']:
                    with col1:
                        st.link_button("🔗 GitHub", project['github_url'])
                if project['demo_url']:
                    with col2:
                        st.link_button("🚀 Live Demo", project['demo_url'])
    
    def render_skills(self):
        """Render skills section"""
        st.markdown("# 🛠️ Skills & Expertise")
        
        for skill_category in self.data.skills:
            st.markdown(f"### {skill_category['category']}")
            skills = skill_category['skills']
            cols = st.columns(4)
            # Create skill badges
            skills_html = ""
            for i, skill in enumerate(skills):
                col = cols[i % 4]  # cycle through columns
                with col:
                    st.markdown(f"""
            <div style="
                background-color: #FDD774;
                color: #262730;
                padding: 8px 16px;
                border-radius: 20px;
                margin: 5px;
                font-size: 14px;
                text-align: center;
            ">{skill}</div>
            """, unsafe_allow_html=True)
        
        
    
    def render_contact(self):
        """Render contact section"""
        st.markdown("# 📞 Contact Information")
        
        contact = self.data.profile['contact']
        whatsapp_number = "+201550935742"
        # Contact card
        st.markdown(f"""
        <div style="
            background-color: #FDD774;
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
        ">
            <h3>Let's Connect!</h3>
            <p>📧 <a href="mailto:{contact['email']}">{contact['email']}</a></p>
            <p>💼 <a href="{contact['linkedin']}" target="_blank">LinkedIn Profile</a></p>
            <p>💻 <a href="{contact['github']}" target="_blank">GitHub Profile</a></p>
            <p>📱 <a href="https://wa.me/{whatsapp_number[1:]}" target="_blank">Chat on WhatsApp</a></p>
            <p>📍 {contact['location']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        
    
    def render_project_details(self):
        """Render detailed project page"""
        if st.session_state.loading:
            st.markdown("""
            <div style="text-align: center; padding: 3rem;">
                <div class="loading-spinner"></div>
                <h3>Loading...</h3>
                <p>Please wait while we prepare your content</p>
            </div>
            """, unsafe_allow_html=True)
            # Simulate loading time
            import time
            time.sleep(1.5)
            st.session_state.loading = False
            st.rerun()
        
        project_id = st.session_state.selected_project
        
        # Define projects for each category
        project_data = {
    'power_bi_dashboards': {
        'title': '📊 Power BI Projects',
        'subtitle': 'Interactive Dashboards and Business Intelligence',
        'projects': [
            {
                "title": "E-commerce Mobile Phones Market Analysis",
                "description": "Interactive dashboard comparing mobile phone market trends between Amazon and Jumia using SQL and Power BI.",
                "technologies": ["Power BI", "SQL", "Python"],
                "features": [
                    "Market share KPIs",
                    "Pricing trend analysis",
                    "Competitor benchmarking",
                    "Interactive filters"
                ],
                "status": "Completed",
                "complexity": "Intermediate",
                "github_url": "https://github.com/sonh2000/E-commerce-Mobile-Phones-Market-Analysis"
            },
            {
                "title": "HR Analytics Dashboard",
                "description": "Analyzed employee attrition and HR metrics to support data-driven workforce decisions.",
                "technologies": ["Power BI", "SQL"],
                "features": [
                    "Attrition trend analysis",
                    "Demographics breakdown",
                    "KPI dashboards",
                    "Custom visuals"
                ],
                "status": "Completed",
                "complexity": "Intermediate",
                "github_url": "https://github.com/sonh2000/-HR-Analytics-Employee-Attrition-Dashboard-Power-BI-Project-"
            }
        ]
    },
    'sql_&_database_analysis': {
        'title': '🗄️ SQL & Database Projects',
        'subtitle': 'Querying and Reporting',
        'projects': [
            {
                "title": "Chinook SQL Analysis",
                "description": "SQL-driven analysis of the Chinook database with sales, artist, and customer KPIs linked to Power BI dashboards.",
                "technologies": ["SQL", "Power BI"],
                "features": [
                    "Revenue and sales KPIs",
                    "Customer lifetime value",
                    "Genre and artist trends"
                ],
                "status": "Completed",
                "complexity": "Intermediate",
                "github_url": "https://github.com/sonh2000/chinook_analysis"
            }
        ]
    },
    'web_scraping_&_data_collection': {
        'title': '🕷️ Web Scraping Projects',
        'subtitle': 'Data Collection from Online Sources',
        'projects': [
            {
                "title": "E-commerce Data Scraper",
                "description": "Automated scraping of product data from Jumia and Amazon for market research and pricing comparison.",
                "technologies": ["Python", "BeautifulSoup", "Pandas"],
                "features": [
                    "Multi-site scraping",
                    "Data cleaning",
                    "Export to CSV",
                    "Basic trend analysis"
                ],
                "status": "Completed",
                "complexity": "Intermediate"
            }
        ]
    },
    'python_/streamlit_apps': {
        'title': '🐍 Python / Streamlit Apps',
        'subtitle': 'Lightweight Data Apps and Visualizations',
        'projects': [
            {
                "title": "Streamlit Analytics App",
                "description": "Interactive Streamlit web app for exploring datasets and visualizing trends, with basic predictive analytics.",
                "technologies": ["Python", "Streamlit", "Plotly", "Scikit-learn"],
                "features": [
                    "Data upload and preprocessing",
                    "Interactive charts",
                    "Basic ML predictions"
                ],
                "status": "In Development",
                "complexity": "Intermediate"
            }
        ]
    },
    'etl_&_data_cleaning': {
        'title': '🔄 ETL & Data Cleaning',
        'subtitle': 'Data Pipeline and Transformation',
        'projects': [
            {
                "title": "ETL Data Pipeline",
                "description": "Automated ETL pipeline to clean and transform multiple data sources for reporting and analysis.",
                "technologies": ["Python", "Pandas", "SQL"],
                "features": [
                    "Automated data extraction",
                    "Data transformation workflows",
                    "Validation checks"
                ],
                "status": "Planned",
                "complexity": "Intermediate"
            }
        ]
    }
}
        
        # Get project data for current category
        current_data = project_data.get(project_id, {
            'title': '📁 Projects',
            'subtitle': 'Coming Soon',
            'projects': []
        })
        
        st.markdown(f"# {current_data['title']}")
        st.markdown(f"### {current_data['subtitle']}")
        
        if current_data['projects']:
            # Display projects
            for i, project in enumerate(current_data['projects']):
                st.markdown(f"## {project['title']}")
                
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(project['description'])
                    
                    # Features
                    st.markdown("**Key Features:**")
                    for feature in project['features']:
                        st.markdown(f"• {feature}")
                    
                    # Technologies
                    tech_badges = " ".join([f"`{tech}`" for tech in project['technologies']])
                    st.markdown(f"**Technologies:** {tech_badges}")
                    #giturl
                    if project.get('github_url'):
                        st.markdown(f"[🔗 GitHub Repository]({project['github_url']})")
                    
                with col2:
                    # Status badge
                    status_color = {
                        "Production": "#28a745",
                        "In Development": "#ffc107", 
                        "Completed": "#007bff"
                    }
                    st.markdown(f"""
                    <div style="
                        background: {status_color.get(project['status'], '#6c757d')};
                        color: white;
                        padding: 0.5rem;
                        border-radius: 20px;
                        text-align: center;
                        margin-bottom: 1rem;
                    ">
                        <strong>{project['status']}</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"**Complexity:** {project['complexity']}")
                
                if i < len(current_data['projects']) - 1:
                    st.markdown("---")
        else:
            st.info("Projects for this category are coming soon! Check back later for updates.")
            st.markdown("### Skills Covered")
            st.markdown("This section will showcase projects demonstrating expertise in this area.")

class PortfolioApp:
    """Main portfolio application class"""
    
    def __init__(self):
        self.data = PortfolioData()
        self.renderer = PortfolioRenderer(self.data)
        self.setup_page()
        
        # Initialize session state for page navigation
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 'main'
        if 'selected_project' not in st.session_state:
            st.session_state.selected_project = None
        if 'loading' not in st.session_state:
            st.session_state.loading = False
    
    def setup_page(self):
        """Setup page configuration"""
        st.set_page_config(
            page_title="Data Analyst Portfolio",
            page_icon="📊", 
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Add enhanced styling with section colors and animations
        st.markdown("""
<style>
/* Make a reusable full-width wrapper you can add to any section */
.section-full {
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  width: 100vw;
  box-sizing: border-box;
  padding: 2.5rem 6rem;  /* vertical and horizontal padding inside the wide band */
}

/* Per-section background colors (change hex to whatever you want) */
.home-section {
  background-color: #ffffff;  /* home background */
  color: #222222;
}
.portfolio-section {
  background-color: #fff8f0;  /* portfolio background */
  color: #222222;
}
.skills-section {
  background-color: #f3fbff;  /* skills background */
  color: #222222;
}
.contact-section {
  background-color: #f7fff4;  /* contact background */
  color: #222222;
}

/* A full-width colored separator "band" between sections */
.section-band {
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  width: 100vw;
  height: 18px;                 /* thickness of the band */
  background-color: #ffd400;    /* change to desired color */
}

/* Keep your loading spinner + other styles as before (copy them back) */
.loading-spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin: 20px auto;
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Optional: tweak inner content max width if you want smaller text line-length */
.section-full > .inner {
  max-width: 1200px;
  margin: 0 auto;
}
</style>
""", unsafe_allow_html=True)
    
    def show_loading(self):
        """Show loading animation"""
        st.markdown("""
        <div style="text-align: center; padding: 3rem;">
            <div class="loading-spinner"></div>
            <h3>Loading...</h3>
            <p>Please wait while we prepare your content</p>
        </div>
        """, unsafe_allow_html=True)
        
    def render_navigation(self):
        """Render navigation sidebar"""
        st.sidebar.title("📋 Navigation")
        
        # Show back button if on project page
        if st.session_state.current_page == 'project':
            if st.sidebar.button("← Back to Portfolio", key="back_button"):
                st.session_state.current_page = 'main'
                st.session_state.selected_project = None
                st.rerun()
            st.sidebar.markdown("---")
        
        if st.session_state.current_page == 'main':
            st.sidebar.markdown("Click to scroll to section:")
            
            # Create navigation links
            nav_items = [
                ("🏠 about me", "#aboutme"),
                ("💼 Portfolio", "#portfolio"), 
                ("🛠️ Skills", "#skills"),
                ("📞 Contact", "#contact")
            ]
            
            for label, anchor in nav_items:
                st.sidebar.markdown(f"[{label}]({anchor})")
        else:
            st.sidebar.markdown("### Project Details")
            st.sidebar.info("Viewing project details")
    
    def run(self):
        """Run the portfolio application"""
        st.markdown("""
                        <style>
                        /* change all links in the sidebar */
                        [data-testid="stSidebar"] a {
                            color: white !important;       /* text color */
                            text-decoration: none !important; /* removes underline */
                            font-weight: bold;             /* optional */
                        }

                        /* also change links in the main body if you want */
                        a {
                            color: white    !important;
                            text-decoration: none !important;
                        }
                        a:hover {
                            color: #FF4B4B  !important;     /* color on hover */
                            text-decoration: underline;    /* optional underline on hover */
                        }
                        </style>
                        """, unsafe_allow_html=True)

        self.render_navigation()
        
        # Handle different page states
        if st.session_state.current_page == 'project':
            self.renderer.render_project_details()
        else:
            st.markdown('<div id="home"></div>', unsafe_allow_html=True)
            self.renderer.render_hero()
            st.markdown('<div id="portfolio"></div>', unsafe_allow_html=True)
            self.renderer.render_portfolio_gallery()
            st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
            self.renderer.render_skills()
            st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
            self.renderer.render_contact()
            


if __name__ == "__main__":
    app = PortfolioApp()
    app.run()
    
