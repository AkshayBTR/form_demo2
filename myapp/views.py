from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from myapp import forms
from myapp.models import *
# Create your views here.

def form_demo1(request):
    if request.method=="POST":
        form=forms.Topic_Form(request.POST)#create a a form instance with data
        form.save()
    form=forms.Topic_Form()
    return render(request,"demo1.html",context={"form":form})

def form_demo2(request):
    if request.method=="POST":
        form=forms.Webpage_Form(request.POST)#create a a form instance with data
        #form.save()
        if form.is_valid():
            print(form.cleaned_data['botcacher'])
            t=Topic.objects.get(top_name=form.cleaned_data['top_name'])#will have a dictionary of data the you have filled
            w=Webpage.objects.get_or_create(top_name=t,name=form.cleaned_data['name'],url=form.cleaned_data['url'])[0]
            w.save()
    
    form=forms.Webpage_Form()
    return render(request,"demo1.html",context={"form":form})

def form_demo3(request):
    if request.method=="POST":
        form=forms.Access_Form(request.POST)#create a a form instance with data
        #form.save()
        # if form.is_valid():
        #     w=Webpage.objects.get(name=form.cleaned_data["name"])#will have a dictionary of data the you have filled
        #     a=Access_Details.objects.get_or_create(name=w,date=form.cleaned_data['date'])[0]
        #     a.save()

    form=forms.Access_Form()
    return render(request,"demo1.html",context={"form":form})

def topics(request):
   
    topics=Topic.objects.all()
    return render(request,"topic_data.html",context={"topics":topics})