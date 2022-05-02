from django.urls import path
from logia import views

urlpatterns = [
    path('create-user/', views.create_user),
    path('patients/', views.GetPatients.as_view()),
    path('pharmacies/', views.GetPharmacies.as_view()),
    path('transactions/', views.GetTransactions.as_view()),
]