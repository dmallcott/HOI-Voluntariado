from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', 'django.contrib.auth.views.login', {'redirect_field_name':'home'}, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'login'}, name='logout'),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
