from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello, home
from books import views

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^publishers/$', views.PublisherList.as_view()),
]

