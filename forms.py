# coding: utf-8
from django.contrib.localflavor.br.forms import BRZipCodeField 
from django.contrib.localflavor.br.forms import BRPhoneNumberField 
from django.contrib.localflavor.br.forms import BRCNPJField 
from django.contrib.localflavor.br.forms import BRCPFField 
from django.contrib.localflavor.br.forms import BRStateChoiceField 
from models import Client
 
class ClientForm(ModelForm): 
    cep = BRZipCodeField(label=u'CEP') 
    cpf = BRCPFField(label=u'CPF', required=False)
    telefone = BRPhoneNumberField(label=u'Telefone') 
    
	class Meta: 
        model = Client