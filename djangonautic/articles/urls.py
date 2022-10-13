from django.urls import path
from djangonautic import views
from articles import views

urlpatterns = [
    path(r'', views.article_list),
]
