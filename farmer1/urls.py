from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
#create your url configurations here.
urlpatterns=[
    url(r'^$',views.homep,name="homep"),
    url(r'^produces/$',views.prod,name="prod"),
    url(r'^market/$',views.mkt,name="mkt"),
    url(r'^sell/$',views.sell,name="sell"),
    url(r'^help/$',views.help,name="help"),
    url(r'^(?P<slug>[\w+@,-]+)/$',views.detail,name="detail"),
    #url(r'^(?P<slug>[\w+@,-]+)/$',views.details,name="details"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
