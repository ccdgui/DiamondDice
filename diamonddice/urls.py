from django.conf.urls import url
from diamonddice.views import DiamondView, RollView, SaveView


urlpatterns = [
    url(r'^$', DiamondView.as_view()),
    url(r'^roll/$', RollView.as_view()),
    url(r'^save/$', SaveView.as_view()),
]
