from django.contrib.auth.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^abc/$', views.abc, name='abc'),
    url(r'^rejestr-zolnierzy', views.rejestr_zolnierzy, name='rejestr-zolnierzy'),
    url(r'^rekrutacja/$', views.rekrutacja, name='rekrutacja'),
    url(r'^majordom-koronny/$', views.majordom_koronny, name='majordom-koronny'),
    url(r'^krolewska-obrona-terytorialna/$', views.obrona_terytorialna, name='obrona-terytorialna'),
    url(r'^zakon-rycerzy-krola-edwarda/$', views.zakon, name='zakon'),
    url(r'^krolewskie-sily-operacyjne/$', views.sily_operacyjne, name='sily-operacyjne'),
    url(r'^gwardia-krolewska/$', views.gwardia, name='gwardia'),
]
