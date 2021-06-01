from django.urls import path

from .import views

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    # ex: /workouts/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /workouts/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /workouts/healthcheck
    path('healthcheck/', views.health, name='health')
]
