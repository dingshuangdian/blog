"""blog URL Configuration

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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
import xadmin

from articles.views import IndexView, ArticlesListView, ArticleDetailView, JottingsListView, JottingsDetailView, \
    ContactView,SearchView,MsgView, GetComment

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('ueditor/', include('DjangoUeditor.urls')),
    re_path(r'articles/(?P<category>\d+)/$', ArticlesListView.as_view(), name='articleslist'),
    re_path(r'article/(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='articledetail'),
    re_path('jottings/$', JottingsListView.as_view(), name='jottinglist'),
    re_path('jotting/(?P<pk>\d+)/$', JottingsDetailView.as_view(), name='jottingdetail'),
    re_path('contact/$', ContactView.as_view(), name='contact'),
    re_path('search/$', SearchView.as_view(), name='search'),
    re_path('msg/$', MsgView.as_view(), name='msg'),
    re_path('get_comment/$', GetComment, name='get_comment'),
]

if settings.DEBUG:
    #  配置静态文件访问处理
    urlpatterns.append(url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}))
    urlpatterns.append(url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}))
