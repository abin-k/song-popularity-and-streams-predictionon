# **SONG POPULARITY AND STREAMS PREDICTION** 
**An end-to-end machine learning project which is deployed using django**
![music-industry-flowchart](https://user-images.githubusercontent.com/116078614/227845575-8fe44b24-416e-46a0-8c48-a9b04387d9bf.jpg)

## RELEVANCE

The music industry is a significant contributor to the global economy, generating billions of dollars in revenue and creating employment opportunities 
for millions of people. The annual revenue of the global recorded music industry is over **$26.2 billion** as of 2022. The U.S. is the top music market in 2022, 
followed by Japan, the U.K., and Germany. The growth of digital streaming platforms has transformed the way we consume music and created new revenue streams for 
the industry. There are approximately **1.8 million** musical artists in the United States alone. However, the complexity is that the number of musical artists is 
always changing and growing. 

The recording industry is highly competitive and is dominated by three big production companies which make up nearly 82% of the total annual album sales.
Unfortunately, the success of an artist's release is highly uncertain: a single may be extremely popular, resulting in widespread radio play and digital downloads, 
while another single may turn out quite unpopular, and therefore unprofitable.

As the industry is growing the competition in the industry becomes more complex. So inorder to survive and become sucess in this new enviornment artists 
and Record companies should effectively utilize new technics to analyze the past data and predict the future

## 1.SONG POPULARITY PREDICTION
By analyzing the features of songs, the model is able to predict the percentage of chance for the song to be a hit or popular. By predicting the chances of a 
song to be a hit before the song is released, the artist can improve the features, that can affect the popularity of the song. Predicting the popularity of the song
after its release can also help in targeting on the right songs for marketing. Spending the capital at right songs helps in increasing the profit at minimum cost. 
Two different models are created for both released and non-released songs

models :  GradientBoostingRegressor with 80% accuracy is used to predict the popularity of released songs,
RandomForestRegressor with 70% accuracy is used to predict the popularity of non-released songs

The model used to predict the popularity of released songs is more accurate becouse the prediction is based on analyzing more features 

![Screenshot (42)](https://user-images.githubusercontent.com/116078614/227997795-1e278d36-a8fe-4fb5-8864-3fb62863a9a9.png)


## 2.SONG STREAMS PREDICTION
Digital streams have revolutionized the way music is shared, discovered, and monetized, creating new opportunities for artists and stakeholders in the music industry.
It have also led to the emergence of new genres and artists, who can now reach global audiences without the support of a major label. As a result, digital streams 
have become a crucial metric for measuring an artist's success and shaping the industry's marketing and investment strategies in the modern music landscape.High stream
counts can boost an artist's profile, attract more attention from industry professionals, and lead to more lucrative opportunities, such as sponsorships and brand partnerships.So having better streams is important.

By analyzing the features, the model is able to predict the number of streams that the artist can get for a song at spotify. RandomForestRegressor with approximately  80% accuracy is used for the prediction


![Screenshot (46)](https://user-images.githubusercontent.com/116078614/227925498-bf740abd-92d6-4d6a-9565-d3b7c8e2f0eb.png)

## 3.Deployment of model
The model is deployed using django web framework as an website
![Screenshot (29)](https://user-images.githubusercontent.com/116078614/227999766-796d602f-cdc1-4ee5-8182-0c002722ac02.png)

## DATASET USED
The dataset include all the songs that have been on the Top 200 Weekly (Global charts of Spotify in 2020 & 2021)

The dataset include the following features:

**Highest Charting Position:** The highest position that the song has been on in the Spotify Top 200 Weekly Global Charts in 2020 & 2021. **Number of Times Charted:** The number of times that the song has been on in the Spotify Top 200 Weekly Global Charts in 2020 & 2021. **Week of Highest Charting:** The week when the song had the Highest Position in the Spotify Top 200 Weekly Global Charts in 2020 & 2021. **Song Name:** Name of the song that has been on in the Spotify Top 200 Weekly Global Charts in 2020 & 2021. **Song iD:** The song ID provided by Spotify (unique to each song). **Streams:** Approximate number of streams the song has. **Artist:** The main artist/ artists involved in making the song. **Artist Followers:** The number of followers the main artist has on Spotify. **Genre:** The genres the song belongs to. **Release Date:** The initial date that the song was released. **Weeks Charted:** The weeks that the song has been on in the Spotify Top 200 Weekly Global Charts in 2020 & 2021. **Popularity:** The popularity of the track. The value will be between 0 and 100, with 100 being the most popular. **Danceability:** Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable. **Acousticness:** A measure from 0.0 to 1.0 of whether the track is acoustic. **Energy:** Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. **Instrumentalness:** Predicts whether a track contains no vocals. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. **Liveness:** Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. **Loudness:** The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track. Values typical range between -60 and 0 db. **Speechiness:** Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. **Tempo:** The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration. **Valence:** A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry). **Chord:** The main chord of the song instrumental.

