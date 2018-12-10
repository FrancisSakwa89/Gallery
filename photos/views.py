from django.shortcuts import render, redirect

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Location, Category, Image
from django.core.exceptions import ObjectDoesNotExist
from .forms import PhotosLetterForm
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email

# Create your views here.

#for displaying homepage
@login_required(login_url='/accounts/login/')
def welcome(request):
  images = Image.objects.all()
  locations = Location.objects.all()
  title = 'Home'
  if request.method == 'POST':
        form = PhotosLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = PhotosLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('welcome')
  else:
        form = PhotosLetterForm()
  return render(request, 'index.html', {'images':images,'title':title,'locations':locations, 'letterForm':form})


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

    return render(request, 'search.html',{'message':message ,'title':title, 'searched_images':searched_images,'locations':locations})

  else:
    message = 'You din\'t searched for any category'
    
    title = 'Not found'
    return render(request,'search.html',{'message':message,'title':title,'locations':locations})


#for displaying images by location
def location(request,location):

  locations = Location.objects.all()

  if Location.objects.get(pk=location):
    images = Image.filter_by_location(location)
    title = (Location.objects.get(pk=location)).location

  else:
    raise Http404()

  return render(request,'location.html',{'title':title,'images':images, 'locations':locations})

def past_days_photos(request,past_date):
    try:

        #Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    
    except ValueError:
        #Raise 404  error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_today)
    
    photos = images.days_photos(date)

    return render(request, 'all-photos/past-photos.html', {"date":date,"photos":photos})
    
def photos_today(request):
    date = dt.date.today()
    photos = Image.todays_photos()
    return render(request, 'all-photos/today-photos.html', {"date": date, "photos":photos})

# def logout(request):
# #   images = Image.objects.all()
# #   locations = Location.objects.all()
# #   title = 'Home'

#   return render(request, 'index.html')

# def login(request):
# #   images = Image.objects.all()
# #   locations = Location.objects.all()
# #   title = 'Home'

#   return render(request, 'login.html')
