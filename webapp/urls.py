from django.conf.urls import url, include
from rest_framework import routers
from . import views


routes = routers.DefaultRouter()
routes.register(r'employees', views.EmployeeCrudApi)
routes.register(r'profiles', views.ProfileApiViewSet)

# urlpatterns = routes.urls

urlpatterns = [
    url(r'^v1/', include(routes.urls)),
    url(r'^auth/', views.login),
    url(r'^register/', views.register),
    #url(r'^profile/', views.ProfileApi.as_view()),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileApi.as_view()),
]

# urlpatterns = [
# #url(r'^employees/', views.EmployeeAPI.as_view())
# #    url(r'^employess/$', views.EmployeeCrudApi.as_view())
#     url(r'^v1/$', routes.urls)
# ]