"""

Summary:
This script reads the daily log files containing listening stream data from a specified log folder. It processes the log data for the last 7 days and calculates the
top 50 songs listened in each country over that period as well as the top 50 songs most listened by users. The results are written to separate text files for each 
country in the specified output folder.

Steps:
1. Define a function 'parse_log_file' to read and parse a log file to extract listening data, this can be used in updating song counts by country and user.
2. Define a function 'process_log_files' to iterate over the log files for the last 'days' days, aggregate the data, and return a dictionary with song counts by country 
   and user.
3. Call 'process_log_files' to get the aggregated listening data.
4. Define a function 'compute_top_songs_by_country' to compute the top 50 songs for each country based on the aggregated listening data.
5. Call 'compute_top_songs_by_country' to get the top songs by country.
6. Define a function 'compute_top_songs_by_user' to compute the top 50 songs for each user based on the aggregated listening data.
7. Call 'compute_top_songs_by_user' to get the top songs by user.
8. Define a function 'write_top_songs_to_files' to write the top songs for each country and user to separate text files in the specified output folder.
9. Call 'write_top_songs_to_files' to write the results.

Note: Please update the 'log_folder', 'days', and 'output_folder' variables according to your specific requirements.

"""

import os
from datetime import datetime, timedelta

import os
from datetime import datetime, timedelta

def parse_log_file(file_path):

    """
    Parses a log file and updates song counts by country and user.

    Args:
        file_path (str): Path to the log file.

    Returns:
        dict: Dictionary containing the updated song counts by country and user.
    """

    listening_data = {"country": {}, "user": {}}
    with open(file_path, 'r') as log_file:
        for line_number, line in enumerate(log_file, 1):
            try:
                song_id, user_id, country = line.strip().split('|')

                # Update song counts by country
                if country not in listening_data["country"]:
                    listening_data["country"][country] = {}
                listening_data["country"][country][song_id] = listening_data["country"][country].get(song_id, 0) + 1

                # Update song counts by user
                if user_id not in listening_data["user"]:
                    listening_data["user"][user_id] = {}
                listening_data["user"][user_id][song_id] = listening_data["user"][user_id].get(song_id, 0) + 1
            except ValueError as e:
                print(f"Error parsing line {line_number} in file {file_path}: {e}")
                # Optionally, you can log the error to a log file instead of printing

    return listening_data

parse_log_file('C:/Users/ythonukunuru/Desktop/Portfolio Projects/de_code/logs/listen-20230713.log')

def process_log_files(log_folder, days):

    """
    Processes the log files for the last number of days required  and aggregates song counts by country and user.

    Args:
        log_folder (str): Path to the folder containing the log files.
        days (int): Number of days to process.

    Returns:
        dict: Dictionary containing the aggregated song counts by country and user.
    """
    today = datetime.today()
    top_7_days = [today - timedelta(days=d) for d in range(1, days + 1)]

    listening_data = {"country": {}, "user": {}}

    for day in top_7_days:
        file_name = f"listen-{day.strftime('%Y%m%d')}.log"
        file_path = os.path.join(log_folder, file_name)
        print(file_path)
        if os.path.exists(file_path):
            daily_data = parse_log_file(file_path)

            # Aggregate data for each day
            for country, songs in daily_data["country"].items():
                if country not in listening_data["country"]:
                    listening_data["country"][country] = {}
                for song_id, count in songs.items():
                    listening_data["country"][country][song_id] = listening_data["country"][country].get(song_id, 0) + count

            for user_id, songs in daily_data["user"].items():
                if user_id not in listening_data["user"]:
                    listening_data["user"][user_id] = {}
                for song_id, count in songs.items():
                    listening_data["user"][user_id][song_id] = listening_data["user"][user_id].get(song_id, 0) + count

    return listening_data

# Assuming you have your log files in a 'logs' folder for the last 7 days
log_folder = 'C:/Users/ythonukunuru/Desktop/Portfolio Projects/de_code/logs'
days = 7
listening_data = process_log_files(log_folder, days)

# print(listening_data)


# Compute the top 50 songs listened to in each country over the last 7 days:

def compute_top_songs_by_country(listening_data, top_n=50):
    top_songs_by_country = {}
    for country, songs in listening_data["country"].items():
        sorted_songs = sorted(songs.items(), key=lambda x: x[1], reverse=True)[:top_n]
        top_songs_by_country[country] = ','.join([f"{song_id}:{count}" for song_id, count in sorted_songs])
    return top_songs_by_country

top_songs_by_country = compute_top_songs_by_country(listening_data)


# Write the top 50 songs for each country to separate text files:
def write_top_songs_to_files(top_songs_by_country, output_folder):
    for country, song_list in top_songs_by_country.items():
        file_name = f"country_top50_{datetime.today().strftime('%Y%m%d')}_{country}.txt"
        file_path = os.path.join(output_folder, file_name)
        with open(file_path, 'w') as output_file:
            output_file.write(f"{country}|{song_list}\n")

output_folder = 'C:/Users/ythonukunuru/Desktop/Portfolio Projects/de_code/output'
write_top_songs_to_files(top_songs_by_country, output_folder)
