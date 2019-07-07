import requests
import json
import pandas as pd
import time
import statsmodels.api as sm
import numpy as np
import argparse

""" Example usage
    python3 prediction.py ./data.json ./prediction.json
"""

def is_win(x_score, y_score):
    return x_score > y_score

def is_draw(x_score, y_score):
    return x_score == y_score

def get_probabilities(x_pred, y_pred):
    trial_num = 10000
    x_poisson = np.random.poisson(x_pred, trial_num)
    y_poisson = np.random.poisson(y_pred, trial_num)

    x_win_count = 0
    draw_count = 0
    for x_score, y_score in zip(x_poisson, y_poisson):
        if is_win(x_score, y_score): x_win_count+=1
        if is_draw(x_score, y_score): draw_count+=1

    return (
        x_win_count/trial_num, 
        draw_count/trial_num, 
        (trial_num-x_win_count-draw_count)/trial_num
    )

def compute_model(df, dep, ind):

    dep_data = np.asarray(df.pop(dep))
    ind_data = np.asarray(sm.add_constant(df[ind]))

    poisson_model = sm.GLM(
        dep_data, 
        ind_data, 
        family=sm.families.Poisson()
    )
    return poisson_model.fit()

def get_matches_with_predicted_goals(df):
    self_merge = df.merge(df, on="matchid")

    dup_checker = []
    rows = []
    for i, k in self_merge.iterrows():
        if k['team_x'] != k['team_y'] and k['matchid'] not in dup_checker:
            dup_checker.append(k['matchid'])
            rows.append(dict(k))
    return pd.DataFrame(rows)

def get_matches_with_1x2_probabiliies(df):
    probability_buff = []
    for i, k in df.iterrows():
        t1Win, draw, t2Win = get_probabilities(
            float(k['predicted_goals_x']), 
            float(k['predicted_goals_y'])
        )
        temp = dict(k)
        temp['t1_win'] = t1Win
        temp['draw'] = draw
        temp['t2_win'] = t2Win
        probability_buff.append(temp)
    return pd.DataFrame(probability_buff)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Accepts the location of the json file, builds model, and outputs the predictions to file location passed in the second argument'
    )

    parser.add_argument(
        'data_location',
        type=str,
        help='Where to find data'
    )

    parser.add_argument(
        'output_location',
        type=str,
        help='Where to output predictions'
    )

    args = parser.parse_args()
    if not args.data_location or not args.output_location:
        raise Exception("Must call with data and output location")
    else:

        with open(args.data_location) as json_file:
            data = json.load(json_file)

        df = pd.DataFrame(data)

        features = ['totalpasses']
        poisson_model = compute_model(
            df,
            'goalsfor',
            ['totalpasses']
        )
        df['predicted_goals'] = poisson_model.predict()

        matches_with_predicted_goals = get_matches_with_predicted_goals(df)
        matches_with_probabilities = get_matches_with_1x2_probabiliies(matches_with_predicted_goals)
        matches_with_probabilities.to_json(args.output_location)
        
