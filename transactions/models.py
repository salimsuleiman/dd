from django.db import models
from users.models import User
from django.forms.models import model_to_dict
<<<<<<< HEAD
# Create your models here.
=======

>>>>>>> dfee7a2... more code

from wallets.models import Wallet

class Transaction(models.Model):
    hash = models.CharField(max_length=200)
<<<<<<< HEAD


    amount = models.DecimalField(decimal_places=7, max_digits=12,default=0.0)
    # invalid | authorized | pending
=======
    amount = models.DecimalField(decimal_places=7, max_digits=12,default=0.0)
    time_stamp = models.DateTimeField(auto_now_add=True)
    txType = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)

   
>>>>>>> dfee7a2... more code
    status = models.CharField(max_length=200, choices=[
        ['Pending', 'Pending'],
        ['Invalid', 'Invalid'],
        ['Authorized', 'Authorized'],
<<<<<<< HEAD
    ], default='invalid')

    verified = models.BooleanField(default=False)

    sender = models.CharField(max_length=200, unique=False, help_text='The user hash:id who sends the coins')
    receiver = models.CharField(max_length=200,unique=False, help_text='The wallet receive address who receive the funds')
    time_stamp = models.DateTimeField(auto_now_add=True)
    

    def get_sender(self):
        return Wallet.objects.filter(receive_key=self.sender).first()

    def get_receiver(self):
=======
    ], default='Invalid')


    sender = models.CharField(max_length=200, unique=False, help_text='The user hash:id who sends the coins')
    receiver = models.CharField(max_length=200,unique=False, help_text='The wallet receive address who receive the funds')
    
    @property
    def payer(self):
        return Wallet.objects.filter(receive_key=self.sender).first()

    @property
    def payee(self):
>>>>>>> dfee7a2... more code
        return Wallet.objects.filter(receive_key=self.receiver).first()


    @property
    def is_valid(self) -> bool:
        # hashes self.data, and return True if hash maches else False
        return True

    @property
    def data(self)-> str:
<<<<<<< HEAD
        l = model_to_dict(Transaction.objects.filter(id=self.id).first(), exclude=['hash','status'])
        return f'{l}'    
    
    def __str__(self):
=======
        instance = model_to_dict(Transaction.objects.filter(id=self.id).first(), exclude=['hash' 'status', 'completed'])
        return f'{instance}'    
    
    def __str__(self)->str:
>>>>>>> dfee7a2... more code
        return  f"{self.sender[:10]}.. TRANSFERRED {self.amount} COINS TO {self.receiver[:10]}.."