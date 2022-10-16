from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'articles/', include('articles.urls')),
    path(r'about/', views.about),
    path(r'', views.homepage),
]
urlpatterns += staticfiles_urlpatterns()