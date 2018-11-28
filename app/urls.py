from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.creating_view, name='create'),
    path('link/<short_code>/', views.showing, name='show'),
    path('<short_code>/', views.go_to, name='goto')
]
