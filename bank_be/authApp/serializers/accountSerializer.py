
from dataclasses import fields
from pyexpat import model
from authApp.models.account import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['balance','lastChangeDate','isActive']