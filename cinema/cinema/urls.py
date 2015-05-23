#from django.conf.urls import url, include, patterns
from django.conf.urls import url, include
#from django.conf.urls.static import static
from django.contrib import admin
#from django.conf import settings
from website import urls as website_urls

#urlpatterns = patterns(
#   'website.views', url(r'^$', 'index'), url(r'^movies/$', 'movies'),
#    url(r'^proj/$', 'projections'), url(r'^reserv/$', 'reservations'),
#    url(r'^show-projection/$', 'show_projection'),
#    url(r'^admin/', include(admin.site.urls)),
#    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
urlpatterns = [
    url(r'^admin/$', include(admin.site.urls)),
    url(r'', include(website_urls))
]
