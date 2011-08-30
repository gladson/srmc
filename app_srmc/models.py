# coding: utf-8
from django.db import models
from django.contrib.localflavor.br.forms import *

class Uf(models.Model):    
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=2)
    
    def __unicode__(self):
        return self.sigla  
        
#
class Municipio(models.Model):    
    municipio_nome = models.CharField(max_length=255)
    municipio_nome_cxalta = models.CharField(max_length=255)
    uf = models.ForeignKey(Uf)
    uf_sigla = models.CharField(max_length=2)    
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    class Meta:
        verbose_name = u'município'
        
    def __unicode__(self):
        return self.municipio_nome

#

class Uso_solo(models.Model):    
    nome = models.CharField(max_length=255)
	unidade = models.CharField(max_length=255)
        
    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'02 | Uso do solo'
#

class Uso_agua(models.Model):    
    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'02 | Uso da Água'

class Criacao(models.Model):    
    nome = models.CharField(max_length=255)
        
    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'02 | Criação'

SEXO_C = (('F','Feminino'),('M','Masculino'),)

class Cad_produtor(models.Model):
    nome = models.CharField(max_length=255, verbose_name=u'Nome do Produtor')
	sexo = models.CharField(max_length=1, choices=SEXO_C)
    data_de_nascimento = models.DateField(verbose_name='Data de Nascimento', null=True,  blank=True)
	cpf = BRCPFField(required=False)
	rg = models.CharField(max_length=255, null=True, blank=True)
    telefone = BRPhoneNumberField()
	email = models.EmailField(max_length=255)
	uf = models.CharField(max_length=2, blank=True, null=True)
    municipio = models.ForeignKey(Municipio, blank=True, null=True, verbose_name=u'município')
    cep = BRZipCodeField()
	bairro = models.CharField(max_length=255, blank=True, null=True)
	endereco = models.CharField(max_length=255, verbose_name=u'Endereço', blank=True, null=True)
    numero = models.CharField(max_length=255, verbose_name=u'Número', blank=True, null=True)
    complemento = models.CharField(max_length=255, verbose_name=u'Complemento', blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'01 Cadastro do Produtor'
        verbose_name_plural = u'01 Cadastro dos Produtores'

class Cad_endereco_propriedade(models.Model):
    nome_propriedade = 	models.CharField(max_length=255, verbose_name=u'Nome da Propriedade')
    endereco = models.CharField(max_length=255, verbose_name=u'Endereço', blank=True, null=True)
    lote = models.CharField(max_length=255, verbose_name=u'lote', blank=True, null=True)
    gleba = models.CharField(max_length=255, verbose_name=u'gleba', blank=True, null=True)
    licenca_ambiental = models.CharField(max_length=255, verbose_name=u'gleba', blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
	
	def __unicode__(self):
        return self.nome_propriedade

    class Meta:
        verbose_name = u'02 Cadastro do Endereço da Propriedade'
        verbose_name_plural = u'02 Cadastro dos Endereços das Propriedades'


class Cad_uso(models.Model):
    uso_do_solo = models.ForeignKey(Uso_solo, related_name=u'nome', verbose_name=u'Uso do Solo', blank=True, null=True)
	numero_area = models.CharField(max_length=255, verbose_name=u'Área')
 	unidade = models.ForeignKey(Uso_solo, related_name=u'unidade', verbose_name=u'Unidade', blank=True, null=True)
	criacao = models.ForeignKey(Criacao, related_name=u'nome', verbose_name=u'Criação', blank=True, null=True)
	numero_criacao = models.PositiveIntegerField(max_length='20', verbose_name=u'Quantidade', blank=True, null=True, help_text='Apenas números')
	
	def __unicode__(self):
        return self.numero_area

    class Meta:
        verbose_name = u'02 | Cadastro de Uso do Solo'

