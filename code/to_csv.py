import argparse
import json
import pandas as pd

""" Example Usage
    
    python3 to_csv.py ./source.json ./output.csv
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Accepts the location of a json file, converts to csv, and outputs to file'
    )

    parser.add_argument(
        'json_location',
        type=str,
        help='Where to find json'
    )

    parser.add_argument(
        'csv_location',
        type=str,
        help='Output location'
    )

    args = parser.parse_args()
    if not args.json_location or not args.csv_location:
        raise Exception("Must call with input json and csv output location")
    else:

        with open(args.json_location) as json_file:
            data = json.load(json_file)

        df = pd.DataFrame(data)
        df.to_csv(args.csv_location)




