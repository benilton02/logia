from rest_framework.decorators import api_view, APIView
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from logia.models import PatientsModel, PharmaciesModel, TransactionsModel, UsersModel, UsersModel
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import json

   
@api_view(['POST'])
def create_user(request):
    payload = json.loads(request.body)
    data = {
        "id": payload.get("uuid"),
        "username": payload.get("username"),
        "password": payload.get("password")
    }
    
    user = User.objects.get_or_create(**data)
    token, created = Token.objects.get_or_create(user=user[0])
    data = {
        "token": token.pk,
    }
    return JsonResponse(data, status=201)


class GetPatients(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        queryset = PatientsModel.objects.all()
        patients = [
            {
                "uuid":query.uuid,
                "first_name":query.first_name,
                "last_name":query.last_name,
                "date_of_birth":query.date_of_birth
            }
                for query in queryset
        ]
        data = {'patients': patients}
        return JsonResponse(data, status=200)


class GetPharmacies(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        queryset = PharmaciesModel.objects.all()
        pharmacies =[
            {
                "uuid": query.uuid,
                "name": query.name,
                "city": query.city
            }
            for query in queryset
        ]
        data = {"pharmacies": pharmacies}
        return JsonResponse(data, status=200)


class GetTransactions(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        queryset = TransactionsModel.objects.all()
        transaction =[
            {
                "patient_id": query.patient_uuid.uuid,
                "first_name": query.patient_uuid.first_name,
                "last_name": query.patient_uuid.last_name,
                "date_of_birth": query.patient_uuid.date_of_birth,
                "pharmacy_id": query.pharmacy_uuid.uuid,
                "pharmacy_name": query.pharmacy_uuid.name,
                "pharmacy_city": query.pharmacy_uuid.city,
                "transaction_id": query.uuid,
                "transaction_amount": query.amount,
                "transaction_timestamp": query.timestamp
            }
            for query in queryset
        ]
        data = {"transaction":transaction}
        return JsonResponse(data, status=200)
