from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('store', views.store, name="store"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('contact', views.contact, name="contact"),
    path('promotions', views.promotions, name="promotions")
]
        
