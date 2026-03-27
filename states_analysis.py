import pandas as pd

# Create Data
data = {
    'State': ['Maharashtra', 'Gujarat', 'Karnataka', 'Rajasthan', 'Punjab'],
    'Area': [307713, 196024, 191791, 342239, 50362],
    'Population': [124000000, 68000000, 70000000, 81000000, 30000000]
}

# Create DataFrame
df = pd.DataFrame(data)

# a) Display all states
print("\nAll States Information:")
print(df)

# b) State with largest area
print("\nState with Largest Area:")
print(df[df['Area'] == df['Area'].max()])

# c) State with largest population
print("\nState with Largest Population:")
print(df[df['Population'] == df['Population'].max()])

# d) Calculate Population Density
df['Density'] = df['Population'] / df['Area']
print("\nPopulation Density of States:")
print(df)

# e) State with highest density
print("\nState with Highest Population Density:")
print(df[df['Density'] == df['Density'].max()])