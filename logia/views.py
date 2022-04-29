from rest_framework.decorators import api_view, APIView
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
import json
# Create your views here.

@api_view(['POST'])
def get_or_create_token(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        data = {'error': 'User does not exist'}
        return JsonResponse(data, status=404)
    
    token = list(Token.objects.get_or_create(user=user))
    data = {
        "username": username,
        "token": str(token[0])
        }
    return JsonResponse(data, status=200)


class GetPatients(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        data = json.loads(request.body)
        return JsonResponse(data, status=200)


class GetPharmacies(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        data = json.loads(request.body)
        return JsonResponse(data, status=200)


class GetTransactions(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        data = json.loads(request.body)
        return JsonResponse(data, status=200)
