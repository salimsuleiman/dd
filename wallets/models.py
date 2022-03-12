from django.db import models
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
import uuid
<<<<<<< HEAD
from Crypto.PublicKey import RSA
=======
>>>>>>> dfee7a2... more code
import hashlib
import json
from Crypto.PublicKey import RSA


class Wallet(models.Model):
    balance = models.DecimalField(decimal_places=7, max_digits=12,default=0.0)
    balance_in_ngn = models.DecimalField(decimal_places=2, max_digits=12,default=0.0)
    public_key = models.CharField(max_length=120, blank=True, unique=True)
    private_key = models.CharField(max_length=1200, blank=True, unique=True)
    date_created = models.DateTimeField(auto_now=True)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='wallet')
    receive_key =  models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Wallet   [ {self.id} ]   ::    owner [ {self.owner.id} ]'.upper()
        

@receiver(post_save, sender= Wallet)
def generate_key(sender: Wallet, instance=None, created=False, **kwargs):
    if created:
<<<<<<< HEAD
        RSAkey = RSA.generate(1024)
        hasher = hashlib.sha256()


        public_key = RSAkey.publickey().exportKey().decode('ascii')
        private_key = RSAkey.exportKey().decode('ascii')     
=======
        hasher = hashlib.sha256()

       
        key = RSA.generate(2048)



        private_key = key.export_key().decode("utf-8") 
        public_key = key.publickey().exportKey().decode("utf-8")

>>>>>>> dfee7a2... more code

        instance.public_key = public_key
        instance.private_key = private_key

        hasher = hashlib.sha256()

        key = bytes(f'{public_key}', encoding='utf8')
        hasher.update(key)
        receive_key =  hasher.hexdigest()
        instance.receive_key = receive_key



        instance.save()
        ...