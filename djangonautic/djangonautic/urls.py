from django.contrib import admin
from django.contrib import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'about/$',)
]
