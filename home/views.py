from django.shortcuts import render
from .models import Blogpost


# Create your views here.
def index(request):
    post = Blogpost.get_all_post()
    return render(request, "post.html", {'bpost': post})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def postdetail(request, id):
    a = Blogpost.objects.filter(post_id=id)
    return render(request, 'postdetails.html', {'xbpost':a})
