from django.shortcuts import render, redirect, HttpResponse
import random
from time import gmtime, strftime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def process_money(request):
    if request.method == 'POST':
        activities = []
        if 'gold' not in request.session:
            request.session['gold'] = 0
        else:
            if request.POST['building'] == 'Farm':
                random_num = random.randint(10,20)
                request.session['gold'] += random_num
                activities.append('Earned {} gold from the farm! ({})'.format(random_num, strftime("%Y-%m-%d %H-%M %P", gmtime())))
            if request.POST['building'] == 'Cave':
                random_num = random.randint(5,10)
                request.session['gold'] += random_num
                activities.append('Earned {} gold from the cave! ({})'.format(random_num, strftime("%Y-%m-%d %H-%M %P", gmtime())))
            if request.POST['building'] == 'House':
                random_num = random.randint(2,5)
                request.session['gold'] += random_num
                activities.append('Earned {} gold from the house! ({})'.format(random_num, strftime("%Y-%m-%d %H-%M %P", gmtime())))
            if request.POST['building'] == 'Casino':
                random_num = random.randint(-50,50)
                request.session['gold'] += random_num
                activities.append('Earned {} gold from the casino! ({})'.format(random_num, strftime("%Y-%m-%d %H-%M %P", gmtime())))
        if 'activities' not in request.session:
            request.session['activities'] = []
        else:
                request.session['activities'] += activities
    return redirect('/')
