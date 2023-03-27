from django.urls import path, include
from home import views
urlpatterns = [
    path('',views.index),
    path('about',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('popularity/',views.popularity,name="popularity"),
    path('recommendation/',views.recommendation,name="recommendation"),
    path('rec_page/',views.rec_page,name='rec_page'),
    path('nonremix_page/',views.nonremix_page,name='nonremix_page'),
    path('result_page/',views.result_page,name='result_page'),
    path('streams_page/',views.streams_page,name='streams_page'),
    path('streamsresult_page/',views.streamsresult_page,name='streamsresult_page')
]