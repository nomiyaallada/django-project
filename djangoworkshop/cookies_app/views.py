from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_cookie(request):
    response=HttpResponse("Cookie set!")
    response.set_cookie('username','Nomiya')

    return response

def get_cookie(request):
    username=request.COOKIES.get('username','Guest')
    return HttpResponse(f"Hello,{username}!")