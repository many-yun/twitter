from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Twit
from django.utils import timezone
from .forms import TwitForm
from django.views.decorators.http import require_POST
from common.forms import UserForm, UserChangeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404

def index(request):
    page_query = 1
    twits = Twit.objects.order_by('-create_date')
    paginator = Paginator(twits, page_query * 10) # 트위터 10개씩
    page = request.GET.get('page', page_query) # 현재페이지 쿼리 파라미터

    try:
        page_obj = paginator.page(page)
    except (EmptyPage, PageNotAnInteger): # 초과된 페이지일 경우 데이터x
        print("트윗이 없습니다.")
        raise Http404("페이지가 존재하지 않습니다.")

    context = {'twits': page_obj}
    return render(request, 'twitter/main.html', context)

def detail(request, twit_id):
    thread = []
    thistwit = get_object_or_404(Twit, pk=twit_id)

    children = thistwit.get_all_children()
    for child in children:
        thread.append({'id': child.id, 'parent_id': child.parent_id, 'content': child.content, 'author': child.author.username, 'create_date': child.create_date, "pp": child.author.pp})

    context = {'thread': thread, 'thistwit': thistwit}
    return render(request, 'twitter/twit_detail.html', context)


@login_required(login_url='common:login')
@require_POST
def twit_create(request):
    form = TwitForm(request.POST)
    if form.is_valid():
        twit = form.save(commit=False)
        twit.author = request.user
        twit.create_date = timezone.now()
        twit.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found')) # post 후 현재 페이지에서 리다이렉트
    else:
        messages.error(request, form.errors)
        return redirect('twitter:index')

@login_required(login_url='common:login')
def twit_delete(request, twit_id):
    twit = get_object_or_404(Twit, pk=twit_id)
    if request.user != twit.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('twit:detail', twit_id=twit.id)
    twit.delete()
    return redirect('twitter:index')


@login_required(login_url='common:login')
def mypage(request, user_id):    
    if request.method =="POST" and request.user.id == user_id :
        form = UserChangeForm(request.POST, request.FILES, instance=request.user, )
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        form = UserChangeForm(instance=request.user)
    
    page_query = 1
    twits = Twit.objects.filter(author_id=user_id).order_by('-create_date')
    my_twit = twits.first
    paginator = Paginator(twits, page_query * 10) # 트위터 10개씩
    page = request.GET.get('page', page_query) # 현재페이지 쿼리 파라미터

    try:
        page_obj = paginator.page(page)
    except (EmptyPage, PageNotAnInteger): # 초과된 페이지일 경우 데이터x
        print("트윗이 없습니다.")
        raise Http404("페이지가 존재하지 않습니다.")

    context = {'form': form, 'twits': page_obj, "my_twit": my_twit }
    return render(request, 'twitter/my_twits.html', context)
