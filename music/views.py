
from django.shortcuts import render,redirect
from .models import Song,Artist,UserPlaylist
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
	return render(request,'music/base.html')

# Create your views here.
def register(request):
	print("working")
	if request.method=='POST':
		u_form=RegisterForm(request.POST)
		if u_form.is_valid():
			u_form.save()
			return render(request,'music/base.html')
	else:
		u_form=RegisterForm()
	context={
	'form':u_form,
	}
	return render(request,'music/register.html',context)

def song_list(request):
	vol=request.GET.get('volume')
	print(vol)
	all_song=Song.objects.all()
	context={
	'songs':all_song,
	'song':all_song[0],
	}
	return render(request,'music/all_song.html',context)

def song_list_with_id(request,id):
	print("id:",id)
	all_song=Song.objects.all()
	song=Song.objects.get(id=id)
	context={
	'songs':all_song,
	'song':song,
	'vol':80,
	}
	return render(request,'music/all_song.html',context)

def volume(request,var):
	some_data = request.GET['myVariableToSend']
	print(some_data)
	return redirect('login')

def details(request,pk):
	song=Song.objects.get(id=pk)
	context={
	'song':song,
	}
	
	return render(request,'music/details.html',context)
def search(request):
	print("searinhg")
	query=request.GET.get('q')
	q_list=query.split(" ")
	print(q_list)
	ignore_list=['by','and','song','songs']
	for i in ignore_list:
		if i in q_list:
			q_list.remove(i)

	print(q_list)

	query=str(" ".join(q_list))
	print(query)
	search_res=Song.objects.search(query)
	print('search',search_res)
	context={
	'songs':search_res,
	}
	
	return render(request,'music/search.html',context)


def prev_song(request,pk):
	v=request.GET.get('value')
	print(v)
	songs=Song.objects.all()
	if pk==9:
		pk=9
	else:
		pk=pk-1
	
	song=Song.objects.get(id=pk)
	context={
	'songs':songs,
	'song':song,
	'vol':80,
	}
	
	return render(request,'music/all_song.html',context)
def next_song(request,pk):
	v=request.GET.get('value')
	print(v)
	vol=request.POST.get('vol')
	print(vol)
	songs=Song.objects.all()
	pk=pk+1
	song=Song.objects.get(id=pk)
	context={
	'songs':songs,
	'song':song,
	'vol':80,
	}
	
	return render(request,'music/all_song.html',context)


def album(request):
	# all_song=Song.objects.all()
	# context={
	# 'songs':all_song,
	# }
	return render(request,'music/album.html')

def artist(request):
	artists=Artist.objects.all()
	context={
	'artists':artists,
	}
	return render(request,'music/right_click_menu.html')
@login_required(login_url='/login/')
def playlist_new(request):
	if request.method=='POST':
		
		title=request.POST.get('playlist_name')
		print(title)

		if title!="":
			print("context:",title)
			obj=UserPlaylist.objects.create(playlist_name=title,user=request.user)
			obj.save()
			print("show created playlist")
			return redirect('playlist_display')
		else:
			obj=UserPlaylist.objects.create(playlist_name='NewPlaylist',user=request.user)
			obj.save()
			print("show created playlist")
			return redirect('playlist_display')

	return render(request,'music/playlist_new.html')

@login_required(login_url='/login/')
def playlist_display(request):
	objects=UserPlaylist.objects.filter(user=request.user)
	# print(request.user)
	context={
	'objects':objects,
	}
	return render(request,'music/playlist_display.html',context)
@login_required(login_url='/login/')
def playlist_songs(request,id):

	obj=UserPlaylist.objects.get(pk=id)
	objects=obj.song.all()
	print(objects)
	context={
	'objects':objects,
	}
	return render(request,'music/playlist_songs.html',context)


