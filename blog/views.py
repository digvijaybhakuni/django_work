from django.http import HttpResponse
from django.shortcuts import render
from blog.forms import PostForm
from django.contrib.auth import hashers


def index(request):
    print("DIGGU >>>>>>>>>>>>>>>>>>>>>>>")
    if request.method == "GET":
        form_post = PostForm()
        return render(request, 'form.html', {'form': form_post.as_table()})
    elif request.method == "POST":
        form_post = PostForm(request.POST)
        form_post.save()
        return render(request, 'index.html', {})


def indexx(request):
    return render(request, 'index.html', {})


def test_admin(request):

    return render(request, 'adminBlog.html',  {})


def post(request, post_id):
    return HttpResponse("You're looking at post id : %s." % post_id)


def author_post(request, author_id):
    response = "You're looking at the results of author %s."
    return HttpResponse(response % author_id)


def like(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def indexHapp(request):
    return render(request, 'happ/base.html')


def add_listing_happ(request):
    return render(request, 'happ/sample_form.html')


def search_listing_happ(request):
    return render(request, 'happ/sample_search.html')


def view_listing_happ(request):
    return render(request, 'happ/sample_search.html', {'cl_view': 'view_only'})
