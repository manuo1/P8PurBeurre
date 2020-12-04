from django.urls import path

from app_products import views

urlpatterns = [
    path('', views.index, name='indexPage'),
    path('results/', views.results, name='resultsPage'),
]
