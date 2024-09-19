from django.shortcuts import render
from . import util
from django import forms
import markdown2
import random

class NewPageForm(forms.Form):
    page = forms.CharField(label="")
    
def ConvertToHTML(title):
    page = util.get_entry(title)
    markdowner = markdown2.Markdown()
    if page == None:
        return None
    else:
        return markdowner.convert(page)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def ShowPage(request, title):
    content = ConvertToHTML(title)
    
    if content == None:
        return render(request, "encyclopedia/Error.html", {
            "errorMessage": "This page does not exist"
        }) 
    else:
        return render(request, "encyclopedia/ShowPage.html", {
            "title": title,
            "content": content
        })

def CreatePage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/addPage.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        exist = util.get_entry(title)
        if exist is not None:
            return render(request, "encyclopedia/Error.html", {
                "errorMessage": "This page already exists"
            }) 
        else:
            util.save_entry(title, content)
            convert = ConvertToHTML(title)
            return render(request, "encyclopedia/ShowPage.html", {
                "title": title,
                "content": convert 
            })
    
def search(request):
    if request.method == "POST":
        search = request.POST['q']
        content= ConvertToHTML(search)
        if content is not None:
            return render(request, "encyclopedia/ShowPage.html", {
                "title": search,
                "content": content
            })
        else:
            list = util.list_entries()
            similar = []
            i=False
            for item in list:
                if search.lower() in item.lower():
                    similar.append(item)
                    i=True
    if i == False:
        return render(request, "encyclopedia/NotFound.html", {
            "NFound": search
        })
    else:
        return render(request, "encyclopedia/SearchPage.html", {
                "similar": similar
        })
            

def edit(request):
    if request.method == 'POST':
        title = request.POST['pageTitle']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
def ConfirmEdit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        convert = ConvertToHTML(title)
        return render(request, "encyclopedia/ShowPage.html", {
            "title": title,
            "content": convert 
        })  

def RandomPage(request):
    randomPage = random.choice(util.list_entries())
    convert = ConvertToHTML(randomPage)
    return render(request, "encyclopedia/ShowPage.html",{
        "title": randomPage,
        "content": convert
    })