# Project Samarth: Agriculture & Climate Q&A

**Project Samarth** is an intelligent Q&A system built using **Python** and **Streamlit** that allows users to query crop production and rainfall patterns in India. It integrates datasets from the **Ministry of Agriculture & Farmers Welfare** and the **India Meteorological Department (IMD)** to provide insights at the state and district levels.

---

## **Features**

- Compare average annual rainfall between any two states over a custom year range.  
- List top crops by production in any state and time period.  
- Identify districts with highest and lowest production for a crop in two states.  
- Analyze trends of crop production vs rainfall and calculate correlation.  
- Interactive **graphs** for visualization of production vs rainfall trends.  
- Citations for all data sources used.

---

## **Datasets**

1. **India_Agriculture_Crop_Production.csv**  
   - Source: Ministry of Agriculture & Farmers Welfare  
   - Columns: State, District, Crop, Year, Season, Area, Production, Yield, etc.

2. **Sub_Division_IMD_2017.csv**  
   - Source: India Meteorological Department  
   - Columns: SUBDIVISION (State), YEAR, ANNUAL (Rainfall), monthly breakdown, etc.

> ⚠️ Datasets are **not included** in this repo due to size. Please download from [data.gov.in](https://data.gov.in/) and place them in the project folder.

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ProjectSamarth.git
cd ProjectSamarth
