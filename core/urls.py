from django.urls import path
from .views import home_view, category_news_list, news_list, news_detail, privacy_policy


urlpatterns = [
    path('', home_view, name="home"),
    path('news-list/', news_list, name="news-list"),
    path('category-news-list/<slug>/', category_news_list, name="category-news-list"),
    path('news-detail/<slug:slug>/', news_detail, name="news-detail"),
    path('privacy-policy/', privacy_policy, name="privacy-policy"),
]

