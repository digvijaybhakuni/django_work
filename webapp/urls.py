from django.conf.urls import url
from . import views

urlpatterns = [
#url(r'^employees/', views.EmployeeAPI.as_view())
url(r'^employees/$', views.EmployeeCrudApi.as_view())
]