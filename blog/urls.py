from django.conf.urls import url
from . import views as blogview

urlpatterns = [
    url(r'^$', blogview.index, name='index'),
    url(r'^bo$', blogview.indexx, name='indexx'),
    url(r'^adminTest$', blogview.test_admin, name='test_admin'),
    url(r'^happ/index$', blogview.indexHapp, name="index_happ"),
    url(r'^happ/form$', blogview.add_listing_happ, name="form_happ"),
    url(r'^happ/search$', blogview.search_listing_happ, name="search_happ"),
    url(r'^happ/view$', blogview.view_listing_happ, name="view_happ"),
]