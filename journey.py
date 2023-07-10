import argparse
import os
from pathlib import Path
from datetime import datetime

def main(directory):
    for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".md"):
         filestem =  Path(filename).stem
         try:
            datetime_object = datetime.strptime(filestem,'%Y %B')
         except:
            continue

         print(datetime_object)



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