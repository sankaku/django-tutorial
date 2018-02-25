from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_by_render/', views.index_by_render, name='index_by_render'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
