from django.shortcuts import render, redirect

from django.http import HttpResponse, Http404
from .models import Location, Category, Image
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

#for displaying homepage
def welcome(request):
  images = Image.objects.all()
  locations = Location.objects.all()
  title = 'Home'

  return render(request, 'index.html', {'images':images,'title':title,'locations':locations})


#for displaying search results
def search_results(request):

  locations = Location.objects.all()
  
  if 'image' in request.GET and request.GET['image']:
    search_term = request.GET.get('image')
    message = f'{search_term}'
    title = 'Search Results'

    try:
      no_ws = search_term.strip()
      id = Category.objects.get(category__icontains = no_ws)
      searched_images = Image.search_image(id)

    except ObjectDoesNotExist:
      searched_images = []

    return render(request, 'search.html',{'message':message ,'title':title, 'searched_images':Image.search_image(id),'locations':locations})

  else:
    message = 'You din\'t searched for any location'
    
    title = 'Search Error'
    return render(request,'search.html',{'message':message,'title':title,'locations':locations})


#for displaying images by location
def location(request,loc):

  locations = Location.objects.all()

  if Location.objects.get(pk=loc):
    images = Image.filter_by_location(loc)
    title = (Location.objects.get(pk=loc)).location

  else:
    raise Http404()

  return render(request,'location.html',{'title':title,'images':images, 'locations':locations})

