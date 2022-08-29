from rest_framework import serializers
from .models import Bio, ContactField

class ContactFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactField
        fields = ['id', 'name', 'value', 'link']
        

class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = ['name', 'profile', 'bio']
        