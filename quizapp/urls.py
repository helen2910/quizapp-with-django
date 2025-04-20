from django.urls import path
from . import views

app_name = "quiz"

urlpatterns = [
    path('', views.index, name="index"),
    path('calculate_score/', views.calculate_score, name="calculate_score"),
    path('result_page/', views.result_page, name="result_page"),
    path('login_user/', views.login_user, name="login_user"),
]
