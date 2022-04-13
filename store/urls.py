from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('products', views.products, name="products"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('contact', views.contact, name="contact"),
    path('promotions', views.promotions, name="promotions")
]
        
