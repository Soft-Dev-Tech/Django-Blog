from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticlePreview, CategoryListView, AuthoListView

app_name = "blog"
urlpatterns = [
    path('', ArticleListView.as_view(), name="home"),
    path('page/<int:page>', ArticleListView.as_view(), name="home"),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name="detail"),
    path('preview/<int:pk>', ArticlePreview.as_view(), name="preview"),
    path('category/<slug:slug>', CategoryListView.as_view(), name="category"),
    path('category/<slug:slug>/page/<int:page>', CategoryListView.as_view(), name="category"),
    path('author/<slug:username>', AuthoListView.as_view(), name="author"),
    path('author/<slug:username>/page/<int:page>', AuthoListView.as_view(), name="author"),
]
 