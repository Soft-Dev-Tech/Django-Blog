from django.contrib.auth import views
from . views import (
                        ArticleListView,
                        ArticleCreateView,
                        ArticleUpdateView,
                        ArticleDeleteView,
                        ProfileView,
                    )
from django.urls import path

app_name = "account"
urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("article/create", ArticleCreateView.as_view(), name="article-create"),
    path("article/update/<int:pk>", ArticleUpdateView.as_view(), name="article-update"),
    path("article/delete/<int:pk>", ArticleDeleteView.as_view(), name="article-delete"),
    path("profile/", ProfileView.as_view(), name = "profile"),
]
