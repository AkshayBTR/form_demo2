from django.shortcuts import render
from myapp import forms
from myapp.models import *
# Create your views here.

def form_demo1(request):
    if request.method=="POST":
        form=forms.Topic_Form(request.POST)#create a a form instance with data
        if form.is_valid():
            print(form.cleaned_data["top_name"])#will have a dictionary of data the you have filled
            t=Topic.objects.get_or_create(top_name=form.cleaned_data["top_name"])[0]
            t.save()
    form=forms.Topic_Form()
    return render(request,"demo1.html",context={"form":form})

def form_demo2(request):
    form=forms.Webpage_Form()
    if request.method=="POST":
        form=forms.Webpage_Form(request.POST)#create a a form instance with data
        if form.is_valid():
            print(form.cleaned_data)#will have a dictionary of data the you have filled
    
    return render(request,"demo1.html",context={"form":form})

def form_demo3(request):
    form=forms.Access_Form()
    if request.method=="POST":
        form=forms.Access_Form(request.POST)#create a a form instance with data
        if form.is_valid():
            print(form.cleaned_data)#will have a dictionary of data the you have filled
    
    return render(request,"demo1.html",context={"form":form})