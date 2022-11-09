from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

class LeadApi(viewsets.ModelViewSet):
  queryset = Lead.objects.all()
  serializer_class = LeadSerializer
  permission_classes = [permissions.AllowAny]
