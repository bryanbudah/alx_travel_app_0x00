from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to ALX Travel API!"}, status=status.HTTP_200_OK)
