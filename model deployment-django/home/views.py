from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import songpopularity
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor



# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):

    data = pd.read_csv('D:\#PUMUKAM\DS\data\spotify_dataset.csv')
    
    data['Artist Followers']=pd.to_numeric(data['Artist Followers'],errors='coerce')
    data['Popularity']=pd.to_numeric(data['Popularity'],errors='coerce')
    data['Danceability']=pd.to_numeric(data['Danceability'],errors='coerce')
    data['Energy']=pd.to_numeric(data['Energy'],errors='coerce')
    data['Loudness']=pd.to_numeric(data['Loudness'],errors='coerce')
    data['Speechiness']=pd.to_numeric(data['Speechiness'],errors='coerce')
    data['Acousticness']=pd.to_numeric(data['Acousticness'],errors='coerce')
    data['Liveness']=pd.to_numeric(data['Liveness'],errors='coerce')
    data['Tempo']=pd.to_numeric(data['Tempo'],errors='coerce')
    data['Duration (ms)']=pd.to_numeric(data['Duration (ms)'],errors='coerce')
    data['Valence']=pd.to_numeric(data['Valence'],errors='coerce')
   
    data = data.drop(['Index','Week of Highest Charting','Weeks Charted','Song Name','Streams','Song ID','Weeks Charted'],axis=1)

    data=data.dropna()

    data['Release Date']=pd.to_datetime(data['Release Date'],infer_datetime_format=True,errors='coerce')
    data['month']=data['Release Date'].dt.month
    data=data.drop('Release Date',axis=1)


    le_Genre =LabelEncoder()
    data['Genre'] =le_Genre.fit_transform(data['Genre'])  

    data =data.drop(['Chord','Artist','Danceability','Speechiness','Liveness','Tempo'],axis=1)

    x=data.drop('Popularity',axis=1)
    y=data['Popularity']

    
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=33)

    scaler =MinMaxScaler()
    x_train=scaler.fit_transform(x_train)
    x_test=scaler.transform(x_test)

    GRDBOOST=GradientBoostingRegressor()
    GRDBOOST_model=GRDBOOST.fit(x_train,y_train)

    if request.method=='POST':
        var1= float(request.POST['n1'])
        var2= float(request.POST['n2'])
        var3= float(request.POST['n3'])
        var4= str(request.POST['n4'])
        var6= float(request.POST['n6'])
        var7= float(request.POST['n7'])
        var9= float(request.POST['n9'])
        var11= float(request.POST['n11'])
        var12= float(request.POST['n12'])
        var13= float(request.POST['n13'])
        #var4=le_Genre.transform([var4])


        # print(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13)
        gener=le_Genre.transform([var4])
        values=scaler.transform([[var1,var2,var3,gener[0],var6,var7,var9,var12,var13,var11]])
        popularity=GRDBOOST_model.predict(values)[0]
        
    # pred= XGBR.predict(np.array([var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13]))
    # pred=round(pred[0])

    # popularity= "the popularity of the song is "+str(pred)

        return render(request,'about.html',{'result':popularity})


def contact(request):
    return render(request,'contact.html')
    
def popularity(request):
    return render(request,'popularity.html')

def rec_page(request):
    return render(request,'recommendation.html')

def recommendation(request):
    data = pd.read_csv('D:\#PUMUKAM\DS\data\spotify_dataset.csv')

    data['Artist Followers']=pd.to_numeric(data['Artist Followers'],errors='coerce')
    data['Popularity']=pd.to_numeric(data['Popularity'],errors='coerce')
    data['Danceability']=pd.to_numeric(data['Danceability'],errors='coerce')
    data['Energy']=pd.to_numeric(data['Energy'],errors='coerce')
    data['Loudness']=pd.to_numeric(data['Loudness'],errors='coerce')
    data['Speechiness']=pd.to_numeric(data['Speechiness'],errors='coerce')
    data['Acousticness']=pd.to_numeric(data['Acousticness'],errors='coerce')
    data['Liveness']=pd.to_numeric(data['Liveness'],errors='coerce')
    data['Tempo']=pd.to_numeric(data['Tempo'],errors='coerce')
    data['Duration (ms)']=pd.to_numeric(data['Duration (ms)'],errors='coerce')
    data['Valence']=pd.to_numeric(data['Valence'],errors='coerce')
    data['Streams']=pd.to_numeric(data['Streams'],errors='coerce')

    data['Release Date']=pd.to_datetime(data['Release Date'],infer_datetime_format=True,errors='coerce')
    data['month']=data['Release Date'].dt.month

    Song_Name=pd.DataFrame(data['Song Name'])

    data=data.drop(['Streams','Song Name','Index','Song ID','Weeks Charted','Week of Highest Charting','Weeks Charted','Release Date'],axis=1)

    data=data.dropna()

    le_Artist=LabelEncoder()
    le_Genre =LabelEncoder()
    le_Chord =LabelEncoder()
    # le_Song  =LabelEncoder()

    data['Artist'] =le_Artist.fit_transform(data['Artist'])
    data['Genre'] =le_Genre.fit_transform(data['Genre'])  
    data['Chord'] =le_Chord.fit_transform(data['Chord'])
    # data['Song Name'] =le_Song.fit_transform(data['Song Name'])

    scaler =MinMaxScaler()
    # scaler_song=MinMaxScaler()
    data['Highest Charting Position'] =scaler.fit_transform(data[['Highest Charting Position']])
    data['Number of Times Charted'] =scaler.fit_transform(data[['Number of Times Charted']])
    # data['Song Name'] =scaler_song.fit_transform(data[['Song Name']])
    data['Artist'] =scaler.fit_transform(data[['Artist']])
    data['Genre'] =scaler.fit_transform(data[['Genre']])
    data['Popularity'] =scaler.fit_transform(data[['Popularity']])
    data['Danceability'] =scaler.fit_transform(data[['Danceability']])
    data['Energy'] =scaler.fit_transform(data[['Energy']])
    data['Loudness'] =scaler.fit_transform(data[['Loudness']])
    data['Speechiness'] =scaler.fit_transform(data[['Speechiness']])
    data['Acousticness'] =scaler.fit_transform(data[['Acousticness']])
    data['Liveness'] =scaler.fit_transform(data[['Liveness']])
    data['Tempo'] =scaler.fit_transform(data[['Tempo']])
    data['Duration (ms)'] =scaler.fit_transform(data[['Duration (ms)']])
    data['Valence'] =scaler.fit_transform(data[['Valence']])
    data['Chord'] =scaler.fit_transform(data[['Chord']])
    data['month'] =scaler.fit_transform(data[['month']])

    km_model =KMeans(n_clusters=50)
    prediction =km_model.fit_predict(data)
    
    data['clusters']=prediction
    data['Song Name']=Song_Name


    if request.method=='POST':
        var22=str(request.POST['song'])

        column=data[data['Song Name']==var22]
        cl_data=column['clusters']
        cl_list=list(cl_data)
        cl_number=cl_list[0]
        cl_data=data[data['clusters']==cl_number]
        cl_data2=pd.DataFrame(cl_data['Song Name'])
        final=list(cl_data2['Song Name'])



        # le=le_Song.transform([var22])
        # song=scaler_song.transform([le])
        # column=data[data['Song Name']==song[0][0]]
        # cluster_no=column['clusters']
        # cluster_num=list(cluster_no)
        # c=cluster_num[0]
        # song_cluster=data[data['clusters']==c]
        # song_id=pd.DataFrame(song_cluster['Song Name'])
        # scaleback=scaler_song.inverse_transform(song_id) 
        # scaleback=scaleback.astype(int)
        # finel=list(le_Song.inverse_transform(scaleback))

        # Songname=le_Song.transform([var22])
        # songgroup=Songname
        # print(songgroup)

    return render(request,'recommendation.html',{'song':final})

def nonremix_page(request):
    return render(request,'nonremixed.html')

def result_page(request):
    data = pd.read_csv('D:\#PUMUKAM\DS\data\spotify_dataset.csv')
    
    data['Artist Followers']=pd.to_numeric(data['Artist Followers'],errors='coerce')
    data['Popularity']=pd.to_numeric(data['Popularity'],errors='coerce')
    data['Danceability']=pd.to_numeric(data['Danceability'],errors='coerce')
    data['Energy']=pd.to_numeric(data['Energy'],errors='coerce')
    data['Loudness']=pd.to_numeric(data['Loudness'],errors='coerce')
    data['Speechiness']=pd.to_numeric(data['Speechiness'],errors='coerce')
    data['Acousticness']=pd.to_numeric(data['Acousticness'],errors='coerce')
    data['Liveness']=pd.to_numeric(data['Liveness'],errors='coerce')
    data['Tempo']=pd.to_numeric(data['Tempo'],errors='coerce')
    data['Duration (ms)']=pd.to_numeric(data['Duration (ms)'],errors='coerce')
    data['Valence']=pd.to_numeric(data['Valence'],errors='coerce')

    data = data.drop(['Index','Highest Charting Position','Number of Times Charted','Week of Highest Charting','Weeks Charted','Song Name','Streams','Song ID'],axis=1)

    data=data.dropna()

    data['Release Date']=pd.to_datetime(data['Release Date'],infer_datetime_format=True,errors='coerce')
    data['month']=data['Release Date'].dt.month
    data=data.drop('Release Date',axis=1)

    data=data.drop(['Artist','Danceability','Speechiness','Liveness','Tempo','Valence','Chord'],axis=1)

    le_Genre =LabelEncoder()
    data['Genre'] =le_Genre.fit_transform(data['Genre'])  

    x=data.drop('Popularity',axis=1)
    y=data['Popularity']
    

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=33)

    scaler =MinMaxScaler()
    x_train=scaler.fit_transform(x_train)
    x_test=scaler.transform(x_test)

    RF=RandomForestRegressor()
    RF_model=RF.fit(x_train,y_train)

    if request.method=='POST':
        var3= float(request.POST['n3'])
        var4= str(request.POST['n4'])
        var6= float(request.POST['n6'])
        var7= float(request.POST['n7'])
        var9= float(request.POST['n9'])
        var12= float(request.POST['n12'])
        var10= float(request.POST['n10'])
        #var4=le_Genre.transform([var4])


        # print(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13)
        gener=le_Genre.transform([var4])
        values=scaler.transform([[var3,gener[0],var6,var7,var9,var12,var10]])
        popularity=RF_model.predict(values)[0]
    return render(request,'secondresult.html',{'result2':popularity})

def streams_page(request):
    return render(request,'streams.html')

def streamsresult_page(request):
    data = pd.read_csv('D:\#PUMUKAM\DS\data\spotify_dataset.csv')
    
    data['Artist Followers']=pd.to_numeric(data['Artist Followers'],errors='coerce')
    data['Popularity']=pd.to_numeric(data['Popularity'],errors='coerce')
    data['Danceability']=pd.to_numeric(data['Danceability'],errors='coerce')
    data['Energy']=pd.to_numeric(data['Energy'],errors='coerce')
    data['Loudness']=pd.to_numeric(data['Loudness'],errors='coerce')
    data['Speechiness']=pd.to_numeric(data['Speechiness'],errors='coerce')
    data['Acousticness']=pd.to_numeric(data['Acousticness'],errors='coerce')
    data['Liveness']=pd.to_numeric(data['Liveness'],errors='coerce')
    data['Tempo']=pd.to_numeric(data['Tempo'],errors='coerce')
    data['Duration (ms)']=pd.to_numeric(data['Duration (ms)'],errors='coerce')
    data['Valence']=pd.to_numeric(data['Valence'],errors='coerce')
    
    data = data.drop(['Index','Song Name','Song ID','Week of Highest Charting','Weeks Charted'],axis=1)

    data=data.dropna()

    data['Streams']=pd.to_numeric(data['Streams'].str.replace(",", ""))


    data['Release Date']=pd.to_datetime(data['Release Date'],infer_datetime_format=True,errors='coerce')
    data['month']=data['Release Date'].dt.month
    data=data.drop('Release Date',axis=1)


    le_Genre =LabelEncoder()
    data['Genre'] =le_Genre.fit_transform(data['Genre'])  

    data =data.drop(['Artist','Genre','Duration (ms)','month','Energy','Chord','Loudness','Acousticness','Valence','Liveness'],axis=1)

    x=data.drop('Streams',axis=1)
    y=data['Streams']

        
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=33)

    scaler =MinMaxScaler()
    x_train=scaler.fit_transform(x_train)
    x_test=scaler.transform(x_test)

    RandomForest=RandomForestRegressor( n_estimators=8,random_state=10,)
    RF_model=RandomForest.fit(x_train,y_train)

    if request.method=='POST':
        var1= float(request.POST['n1'])
        var2= float(request.POST['n2'])
        var3= float(request.POST['n3'])
        var4= str(request.POST['n4'])
        var5= float(request.POST['n5'])
        var8= float(request.POST['n8'])
        var11= float(request.POST['n11'])
            #var4=le_Genre.transform([var4])


            # print(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13)
        values=scaler.transform([[var1,var2,var3,var4,var5,var8,var11]])
        streams=RF_model.predict(values)[0]
        streams=round(streams)
    
    return render(request,'streams_result.html',{'result3':streams})





# def predict(request):
#     model = pd.read_pickle('reg_pickle.pickle')


#     Highest_Charting_Position= request.GET['HighestChartingPosition']
#     Number_of_Times_Charted= request.GET['NumberofTimesCharted']
#     Artist_Followers= request.GET['ArtistFollowers']
#     Genre = request.GET['Genre']
#     Danceability = request.GET['Danceability']
#     Energy = request.GET['Energy']
#     Loudness = request.GET['Loudness']
#     Valence = request.GET['Valence']
#     Duration = request.GET['Duration(ms)']
#     Tempo = request.GET['Tempo']
#     Liveness = request.GET['Liveness']
#     Acousticness = request.GET['Acousticness']
#     Speechiness = request.GET['Speechiness']

    
#     list =[ ]
#     list.append(Highest_Charting_Position) 
#     list.append(Number_of_Times_Charted)  
#     list.append(Artist_Followers)        
#     list.append(Genre)        
#     list.append(Danceability)        
#     list.append(Energy)        
#     list.append(Loudness)        
#     list.append(Speechiness)        
#     list.append(Acousticness)        
#     list.append(Liveness)        
#     list.append(Tempo)        
#     list.append(Duration)        
#     list.append(Valence)        

#     print(list)

    

#     songpopularity.objects.create(
#     Highest_Charting_Position= Highest_Charting_Position,
#     Number_of_Times_Charted=Number_of_Times_Charted,
#     Artist_Followers= Artist_Followers,
#     Genre = Genre,
#     Danceability = Danceability,
#     Energy = Energy,
#     Loudness = Loudness,
#     Valence = Valence,
#     Duration = Duration,
#     Tempo = Tempo,
#     Liveness = Liveness,
#     Acousticness = Acousticness, 
#     Speechiness = Speechiness,
#     )

#     classification = model.predict([list])
#     return render(request,'about.html',{'classification_result':classification})
#      #labelencoding

#      #scaling


# def db_record(request):
#     songpopularity = songpopularity.objects.all()
#     context = {
#         'songpopularity_records': songpopularity
#     }
#     return render(request, 'database.htal', context)
