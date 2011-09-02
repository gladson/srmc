# coding: utf-8
from django.db import models

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

SEXO_C = (('F','Feminino'),('M','Masculino'),)

class Cad_produtor(models.Model):
    nome = models.CharField(max_length=255, verbose_name=u'Nome do Produtor')
    sexo = models.CharField(max_length=1, choices=SEXO_C)
    data_de_nascimento = models.DateField(verbose_name=u'Data de Nascimento', null=True,  blank=True)
    cpf = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'CPF')
    rg = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'RG')
    telefone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True,  blank=True)
    uf = models.ForeignKey(Uf, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, null=True, blank=True, verbose_name=u'município')
    cep = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    endereco = models.CharField(max_length=255, verbose_name=u'Endereço', blank=True, null=True)
    numero = models.CharField(max_length=255, verbose_name=u'Número', blank=True, null=True)
    complemento = models.CharField(max_length=255, verbose_name=u'Complemento', blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'Cadastro do Produtor'
        verbose_name_plural = u'01 Cadastro dos Produtores'

#
class Cad_endereco_propriedade(models.Model):
    nome_propriedade = 	models.CharField(max_length=255, verbose_name=u'Nome da Propriedade')
    endereco = models.CharField(max_length=255, verbose_name=u'Endereço', blank=True, null=True)
    lote = models.CharField(max_length=255, verbose_name=u'lote', blank=True, null=True)
    gleba = models.CharField(max_length=255, verbose_name=u'gleba', blank=True, null=True)
    licenca_ambiental = models.CharField(max_length=255, verbose_name=u'gleba', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.nome_propriedade

    class Meta:
        verbose_name = u'Cadastro do Endereço da Propriedade'
        verbose_name_plural = u'02 Cadastro dos Endereços das Propriedades'

#
class Uso_solo(models.Model):
    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'Uso do solo'
        verbose_name_plural = u'02 | Uso do solo'
#
class Uso_solo_unidade(models.Model):
    nome = models.CharField(max_length=255, verbose_name=u'Unidade')

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'Uso do solo - Unidade'
        verbose_name_plural = u'02 | Uso do solo - Unidade'
#
class Uso_agua(models.Model):
    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'Uso da Água'
        verbose_name_plural = u'02 | Uso da Água'
#
class Criacao(models.Model):
    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'Criação'
        verbose_name_plural = u'02 | Criação'
#
class Cad_uso(models.Model):
    nome = models.ForeignKey(Uso_solo, related_name=u'uso_solo', verbose_name=u'Uso do Solo', blank=True, null=True)
    numero_area = models.CharField(max_length=255, verbose_name=u'Área')
    unidade = models.ForeignKey(Uso_solo_unidade, related_name=u'uso_solo_unidade', verbose_name=u'Unidade', blank=True, null=True)
    criacao = models.ForeignKey(Criacao, related_name=u'criacao', verbose_name=u'Criação', blank=True, null=True)
    numero_criacao = models.PositiveIntegerField(max_length='20', verbose_name=u'Quantidade', blank=True, null=True, help_text='Apenas números')

    def __unicode__(self):
        return self.numero_area

    class Meta:
        verbose_name = u'Cadastro de Uso do Solo'
        verbose_name_plural = u'02 | Cadastro de Uso do Solo'
