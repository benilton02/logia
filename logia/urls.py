from django.urls import path
from logia import views

urlpatterns = [
    path('get-or-create-token/<str:username>', views.get_or_create_token),
    path('patients/', views.GetPatients.as_view()),
    path('pharmacies/', views.GetPharmacies.as_view()),
    path('transactions/', views.GetTransactions.as_view()),
]