# YouTube Downloader
    #### Video Demo:  <https://youtu.be/Q0uDsD73Mb4>
    #### Description:
    This Python script facilitates easy video downloads from YouTube using command line input. Simply provide the YouTube video URL, and the script handles the rest, downloading the video at the highest resolution available and saving its details to a CSV file.

    TODO
    1. Run the script by providing a YouTube URL as a command line argument:
    python project.py <YouTube_URL>
    Replace <YouTube_URL> with the actual URL of the video you want to download.

    2. The script will validate the URL and download the video to the specified directory (D:\user files\Desktop by default).

    3. The downloaded video details (title and views) will be saved to data.csv.

    Additional Notes

    Ensure the provided URL is a valid YouTube link.
    The script validates the command line argument to ensure correct usage.
    In case of errors during download or validation, appropriate error messages will be displayed.

    Objective:
    The primary goal of this project is to streamline the downloading process from YouTube by utilizing the pytube library, enabling users to easily access videos by providing the URL as a command-line argument.

    Key Features:

    YouTube Video Download: The script fetches the highest resolution video stream from the given URL and downloads it to a specified directory.
    Data Collection: Additionally, it extracts vital information such as the video's title and view count, storing this data in a CSV file (data.csv).
    Workflow:

    Accepts a YouTube URL as a command-line argument.
    Retrieves video details like title and view count.
    Downloads the video with the highest resolution to a specified directory.
    Appends the video's title and view count to a CSV file for data tracking purposes.
    Usage:

    Users simply need to provide a valid YouTube URL via the command line to initiate the download process.
    The script automatically verifies the input and ensures the URL is valid before proceeding.
