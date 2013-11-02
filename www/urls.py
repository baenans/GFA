from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'plantas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'www.views.index', name='index'),
    url(r'^login/$', 'www.views.loginView', name='loginView'),
    url(r'^logout/$', 'www.views.logoutView', name='logoutView'),

)
