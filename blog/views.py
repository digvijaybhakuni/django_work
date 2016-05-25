from django.http import HttpResponse
from django.shortcuts import render
from blog.forms import PostForm


def index(request):
    print("DIGGU >>>>>>>>>>>>>>>>>>>>>>>")
    if request.method == "GET":
        form_post = PostForm()
        return render(request, 'form.html', {'form': form_post.as_ul()})
    elif request.method == "POST":
        form_post = PostForm(request.POST)
        form_post.save()
        return render(request, 'index.html', {})

def indexx(request):
    return render(request, 'index.html', {})

def post(request, post_id):
    return HttpResponse("You're looking at post id : %s." % post_id)

def author_post(request, author_id):
    response = "You're looking at the results of author %s."
    return HttpResponse(response % author_id)

def like(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
