import os
import zipfile
from io import BytesIO
import pandas as pd
import requests
import urllib
import pickle
import seaborn as sns
import matplotlib.pyplot as plt


if not os.path.exists('elections.pic'):

    urls = ['https://storage.googleapis.com/kaggle-data-sets/935914/1632066/compressed/hashtag_donaldtrump.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20201119%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20201119T093253Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=2e25694c40b3cebeb489e9a9d85ad8dc6c842fc902628e57a85455da3328b392eea6e0e78899118bbd71e33efb7485f5f75cd2ddb2c5f017bc6b3ac21e814f74ee8f41406c9bc28a566b36d6c052c4aa7bd76ac460699fd783423e0fc2a2a94cfbfd904385ca7edfed08fd84bb1bf841df2d4573d19489ee176ca5eedafe43759e7465c36e123b4ea7c60a7fb6f8c643394f7f09870200b82d72783d00fef5a05874f5986061dcdd09adae0125185f3258661dfec874b471b6eb8c7d30628ce9fc1b7cfe78784ff82ddb84726e303b56b64197ad782eec7e302152395d9bb7fbd889ddea89058c2ff700a1af90c59db6fb746c12e1f004650ffa355c8b36b782',
            'https://storage.googleapis.com/kaggle-data-sets/935914/1632066/compressed/hashtag_joebiden.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20201119%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20201119T095752Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=3735a9e873ee7beeedffaca63074a5e5ff9412f9661db8e716a0c4c2ea9af245adc4ca857a305ce4670fbf3f98ba2fecdf56a194d94db6a973def4207d963a8161514066c17ac51ed7cba77094138cd1f669985b312e35346b79a218c673b01d083d68594bd706e869a2aae9648d37196204a280c125db6ad550ce92f21ba1b8929a7aea565136381eeff6d5ca65fefaedde8d498c3204f3fed320715a3c2687151b63b2a93a5d8dfa5dd51f69dc634e27d29efdfd47c338b0213c199d9727459475e72bfc8c04603a492570932b9498443f3081cba41c0384ca8e00a03a411d7ab630ec72f8cf43d356109c30d8ab3fd20c22abd90848e2c968236806594047']

    if not os.path.exists('./hashtag_donaldtrump.csv') or not os.path.exists('./hashtag_joebiden.csv'):  # Pour ne pas télécharger à chaque fois les fichiers zip
        for url in urls: # On fait le parcours de la liste des URLs pour les fichiers à télécharger
            r = urllib.request.urlopen(url) # On ouvre un stream/flux du fichier zip

            with zipfile.ZipFile(BytesIO(r.read())) as f: # En utilisant le package zipfile, on peut créer les fichiers zip à partir du stream
                # BytesIO est un stream d'octets qui représente le fichier zip
                f.extractall()  # On extrait le fichier à l'intérieur du zip

    df_trump = pd.read_csv('./hashtag_donaldtrump.csv', lineterminator='\n')
    df_trump['candidate'] = 'trump'
    print(df_trump.shape)

    df_biden = pd.read_csv('./hashtag_joebiden.csv', lineterminator='\n')
    df_biden['candidate'] = 'biden'
    print(df_biden.shape)

    df = df_trump.append(df_biden)

    print(df.shape)

    df.drop_duplicates(subset=['tweet_id', 'candidate'], inplace=True)  # Supprimer les doublons

    print(df.shape)
    df.fillna(0, inplace=True)  # Imputation des valeurs manquantes

    # Conversion de données
    for col in ["created_at", "user_join_date", "collected_at"]:
        df[col] = pd.to_datetime(df[col]).astype('datetime64[us]')
    for col in ["tweet_id", "likes", "retweet_count", "user_id", "user_followers_count"]:
        df[col] = df[col].astype(int)

    with open('elections.pic', 'wb') as f:
        pickle.dump(df, f)

with open('elections.pic', 'rb') as f:
    df = pickle.load(f)
    print(df.shape)
    sns.scatterplot(data=df, x='created_at', y='likes', hue='candidate', size='retweet_count')

    plt.show()