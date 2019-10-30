from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('tracker',views.tracker,name='tracker'),
    path('search',views.search,name='search'),
    path('prod_view/<int:myid>',views.productview,name='productview'),
    path('checkout',views.checkout,name='checkout'),
]
#in this <int:myid> is pass the value of product id and we handle
#this value on view page 