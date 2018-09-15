from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, models
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status, generics, mixins
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from .models import Employee, Profile, BinaryStorage
from .serializers import EmployeeSerializer, UserSerializer, ProfileSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, MultiPartParser
# Create your views here.


class EmployeeSearchAPI(APIView):

    def get(self, request):
        emps = Employee.objects.all()
        empsjs = EmployeeSerializer(emps, many=True)
        return Response(empsjs.data)


class EmployeeCrudApi(ModelViewSet): # generics.ListCreateAPIView
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        emp_list = Employee.objects.filter(owner=request.user)
        serialized = EmployeeSerializer(emp_list, many=True)
        return Response(serialized.data)


class ProfileApiViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)


class ProfileApi(APIView):

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = ProfileSerializer(photo)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            print("data " + serializer.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        #pk = request.data['pk']
        print("pk "+ pk)
        id = request.data['id']
        if id:
            instance = self.get_object(pk=id)
            serializer = ProfileSerializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Id Not Provider"}, status=status.HTTP_400_BAD_REQUEST)

    def pre_save(self, obj):
        print("pre save " + obj)
        obj.emp = Employee.objects.get(pk=self.request.data.emp)


class ImageUploadParser(FileUploadParser):
    media_type = 'image/*'


@permission_classes((AllowAny,))
class UploadImageAPI(APIView):
    parser_classes = (MultiPartParser, FileUploadParser,)

    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")
        f = request.data['file']
        bstoreObj = BinaryStorage(name=f.name, data=f, data_binary=f.read()).save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, pk, format=None):
        obj = BinaryStorage.objects.get(pk=pk)
        return HttpResponse(obj.data_binary, content_type='image/jpeg')


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def image(request):
    pass


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if email is None or password is None:
        return Response({'error': 'Please provide both email and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = models.User.objects.create_user(email, email, password)
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    if last_name or first_name:
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        user.save()
    serializer = UserSerializer(user)
    token, _ = Token.objects.get_or_create(user=user)
    res = {'token': token.key, 'user': serializer.data}
    return Response(res, status=status.HTTP_201_CREATED)