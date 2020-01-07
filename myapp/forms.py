from django import forms
from myapp.models import *

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
    
class Webpage_Form(forms.Form):
    top_name=forms.ChoiceField(choices=get_topics(),label="Topic Name",required=True)
    name=forms.CharField(max_length=30,min_length=2,label="Webpage Name",required=True)
    url=forms.URLField(required=True,label="Webpage URL")

class Access_Form(forms.Form):
    name=forms.ChoiceField(choices=get_webpages(),label="Webpage Name",required=True)
    date=forms.DateField(required=True)


