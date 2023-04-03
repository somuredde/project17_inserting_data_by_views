from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_topic(request):
    tn=input('enter a topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse("insert successfully")

def insert_webpage(request):
    tn=input ('enter a topic name')
    name=input('enter a name')
    url=input('enter a url')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    WO=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    WO.save()
    return HttpResponse('webpage inserted successfully')

def insert_access(request):
    tn=input('enter a topic name')
    name=input('enter a name')
    url=input('enter a url')
    au=input('enter a author name')
    d=input('enter a date')
    TO1=Topic.objects.get_or_create(topic_name=tn)[0]
    TO1.save()
    WO1=Webpage.objects.get_or_create(topic_name=TO1,name=name,url=url)[0]
    WO1.save()
    AO=AccessRecord.objects.get_or_create(name=WO1,author=au,data=d)[0]
    AO.save()
    return HttpResponse('Accessrecord inserted successfully')