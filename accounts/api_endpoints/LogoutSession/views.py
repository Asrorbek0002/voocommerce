from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SessionLogoutAPIView(APIView):
    permission_classes = []  # Or add appropriate permissions if needed

    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_400_BAD_REQUEST)
