import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Create a SQLite connection
conn = sqlite3.connect('data/database.db')

# Load data from SQLite tables
df1 = pd.read_sql_query("SELECT * FROM Gefahrenkontrollen", conn)
df2 = pd.read_sql_query("SELECT * FROM Gefahrgutzwischenfaelle", conn)

# Perform exploratory data analysis
# Get the number of accidents per year
accidents_per_year = df2.groupby('Year')['Incidents/Accidents'].sum()

# Get the number of controls per year
controls_per_year = df1.groupby('Year').size()

# Combine the two series into a DataFrame
analysis_df = pd.DataFrame({'Accidents': accidents_per_year, 'Controls': controls_per_year})

# Plotting the number of accidents and controls over the years
analysis_df.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Number of Accidents and Controls Over the Years')
plt.legend()
plt.show()

# Display the combined DataFrame
print(analysis_df)