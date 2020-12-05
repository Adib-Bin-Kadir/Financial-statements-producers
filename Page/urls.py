from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('income_statement/<str:id>/', views.income_statement),
    path('balance_sheet/<str:id>/', views.balance_sheet),
    path('trial_balance/<str:id>/', views.trial_balance),
    path('income_statement_form/<str:id>/', views.income_statement_form),
    path('balance_sheet_form/<str:id>/', views.balance_sheet_form),
    path('trial_balance_form/<str:id>/', views.trial_balance_form),
    path('clear_all/',views.clear_all)
]
