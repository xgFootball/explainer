import argparse
import sys
import json

from api import API

if __name__ == "__main__":

    """
    Example usage:
    python3 fetch.py /team/averages/1
    python3 fetch.py /team/averages/1 -j test.json
    python3 fetch.py /team/averages/1 -c test.csv
    """

    parser = argparse.ArgumentParser(
        description='Accepts a path, fetches path and outputs json to stdout if no outfile given or csv/json file if given'
    )

    parser.add_argument(
        'path',
        type=str,
        help='path to resource on xG api'
    )

    parser.add_argument(
        '-c', 
        '--csvfile', 
        nargs='?', 
        type=str, 
        help='output file, in csv format'
    )

    parser.add_argument(
        '-j', 
        '--jsonfile', 
        nargs='?', 
        type=str, 
        help='output file, in json format'
    )

    args = parser.parse_args()
    if not args.path:
        raise Exception("Must call with path to resource on xG api")
    else:
        res = API().plain_request(args.path)

        if args.jsonfile and args.csvfile:
            raise Exception("Cannot call with csvfile and jsonfile")
        elif args.jsonfile:
            with open(args.jsonfile, 'w') as f:
                json.dump(res, f)
        elif args.csvfile:
            import pandas as pd
            df = pd.DataFrame(res)
            df.to_csv(args.csvfile)
        else:
            print(json.dumps(res))

