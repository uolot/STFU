from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

import gdata.youtube
import gdata.youtube.service



def home(request):
    return render(request, 'base.html')


def get_auth_sub_url():
    next = 'http://localhost:8000/test2/'
    scope = 'http://gdata.youtube.com'
    secure = False
    session = True

    yt_service = gdata.youtube.service.YouTubeService()
    return yt_service.GenerateAuthSubURL(next, scope, secure, session)

def test(request):
    auth_sub_url = get_auth_sub_url()
    return redirect(str(auth_sub_url))

def test2(request):
    token = request.GET.get('token', None)
    return HttpResponse('token: %s' % token)
