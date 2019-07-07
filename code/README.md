
A set of scripts to:
* Fetch data from our API
* Build a dataset which can be used for prediction
* Predict results

    python3 rolling_averages_build.py ./data.json
    python3 prediction.py ./data.json ./prediction.json

However, there are more general purpose scripts here the fetch script can be used to fetch any path from our API and the to_csv will convert a pandas-valid json file to csv.

In addition, because there was some confusion last time, you do not need to be a member of our website to use our API. You will need to subscribe and login to access all of our data but we make a small subset of this data publicly available.

