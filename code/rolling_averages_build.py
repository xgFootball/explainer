import pandas as pd
import argparse

from api import API

""" Example Usage:

    python3 rolling_averages_build.py ./data.json

    Explanation:

    We want to predicting the number of goals scored in the next match
from the average of total passes in the last ten matches.
    This isn't supposed to be an effective model, this is supposed to be
an example of how to build a model.
    This stage just collects the necessary data.

    The column starttime in the rolling averages is shifted so that the rolling average
for the last five matches has the same starttime value as the next match in the series.
    Our rolling averages data is only computed for the team's main leagues (so it won't
compute the date incorrectly for Champions League teams, for example).
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Accepts a file location, fetches data and outputs json to that location'
    )

    parser.add_argument(
        'location',
        type=str,
        help='Where to save json output'
    )

    args = parser.parse_args()
    if not args.location:
        raise Exception("Must call with file location")
    else:
        matches = API().plain_request('/season/teamstats/357')
        rolling_averages = API().plain_request('/season/averagesrolling/357')

        df_matches = pd.DataFrame(matches)
        df_rolling = pd.DataFrame(rolling_averages)

        extract = ['team','starttime','matchid','goalsfor','goalsagainst']
        df_matches_goals = df_matches[extract]

        model_features = ['team', 'starttime', 'totalpasses']
        df_rolling_features = df_rolling[model_features]

        df_rolling_features_with_scores = df_rolling_features.merge(
                df_matches_goals, 
                on=['team','starttime']
        )

        df_rolling_features_with_scores.to_json(args.location)

