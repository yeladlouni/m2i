import pandas as pd

dfs = pd.read_html('C:\\Users\\yelad\\OneDrive\\Bureau\\covid.html')

dfs[0].to_json('covid.json', lines=True, orient='records')