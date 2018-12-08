from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Location, Category, Image
from django.core.exceptions import ObjectDoesNotExist
import datetime as dt

# Create your views here.
# Create your views here.
def welcome(request):
 images = Image.objects.all()
 locations = Location.objects.all()
 title = 'Homepage'
 return render(request,'index.html')
  
def photos_today(request):
    date = dt.date.today()
    photos = Image.todays_photos()
    return render(request, 'all-photos/today-photos.html', {"date": date, "photos":photos})
def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day  
# View Function to present news from past days
def past_days_photos(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)

    return render(request, 'all-photos/past-photos.html', {"date": date})

def location(request,loc):

  locations = Location.objects.all()

  if Location.objects.get(pk=loc):
    images = Image.filter_by_location(loc)
    title = (Location.objects.get(pk=loc)).location

  else:
    raise Http404()

  return render(request,'location.html',{'title':title,'images':images, 'locations':locations})


def search_results(request):

  locations = Location()
  
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

    return render(request, 'all-photos/search.html',{'message':message ,'title':title, 'searched_images':searched_images,'locations':locations})

  else:
    message = 'You haven\'t searched for any location'
    
    title = 'Search Error'
    return render(request,'all-photos/search.html',{'message':message,'title':title,'locations':locations})

