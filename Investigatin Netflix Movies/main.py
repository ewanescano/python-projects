# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Filter the DataFrame for movies released between 1990 and 2000
new_df = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000) & (netflix_df['type'] == 'Movie') & (netflix_df['genre'] == 'Action')]

# Initialize variables
short_movie_count = 0
frequency = {}

# Iterate through the filtered DataFrame
for index, row in new_df.iterrows(): 
    if row['duration'] in frequency:
        frequency[row['duration']] += 1  
    else:
        frequency[row['duration']] = 1

    if row['duration'] < 90:
        short_movie_count += 1

# Plot the histogram of movie durations
plt.hist(list(frequency.keys()), weights=list(frequency.values()), bins=range(min(frequency.keys()), max(frequency.keys()) + 1, 10))
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.title('Distribution of Movie Durations (1990-1999)')
plt.show()

# Find the most common movie duration
duration = max(frequency, key=frequency.get)