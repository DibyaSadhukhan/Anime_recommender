#importing required packages
from Anime_recommendations import anime_recommendations
from flask import Flask,Response,render_template,request
import json
from wtforms import Form,StringField
import urllib.request 


app = Flask(__name__, template_folder="Templates")
app.config['SECRET_KEY']='Anime_recommender_2022_upvamp_secret_Code'

class SearchForm(Form):
    autocomp = StringField('Anime Name', id='anime_autocomplete',render_kw={"placeholder": "Please type in the name of the anime you have last seen"})
 
 
@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    link="https://raw.githubusercontent.com/DibyaSadhukhan/Anime_recommender_data/main/Data/titles.txt"
    response = urllib.request.urlopen(link)
    Text = response.read()
    Text = Text.decode("utf-8")
    Text=Text.split('||')
    return Response(json.dumps(Text), mimetype='application/json')
 

@app.route('/', methods =['POST', 'GET'])
def home():
        form = SearchForm(request.form)
        return render_template('Home.html',form=form)
@app.route('/recommend', methods =['POST'])
def recommend():
    form =SearchForm(request.form)
    name=form.autocomp.data
    #print(name)
    if name !=None:
        ob=anime_recommendations()
        details=ob.Get_recommendations_details(name)
        message="table"
    else:
        details={}
        message="error"
    #return render_template('index.html',form=form)
    return render_template('Recommend.html',form=form,data=details,message=message)
@app.route('/features.txt', methods=['GET'])
def features():
    return '<object data="./features.txt" width="100vw" height="100vh">Not supported</object>'
if __name__ == '__main__':
    app.run(debug = True)