import flask
import pandas as pd
from sklearn.preprocessing import MaxAbsScaler
from sklearn.neighbors import NearestNeighbors
app = flask.Flask(__name__, template_folder="Templates")
df = pd.read_csv('/home/dibyasadhukhan/Anime_recommender/Data/anime.csv')
all_titles=[df['name'][i] for i in range(len(df['name']))]
top_anime=(df.sort_values(by=[ 'members','rating'], ascending= False))
top_anime = top_anime[['name', 'genre','type','rating']]
top_anime= top_anime.head(10)
top_anime.index = list(range(1,11))

Anime_final = pd.read_csv('/home/dibyasadhukhan/Anime_recommender/Data/Anime_final.csv')
#since the values of rating episodes and members are comparitively large we need to scale the dataset
scaled = MaxAbsScaler()
Anime_final = scaled.fit_transform(Anime_final)
recommendations = NearestNeighbors(n_neighbors=11, algorithm='ball_tree').fit(Anime_final)
recommendations.kneighbors(Anime_final)
anime_indices = recommendations.kneighbors(Anime_final)[1]

def recommendation(anime):


    names=[]
    genre=[]
    rating=[]
    index=df[(df.name).str.lower() == anime.lower()].index.tolist()[0]
    for i in anime_indices[index][1:]:
            names.append(df.iloc[i]['name'])
            genre.append(df.iloc[i]['genre'])
            rating.append(df.iloc[i]['rating'])
    Data=list(zip(names,genre,rating))
    return pd.DataFrame(Data, columns=['Name','Genre','Rating'], index=['1','2','3','4','5','6','7','8','9','10'])

@app.route('/')
def home():
    return flask.render_template('index.html',recommendations_table = top_anime.to_html())

@app.route('/recommend',methods=['POST'])
def recommend():
    if flask.request.method == 'POST':
        a_name=flask.request.form['input']
        if a_name not in all_titles:
            return (flask.render_template('Error.html',Anime_name=a_name))
        else:
            result_final=recommendation(a_name)
            return flask.render_template('Recommendations.html',recommendations_table = result_final.to_html(),Anime_name=a_name)
@app.route('/Contactus')
def Contactus():
     return flask.render_template('Test.html')

if __name__=='__main__':
    app.run(host="0.0.0.0", port='5000', debug=True)
