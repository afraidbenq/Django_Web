from django.urls import path
from . import views

urlpatterns = [
    # ex: /Test_platform/
    path('', views.index, name='index'),
    # ex: /Test_platform/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /Test_platform/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /Test_platform/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
