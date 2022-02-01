import pandas as pd
class anime_details:
    def Get_anime_UID(name):
        data = pd.read_csv('https://raw.githubusercontent.com/DibyaSadhukhan/Anime_recommender_data/main/Data/animes_cleaned.csv')
        uid=data.loc[data['title']==name]['uid'].values[0]
        return uid
    def Get_anime_details(self,uid):
        #takes the uid of the animes and returns the 
        pass
    def get_anime_recommendations(self,uid):
        #get 10 recommendations for the searched anime.
        pass