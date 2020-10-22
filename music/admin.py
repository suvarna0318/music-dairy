from django.contrib import admin
from .models import UserPlaylist,Song,Artist,Profile

# Register your models here.
admin.site.register(UserPlaylist)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Profile)

