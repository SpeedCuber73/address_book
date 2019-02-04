from rest_framework.permissions import IsAuthenticated
from .models import AddressBook
from . import serializers
from rest_framework import viewsets
#  from .permissions import IsOwner


class AddressBookViewSet(viewsets.ModelViewSet):

    queryset = AddressBook.objects.all()
    serializer_class = serializers.AddressBookSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return AddressBook.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
