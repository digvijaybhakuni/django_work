from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^bo$', 'blog.views.indexx', name='indexx'),
]