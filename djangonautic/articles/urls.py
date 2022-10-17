from django.urls import path, re_path
from djangonautic import views
from articles import views

urlpatterns = [
    path(r'', views.article_list),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail),
]

