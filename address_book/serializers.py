from rest_framework import serializers
from . import models


class AddressBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddressBook
        fields = ('organization', 'city', 'house_num')
