

OVERVIEW

The Patient Risk Assessment Dashboard is a healthcare data analytics project built using Python, Streamlit, and Plotly Express. It enables doctors, data analysts, and healthcare professionals to visualize and interpret patient data efficiently.

The dashboard processes raw patient information — including age, gender, blood pressure, cholesterol levels, diagnosis, city, risk status, and follow-up needs into interactive visual insights that help identify high-risk groups and trends.


TECH STACK

	•	Python — Core language
	•	l Pandas — Data cleaning and manipulation
	•	Plotly Express — Data visualization
	•	 Streamlit — Dashboard UI framework


 KEY FEATURES

Interactive Filters: Filter data by City and Diagnosis for dynamic insights

Real-time Dataframe View: 
Instantly view and analyze filtered patient data

Key Health Metrics:
	•	Total patient count
	•	Average blood pressure (mm Hg)
	•	Average cholesterol (mg/dL)

Visualizations:
	•	Bar Chart: Average BP per city
	•	Pie Chart: Patient distribution by diagnosis
	•	Box Plot: BP variation across diagnosis categories
	•	Scatter Plot: Cholesterol variation with age
	•	Line Chart: BP trend with age

Top 5 Healthy Individuals: 
Displays the healthiest patients based on key metrics

Download Option: Export filtered data as a CSV file


BENEFITS

	•	Helps health professionals identify trends in patient health across demographics
	•	Enables risk analysis through cholesterol and BP pattern visualization
	•	Simplifies data driven healthcare decision-making
	•	Makes data exploration accessible without coding knowledge
	•	Fully customizable and extendable for other datasets


HOW TO RUN

(In bash)
pip install streamlit plotly pandas
python -m streamlit run Health_data.py


CONTRIBUTIONS:

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.


DATA SOURCE: 

This project uses a self-created health dataset, simulating real-world patient data.
Both the raw (health_data.csv) and cleaned (Health_data_new.csv) versions of the dataset are included in this repository for full transparency and reproducibility.
