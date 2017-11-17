from django.contrib import admin
from django.conf.urls import url, include
from diamonddice.views import DiamondView, RollView, SaveView

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', DiamondView.as_view()),
    url(r'^roll/$', RollView.as_view()),
    url(r'^save/$', SaveView.as_view()),
]
