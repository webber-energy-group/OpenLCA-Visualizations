#WEGR MAIN
#region Instructions
"""When running this code on a personal laptop there a few thing you might want to change. The 1st you must change.
1st. Under region importing files, you must change the file_path variable to the proper directory in which the Excel document is stored on your computer
2nd. Under region WEGR4 you can edit the search words for specific elements or compounds that you would like to see around line 1010 (ctrl f 'Flows With Key Words') 
All the flows containing key words will be the FIRST thing printed in the output. 
From this you can specifcy further which flows you want around line 1142 under the list 'values_to_keep' (ctrl f 'List of Values to Keep')
The specified flows containing key words will be the second thing printed in the output
These specified flows are also used later in WEGR 7 as the final graph produced.
3rd. Under WEGR region 6, you can alter the number of flows/processes shown on the graph by editing the 'top_20_values = sorted_impact_df.head(20)' line.
To find where to edit the # of flows it is around line 1309 or ctrl f 'Edit Top X Flows'. To find where to edit processes it is around line 1471 or ctrl f 'Edit Top X Processes' 
NOTE: Sometimes line 713 needs to be commented in/out depending on the Excel File, this will be apparent if errors show up in the first few graphs"""
#endregion
#region importing
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
#endregion
#region dictionary
# Dictionary to map abbreviations to their full forms

#endregion
continent_dict = {
  'CN-NCGC': 'Asia',
  'CN-ECGC': 'Asia', 
  'CN-NECG': 'Asia',
  'CN-CCG': 'Asia',
  'CN-SWG': 'Asia',
  'CN-NWG': 'Asia',
  'RoE': 'Europe',
  'GLO': 'Global',
  'UN-EASIA': 'Asia',
  'RLA': 'South America',
  'WEU': 'Europe',
  'UN-NAFRICA': 'Africa',
  'UN-SASIA': 'Africa',
  'UN-EAFRICA': 'Africa',
  'UN-WASIA': 'Asia',
  'RNA': 'North America',
  'UN-SAMERICA': 'South America',
  'UN-MICRONESIA': 'Oceania',
  'UN-POLYNESIA': 'Oceania',
  'SAS': 'Asia',
  'UN-CAMERICA': 'North America',
  'UN-CARIBBEAN': 'North America',
  'UN-MAFRICA': 'Africa',
  'UN-WAFRICA': 'Africa',
  'UN-SEUROPE': 'Europe',
  'UN-AUSTRALIANZ': 'Oceania',
  'UN-EEUROPE': 'Europe',
  'UN-NEUROPE': 'Europe',
  'Central Asia': 'Asia',
  'UN-SEASIA': 'Asia',
  'UN-MELANESIA': 'Oceania',
  'UN-EUROPE': 'Europe',
  'UN-OCEANIA': 'Oceania',
  'UN-ASIA': 'Asia',
  'RAF': 'Africa',
  'UN-AMERICAS': 'North America', 
  'IN-LD': 'Asia',
  'US-AL': 'North America',
  'US-WI': 'North America',
  'IN-TN': 'Asia',
  'US-NY': 'North America',
  'IN-NL': 'Asia',
  'US-NH': 'North America',
  'US-WY': 'North America',
  'US-NJ': 'North America',
  'US-ND': 'North America',
  'CN-NX': 'Asia',
  'US-CT': 'North America',
  'CN-HB': 'Asia',
  'BR-MT': 'South America',
  'CN-LN': 'Asia',
  'IN-GA': 'Asia',
  'CN-SX': 'Asia',
  'CA-YK': 'North America',
  'IN-AS': 'Asia',
  'IN-AP': 'Asia',
  'US-MT': 'North America',
  'AUS-IOT': 'Oceania',
  'CN-GD': 'Asia',
  'US-MI': 'North America',
  'IN-MP': 'Asia',
  'US-AZ': 'North America',
  'IN-KL': 'Asia',
  'CN-TJ': 'Asia',
  'BR-CE': 'South America',
  'CA-NU': 'North America',
  'CN-HN': 'Asia',
  'IN-DN': 'Asia',
  'IN-PY': 'Asia',
  'BR-AL': 'South America',
  'CN-HE': 'Asia',
  'IN-TR': 'Asia',
  'BR-GO': 'South America',
  'US-ID': 'North America',
  'US-OK': 'North America',
  'US-VA': 'North America',
  'US-MO': 'North America',
  'CN-JL': 'Asia',
  'US-WA': 'North America',
  'IN-ML': 'Asia',
  'IN-PB': 'Asia',
  'BR-ES': 'South America',
  'IN-UT': 'Asia',
  'IN-KA': 'Asia',
  'IN-MH': 'Asia',
  'US-VT': 'North America',
  'BR-TO': 'South America',
  'US-AK': 'North America',
  'AUS-TSM': 'Oceania',
  'CA-ON': 'North America',
  'IN-AN': 'Asia',
  'CA-QC': 'North America',
  'CN-GZ': 'Asia',
  'CA-NF': 'North America',
  'IN-HR': 'Asia',
  'US-MN': 'North America',
  'CN-NM': 'Asia',
  'US-KS': 'North America',
  'CN-FJ': 'Asia',
  'BR-PB': 'South America',
  'US-SD': 'North America',
  'US-IA': 'North America',
  'BR-AM': 'South America',
  'CA-NB': 'North America',
  'IN-GJ': 'Asia',
  'IN-OR': 'Asia',
  'IN-CH': 'Asia',
  'AUS-ACT': 'Oceania',
  'CN-HU': 'Asia',
  'BR-RJ': 'South America',
  'US-KY': 'North America',
  'IN-HP': 'Asia',
  'BR-SP': 'South America',
  'US-PA': 'North America',
  'IN-BR': 'Asia',
  'AUS-SAS': 'Oceania',
  'AUS-VCT': 'Oceania',
  'US-GA': 'North America',
  'US-TX': 'North America',
  'BR-BA': 'South America',
  'US-WV': 'North America',
  'CA-MB': 'North America',
  'CN-SD': 'Asia',
  'CA-SK': 'North America',
  'US-IN': 'North America',
  'IN-RJ': 'Asia',
  'CN-JX': 'Asia',
  'CN-XJ': 'Asia',
  'BR-RR': 'South America',
  'CN-ZJ': 'Asia',
  'CN-XZ': 'Asia',
  'BR-SC': 'South America',
  'US-FL': 'North America',
  'US-RI': 'North America',
  'CA-PE': 'North America',
  'IN-CT': 'Asia',
  'CA-NS': 'North America',
  'AUS-NSW': 'Oceania',
  'BR-RO': 'South America',
  'US-TN': 'North America',
  'US-DE': 'North America',
  'AUS-QNS': 'Oceania',
  'CN-SH': 'Asia',
  'US-CA': 'North America',
  'US-NE': 'North America',
  'IN-WB': 'Asia',
  'IN-JH': 'Asia',
  'CN-QH': 'Asia',
  'US-NM': 'North America',
  'US-IL': 'North America',
  'CN-SC': 'Asia',
  'CN-YN': 'Asia',
  'BR-AC': 'South America',
  'IN-SK': 'Asia',
  'BR-MG': 'South America',
  'CA-BC': 'North America',
  'BR-RN': 'South America',
  'IN-MZ': 'Asia',
  'US-SC': 'North America',
  'CN-HA': 'Asia',
  'CN-HL': 'Asia',
  'BR-MA': 'South America',
  'AUS-WAS': 'Oceania',
  'CN-GS': 'Asia',
  'BR-PI': 'South America', 
  'IN-UP': 'Asia',
  'BR-MS': 'South America',
  'US-MA': 'North America',
  'BR-DF': 'South America',
  'US-NV': 'North America',
  'AUS-NTR': 'Oceania',
  'BR-PE': 'South America',
  'US-ME': 'North America',
  'CN-GX': 'Asia',
  'IN-MN': 'Asia',
  'US-DC': 'North America',
  'US-NC': 'North America',
  'IN-DL': 'Asia',
  'BR-PR': 'South America',
  'BR-AP': 'South America',
  'US-MD': 'North America',
  'US-OH': 'North America',
  'US-HI': 'North America',
  'IN-JK': 'Asia',
  'US-CO': 'North America',
  'Coral Sea Islands': 'Oceania',
  'CN-BJ': 'Asia',
  'US-UT': 'North America',
  'IN-DD': 'Asia',
  'BR-PA': 'South America',
  'AUS-AC': 'Oceania',
  'IN-AR': 'Asia',
  'CN-JS': 'Asia',
  'CN-CQ': 'Asia',
  'CN-SA': 'Asia',
  'CA-NT': 'North America',
  'CN-AH': 'Asia',
  'US-MS': 'North America',
  'US-OR': 'North America',
  'US-LA': 'North America',
  'CA-AB': 'North America',
  'US-AR': 'North America',
  'BR-RS': 'South America',
  'BR-SE': 'South America',
  'XK': 'Europe',
  'Serranilla Bank': 'North America',
  'Spratly Islands': 'Asia',
  'Dhekelia Base': 'Asia',
  'CS': 'Europe',
  'Cyprus No Mans Area': 'Asia',
  'Siachen Glacier': 'Asia',
  'Akrotiri': 'Asia',
  'Bajo Nuevo': 'North America',
  'TW': 'Asia',
  'Scarborough Reef': 'Asia',
  'Northern Cyprus': 'Asia',
  'Guantanamo Bay': 'North America',
  'Somaliland': 'Africa',
  'US-RFC': 'North America',
  'UCTE without France': 'Europe',
  'US-SERC': 'North America',
  'US-TRE': 'North America',
  'IN-Western grid': 'Asia',
  'BR-Mid-western grid': 'South America',
  'US-WECC': 'North America',
  'US-SPP': 'North America',
  'CENTREL': 'Europe',
  'US-NPCC': 'North America',
  'US-ASCC': 'North America',
  'IN-Southern grid': 'Asia',
  'IN-Northern grid': 'Asia',
  'BR-South-eastern grid': 'South America',
  'BR-Southern grid': 'South America',
  'US-HICC': 'North America',
  'IN-Islands': 'Asia',
  'IN-North-eastern grid': 'Asia',
  'US-MRO': 'North America',
  'WECC': 'North America',
  'BR-Northern grid': 'South America',
  'Québec, HQ distribution network': 'North America',
  'NORDEL': 'Europe',
  'NPCC': 'North America',
  'CN-SGCC': 'Asia',
  'IN-Eastern grid': 'Asia',
  'UCTE without Germany': 'Europe',
  'UCTE without Germany and France': 'Europe',
  'BR-South-eastern/Mid-western grid': 'South America',
  'ENTSO-E': 'Europe',
  'US-FRCC': 'North America',
  'UCTE': 'Europe',
  'BR-North-eastern grid': 'South America',
  'BALTSO': 'Europe',
  'CN-CSG': 'Asia',
  'RME': 'Asia',
  'Russia (Europe)': 'Europe',
  'FSU': 'Europe', 
  'NAFTA': 'North America',
  'Russia (Asia)': 'Asia',
  'RAS': 'Asia',
  'RER': 'Europe',
  'RoW': 'Global',
  'RER w/o DE+NL+RU': 'Europe',
  'Europe without Switzerland and Austria': 'Europe',
  'RER w/o DE+NL+NO+RU': 'Europe',
  'RER w/o DE+NL+NO': 'Europe',
  'China w/o Inner Mongol': 'Asia',
  'Europe without Austria': 'Europe',
  'Asia without China': 'Asia',
  'RER w/o RU': 'Europe',
  'RER w/o CH+DE': 'Europe',
  'Canada without Alberta': 'North America',
  'Europe without Switzerland and France': 'Europe',
  'Europe without Switzerland': 'Europe',
  'North America without Quebec': 'North America',
  'RER w/o AT+BE+CH+DE+FR+IT': 'Europe',
  'Europe without NORDEL (NCPA)': 'Europe',
  'Europe, without Russia and Turkey': 'Europe',
  'Canada without Alberta and Quebec': 'North America',
  'Canada without Quebec': 'North America',
  'TN': 'Africa',
  'BG': 'Europe',
  'GI': 'Europe',
  'RS': 'Europe',
  'TR': 'Asia',
  'TG': 'Africa',
  'TJ': 'Asia',
  'KP': 'Asia',
  'GM': 'Africa',
  'AU': 'Oceania',
  'JP': 'Asia',
  'PL': 'Europe',
  'BZ': 'North America',
  'JO': 'Asia',
  'GY': 'South America',
  'SC': 'Africa',
  'Clipperton Island': 'North America',
  'TK': 'Oceania',
  'ME': 'Europe',
  'UM': 'Oceania',
  'UA': 'Europe',
  'KI': 'Oceania',
  'TC': 'North America',
  'BL': 'North America',
  'PH': 'Asia',
  'LU': 'Europe',
  'MN': 'Asia',
  'NL': 'Europe', 
  'ID': 'Asia',
  'PT': 'Europe',
  'HU': 'Europe',
  'CR': 'North America',
  'BI': 'Africa',
  'PG': 'Oceania',
  'AZ': 'Asia',
  'KG': 'Asia',
  'LI': 'Europe',
  'LC': 'North America',
  'FO': 'Europe',
  'ZW': 'Africa',
  'AS': 'Oceania', 
  'SS': 'Africa',
  'BS': 'North America',
  'WF': 'Oceania',
  'IR': 'Asia',
  'AG': 'North America',
  'TV': 'Oceania',
  'BA': 'Europe',
  'EC': 'South America',
  'BR': 'South America',
  'HK': 'Asia',
  'AW': 'North America',
  'AM': 'Asia',
  'DE': 'Europe',
  'FR': 'Europe',
  'LY': 'Africa',
  'KR': 'Asia',
  'DJ': 'Africa',
  'YE': 'Asia',
  'EH': 'Africa',
  'BY': 'Europe',
  'ZM': 'Africa',
  'BH': 'Asia',
  'TL': 'Asia',
  'CK': 'Oceania',
  'BM': 'North America',
  'NE': 'Africa',
  'NF': 'Oceania',
  'ZA': 'Africa',
  'GS': 'South America',
  'OM': 'Asia',
  'SG': 'Asia',
  'TM': 'Asia',
  'CU': 'North America',
  'LR': 'Africa',
  'BE': 'Europe',
  'CW': 'North America',
  'AE': 'Asia',
  'LS': 'Africa',
  'SK': 'Europe',
  'Canary Islands': 'Europe',
  'FJ': 'Oceania',
  'BB': 'North America',
  'LB': 'Asia',
  'GD': 'North America',
  'GR': 'Europe',
  'France, including overseas territories': 'Europe',
  'CD': 'Africa',
  'MD': 'Europe',
  'GN': 'Africa',
  'KM': 'Africa',
  'CA': 'North America',
  'SX': 'North America',
  'SI': 'Europe',
  'PM': 'North America',
  'MG': 'Africa',
  'BQ': 'North America', 
  'RE': 'Africa',
  'IL': 'Asia',
  'PE': 'South America',
  'WS': 'Oceania',
  'MZ': 'Africa',
  'AX': 'Europe',
  'ML': 'Africa',
  'CY': 'Asia', 
  'TZ': 'Africa',
  'BW': 'Africa',
  'KY': 'North America',
  'SJ': 'Europe',
  'KH': 'Asia',
  'SZ': 'Africa',
  'JM': 'North America',
  'CI': 'Africa',
  'MX': 'North America',
  'IN': 'Asia',
  'KZ': 'Asia',
  'HN': 'North America',
  'ET': 'Africa',
  'MW': 'Africa',
  'LA': 'Asia',
  'MA': 'Africa',
  'RW': 'Africa',
  'CL': 'South America',
  'DM': 'North America',
  'CX': 'Asia',
  'GG': 'Europe',
  'GB': 'Europe',
  'IQ': 'Asia',
  'AO': 'Africa',
  'MC': 'Europe',
  'BJ': 'Africa',
  'NZ': 'Oceania',
  'PN': 'Oceania',
  'BF': 'Africa',
  'MF': 'North America',
  'TH': 'Asia',
  'DO': 'North America',
  'PA': 'North America',
  'IO': 'Asia',
  'IT': 'Europe',
  'CN': 'Asia',
  'VN': 'Asia',
  'GU': 'Oceania',
  'SE': 'Europe',
  'AF': 'Asia',
  'MT': 'Europe',
  'FI': 'Europe',
  'CM': 'Africa',
  'CC': 'Asia',
  'IS': 'Europe',
  'GH': 'Africa',
  'MS': 'North America',
  'FK': 'South America',
  'QA': 'Asia',
  'MV': 'Asia',
  'PS': 'Asia',
  'LT': 'Europe',
  'SN': 'Africa',
  'NP': 'Asia',
  'GE': 'Asia',
  'MP': 'Oceania',
  'HT': 'North America',
  'AT': 'Europe',
  'DK': 'Europe',
  'TD': 'Africa',
  'GW': 'Africa',
  'SD': 'Africa',
  'YT': 'Africa',
  'SB': 'Oceania',
  'NA': 'Africa',
  'MH': 'Oceania',
  'VG': 'North America',
  'TT': 'North America',
  'GT': 'North America',
  'AR': 'South America',
  'BV': 'Antarctica',
  'GL': 'North America',
  'SM': 'Europe',
  'VU': 'Oceania',
  'LK': 'Asia',
  'GP': 'North America',
  'NI': 'North America',
  'MO': 'Asia',
  'GQ': 'Africa',
  'SO': 'Africa',
  'SH': 'Africa',
  'SY': 'Asia',
  'CH': 'Europe',
  'IM': 'Europe',
  'SV': 'North America',
  'GF': 'South America',
  'VC': 'North America',
  'MM': 'Asia',
  'AL': 'Europe',
  'SR': 'South America',
  'CV': 'Africa',
  'ES': 'Europe',
  'DZ': 'Africa',
  'BD': 'Asia',
  'JE': 'Europe',
  'AI': 'North America',
  'EE': 'Europe',
  'RO': 'Europe',
  'NG': 'Africa',
  'NC': 'Oceania',
  'CG': 'Africa',
  'KN': 'North America',
  'NO': 'Europe',
  'MK': 'Europe',
  'BT': 'Asia',
  'IE': 'Europe',
  'LV': 'Europe',
  'SA': 'Asia',
  'KE': 'Africa',
  'ST': 'Africa',
  'EG': 'Africa',
  'BO': 'South America',
  'AQ': 'Antarctica',
  'US-PR': 'North America',
  'VE': 'South America',
  'UY': 'South America',
  'SL': 'Africa',
  'HR': 'Europe',
  'HM': 'Antarctica',
  'NR': 'Oceania',
  'CO': 'South America',
  'PW': 'Oceania',
  'GA': 'Africa',
  'US': 'North America',
  'BN': 'Asia',
  'UZ': 'Asia',
  'UG': 'Africa',
  'TO': 'Oceania',
  'MY': 'Asia',
  'AD': 'Europe',
  'MU': 'Africa',
  'MQ': 'North America',
  'PK': 'Asia',
  'TF': 'Antarctica',
  'KW': 'Asia',
  'PF': 'Oceania',
  'ER': 'Africa',
  'MR': 'Africa',
  'RU': 'Europe',
  'VI': 'North America',
  'FM': 'Oceania',
  'VA': 'Europe',
  'CZ': 'Europe',
  'CF': 'Africa',
  'NU': 'Oceania',
  'PY': 'South America',
  'IAI Area, South America': 'South America',
  'IAI Area, Africa': 'Africa',
  'IAI Area, North America, without Quebec': 'North America',
  'IAI Area, North America': 'North America',
  'IAI Area, Russia & RER w/o EU27 & EFTA': 'Europe',
  'IAI Area, Asia, without China and GCC': 'Asia',
  'IAI Area, EU27 & EFTA': 'Europe',
  'IAI Area, Gulf Cooperation Council': 'Asia'
}
#region importing files

#Different File Names
#Electrolysis___Renewable___H2.xlsx

file_path = "C:\\Users\\Kimble\\Downloads\\Electrolysis Renewable H2.xlsx"
df_PFC = pd.read_excel(file_path, sheet_name='Process flow contributions')
df_PIC = pd.read_excel(file_path, sheet_name='Process impact contributions')
df_FIC = pd.read_excel(file_path, sheet_name='Flow impact contributions')

#endregion

#region WEGR1 Impact Category by Category and Sub-Category, fic
#region For Categories
df = df_FIC.copy()
#print(df)
# Step 2: Drop the first, second, and fourth columns
df.drop(df.columns[[0, 1, 3,4]], axis=1, inplace=True)

# Step 3: Drop the first two rows
df.drop([0, 1, 3], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

# Remove rows where all elements are NaN
df = df.dropna(how='all')

# Drop the row at index 1
df.drop(index=1, inplace=True)

# Reset the index
df.reset_index(drop=True, inplace=True)

# Rename the first column
first_col_name = df.iloc[0, 0] if df.iloc[0, 0] is not None else 'Impact category'
df.rename(columns={df.columns[0]: first_col_name}, inplace=True)

# Rename the other columns based on the values in the first row
new_columns = {df.columns[i]: df.iloc[0, i] for i in range(1, len(df.columns))}
df.rename(columns=new_columns, inplace=True)

# Drop the first row
df.drop(index=0, inplace=True)

# Reset the index again
df.reset_index(drop=True, inplace=True)

# Remove the row with 'Impact category'
df = df[df.iloc[:, 0] != 'Impact category']

# Reset the index after removing the row
df.reset_index(drop=True, inplace=True)

# Rename the first column to 'Impact category'
df.rename(columns={df.columns[0]: 'Impact category'}, inplace=True)

# Save the 'Impact category' column for later
impact_category = df['Impact category']

# Drop the 'Impact category' column
df_temp = df.drop(columns=['Impact category'])

# Convert all to numeric, ignoring errors to keep non-convertible columns
df_temp = df_temp.apply(pd.to_numeric, errors='ignore')

# Group by the columns and sum them up
df_grouped = df_temp.groupby(df_temp.columns, axis=1).sum()

# Add 'Impact category' back as the first column
df_grouped['Impact category'] = impact_category
cols = ['Impact category'] + [col for col in df_grouped if col != 'Impact category']
df_grouped = df_grouped[cols]

#print(df_grouped.columns)
#print(df_grouped)

# Assuming df_grouped is your DataFrame

#Top 3
#df_grouped_subset = df_grouped.iloc[:3]

#Just GWP 100
df_grouped_subset = df_grouped.iloc[[1]]

# Create the stacked bar chart
fig = px.bar(df_grouped_subset, 
             x='Impact category', 
             y=['Emission to air', 'Emission to soil', 'Emission to water', 'Inventory indicator', 'Resource'],
             title='Impact Categories and Their Values Split by Category of Flow',
             labels={'value': 'Kg CO2-eq', 'variable': 'Category'},
             height=800,  # Adjust the height
             width=800,  # Adjust the width
             barmode='stack')

# Update layout for black background
fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',  # Making the plot background transparent
    'paper_bgcolor': 'rgba(0, 0, 0, 1)',  # Setting paper (around the plot) background to black
    'font': {
        'color': 'white'  # Making font color white for visibility against black background
    }
})

fig.show()
#endregion
#region for sub categories
df = df_FIC.copy()
#print(df)
# Step 2: Drop the first, second, and fourth columns
df.drop(df.columns[[0, 1, 3,4]], axis=1, inplace=True)

# Step 3: Drop the first two rows
df.drop([0, 1, 2], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

# Remove rows where all elements are NaN
df = df.dropna(how='all')

# Drop the row at index 1
df.drop(index=1, inplace=True)

# Reset the index
df.reset_index(drop=True, inplace=True)

# Rename the first column
first_col_name = df.iloc[0, 0] if df.iloc[0, 0] is not None else 'Impact category'
df.rename(columns={df.columns[0]: first_col_name}, inplace=True)

# Rename the other columns based on the values in the first row
new_columns = {df.columns[i]: df.iloc[0, i] for i in range(1, len(df.columns))}
df.rename(columns=new_columns, inplace=True)

# Drop the first row
df.drop(index=0, inplace=True)

# Reset the index again
df.reset_index(drop=True, inplace=True)

# Remove the row with 'Impact category'
df = df[df.iloc[:, 0] != 'Impact category']

# Reset the index after removing the row
df.reset_index(drop=True, inplace=True)

# Rename the first column to 'Impact category'
df.rename(columns={df.columns[0]: 'Impact category'}, inplace=True)
#print(df)
#print(df.columns)

# Save the 'Impact category' column for later
impact_category = df['Impact category']
#impact_category = impact_category.iloc[:, 0]
print(impact_category)

# Drop the 'Impact category' column
df_temp = df.drop(columns=['Impact category'])

# Convert all to numeric, ignoring errors to keep non-convertible columns
df_temp = df_temp.apply(pd.to_numeric, errors='ignore')

# Group by the columns and sum them up
df_grouped = df_temp.groupby(df_temp.columns, axis=1).sum()

# Add 'Impact category' back as the first column
df_grouped['Impact category'] = impact_category
cols = ['Impact category'] + [col for col in df_grouped if col != 'Impact category']
df_grouped = df_grouped[cols]

#print(df_grouped.columns)
#print(df_grouped)

# Assuming df_grouped is your DataFrame
#df_grouped_subset = df_grouped.iloc[:3]

#Just GWP 100
df_grouped_subset = df_grouped.iloc[[1]]

# Create the stacked bar chart
fig = px.bar(df_grouped_subset, 
             x='Impact category', 
             y=['agricultural', 'biotic', 'forestry', 'fossil well',
       'ground water', 'ground water, long-term', 'high population density',
       'in air', 'in ground', 'in water', 'industrial', 'land',
       'low population density', 'low population density, long-term',
       'lower stratosphere + upper troposphere', 'ocean', 'surface water',
       'unspecified', 'waste'],
             title='Impact Categories and Their Values Split by Sub-Category of Flow',
             labels={'value': 'Kg CO2-eq', 'variable': 'Sub-Category'},
             height=800,  # Adjust the height
             width=800,  # Adjust the width
             barmode='stack')

# Update layout for black background
fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',  # Making the plot background transparent
    'paper_bgcolor': 'rgba(0, 0, 0, 1)',  # Setting paper (around the plot) background to black
    'font': {
        'color': 'white'  # Making font color white for visibility against black background
    }
})

fig.show()
#endregion
#endregion
#region WEGR2 Emissions by Category and Sub-Category, pfc
#region Category Stacked Bar Chart

df = df_PFC.copy()

# Step 2: Drop the first, second, and fourth columns
df.drop(df.columns[[0, 1, 2, 4, 5,]], axis=1, inplace=True)

# Step 3: Drop the first two rows
df.drop([0, 1, 3], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

# Remove rows where all elements are NaN
df = df.dropna(how='all')

# Set the first row as the column header and remove the first row
df.columns = df.iloc[0]
df = df[1:]

# Drop the 'Location' column
df = df.drop(columns=['Location'])

df.columns.values[0] = 'Category'

# Reset the index for good measure
df.reset_index(drop=True, inplace=True)

# Replace column names starting from the second column (skipping 'Impact category')
new_col_names = ['Category'] + [continent_dict.get(col, col) for col in df.columns[1:]]

# Apply new column names to the DataFrame
df.columns = new_col_names

# Group by columns with the same name and sum them up
df = df.groupby(df.columns, axis=1).sum()

# Group by 'Category' and sum the values
df = df.groupby('Category').sum().reset_index()

# Filter to retain only the desired categories
desired_categories = ['Emission to air', 'Emission to soil', 'Emission to water', 'Inventory indicator', 'Resource']
df = df[df['Category'].isin(desired_categories)]

# Melt the DataFrame into long format
df_melted = pd.melt(df, id_vars='Category', var_name='Continent', value_name='Value')

# Create the stacked bar chart
fig = px.bar(df_melted, 
             x='Category', 
             y='Value', 
             color='Continent',
             title='Emissions by Category',
             labels={'Value': 'Kg'},
             height=600,
             width=600)

# Update background color
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white')
)

# Remove lines inside the bars
fig.update_traces(marker=dict(line=dict(width=0)))

# Show the plot
fig.show()

print(df.head())
#endregion
#region Sub-Category Stacked Bar Chart
df = df_PFC.copy()

# Step 2: Drop the first, second, and fourth columns
df.drop(df.columns[[0, 1, 2, 3, 5,]], axis=1, inplace=True)

# Step 3: Drop the first two rows
df.drop([0, 1, 3], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

# Remove rows where all elements are NaN
df = df.dropna(how='all')

# Set the first row as the column header and remove the first row
df.columns = df.iloc[0]
df = df[1:]

# Drop the 'Location' column
df = df.drop(columns=['Location'])

df.columns.values[0] = 'Category'

# Reset the index for good measure
df.reset_index(drop=True, inplace=True)

# Replace column names starting from the second column (skipping 'Impact category')
new_col_names = ['Sub-Category'] + [continent_dict.get(col, col) for col in df.columns[1:]]

# Apply new column names to the DataFrame
df.columns = new_col_names

# Group by columns with the same name and sum them up
df = df.groupby(df.columns, axis=1).sum()

# Group by 'Category' and sum the values
df = df.groupby('Sub-Category').sum().reset_index()

# Melt the DataFrame into long format
df_melted = pd.melt(df, id_vars='Sub-Category', var_name='Continent', value_name='Value')

# Create the stacked bar chart
fig = px.bar(df_melted, 
             x='Sub-Category', 
             y='Value', 
             color='Continent',
             title='Emissions by Sub-Category',
             labels={'Value': 'Kg'},
             height=600,
             width=600)

# Update background color
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white')
)

# Remove lines inside the bars
fig.update_traces(marker=dict(line=dict(width=0)))

# Show the plot
fig.show()

print(df.head())
#endregion
#endregion
#region WEGR3 Impact Category kg CO2-eq by Continent, pic
#region Process Impact Contributions. Impact Category Stacked(countries) Bar Chart
# Step 1: Load the Excel file into a DataFrame
df_process_impact_contributions = df_PIC.copy()

# Step 2: Drop the first, second, and fourth columns
df_process_impact_contributions.drop(df_process_impact_contributions.columns[[0, 1, 3]], axis=1, inplace=True)

# Step 3: Drop the first two rows
df_process_impact_contributions.drop([0, 1], axis=0, inplace=True)
df_process_impact_contributions.reset_index(drop=True, inplace=True)

# Remove rows where all elements are NaN
df_cleaned = df_process_impact_contributions.dropna(how='all')

# Combine the first two rows to form a more meaningful header
header_row = df_cleaned.iloc[0].fillna('') + ' ' + df_cleaned.iloc[1].fillna('')
header_row = header_row.str.strip()

# Drop the rows used for header
df_cleaned = df_cleaned[2:]

# Assign the new header
df_cleaned.columns = header_row

# Reset the index for good measure
df_cleaned.reset_index(drop=True, inplace=True)

# Drop the 'Location' column
df_cleaned = df_cleaned.drop(columns=['Location'])

# Replace column names starting from the second column (skipping 'Impact category')
new_col_names = ['Impact Category'] + [continent_dict.get(col, col) for col in df_cleaned.columns[1:]]

print(new_col_names)

# Apply new column names to the DataFrame
df_cleaned.columns = new_col_names

# Group by columns with the same name and sum them up
df_grouped = df_cleaned.groupby(df_cleaned.columns, axis=1).sum()
# Reorder the columns such that "Impact category" is the first column

# Reordering the columns to move "Impact category" to the first position
cols = df_grouped.columns.tolist()
cols.insert(0, cols.pop(cols.index('Impact Category')))
df_grouped = df_grouped.reindex(columns= cols)

print(df_grouped.columns.tolist())
print(df_grouped)

# Melt the DataFrame to make it suitable for Plotly
df_melted = df_grouped.melt(id_vars=['Impact Category'], var_name='Continent', value_name='value')

# Filter to only include the first 3 impact categories
#df_first_3_rows = df_melted[df_melted['Impact category'].isin(df_grouped['Impact category'].unique()[:3])]

# Filter to only include GWP 100
df_first_3_rows = df_melted[df_melted['Impact Category'].isin(df_grouped['Impact Category'].unique()[[1]])]

# Renaming the 'Impact category' values to keep only the text inside the last set of parentheses
df_first_3_rows['Impact Category'] = df_first_3_rows['Impact Category'].apply(lambda x: x.split('(')[-1].replace(')', '') if '(' in x else x)


# Create the bar chart
fig = px.bar(df_first_3_rows, 
             x='Impact Category', 
             y='value', 
             color='Continent',
             color_continuous_scale='Viridis',  # Color gradient
             title='Impact by Continent for Different Impact Categories',
             labels={'value': 'Kg CO2-eq'},
             height=600,  # Square plot
             width=600)

# Update background color
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white')
)

# Remove lines inside the bars
fig.update_traces(marker=dict(line=dict(width=0)))

# Show the plot
fig.show()
#endregion
#endregion
#region WEGR4 Kg CO2, Methane, and Hydrogen Compunds as Group and Inidividual, pfc
df = df_PFC.copy()

# Step 2: Drop the first, second, and fourth columns
df.drop(df.columns[[0, 1, 3, 4, 5,]], axis=1, inplace=True)

# Drop the first 4 rows
df = df.iloc[4:].reset_index(drop=True)

# Rename the first column to 'Flow'
df.columns.values[0] = 'Flow'

# Remove rows where all elements are NaN
df = df.dropna(how='all')

# Reset the index for good measure
df.reset_index(drop=True, inplace=True)

"""Flows With Key Words"""
# List of words to search for
search_words = ['Hydrogen', 'Methane', 'Carbon dioxide']

# Filter rows based on the presence of the search words in the 'Flow' column
filtered_df = df[df['Flow'].str.contains('|'.join(search_words), case=False, na=False)]

# Exclude rows containing "non-methane"
filtered_df = filtered_df[~filtered_df['Flow'].str.contains('non-methane', case=False, na=False)]
#print('summing all columns')
#print(filtered_df.iloc[:, 1:].sum(axis=1))

unfiltered_df = filtered_df
unfiltered_df_numbers = filtered_df.iloc[:, 1:].sum(axis=1)

# Create a new column to store the grouping key
for word in search_words:
    filtered_df.loc[filtered_df['Flow'].str.contains(word, case=False, na=False), 'Group'] = word

# Iterate through the first column and print each value. 
"""Print Flows With Key Words"""
for value in filtered_df.iloc[:, 0]:
    print(value)

# Group by the new 'Group' column and combine the rows
combined_df = filtered_df.groupby('Group').first().reset_index()

combined_df = combined_df.drop(columns=['Flow'])

# Combine all columns except the first one ('Group')
combined_df['Value'] = combined_df.iloc[:, 1:].sum(axis=1)

# Drop the original columns, keeping only 'Group' and 'Values'
combined_df = combined_df[['Group', 'Value']]

# Show the filtered DataFrame
#print(combined_df)



# Create the bar chart
fig = px.bar(combined_df,
             x='Group',
             y='Value',
             title='Kg of CO2, Methane, and Hydrogen Compounds',
             color='Group')

# Customize the chart
fig.update_layout(
    xaxis_title='Group',
    yaxis_title='Kg',
    plot_bgcolor='black',  # Setting plot background to black
    paper_bgcolor='black',  # Setting paper background to black
    font=dict(
        color='white',  # Changing font color to white for visibility against black background
        size=14
    )
)

# Show the plot
fig.show()



#print(unfiltered_df)
#print(unfiltered_df.iloc[:, 1:].sum(axis=1))
#For filtered

# Group by the new 'Group' column and combine the rows
#unfiltered_df = unfiltered_df.groupby('Group').first().reset_index()

# Combine all columns except the first one ('Group')
unfiltered_df['Value'] = unfiltered_df.iloc[:, 1:].sum(axis=1)

# Drop the original columns, keeping only 'Group' and 'Values'
unfiltered_df = unfiltered_df[['Flow', 'Value']]

unfiltered_df['Value'] = unfiltered_df_numbers

#print(unfiltered_df)
# Create the bar chart
fig = px.bar(unfiltered_df,
             x='Flow',
             y='Value',
             title='Kg of CO2, Methane, and Hydrogen',
             color='Flow')

# Customize the chart
fig.update_layout(
    xaxis_title='Flow',
    yaxis_title='Kg',
    plot_bgcolor='black',  # Setting plot background to black
    paper_bgcolor='black',  # Setting paper background to black
    font=dict(
        color='white',  # Changing font color to white for visibility against black background
        size=14
    )
)

for trace in fig.data:
    trace.marker.line.color = trace.marker.color
    trace.marker.line.width = 1  # You can adjust the width as needed

# Show the plot
fig.show()
#endregion
#region WEGR5 Kg CO2, Methane, and Hydrogen Compunds as Group and Inidividual but Specifically, pfc
df = df_PFC.copy()

# Step 2: Drop the first, second, and fourth columns
df.drop(df.columns[[0, 1, 3, 4, 5,]], axis=1, inplace=True)

# Drop the first 4 rows
df = df.iloc[4:].reset_index(drop=True)

# Rename the first column to 'Flow'
df.columns.values[0] = 'Flow'

# Remove rows where all elements are NaN
df = df.dropna(how='all')

# Reset the index for good measure
df.reset_index(drop=True, inplace=True)

# List of words to search for
search_words = ['Hydrogen', 'Methane', 'Carbon dioxide']

# Filter rows based on the presence of the search words in the 'Flow' column
filtered_df = df[df['Flow'].str.contains('|'.join(search_words), case=False, na=False)]
#print('filtered_df')
#print(filtered_df)

# List of values to keep
"""List of Values to Keep"""
values_to_keep = [
    "Carbon dioxide, fossil",
    "Carbon dioxide, non-fossil",
    "Hydrogen",
    "Methane, fossil",
    "Methane, non-fossil",
    "Carbon dioxide, from soil or biomass stock",
    "Carbon dioxide, to soil or biomass stock",
    "Carbon dioxide, in air",
    "Carbon dioxide, non-fossil, resource correction"
]

# Filter the dataframe
filtered_df = filtered_df[filtered_df['Flow'].isin(values_to_keep)]


#print('summing all columns')
#print(filtered_df.iloc[:, 1:].sum(axis=1))

unfiltered_df = filtered_df
unfiltered_df_numbers = filtered_df.iloc[:, 1:].sum(axis=1)

# Create a new column to store the grouping key
for word in search_words:
    filtered_df.loc[filtered_df['Flow'].str.contains(word, case=False, na=False), 'Group'] = word

# Iterate through the first column and print each value
print('values after being specified')
for value in filtered_df.iloc[:, 0]:
    print(value)

# Group by the new 'Group' column and combine the rows
combined_df = filtered_df.groupby('Group').first().reset_index()

combined_df = combined_df.drop(columns=['Flow'])

# Combine all columns except the first one ('Group')
combined_df['Value'] = combined_df.iloc[:, 1:].sum(axis=1)

# Drop the original columns, keeping only 'Group' and 'Values'
combined_df = combined_df[['Group', 'Value']]

# Show the filtered DataFrame
#print(combined_df)



# Create the bar chart
fig = px.bar(combined_df,
             x='Group',
             y='Value',
             title='Kg of CO2, Methane, and Hydrogen Compounds of Specific Compunds',
             color='Group')

# Customize the chart
fig.update_layout(
    xaxis_title='Group',
    yaxis_title='Kg',
    plot_bgcolor='black',  # Setting plot background to black
    paper_bgcolor='black',  # Setting paper background to black
    font=dict(
        color='white',  # Changing font color to white for visibility against black background
        size=14
    )
)

# Show the plot
fig.show()



#print(unfiltered_df)
#print(unfiltered_df.iloc[:, 1:].sum(axis=1))
#For filtered

# Group by the new 'Group' column and combine the rows
#unfiltered_df = unfiltered_df.groupby('Group').first().reset_index()

# Combine all columns except the first one ('Group')
unfiltered_df['Value'] = unfiltered_df.iloc[:, 1:].sum(axis=1)

# Drop the original columns, keeping only 'Group' and 'Values'
unfiltered_df = unfiltered_df[['Flow', 'Value']]

unfiltered_df['Value'] = unfiltered_df_numbers

#print(unfiltered_df)
# Create the bar chart
fig = px.bar(unfiltered_df,
             x='Flow',
             y='Value',
             title='Kg of CO2, Methane, and Hydrogen of Specific Compunds',
             color='Flow')

# Customize the chart
fig.update_layout(
    xaxis_title='Flow',
    yaxis_title='Kg',
    plot_bgcolor='black',  # Setting plot background to black
    paper_bgcolor='black',  # Setting paper background to black
    font=dict(
        color='white',  # Changing font color to white for visibility against black background
        size=14
    )
)

for trace in fig.data:
    trace.marker.line.color = trace.marker.color
    trace.marker.line.width = 1  # You can adjust the width as needed

# Show the plot
fig.show()
#endregion
#region WEGR6 Top 10-15 flows/processes by impact cat, fic & pic
#region top 10-15 flows

#Can change the impact category selected and number of flows/processes found

#WEGR Parsing columns and rows
df_F = df_FIC.copy()

# Drop the first 2 columns
df_F = df_F.iloc[:, 2:]

# Replace the column names with values from row at index 1
df_F.columns = df_F.iloc[1]

# Drop the row at index 1
df_F = df_F.drop([1,2,3,4])

# Drop columns containing only NaNs
df_F = df_F.dropna(axis=1, how='all')

df_F.columns.values[0] = 'Impact category'

print(df_F.head(5))

# Step 1: Filter the row corresponding to the impact category "climate change - global warming potential (GWP100)"
impact_row = df_F[df_F['Impact category'] == "climate change - global warming potential (GWP100)"].iloc[0, 3:]

# Step 2: Grab the UUID row
uuid_row = df_F.iloc[0, 3:]

# Step 3: Create a new DataFrame
impact_df = pd.DataFrame({
    'Flow': impact_row.index,
    'UUID': uuid_row.values,
    'Impact_Value': impact_row.values
})

print(impact_df)

#grouping
grouped_impact_df = impact_df.groupby('Flow').agg({
    'UUID': 'first',           # Keeps the first UUID encountered in each group. Modify this if needed.
    'Impact_Value': 'sum'      # Sums up the Impact_Value for each group.
}).reset_index()

print(grouped_impact_df)


# Step 4: Sort the impact_df DataFrame based on 'Impact_Value' in descending order
sorted_impact_df = grouped_impact_df.sort_values(by='Impact_Value', ascending=False)
print(sorted_impact_df)

# Step 3: Take the top 20 values
"""Edit Top X Flows"""
top_20_values = sorted_impact_df.head(20)
top_20_values = top_20_values.drop('UUID', axis=1)
# Step 4: Get all other values
other_values = sorted_impact_df.drop(top_20_values.index)
other_values = other_values.drop('Flow', axis=1)
print(other_values)
# Replace the values in the 'UUID' column with the keys from uuid_dictionary
#other_values['UUID'] = other_values['UUID'].map(uuid_dict)

print("Top 20 Values:")
print(top_20_values)
print("Other Values with UUIDs:")
print(other_values)
# Check which UUIDs are in the dictionary
#print("UUIDs in dictionary:", other_values['UUID'].isin(uuid_dict.keys()))

# Calculate the 'Other' value
other_value = other_values.sum()
print("Top 20 Values:")
print(top_20_values)

other_values['Impact_Value'] = pd.to_numeric(other_values['Impact_Value'], errors='coerce')
sum_other_values = other_values['Impact_Value'].sum()
count_other_values = len(other_values['Impact_Value'])
mean_other_values = other_values['Impact_Value'].mean()
std_other_values = other_values['Impact_Value'].std()

# Create a new DataFrame for the "Other" row
other_row = pd.DataFrame({'Flow': ['Other'], 'Impact_Value': [sum_other_values]})

# Append the "Other" row to top_20_values
top_20_values_with_other = pd.concat([top_20_values, other_row], ignore_index=True)

print("Top 20 Values with 'Other' included:")
print(top_20_values_with_other)

# Create the bar chart
fig = px.bar(top_20_values_with_other, 
             x='Flow', 
             y='Impact_Value',
             color='Flow',
             title='Top 20 Flows in GWP 100',
             labels={'Flow': 'Flows', 'Impact_Value': 'Kg CO2-Eq'},
             color_discrete_sequence=px.colors.qualitative.Plotly)

# Update layout for a black background
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    title=dict(font=dict(color='white')),
    xaxis=dict(showgrid=True, gridcolor='grey', tickfont=dict(color='white')),
    yaxis=dict(showgrid=True, gridcolor='grey', tickfont=dict(color='white')),
    font=dict(color='white')
)

# Add annotations for the statistics above the "Other" bar
fig.add_annotation(
    x='Other',
    y=mean_other_values,  # Replace with the actual mean value of the "Other" column
    text=f"Count: {count_other_values}<br>Mean: {mean_other_values:.5f}<br>Std: {std_other_values:.5f}",
    showarrow=True,
    arrowhead=1,
    font=dict(color='white')
)

# Show the plot
fig.show()



#endregion
#region top 10-15 processes
#WEGR Parsing columns and rows

#region Organizing other Excel File
df = pd.read_excel("C:\\Users\\Kimble\\Downloads\\Combined_Process_Spreadsheet.xlsm")
#print(df.columns)
df.drop('UUID', axis=1, inplace=True)
df['Category '] = df['Category '].str[0]# Keep only the first letter of each value in the 'Category' column
#print(df)
df['Name '] = df['Name '].apply(lambda x: '|'.join(x.split('|')[:2]).strip())
#print(df.head(5))

#Make a UUID-Letter dictionary
uuid_dict = dict(zip(df['Name '], df['Category ']))
#print(uuid_dict)
#Make a Letter-Category dictionary
industry_dict = {
    'A': 'Agriculture, forestry and fishing',
    'B': 'Mining and quarrying',
    'C': 'Manufacturing',
    'D': 'Electricity, gas, steam and air conditioning supply',
    'E': 'Water supply; sewerage, waste management and remediation activities',
    'F': 'Construction',
    'G': 'Wholesale and retail trade; repair of motor vehicles and motorcycles',
    'H': 'Transportation and storage',
    'I': 'Accommodation and food service activities',
    'J': 'Information and communication',
    'K': 'Financial and insurance activities',
    'L': 'Real estate activities',
    'M': 'Professional, scientific and technical activities',
    'N': 'Administrative and support service activities',
    'O': 'Public administration and defence; compulsory social security',
    'P': 'Education',
    'Q': 'Human health and social work activities',
    'R': 'Arts, entertainment and recreation',
    'S': 'Other service activities',
    'T': 'Activities of households as employers; undifferentiated goods- and services-producing activities of households for own use',
    'U': 'Activities of extraterritorial organizations and bodies'
}
#endregion
#region top Process

df_C = df_PIC.copy()

# Drop the first 2 columns
df_C = df_C.iloc[:, 2:]

# Replace the column names with values from row at index 1
df_C.columns = df_C.iloc[1]

# Drop the row at index 1
df_C = df_C.drop([1,2])

# Drop columns containing only NaNs
df_C = df_C.dropna(axis=1, how='all')

df_C.columns.values[0] = 'Impact category'

#print(df_FIC.head(5))

# Step 1: Filter the row corresponding to the impact category "climate change - global warming potential (GWP100)"
impact_row = df_C[df_C['Impact category'] == "climate change - global warming potential (GWP100)"].iloc[0, 3:]

# Step 2: Grab the UUID row
uuid_row = df_C.iloc[0, 3:]

# Step 3: Create a new DataFrame
impact_df = pd.DataFrame({
    'Process': impact_row.index,
    'UUID': uuid_row.values,
    'Impact_Value': impact_row.values
})
#print("impact_df")
#print(impact_df)

#grouping
grouped_impact_df = impact_df.groupby('Process').agg({
    'UUID': 'first',           # Keeps the first UUID encountered in each group. Modify this if needed.
    'Impact_Value': 'sum'      # Sums up the Impact_Value for each group.
}).reset_index()

#print(grouped_impact_df)


# Step 4: Sort the impact_df DataFrame based on 'Impact_Value' in descending order
sorted_impact_df = grouped_impact_df.sort_values(by='Impact_Value', ascending=False)
#print(sorted_impact_df)

"""Edit Top X Processes"""
# Step 3: Take the top 20 values
top_20_values = sorted_impact_df.head(10)
top_20_values = top_20_values.drop('UUID', axis=1)
# Step 4: Get all other values
other_values = sorted_impact_df.drop(top_20_values.index)
other_values = other_values.drop('UUID', axis=1)
#print(other_values)
other_values['Process'] = other_values['Process'].apply(lambda x: '|'.join(x.split('|')[:2]).strip())
#print("other_values_stripped")
#print(other_values)
# Replace the values in the 'UUID' column with the keys from uuid_dictionary
#other_values['UUID'] = other_values['UUID'].map(uuid_dict)

#print("Top 20 Values:")
#print(top_20_values)
#print("Other Values with UUIDs:")
#print(other_values)

# Check which UUIDs are in the dictionary
#print("Processes in dictionary:", other_values['Process'].isin(uuid_dict.keys()))

# Replace the values in 'Process' column with corresponding values from uuid_dict
other_values['Process'] = other_values['Process'].map(uuid_dict).fillna(other_values['Process'])
#print(other_values)

# Group by 'Process' and sum the 'Impact_Value'
grouped = other_values.groupby('Process').agg({'Impact_Value': 'sum'}).reset_index()
#print("grouped")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
#print(grouped)
#print(grouped["Impact_Value"].sum())

# Mask for rows where 'Process' has more than one letter
mask = grouped['Process'].str.len() > 1

# Sum the 'Impact_Value' for these rows
other_val = grouped.loc[mask, 'Impact_Value'].sum()

# Remove these rows from 'grouped'
grouped = grouped.loc[~mask]

# Create a DataFrame for the new row to append
new_row = pd.DataFrame({'Process': ['Other'], 'Impact_Value': [other_val]})

# Use pandas.concat to append the new row to the existing DataFrame
grouped = pd.concat([grouped, new_row], ignore_index=True)

#print("grouped")
#print(grouped)
grouped['Process'] = grouped['Process'].map(industry_dict).fillna(grouped['Process'])
#print("grouped")
#print(grouped)

#print(uuid_dict.keys())
#print(other_values['Process'])
# Calculate the 'Other' value
other_value = other_values.sum()
#print("Top 20 Values:")
#print(top_20_values)

other_values['Impact_Value'] = pd.to_numeric(other_values['Impact_Value'], errors='coerce')
sum_other_values = other_values['Impact_Value'].sum()
count_other_values = len(other_values['Impact_Value'])
mean_other_values = other_values['Impact_Value'].mean()
std_other_values = other_values['Impact_Value'].std()

# Create a new DataFrame for the "Other" row
other_row = pd.DataFrame({'Process': ['Other'], 'Impact_Value': [sum_other_values]})

# Append the "Other" row to top_20_values
top_20_values_with_other = pd.concat([top_20_values, other_row], ignore_index=True)

#print("Top 20 Values with 'Other' included:")
#print(top_20_values_with_other)

# Extract the main data (excluding 'Other')
main_data = top_20_values_with_other[top_20_values_with_other['Process'] != 'Other']

# Create bars for the main data
bars_main = [
    go.Bar(name=row['Process'], x=[row['Process']], y=[row['Impact_Value']], 
           marker_color=px.colors.qualitative.Plotly[i % len(px.colors.qualitative.Plotly)], showlegend=False) 
    for i, row in main_data.iterrows()
]

# Create the figure and add the bars
fig_main = go.Figure(data=bars_main)

# Update the layout for the main data
fig_main.update_layout(
    barmode='stack',
    title='Top Processes in GWP 100 Impact Category (Excluding Other)',
    xaxis_title='Processes',
    yaxis_title='Impact Value Kg CO2-Eq',
    plot_bgcolor='black',
    paper_bgcolor='black',
    title_font_color='white',
    xaxis=dict(showgrid=True, gridcolor='grey', tickfont=dict(color='white')),
    yaxis=dict(showgrid=True, gridcolor='grey', tickfont=dict(color='white')),
    font=dict(color='white')
)

fig_main.show()

# Bars for the 'Other' components from the `grouped` dataframe
bars_other = [
    go.Bar(name=row['Process'], x=['Other'], y=[row['Impact_Value']], 
           marker_color=px.colors.qualitative.Plotly[(i + len(main_data)) % len(px.colors.qualitative.Plotly)]) 
    for i, row in grouped.iterrows()
]

# Create the figure for the 'Other' data and add the bars
fig_other = go.Figure(data=bars_other)

# Update the layout for the 'Other' data
fig_other.update_layout(
    barmode='stack',
    title='"Other" Processes in GWP 100 Impact Category',
    xaxis_title='Process',
    yaxis_title='Impact Value Kg CO2-Eq',
    plot_bgcolor='black',
    paper_bgcolor='black',
    title_font_color='white',
    xaxis=dict(showgrid=False, gridcolor='grey', tickfont=dict(color='white')),
    yaxis=dict(showgrid=True, gridcolor='grey', tickfont=dict(color='white')),
    width=800,  # Set the width (in pixels)
    height=700,  # Set the height (in pixels)
    font=dict(color='white')
)

# Add your annotations for the statistics above the "Other" bar
fig_other.add_annotation(
    x='Other',
    y=mean_other_values,  # Replace with the actual mean value of the "Other" column
    text=f"Count: {count_other_values}<br>Mean: {mean_other_values:.5f}<br>Std: {std_other_values:.5f}",
    showarrow=True,
    arrowhead=1,
    font=dict(color='white')
)

fig_other.show()

#endregion
#endregion
#endregion
#region WEGR7 KG of CO2-eq of specific compunds, fic
df = df_FIC.copy()

# Step 2: Drop the first, second, and fourth columns
df.drop(df.columns[[0, 1, 2, 4 ]], axis=1, inplace=True)

# Drop the first 4 rows
df = df.iloc[1:].reset_index(drop=True)

df = df.drop([1, 2, 3, 4])

# List of values to keep
"""values_to_keep = [
    "Carbon dioxide, fossil",
    "Carbon dioxide, non-fossil",
    "Hydrogen",
    "Methane, fossil",
    "Methane, non-fossil",
    "Carbon dioxide, from soil or biomass stock",
    "Carbon dioxide, to soil or biomass stock",
    "Carbon dioxide, in air",
    "Carbon dioxide, non-fossil, resource correction"
]"""

# Identify columns to keep based on values in the first row
cols_to_keep = df.columns[df.iloc[0].isin(values_to_keep)].tolist()

# Filter the dataframe to only keep those columns
df = df[cols_to_keep]

# Set the first row as column headers
df.columns = df.iloc[0]

# Drop the first row
df = df.drop(0)

df = df.groupby(by=df.columns, axis=1).sum()

# Print all the column names
#print(df.columns.tolist())

#print(df.head(5))

# Melt the dataframe into a long format
df_melted = df.melt(var_name='Flow', value_name='Value')

# Create the bar chart using Plotly
fig = px.bar(df_melted,
             x='Flow',
             y='Value',
             title='Kg of CO2 Equivalent for CO2, Methane, and Hydrogen of Specific Compounds',
             color='Flow')

# Customize the chart
fig.update_layout(
    xaxis_title='Flow',
    yaxis_title='Kg of CO2-Eq',
    plot_bgcolor='black',  # Setting plot background to black
    paper_bgcolor='black',  # Setting paper background to black
    font=dict(
        color='white',  # Changing font color to white for visibility against black background
        size=14
    )
)

for trace in fig.data:
    trace.marker.line.color = trace.marker.color
    trace.marker.line.width = 1  # You can adjust the width as needed

# Show the plot
fig.show()

#endregion