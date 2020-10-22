from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import Q


class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.user.name

GENER_CHOICES=(
	('Rock','Rock'),
	('pop','pop'),
	('hip hop','hip,hop'),
	('country','country'),
	('classical','classcical'),

	)
LANG_CHOICES=(
	('kannada','kannada'),
	('hindi','hindi'),
	('english','english'),
	('tamil','tamil')
	)

class Artist(models.Model):
	name=models.CharField(max_length=200)
	image=models.ImageField(upload_to="images")

	def __str__(self):
		return self.name
class SongManager(models.Manager):
	def search(self, query):
		lookups=(Q(title__icontains=query)|Q(artists__name__icontains=query)|Q(lang__icontains=query)|Q(genre__icontains=query))              
		return self.model.objects.filter(lookups)


class Song(models.Model):
    title = models.CharField(max_length=200, verbose_name="Song name")
    cover_img = models.ImageField(upload_to="song_cover_img", blank=False)
    song = models.FileField(upload_to='song_directory_path')
    genre = models.CharField(max_length=100,choices=GENER_CHOICES)
    artists = models.ForeignKey(Artist,on_delete=models.CASCADE)
    lang=models.CharField(max_length=200,choices=LANG_CHOICES)

    objects=SongManager()
    def __str__(self):
    	return self.title

class UserPlaylist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	playlist_name=models.CharField(max_length=120)
	song=models.ManyToManyField(Song)


	def __str__(self):
		return self.playlist_name