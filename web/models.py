from django.db import models

class Album(models.Model):
    Name=models.CharField(max_length=50)
    Artist=models.CharField(max_length=50)
    image=models.ImageField(null=True)
    def __str__(self):
        return self.Name

class Song(models.Model):
    title=models.CharField(max_length=50)
    #album_id=models.IntegerField(null=True)
    album_id=models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
    file=models.FileField(null=True)

    def __str__(self):
        return self.title