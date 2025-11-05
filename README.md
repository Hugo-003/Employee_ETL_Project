# 🗂️ Employee Data Processing & Analysis Project

This project implements an **interactive ETL (Extract, Transform, Load) pipeline** in Python to process employee data from multiple companies. The system allows users to perform data transformations, compute metrics, and generate insights about employee structure, salaries, bonuses, and age distributions.  

It demonstrates a **modular, object-oriented approach**, combining technical ETL skills with practical data analysis.

---

## 📊 Project Overview

The main objectives of this project are:

1. **Data Processing (ETL):**  
   - Load raw employee data from CSV files  
   - Fill missing values and normalize columns (e.g., full_time, part_time)  
   - Compute derived columns such as additional bonuses, salary increases, and composite keys  
   - Categorize employees by age ranges and calculate differences relative to group averages  

2. **Data Analysis & Insights:**  
   - Examine salary, bonus, and experience distributions per company and department  
   - Inspect data by unique companies and departments  
   - Generate transformed datasets for further analysis or reporting  

The pipeline is interactive, allowing the user to choose which operations to run step by step.

---

## 🧑‍💻 How It Works

main.py is the entry point. It initializes configuration and logging, then runs an interactive menu allowing the user to perform ETL steps and analyses. When executed, it allows the user to:

1. Load the CSV and display the first 5 rows
2. Fill or normalize columns (`full_time`, `part_time`)
3. Assign additional bonuses
4. Calculate salary increases
5. Create composite keys combining company, department, and employee ID
6. Categorize employees into age ranges
7. Compute difference between employee age and the average age in their group
8. Save all transformations into final CSVs (7 outputs stored in `data/`)
9. Exit the program

Transformed datasets are saved automatically to CSV files.
Each step is logged using a custom logger, providing **real-time feedback** and **error handling**.

---

## 🚀 Usage

Place your CSV dataset in the data/ folder.

Run the script from the terminal or your IDE:

- python main.py


Follow the interactive menu to apply transformations or view data insights.

---

## ⚙️ Requirements

- Python >= 3.8  
- pandas  
- numpy  
- logging  

---

## 📌 Features

Interactive menu for step-by-step processing

Modular, reusable classes for each company

Automatic calculation of bonuses, salary increases, and composite keys

Age range classification and deviation from departmental averages

Saves processed datasets for further analysis

---

## 🔮 Possible Extensions

- Automate the pipeline to run all transformations sequentially without manual input  
- Integrate visualizations for salary, bonus, and age distributions 
- Incorporate additional metrics for deeper employee insights 
- Include support for multiple CSV sources from other companies  

---

## 📝 Author

**Hugo Crespo**
