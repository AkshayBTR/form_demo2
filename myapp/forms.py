from django import forms
from myapp.models import *
from django.core import validators

def get_topics():
    topic_options=[]
    data=Topic.objects.all()
    for i in data:
        topic_options.append((i,i.top_name))
    return topic_options
def get_webpages():
    webpage_options=[]
    data=Webpage.objects.all()
    for i in data:
        webpage_options.append((i,i.name))
    return webpage_options
class Topic_Form(forms.Form):
    top_name=forms.CharField(min_length=5,max_length=20,label="Topic Name",required=True)
    
def check_for_name(name):
    if not name.startswith('a'):
        raise forms.ValidationError("not starting with a")
    return name
class Webpage_Form(forms.Form):
    top_name=forms.ChoiceField(choices=get_topics(),label="Topic Name",required=True)
    name=forms.CharField(max_length=30,min_length=2,label="Webpage Name",required=True,validators=[check_for_name,])
    url=forms.CharField(required=True,label="Webpage URL")
    botcacher=forms.CharField(required=False,validators=[validators.MaxLengthValidator(0)])

class Access_Form(forms.Form):
    name=forms.ChoiceField(choices=get_webpages(),label="Webpage Name",required=True)
    date=forms.DateField(required=True,help_text="<br>*enter date in yyyy-mm-dd")

# class Topic_Form(forms.ModelForm):
#     class Meta:
#         model=Topic
#         fields=['top_name',]

# class Webpage_Form(forms.ModelForm):
#     class Meta:
#         model=Webpage
#         exclude=[]#name is an attribute in webpage model

# class Access_Form(forms.ModelForm):
#     class Meta:
#         model=Access_Details
#         fields='__all__'#name is an attribute in webpage model