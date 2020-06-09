"""MusicWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import *
from django.conf import settings
from django.conf.urls.static import static
#These Are the URL's
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('Myalbum/<int:a_id>/', MyAlbum, name='myalbum'),
    path('SongsList/', Songlist, name='songlist'),
    path('addalbum', add_album, name='addalbum'),
    path('addsong/', add_song, name='addsong'),
    path('login/<str:location>/', login_now, name='login'),
    path('register_now/', Register, name='register'),
    path('logout/', Logout, name='logout'),
    path('delete_album/<int:a_id>/', delete_album, name='delete'),
    path("edit_album/<int:a_id>/", edit_album, name="editalbum"),

    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
