import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_processing import compare_rainfall, top_crops, district_crop_comparison, crop_climate_trend

st.set_page_config(page_title="Project Samarth Q&A", layout="wide")
st.title("Project Samarth: Agriculture & Climate Q&A")

st.markdown("""
Type questions about **crop production** and **rainfall patterns** in India. Examples:

- Compare rainfall between Maharashtra and Karnataka from 2010 to 2017  
- Top crops in Maharashtra between 2010 and 2017  
- District comparison for Rice in Maharashtra and Karnataka  
- Trend of Rice production vs rainfall in Maharashtra from 2010 to 2017
""")

# Inputs
question_type = st.selectbox("Select question type:", 
                             ["Compare Rainfall", "Top Crops", "District Comparison", "Trend Analysis"])

# Common inputs
state_x = st.text_input("State X (for rainfall/district comparison)", "Maharashtra")
state_y = st.text_input("State Y (for rainfall/district comparison)", "Karnataka")
crop_name = st.text_input("Crop Name (for district/trend analysis)", "Rice")
start_year = st.number_input("Start Year", 2000, 2025, 2010)
end_year = st.number_input("End Year", 2000, 2025, 2017)

if st.button("Get Answer"):
    if question_type == "Compare Rainfall":
        answer = compare_rainfall(state_x, state_y, start_year, end_year)
        st.write(f"Average Rainfall from {start_year} to {end_year}:")
        st.write(answer)

    elif question_type == "Top Crops":
        answer = top_crops(state_x, start_year, end_year, top_m=5)
        st.write(f"Top crops in {state_x.title()} from {start_year} to {end_year}:")
        st.write(answer)

    elif question_type == "District Comparison":
        answer = district_crop_comparison(state_x, state_y, crop_name)
        st.write(f"District comparison for {crop_name.title()}:")
        st.write(answer)

    elif question_type == "Trend Analysis":
        result = crop_climate_trend(crop_name, state_x, start_year, end_year)
        st.write(f"Trend Analysis for {crop_name.title()} in {state_x.title()}:")
        st.write(result)

        # Plot graph
        merged_df = pd.DataFrame(result['Merged_Data'])
        if not merged_df.empty:
            fig, ax1 = plt.subplots()
            ax1.plot(merged_df['Year'], merged_df['Production'], color='green', marker='o', label='Production')
            ax1.set_xlabel('Year')
            ax1.set_ylabel('Production', color='green')
            ax2 = ax1.twinx()
            ax2.plot(merged_df['Year'], merged_df['Rainfall'], color='blue', marker='x', label='Rainfall')
            ax2.set_ylabel('Rainfall', color='blue')
            fig.tight_layout()
            st.pyplot(fig)

