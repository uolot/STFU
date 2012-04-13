from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'test/$', 'playlists.views.test', name='test'),
    url(r'test2/$', 'playlists.views.test2', name='test2'),
    url(r'$', 'playlists.views.home', name='home'),
)
