from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('api/', include('api.urls')),
]
