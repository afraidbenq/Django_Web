from django.urls import path
from . import views

app_name = 'Test_platform'
urlpatterns = [
    # ex: /Test_platform/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /Test_platform/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /Test_platform/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /Test_platform/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
