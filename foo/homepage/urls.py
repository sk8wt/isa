from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import home

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
#     url(r'^homepage/', homepage.site.urls),
#     url(r'^$', views.index, name='homepage'),
	 path('homepage', home.hello_world, name='home'),	 
 ]
