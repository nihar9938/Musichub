from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .forms import *

def Home(request):
    data=Album.objects.all()
    data1=data[::-1]
    Dict={
        "albums":data1
    }
    return render(request,'index.html',Dict)

def MyAlbum(request,a_id):
        data1=Album.objects.get(id = a_id)
        songs=Song.objects.filter(album_id = a_id)
        Dict={
            "album":data1,"album_songs":songs
        }
        return render(request,'myalbum.html', Dict)


def Songlist(request):
    data=Song.objects.all()
    Dict={
        "songs":data
    }
    return render(request,'songs.html',Dict)

def add_album_unused(request):
    if not request.user.is_authenticated:
        return redirect('login','addalbum')
    if(request.method == "POST"):
        Dict=request.POST
        name=Dict['album_name']
        artist=Dict['album_artist']
        image=request.FILES['album_banner']
        obj=Album()
        obj.Name=name
        obj.Artist=artist
        obj.image=image
        obj.save()
        return redirect('addalbum')
    return render(request,'addalbum.html')

def add_album(request):
    if not request.user.is_authenticated:
        return redirect("login", "addalbum")

    form = Add_Album_Form()
    if request.method == "POST":
        form = Add_Album_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    Dict = {"form": form}
    return render(request, "addalbumnew.html", Dict)



def delete_album(request,a_id):
    data=Album.objects.get(id=a_id)
    data.delete()
    return redirect('home')

def edit_album(request, a_id):
    album = Album.objects.get(id = a_id)
    form = Add_Album_Form(request.POST or None, request.FILES or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect("home")
    Dict = {
        "form":form
    }
    return render(request, "addalbumnew.html", Dict)













def add_song(request):
    if (request.method == "POST"):
        Data=request.POST
        album_id=Data['album']
        song_name=Data['song_title']
        album=Album.objects.get(id = album_id)
        songfile=request.FILES['song_file']
        Song.objects.create(title=song_name,album_id=album,file=songfile)
        '''song=Song()
        song.title=song_name
        song.album_id=album
        song.file=songfile
        song.save()'''
        return redirect('myalbum',album_id)
    album_list=Album.objects.all()
    Dict={
        "albums":album_list
    }
    return render(request,'addsong.html',Dict)

def login_now(request,location):
    error=False
    lun=""
    if request.method=="POST":
        data=request.POST
        un=data['un']
        ps=data['ps']
        lun = un
        usr=authenticate(username=un, password=ps)
        if usr != None:
            login(request,usr)
            return redirect(location)
        error=True
    Dict={
        "error":error,"lun":lun,"location":location
    }
    return render(request,'login.html',Dict)


def Logout(request):
    logout(request)
    return redirect("home")


def Register(request):
    if request.method == "POST":
        data = request.POST
        un = data["un"]
        ps = data["ps"]
        name = data["name"]
        email = data["email"]
        usr = User.objects.create_user(un, email, ps)
        usr.first_name = name
        usr.save()
        return redirect("login")
    return render(request, "register.html")
