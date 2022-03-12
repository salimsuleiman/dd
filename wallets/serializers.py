from rest_framework import serializers
from .models import Wallet

 

class WalletSerializers(serializers.ModelSerializer):
     class Meta:
        model = Wallet
        fields = ['balance', 'receive_key', 'public_key', 'private_key']