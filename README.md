# End-to-End Vendor Performance & Sales Analytics Platform

## 📌 Project Overview
This project delivers an end-to-end data analytics solution designed to track, manage, and optimize a $441.41M vendor portfolio. Instead of just building a dashboard, this project implements a complete data pipeline—from data ingestion and storage using Python and SQLite to advanced Exploratory Data Analysis (EDA) and final interactive business intelligence visualization in Power BI.

The primary business objective is to analyze vendor performance, evaluate purchase-to-sales ratios, manage unsold capital, and isolate high-margin, low-sales target brands for strategic business growth.

---

## 🏗️ Project Architecture & Data Pipeline
The project is engineered through a structured 4-step pipeline to ensure scalability and clean separation of concerns:

1. **Data Ingestion (`/scripts`):** Written custom Python scripts (`ingestion_db.py`) to automate data loading from raw CSV files into a structured relational SQLite database (`inventory.db`).
2. **Exploratory Data Analysis (`/notebooks`):** Conducted thorough EDA using Pandas, Matplotlib, and Seaborn to check data distributions, handle outliers, and analyze vendor-specific matrices.
3. **Data Modeling & DAX:** Developed a clean star-schema data model within Power BI and implemented advanced DAX measures (like `PERCENTILEX.INC`) to segment brands and calculate complex metrics like Unsold Capital.
4. **Interactive Dashboarding:** Created an executive-level Power BI dashboard featuring scatter plots and breakdown charts for actionable decision-making.

---

## 🛠️ Technical Skillset Used
* **Data Engineering & Ingestion:** Python, Pandas, SQLite3
* **Statistical & Data Analysis (EDA):** Jupyter Notebook, Matplotlib, Seaborn
* **Business Intelligence & Visualization:** Power BI Desktop
* **Advanced Analytics:** Custom DAX Functions (`PERCENTILEX.INC`, Advanced Filtering)

---

## 📊 Key Business Insights & KPIs Tracked
* **Total Portfolio Scale:** Successfully analyzed **$441.41M in Total Sales** against **$307.34M in Total Purchases**, maintaining a robust **38.72% Profit Margin** across the vendor ecosystem.
* **Unsold Capital Identification:** Isolated **$2.71M in Unsold Capital**, helping supply chain teams pinpoint exactly where cash flow is bottlenecked in dead stock.
* **Brand Segmentation via Scatter Plot:** Engineered a custom scatter plot mapping Total Sales against Average Profit Margin. This isolated high-margin, low-sales brands, providing a direct roadmap for marketing teams to drive strategic expansion.
* **Vendor Contribution:** Identified that the Top 10 Vendors contribute **65.7%** of the total purchase share, highlighting the business's heavy reliance on core partners.

---

## 📁 Repository Structure
```text
VendorProject/
│
├── data/                       # Contains relational database and underlying raw sheets
│   ├── inventory.db            # Main SQLite relational database file
│   └── *.csv                   # Clean transactional source data datasets
│
├── notebooks/                  # Advanced analysis files
│   ├── Exploratory Data Analysis.ipynb
│   └── Vendor Performance Analysis.ipynb
│
├── scripts/                    # Python automation engine
│   ├── ingestion_db.py         # Automates CSV data loading into SQLite
│   └── get_vendor_summary.py   # Script for extracting data summaries
│
├── logs/                       # System and debugging tracking
│   └── ingestion_db.log
│
└── VendorProjectDashboard.pbix # Final operational Power BI Dashboard