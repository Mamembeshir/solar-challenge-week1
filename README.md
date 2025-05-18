☀️ Solar EDA Project
Exploratory Data Analysis (EDA) of Solar Datasets for Regional Comparison

🌍 Overview
This project analyzes solar irradiance data from various countries (e.g., Benin) to uncover trends, clean inconsistencies, and prepare data for regional comparisons. Conducted using Python and Jupyter Notebooks.

Features:

Data cleaning & outlier handling

Statistical summaries & time series analysis

Correlation heatmaps & scatter plots

Wind rose, bubble charts, and more

👨‍💻 Contributions
Project Setup: Organized structure (data/, notebooks/, .gitignore)

Branching: Country-specific branches (e.g., eda-benin)

EDA:

Cleaning: handled missing values, outliers (Z-scores), imputation

Visuals: GHI, DNI, DHI trends, ModA vs. ModB, RH vs. GHI

Analysis: Correlation, humidity-temp interaction, wind patterns

Documentation: Clear markdown with methodology and insights

⚙️ Stack & Structure
Tech: Python 3, pandas, numpy, matplotlib, seaborn, scipy, windrose

bash
Copy
Edit
solar-eda-project/
├── data/           # Raw/cleaned datasets (ignored)
│   └── benin-malanville.csv
├── notebooks/      # Jupyter notebooks
│   └── benin_eda.ipynb
├── .gitignore
└── README.md
🚀 Run the Project
bash
Copy
Edit
# Clone the repo
git clone https://github.com/your-username/solar-eda-project.git
cd solar-eda-project

# Install dependencies
pip install pandas numpy matplotlib seaborn scipy windrose

# Add dataset to data/
cd notebooks && jupyter notebook benin_eda.ipynb
📌 Key Insights
Cleaned and imputed missing/invalid solar data

GHI peaks around midday; RH negatively correlates with GHI

Cleaning enhances sensor accuracy (ModA vs. ModB)

🧭 Add This to Your Repo
bash
Copy
Edit
# Create folders
mkdir data notebooks

# Move files
mv benin_eda.ipynb notebooks/
mv benin-malanville.csv data/

# Add to Git
echo "data/" >> .gitignore
git add .
git commit -m "Add EDA notebook and update README"
git push origin main  # or push to eda-benin
