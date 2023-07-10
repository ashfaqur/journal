import argparse
import os
from datetime import datetime
from pathlib import Path


def main(journal_directory):
    for file in os.listdir(journal_directory):
        filename = os.fsdecode(file)
        if filename.endswith(".md"):
            file_stem = Path(filename).stem
            try:
                datetime_object = datetime.strptime(file_stem, '%Y %B')
            except:
                print(f'Skipping file "{file}" as not a journal')
                continue

            parsefile(os.path.join(journal_directory, file), datetime_object.year, datetime_object.month)


def parsefile(file, year, month):
    with open(file) as f:
        for line in f:
            content = line.rstrip()
            if not content:
                continue
            if content[0] == "#":
                date = content.split('#')[1].strip()
                if date:
                    try:
                        date = datetime.strptime(date, '%d %B %Y')
                    except:
                        print(f'{date} is invalid')
                        date = None
                        continue
            else:
                print(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Jounal analysis script')
    parser.add_argument('journal_dir', metavar='journal_dir',
                        type=str, help='journal directory')
    args = parser.parse_args()
    directory = args.journal_dir

    if not os.path.isdir(directory):
        print(f'Given journal path "{directory}" is not a directory')
        exit(1)

    main(directory)
