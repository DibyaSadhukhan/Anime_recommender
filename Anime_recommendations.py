import pandas as pd
import random
class anime_recommendations:

    def Get_anime_UID(self,name):
        data = pd.read_csv('https://raw.githubusercontent.com/DibyaSadhukhan/Anime_recommender_data/main/Data/animes_cleaned.csv')
        uid=data.loc[data['title']==name]['uid'].values[0]
        del data
        return uid
    def get_anime_recommendations(self,name):
        #get 10 recommendations for the searched anime.
        data = pd.read_csv('https://raw.githubusercontent.com/DibyaSadhukhan/Anime_recommender_data/main/Data/recommendations.csv')
        data=data.rename(columns = {'0':'uid'})
        rec=data.loc[data['uid']==self.Get_anime_UID(name)]
        rec=rec.values[0]
        del data
        return rec  
    def Get_recommendations_details(self,name,start=1,end=13):
        details=[]
        data=pd.read_csv('https://raw.githubusercontent.com/DibyaSadhukhan/Anime_recommender_data/main/Data/animes_details_cleaned.csv')
        rec=self.get_anime_recommendations(name)
        detail=data.loc[data.uid.isin(rec[start:end])]
        for i in range(len(detail)):
            details.append(dict(detail.iloc[i]))
        del data
        del rec
        del detail
        return details
    def Get_Random_details(self):
        details=[]
        data=pd.read_csv('https://raw.githubusercontent.com/DibyaSadhukhan/Anime_recommender_data/main/Data/animes_Home_page.csv')
        detail=data.loc[data.index.isin(random.sample(range(random.randint(0,10000),15110),8))]
        for i in range(len(detail)):
            details.append(dict(detail.iloc[i]))
        del data
        del detail
        return details