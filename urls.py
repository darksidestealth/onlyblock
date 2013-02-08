from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {
        "template": "homepage.html",
    }, name="home"),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^about/", include("about.urls")),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^openid/", include(PinaxConsumer().urls)),
    url(r"^profiles/", include("idios.urls")),
    #url(r"^notices/", include("notification.urls")),
    url(r"^announcements/", include("announcements.urls")),
	url(r'^weblog/', include('zinnia.urls')),
	url(r'^comments/', include('django.contrib.comments.urls')),
	url(r'^', include('zinnia.urls.capabilities')),
	url(r'^search/', include('zinnia.urls.search')),
	url(r'^sitemap/', include('zinnia.urls.sitemap')),
	url(r'^trackback/', include('zinnia.urls.trackback')),
	url(r'^blog/tags/', include('zinnia.urls.tags')),
	url(r'^blog/feeds/', include('zinnia.urls.feeds')),
	url(r'^blog/authors/', include('zinnia.urls.authors')),
	url(r'^blog/categories/', include('zinnia.urls.categories')),
	url(r'^blog/comments/', include('zinnia.urls.comments')),
	url(r'^blog/', include('zinnia.urls.entries')),
	url(r'^blog/', include('zinnia.urls.archives')),
	url(r'^blog/', include('zinnia.urls.shortlink')),
	url(r'^blog/', include('zinnia.urls.quick_entry')),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
