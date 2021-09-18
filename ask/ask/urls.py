"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from qa import views

# urlpatterns = [
#     path('', views.test, name='test'),
#     path('login/', views.test, name='login'),
#     path('signup/', views.test, name='signup'),
#     path('question/<int:id>/', views.test, name='question'),
#     path('ask/', views.test, name='ask'),
#     path('popular/', views.test, name='popular'),
#     path('new/', views.test, name='new'),
# ]

urlpatterns = [
    url(r'^$', views.home),
    url('admin/', admin.site.urls),
    url(r'^login/$', views.test, name='login'),
    url(r'^signup/$', views.test, name='signup'),
    url(r'^question/(?P<id>[0-9]+)/$', views.question, name='question'),
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^new/$', views.test, name='new'),
]
