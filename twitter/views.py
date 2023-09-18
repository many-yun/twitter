from django.shortcuts import render, get_object_or_404, redirect
from .models import Twit
from django.utils import timezone
from .forms import TwitForm

def index(request):
    twits = Twit.objects.order_by('-create_date')
    context = {'twits': twits}
    return render(request, 'twitter/twits.html', context)

def detail(request, twit_id):
    twit = get_object_or_404(Twit, pk=twit_id)
    context = {'twit': twit}
    return render(request, 'twitter/twit_detail.html', context)

def twit_create(request):
    form = TwitForm(request.POST)
    
    if form.is_valid():
        twit = form.save(commit=False)
        twit.create_date = timezone.now()
        twit.save()
        return redirect('twitter:index')
    else:
        print(form.errors)
        return redirect('twitter:index')