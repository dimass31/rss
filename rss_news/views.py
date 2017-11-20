from django.http import HttpResponse
from django.shortcuts import render
from rss_news.models import Post
from django.http import HttpResponseRedirect


def index(request):

    posts = reversed(Post.objects.all())

    context = {
        'posts': posts
    }
    return render(request, "index.html", context)

def post(request, index):

    try:
        post = Post.objects.get(id=index)
        previous_id = post.id - 1
        next_id = post.id + 1
        context = {
            'posts': post,
            'previous_id': previous_id,
            'next_id': next_id,
            'max_id': len(Post.objects.all()),
        }
        return render(request, "post.html", context)
    except:
        return render(request, "error_page.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def signup_user(request):

    #if request.POST:
        #user_name = request.Post["user_name"]
        #password = request.Post["password"]
        #repeat_password = request.Post["repeat_password"]
        #email = request.Post["email"]
        #print(user_name)

    return HttpResponseRedirect("/")

def login_user(request):
    return HttpResponseRedirect("/")