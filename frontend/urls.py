from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('doctors', views.index),
    path('specialization', views.index),
    path('doctors/<int:id>', views.index)
    # path(r'.*', views.index)
]
