"""jobRoller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from jobView import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('about/', views.about, name='about'), 
    path('futures/', views.futures, name='futures'),
    path('search/', views.search, name='search'),
    path('search/<int:id>/', views.course_detail_view, name='detail'),
    path('kw_search/<int:id>', views.kw_detail_view, name='kw_detail'),
    #path('soup/', views.get_name, name='soup'),
    path('soupify/', views.soupify, name='soupify'),
    path('courses/', views.KeywordListView.as_view(), name='kw_list'),
    path('kw_search/', views.kw_search, name='kw_search')
]
