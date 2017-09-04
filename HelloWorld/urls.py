"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import view_hello,view_handledb,view_search1,view_search2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test-hello$', view_hello.hello),
    url(r'^test-hello/3$', view_hello.hello),
    url(r'^test-db$', view_handledb.testdb),
    url(r'^search-form$', view_search1.search_form),
    url(r'^search$', view_search1.search),
    url(r'^search-post$', view_search2.search_post),
]
