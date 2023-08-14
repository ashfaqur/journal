import argparse
import os
import time
from datetime import datetime
from pathlib import Path

from model.analysis import analyze
from model.day import Day
from model.month import Month

JOURNAL_FILE_EXTENSION = ".md"


def main(journal_directory):
    months = []
    for file in os.listdir(journal_directory):
        filename = os.fsdecode(file)
        if filename.endswith(JOURNAL_FILE_EXTENSION):
            file_stem = Path(filename).stem
            try:
                datetime_object = datetime.strptime(file_stem, '%Y %B')
            except:
                print(f'Skipping file "{file}" as not a journal')
                continue

            days = parsefile(os.path.join(journal_directory, file), datetime_object.year, datetime_object.month)
            month = Month(datetime_object, days)
            months.append(month)

    analyze(months)


def parsefile(file, year, month):
    days = []
    with open(file) as f:
        day = None
        for line in f:
            content = line.rstrip()
            if not content:
                continue
            if content[0] == "#":
                date = content.split('#')[1].strip()
                if date:
                    try:
                        date = datetime.strptime(date, '%d %B %Y')
                        day = Day(date)
                        days.append(day)
                        # print(f'date {day}')
                    except:
                        print(f'{date} is invalid')
                        date = None
                        continue
            else:
                if day:
                    day.add_content(content)
    return days


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Jounal analysis script')
    parser.add_argument('journal_dir', metavar='journal_dir',
                        type=str, help='journal directory')
    args = parser.parse_args()
    directory = args.journal_dir

    if not os.path.isdir(directory):
        print(f'Given journal path "{directory}" is not a directory')
        exit(1)
    start_time = time.time()
    main(directory)
    print(f"--- {round(time.time() - start_time, 2)} seconds ---")
