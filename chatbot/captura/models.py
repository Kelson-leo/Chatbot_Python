from django.db import models

# Create your models here.

class Captura(models.Model):
 code = models.CharField(max_length=15)
 code_user = models.CharField(max_length=15)
 active  = models.IntegerField()
 name = models.CharField(max_length=100) #nome
 age = models.IntegerField() #idade
 sex = models.CharField(max_length=10) #sexo
 email = models.CharField(max_length=100) #email
 cellphone = models.CharField(max_length=15) #telefone celular
 phone = models.CharField(max_length=10) #telefone fixo
 cep = models.CharField(max_length=10) #cep - exemplo: 04538-133
 state = models.CharField(max_length=50) #Estado
 city = models.CharField(max_length=100) #Cidade
 name = models.CharField(max_length=100) #nome
 neighborhood = models.CharField(max_length=100) #bairro
 address = models.CharField(max_length=200) #endereço
 number=models.CharField(max_length=5) #numero
 cpf = models.CharField(max_length=15) #cpf - 542.458.414-43
 cnpj = models.CharField(max_length=15) #cnpj - 76.255.668/0001-41



def _str_(self):
    return self.code



