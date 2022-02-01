import pandas as pd
class anime_recommendations:

    def Get_anime_UID(self,name):
        data = pd.read_csv('https://raw.githubusercontent.com/DibyaSadhukhan/Anime_recommender_data/main/Data/animes_cleaned.csv')
        uid=data.loc[data['title']==name]['uid'].values[0]
        del data
        return uid
    def get_anime_recommendations(self,name):
        #get 10 recommendations for the searched anime.
        data = pd.read_csv('https://raw.githubusercontent.com/DibyaSadhukhan/Anime_recommender_data/main/Data/recommendations.csv')
        rec=data.loc[data['uid']==self.Get_anime_UID(name)]
        rec=rec.values[0]
        del data
        return rec  
    def Get_recommendations_details(self,name):
        details=[]
        data=pd.read_csv('https://raw.githubusercontent.com/DibyaSadhukhan/Anime_recommender_data/main/Data/animes_details_cleaned.csv')
        rec=self.get_anime_recommendations(name)
        for i in rec[1:]:
            detail=data.loc[data['uid'] == i]
            details.append(dict(detail.iloc[0]))
        del data
        del rec
        return details
