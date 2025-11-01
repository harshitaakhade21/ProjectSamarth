import pandas as pd

# -------------------------------
# 1. Load datasets
# -------------------------------
crop_df = pd.read_csv("India Agriculture Crop Production.csv")
imd_df = pd.read_csv("Sub_Division_IMD_2017.csv")

# -------------------------------
# 2. Preprocess datasets
# -------------------------------
def preprocess_data():
    global crop_df, imd_df

    # --- Crop data preprocessing ---
    crop_df['State'] = crop_df['State'].str.strip().str.lower()
    crop_df['District'] = crop_df['District'].str.strip().str.lower()
    crop_df['Crop'] = crop_df['Crop'].str.strip().str.lower()
    
    # Convert Year from "2001-02" format to int
    crop_df['Year'] = crop_df['Year'].apply(lambda x: int(str(x).split('-')[0]))
    crop_df['Production'] = pd.to_numeric(crop_df['Production'], errors='coerce')

    # --- IMD data preprocessing ---
    imd_df.rename(columns={
        'SUBDIVISION': 'State',
        'YEAR': 'Year',
        'ANNUAL': 'Rainfall'
    }, inplace=True)
    imd_df['State'] = imd_df['State'].str.strip().str.lower()
    imd_df['Year'] = imd_df['Year'].astype(int)
    imd_df['Rainfall'] = pd.to_numeric(imd_df['Rainfall'], errors='coerce')

preprocess_data()

# -------------------------------
# 3. Query functions
# -------------------------------

def compare_rainfall(state_x, state_y, start_year, end_year):
    state_x = state_x.lower()
    state_y = state_y.lower()
    filtered = imd_df[imd_df['Year'].between(start_year, end_year)]
    
    rainfall_x = filtered[filtered['State']==state_x]['Rainfall'].mean()
    rainfall_y = filtered[filtered['State']==state_y]['Rainfall'].mean()
    
    return {
        'State_X_Rainfall': rainfall_x,
        'State_Y_Rainfall': rainfall_y,
        'Source': 'Sub_Division_IMD_2017.csv'
    }

def top_crops(state, start_year, end_year, top_m=5):
    state = state.lower()
    df = crop_df[(crop_df['State']==state) &
                 (crop_df['Year'].between(start_year, end_year))]
    
    top_crops_df = df.groupby('Crop')['Production'].sum().sort_values(ascending=False).head(top_m)
    return {'Top_Crops': top_crops_df.to_dict(), 'Source': 'India_Agriculture_Crop_Production.csv'}

def district_crop_comparison(state_x, state_y, crop_name):
    state_x = state_x.lower()
    state_y = state_y.lower()
    crop_name = crop_name.lower()
    
    recent_year = crop_df['Year'].max()
    
    df_x = crop_df[(crop_df['State']==state_x) & (crop_df['Crop']==crop_name) & (crop_df['Year']==recent_year)]
    df_y = crop_df[(crop_df['State']==state_y) & (crop_df['Crop']==crop_name) & (crop_df['Year']==recent_year)]
    
    max_district = df_x.loc[df_x['Production'].idxmax()]['District'] if not df_x.empty else None
    min_district = df_y.loc[df_y['Production'].idxmin()]['District'] if not df_y.empty else None
    
    return {
        'Max_District_State_X': max_district,
        'Min_District_State_Y': min_district,
        'Source': 'India_Agriculture_Crop_Production.csv'
    }

def crop_climate_trend(crop_name, state, start_year, end_year):
    crop_name = crop_name.lower()
    state = state.lower()
    
    crop_data = crop_df[(crop_df['Crop']==crop_name) &
                        (crop_df['State']==state) &
                        (crop_df['Year'].between(start_year, end_year))]
    
    climate_data = imd_df[(imd_df['State']==state) &
                          (imd_df['Year'].between(start_year, end_year))]
    
    merged = pd.merge(crop_data.groupby('Year')['Production'].sum().reset_index(),
                      climate_data.groupby('Year')['Rainfall'].mean().reset_index(),
                      on='Year')
    
    correlation = merged['Production'].corr(merged['Rainfall']) if not merged.empty else None
    
    return {
        'Correlation_Production_Rainfall': correlation,
        'Merged_Data': merged.to_dict(orient='records'),
        'Sources': ['India_Agriculture_Crop_Production.csv', 'Sub_Division_IMD_2017.csv']
    }
