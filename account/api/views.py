from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.api.serializers import RegistrationSerializer
from account.models import Account
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from rest_framework import status
import jwt
import datetime

from VotingBackend.settings import SECRET_KEY



class TokenBuilder:
    def __init__(self) -> None:
        self.secret="my_secret_key"
    @staticmethod
    def accessToken(payload={},time=3):
         tokenBuilder = TokenBuilder()

                
         payload['exp']=datetime.datetime.utcnow() + datetime.timedelta(days=time)
         access_token = jwt.encode(payload, tokenBuilder.secret, algorithm='HS256')
         return access_token
    def refreshToken(payload={},time=30):
         tokenBuilder = TokenBuilder()

                
         payload['exp']=datetime.datetime.utcnow() + datetime.timedelta(days=time)
         access_token = jwt.encode(payload, tokenBuilder.secret, algorithm='HS256')
         return access_token


@api_view(['POST'])
def registration_view(request):
    serializer  = RegistrationSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        account = serializer.save()
        # data['response']= "succsssfully registered a new user."
        data['regNo'] = account.regNo
        data['username'] = account.username
        data['id'] = account.pk

        access_token=TokenBuilder.accessToken(payload=data)

        refresh_token=TokenBuilder.refreshToken(payload=data)

        secret_key = 'your_secret_key'

        return Response({'payload':{'user':data,'token':{'access_token':access_token, 'refresh_token': refresh_token}}})
    else:
        data = serializer.errors
        
    return Response(data, status=400)

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'token',
        '/token/refresh'
    ]

    return Response(routes)

# @api_view(['POST'])
# def login(request):
#     User = get_user_model()
#     username = request.data.get('username')
#     password = request.data.get('password')
#     # account=Account.objects.all()
    
    object
#     if password ==Account.objects.get(password):
#         if username == Account.objects.get(username):
             
#              access_token=TokenBuilder.accessToken(payload=data)
#              refresh_token=TokenBuilder.refreshToken(payload=data)


#         # return Response({'access_token': access_token})
#         return Response({'error': 'err'})
        
#     else:
#         return Response({"error": "something went wrong"})




@api_view(['POST'])
def login(request):
    regNo = request.data.get('regNo')
    password = request.data.get('password')

    user = authenticate(request, regNo=regNo, password=password)
    if user is not None:
        # Authentication successful, generate tokens
        data = {}
        data['regNo'] = user.regNo
        data['username'] = user.username
        data['id'] = user.pk

        access_token = TokenBuilder.accessToken(payload=data)
        refresh_token = TokenBuilder.refreshToken(payload=data)

        return Response({
            'payload': {
                'user': data,
                'token': {
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
            }
        })
    else:
        # Authentication failed
        return Response({'error': 'Invalid credentials'}, status=400)

@api_view(['GET'])
def refreshedToken(request):
    query_params = request.query_params["refresh_token"]
    print(query_params)
    try:
        decoded_token = jwt.decode(query_params, 'my_secret_key', algorithms=['HS256'])
        user_id = decoded_token['id']
        user = Account.objects.get(pk=user_id)
        print(user.is_admin)
        data = {}
        data['regNo'] = user.regNo
        data['username'] = user.username
        data['id'] = user.pk
        print(data)
        access_token = TokenBuilder.accessToken(payload=data)
        return Response({'token': access_token}, status=200)

    except Exception as e:
         print(str(e))
         return Response({'token': "kk"}, status=401)


   