from rest_framework import viewsets, permissions
from .serializers import ProcuradorSerializer
from .models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class ProcuradorViewSet(viewsets.ModelViewSet):
    queryset = Procurador.objects.all()
    serializer_class = ProcuradorSerializer
    permission_classes = [permissions.IsAuthenticated]  
    authentication_classes = [SessionAuthentication, BasicAuthentication]

