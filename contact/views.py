from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import ContactSubmission
from .serializers import ContactSerializer

class ContactCreateView(generics.CreateAPIView):
    """
    Allows any visitor to send a contact message.
    """
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny] 
