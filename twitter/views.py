from django.shortcuts import render, get_object_or_404, redirect
from .models import Twit
from django.utils import timezone
from .forms import TwitForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    twits = Twit.objects.order_by('-create_date')
    context = {'twits': twits}
    return render(request, 'twitter/twits.html', context)

def detail(request, twit_id):
    thread = []
    thistwit = get_object_or_404(Twit, pk=twit_id)

    children = thistwit.get_all_children()
    for child in children:
        thread.append({'id': child.id, 'parent_id': child.parent_id, 'content': child.content, 'author': child.author.username, 'create_date': child.create_date})
    
    context = {'thread': thread, 'thistwit': thistwit}
    return render(request, 'twitter/twit_detail.html', context)


@login_required(login_url='common:login')
def twit_create(request):
    if request.method == "POST":
        form = TwitForm(request.POST)
        if form.is_valid():
            twit = form.save(commit=False)
            twit.author = request.user
            twit.create_date = timezone.now()
            twit.save()
            return redirect('twitter:index')
    else:
        form = TwitForm()

    return redirect('twitter:index', {'form': form})

@login_required(login_url='common:login')
def twit_delete(request, twit_id):
    twit = get_object_or_404(Twit, pk=twit_id)
    if request.user != twit.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('twit:detail', twit_id=twit.id)
    twit.delete()
    return redirect('twitter:index')
    