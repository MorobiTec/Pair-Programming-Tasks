import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the Excel file
song = pd.read_excel('spotify_global_2019_most_streamed_tracks_audio_features.xlsx')

# Set pandas to display all columns
pd.set_option('display.max_columns', None)

# Display basic information about the dataset
print(song.info())

# Display the first few rows of the dataset
print(song.head())

# Example of visualizing the distribution of a specific column, such as 'tempo'
plt.figure(figsize=(10, 6))
sns.histplot(song['tempo'], kde=True)
plt.title('Distribution of Song Tempos')
plt.xlabel('Tempo')
plt.ylabel('Frequency')
plt.show()

# Example of creating a playlist of only upbeat music using 'tempo' as the criterion
# and including artist name, track name, tempo, and streams
upbeat_playlist = song[song['tempo'] > 120][['artist_name', 'track_name', 'tempo', 'streams']]

# Display the upbeat playlist
print(upbeat_playlist)

# Save the upbeat playlist to an Excel file
upbeat_playlist.to_excel('upbeat_playlist.xlsx', index=False)
