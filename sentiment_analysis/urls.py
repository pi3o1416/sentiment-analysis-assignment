
from django.urls import path
from .views import TextSentimentAnalysis


app_name='sentiment_analysis'
urlpatterns = [
    path('roberta/', TextSentimentAnalysis.as_view(), name='roberta-model')
]
