# Deezer Log Analyzer

## Description

The Deezer Log Analyzer is a Python script that processes daily log files containing listening stream data from Deezer. It calculates the top 50 songs listened to in each country over the last 7 days and provides the option to calculate the top 50 songs listened to by each user as well. The script utilizes the pandas library to efficiently handle and analyze the data.

## Getting Started

### Prerequisites

- Python 3.x
- pandas library

### Installation

1. Clone the repository or download the script files.
2. Install the required dependencies by running the following command:
   pip install pandas

## Execution Steps 

1. Define a function `parse_log_file` to read and parse a log file to extract listening data, which can be used in updating song counts by country and user.
2. Define a function `process_log_files` to iterate over the log files for the last 'days' days, aggregate the data, and return a dictionary with song counts by country and user.
3. Call `process_log_files` to get the aggregated listening data.
4. Define a function `compute_top_songs_by_country` to compute the top 50 songs for each country based on the aggregated listening data.
5. Call `compute_top_songs_by_country` to get the top songs by country.
6. Define a function `compute_top_songs_by_user` to compute the top 50 songs for each user based on the aggregated listening data.
7. Call `compute_top_songs_by_user` to get the top songs by user.
8. Define a function `write_top_songs_to_files` to write the top songs for each country and user to separate text files in the specified output folder.
9. Call `write_top_songs_to_files` to write the results.
