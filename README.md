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
after its release can also help in targeting on the right songs for marketing. Spending the capital at righ songs helps in increasing the profit at minimum cost. 
Two different models are created for both released and non-released songs


models :  GradientBoostingRegressor with 80% accuracy is used to predict the popularity of released songs,
RandomForestRegressor with 70% accuracy is used to predict the popularity of non-released songs

The model used to predict the popularity of released songs is more accurate becouse the prediction is based on analyzing more features 


![Screenshot (47)](https://user-images.githubusercontent.com/116078614/227913264-58b4e889-4ebf-4d19-a96e-fe6a5d6439af.png)


## 2.SONG STREAMS PREDICTION
Digital streams have revolutionized the way music is shared, discovered, and monetized, creating new opportunities for artists and stakeholders in the music industry.
It have also led to the emergence of new genres and artists, who can now reach global audiences without the support of a major label. As a result, digital streams 
have become a crucial metric for measuring an artist's success and shaping the industry's marketing and investment strategies in the modern music landscape.High stream
counts can boost an artist's profile, attract more attention from industry professionals, and lead to more lucrative opportunities, such as sponsorships and brand partnerships.
So having more is important.

By analyzing the features, the model is able to predict the number of streams that the artist can get for a song at spotify. RandomForestRegressor with approximately  80% 
accuracy is used for the prediction


![Screenshot (46)](https://user-images.githubusercontent.com/116078614/227925498-bf740abd-92d6-4d6a-9565-d3b7c8e2f0eb.png)
