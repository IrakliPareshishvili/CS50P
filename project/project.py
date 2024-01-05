import sys
import csv
import os
from os.path import splitext
from pytube import YouTube

def main():
    try:
        # Passing YouTube URL through command_line
        url = sys.argv[1]

        # Creating a YouTube object
        yt = YouTube(url)

        title = yt.title
        views = yt.views
        append_to_csv(title, views)

        # Get the highest resolution stream
        yd = yt.streams.get_highest_resolution()

        # Directory to save the video (Desktop in this case)
        save_path = r"D:\user files\Desktop"

        # Downloading the video to the current directory
        yd.download(save_path)

        print("Download complete.")
    except Exception as e:
        print("An error occurred:", str(e))



def append_to_csv(title, views):
    # Creating csv file to save data
    csv_file = "data.csv"
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode='a', newline='') as file:
        fieldnames = ["Title", "Views"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({"Title": title, "Views": views})

def check_command_line():
    # Validating the command_line_argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    link = splitext(sys.argv[1])
    if check_extensions(link[0]) == False:
        sys.exit("Invalid input")


def check_extensions(link):
    # Validating url
    if "youtube" in link.lower():
        return True
    return False

if __name__ == "__main__":
    main()
