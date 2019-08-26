from django.shortcuts import render
from rest_framework.views import APIView
from .models import Customer
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializer import CustomerSerializer, LoginSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.


class CustomerView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object_by_id(self, id):
        try:
            instance = Customer.objects.get(custid=id)
            return instance
        except Customer.DoesNotExist as e:
            return JsonResponse({"msg": "object does not exist with given id"}, status=400)

    def get(self, request, id=None):
        qs = None
        serializer = None
        if id is None:
            qs = Customer.objects.all()
            serializer = CustomerSerializer(qs, many=True)
        else:
            qs = self.get_object_by_id(id)
            serializer = CustomerSerializer(qs)
        content = {
            'user': request.user,  # `django.contrib.auth.User` instance.
            'auth': request.auth  # None
        }
        return JsonResponse(content, status=200, safe=False)
        # return JsonResponse(serializer.data, status=200, safe=False)

    @csrf_exempt
    def post(self, request):
        data = request.data
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def put(self, request, id):
        data = request.data
        instance = self.get_object_by_id(id)
        serializer = CustomerSerializer(
            data=data, instance=instance, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    '''
    def patch(self, request, id):
        data = request.data
        instance = self.get_object_by_id(id)
        serializer = CustomerSerializer(data=data, instance=instance, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    '''
    @csrf_exempt
    def delete(self, request, id):
        instance = self.get_object_by_id(id)
        if instance is None:
            return JsonResponse({"msg": "object to be deleted DoesNotExist"}, status=402)
        xp = instance.delete()
        return JsonResponse({"msg": "resouce deleted"}, status=400)


class GenericCustomerView(generics.ListAPIView,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.RetrieveModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = "custid"
    authentication_classes = [TokenAuthentication,SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, custid=None):
        if custid:
            self.retrieve(request, custid)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, custid=None):
        return self.update(request, custid)

    def delete(self, request, custid=None):
        x = self.destroy(request, custid)
        return JsonResponse({"sucess": "resource deleted successfully"}, status=200)

class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user=user)
        token, created =Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication, ]
    def post(self, request):
        django_logout(request)
        return Response(status=200)

from rest_framework import viewsets
class CustomerViewSet(viewsets.ViewSet):
    queryset = Customer.objects.all()
    serializer = CustomerSerializer
    lookup_field = "custid"
