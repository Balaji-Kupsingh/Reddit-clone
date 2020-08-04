
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path


from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    path('', views.home, name="home"),
]
