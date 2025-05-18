The Exploratory Data Analysis (EDA) project for the solar dataset is hosted in the following GitHub repository:
Solar EDA Project Repository
Project Overview
This repository contains the end-to-end EDA process for solar datasets from various countries (e.g., Benin), focusing on cleaning, analyzing, and visualizing solar irradiance data to prepare it for comparison and region-ranking tasks. The project includes data preprocessing, statistical analysis, time series visualization, and correlation studies, all performed using Python in Jupyter Notebooks.
My Contributions
Project Setup: Initialized a Git repository with a structured layout, including separate data/ and notebooks/ folders, and configured .gitignore to exclude raw and cleaned datasets.

Branching: Created country-specific branches (e.g., eda-benin) for isolated EDA workflows.

EDA Implementation:
Developed benin_eda.ipynb, a Jupyter Notebook that performs:
Summary statistics and missing value analysis.

Outlier detection using Z-scores and cleaning (imputation with medians, fixing invalid entries).

Time series analysis with visualizations (GHI, DNI, DHI, Tamb trends).

Cleaning impact analysis on sensor readings (ModA, ModB).

Correlation analysis with heatmaps and scatter plots.

Wind and distribution analysis (wind rose, histograms).

Temperature and humidity relationship analysis.

Bubble chart visualization (GHI vs. Tamb with RH as bubble size).

Exported cleaned data to data/benin_clean.csv (not committed, per .gitignore).

Documentation: Added detailed markdown sections in the notebook to explain each step, including insights, methodology, and references to resources like the Pandas and Seaborn documentation.

Implementation Details
Tech Stack: Python 3, Jupyter Notebook, pandas, numpy, matplotlib, seaborn, scipy, windrose.

Directory Structure:

solar-eda-project/
├── data/                    # Raw and cleaned datasets (ignored by .gitignore)
│   └── benin-malanville.csv
├── notebooks/               # Jupyter Notebooks for EDA
│   └── benin_eda.ipynb
├── .gitignore               # Ignores data/ folder
└── README.md                # Project documentation

How to Run:
Clone the repository: git clone https://github.com/your-username/solar-eda-project.git

Install dependencies: pip install pandas numpy matplotlib seaborn scipy windrose

Place the dataset (benin-malanville.csv) in the data/ folder.

Open the notebook: cd notebooks && jupyter notebook benin_eda.ipynb

Run the cells in order to perform the EDA.

Key Insights
Identified and handled missing values and outliers in solar irradiance data (e.g., GHI, DNI).

Discovered daily and monthly trends in solar irradiance, with GHI peaking around noon.

Found that cleaning significantly improves sensor readings (ModA, ModB).

Observed a negative correlation between relative humidity (RH) and GHI, indicating cloud cover impacts.

Steps to Add This to Your Repository
Create the Repository:
Go to GitHub and sign in.

Click the “+” icon (top right) > “New repository.”

Name it solar-eda-project, set it to public, and initialize with a README.

Clone it to your local machine:
bash

git clone https://github.com/your-username/solar-eda-project.git

Set Up the Directory Structure:
Create the data/ and notebooks/ folders:
bash

mkdir data notebooks

Move your benin_eda.ipynb to the notebooks/ folder.

Place benin-malanville.csv in the data/ folder (if you have it; it won’t be committed).

Ensure .gitignore contains:

data/

Update the README:
Open README.md in a text editor (e.g., VS Code, Notepad).

Copy and paste the section above.

Replace your-username in the GitHub link with your actual GitHub username.

Commit and Push:
Add and commit your changes:
bash

git add .
git commit -m "Add EDA notebook and update README with documentation"
git push origin main

If you’re working on the eda-benin branch, push that branch:
bash

git push origin eda-benin

Verify:
Visit your repository on GitHub (e.g., https://github.com/your-username/solar-eda-project).

Ensure the README displays correctly and the notebook is in the notebooks/ folder.

Check that the data/ folder is not committed (it should be ignored by .gitignore)

