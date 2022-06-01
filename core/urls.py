from django.urls import path

from . import views

"""
Inicio home/
Historia about /
Servicio services/
Visitanos store/
Contacto contact/
Blog blog/
Sample sample/
"""

urlpatterns = [

    # Paths del core
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('sample/', views.sample, name='sample'),

]
