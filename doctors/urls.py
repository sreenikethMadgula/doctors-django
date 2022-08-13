from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search_doctors',views.search_doctors, name="search-doctors"),
    path('search_results',views.search_results,name="search-results"),
    # path('doctor_profile',views.doctor_profile, name="doctor-profile"),
    path('doctor_profile/<int:id>',views.doctor_profile, name="doctor-profile"),
    path('category_doctors/<str:category>',views.category_doctors, name="category-doctors"),
]
