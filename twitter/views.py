from django.shortcuts import render, get_object_or_404, redirect
from .models import Twit
from django.utils import timezone

def index(request):
    twits = Twit.objects.order_by('-create_date')
    context = {'twits': twits}
    return render(request, 'twitter/twits.html', context)

def detail(request, twit_id):
    twit = get_object_or_404(Twit, pk=twit_id)
    context = {'twit': twit}
    return render(request, 'twitter/twit_detail.html', context)

def twit_create(request, twit_id, parent):
    twit = get_object_or_404(Twit, pk=twit_id)
    if parent == None:
        twit.twit_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('twitter:detail', twit_id=twit.id)