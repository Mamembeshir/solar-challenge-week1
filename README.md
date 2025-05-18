Solar EDA Project
Exploratory Data Analysis (EDA) of Solar Datasets for Regional Comparison

🌍 Project Overview
This repository contains an end-to-end EDA workflow for solar datasets from various countries (e.g., Benin). The focus is on cleaning, analyzing, and visualizing solar irradiance data to enable regional comparison and ranking.

The project includes:

Data preprocessing

Statistical summaries

Time series and correlation visualizations

Outlier handling

Domain-specific insights (e.g., humidity vs. GHI)

All analysis is conducted in Python using Jupyter Notebooks.

👨‍💻 My Contributions
🔧 Project Setup
Initialized the Git repository with a structured layout.

Created data/ and notebooks/ folders.

Configured .gitignore to exclude raw and processed datasets.

🌿 Branching Strategy
Created country-specific branches (e.g., eda-benin) to isolate EDA workflows.

📊 EDA Implementation (benin_eda.ipynb)
Data Cleaning & Summary:

Missing value detection

Outlier detection (Z-scores)

Imputation (medians)

Fixing invalid entries

Time Series Analysis:

Visualized trends for GHI, DNI, DHI, Tamb

Sensor Performance:

Compared ModA and ModB before and after cleaning

Correlation Studies:

Heatmaps and scatter plots

Wind & Distribution Analysis:

Wind rose plots

Histograms

Other Visualizations:

RH vs. GHI bubble chart

Temperature-humidity interaction

Exported Cleaned Data:

Output saved to data/benin_clean.csv (ignored via .gitignore)

📝 Documentation
Detailed Markdown commentary throughout the notebook

Methodology explanations and insights

Referenced documentation (e.g., Pandas, Seaborn)

⚙️ Implementation Details
📚 Tech Stack
Python 3

Jupyter Notebook

pandas, numpy, matplotlib, seaborn, scipy, windrose

📁 Directory Structure
bash
Copy
Edit
solar-eda-project/
├── data/                    # Raw and cleaned datasets (ignored by .gitignore)
│   └── benin-malanville.csv
├── notebooks/               # Jupyter notebooks for EDA
│   └── benin_eda.ipynb
├── .gitignore               # Ignores the data/ folder
└── README.md                # Project documentation
🚀 How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/solar-eda-project.git
Install dependencies:

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn scipy windrose
Prepare the dataset:

Place benin-malanville.csv inside the data/ folder.

Launch the notebook:

bash
Copy
Edit
cd notebooks
jupyter notebook benin_eda.ipynb
Run all cells to execute the EDA workflow.

📌 Key Insights
Successfully handled missing values and outliers in solar irradiance data (e.g., GHI, DNI).

Identified daily and monthly irradiance trends with midday GHI peaks.

Showed significant improvement in sensor data after cleaning.

Found negative correlation between RH and GHI—cloud cover impacts solar output.

🧭 How to Add This to Your Repository
1. Create the Repository on GitHub
Navigate to GitHub → click “+” → New repository

Name it solar-eda-project, set to public, and initialize with a README

2. Clone Locally
bash
Copy
Edit
git clone https://github.com/your-username/solar-eda-project.git
cd solar-eda-project
3. Set Up Structure
bash
Copy
Edit
mkdir data notebooks
Move benin_eda.ipynb → notebooks/

Place benin-malanville.csv → data/ (won’t be committed)

4. Create .gitignore
Add:

kotlin
Copy
Edit
data/
5. Update README
Open README.md in your text editor

Paste this content

Replace your-username with your actual GitHub username

6. Commit & Push
bash
Copy
Edit
git add .
git commit -m "Add EDA notebook and update README"
git push origin main
Or, for a feature branch:

bash
Copy
Edit
git checkout -b eda-benin
git push origin eda-benin
7. Verify on GitHub
Check the structure and README rendering

Ensure data/ is ignored
