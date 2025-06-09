from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    template = loader.get_template('all_members.html')
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template("main.html")
    context = {}
    return HttpResponse(template.render(context, request))

def test(request):
    template = loader.get_template("test.html")
    mydata = Member.objects.filter(first_name='Chad').values()
    # Context is on Json format
    context = {
        'fruits' : ['apple', 'banana', 'cherry'],
        'mymembers_list': mydata,
    }
    return HttpResponse(template.render(context, request))

def template(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("template.html")
    context = {
        "first_name": 'John',
        "mymembers": mymembers,
        'greeting': 1,
    }
    return HttpResponse(template.render(context, request))