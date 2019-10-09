from django.db import models
import math

# Create your models here.


class Pessoa(models.Model):
    """ classe que registra cada cliente do estacionamento"""
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Marca(models.Model):
    """ classe que armazena nomes das marcas dos carros"""
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    """ classe que identifica a placa, cor, observações dos veículos que fazem checkin
    no estacionamento. cada veiculo tem UM proprietário e UMA marca"""
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=20)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.marca.nome + ' - ' + self.placa


class Parametros(models.Model):
    """ classe que armazena os valores de cobrança do estacionamento"""
    valor_hora = models.DecimalField(max_digits=5,decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "Parâmetros gerais"


class MovRotativo(models.Model):
    """ classe que armazena informações de entradas rotativas no estacionamento """
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora = models.DecimalField(max_digits=5,decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def horas_total(self):
        """ método para calcular a quantidade de horas estacionado"""
        return math.ceil( (self.checkout - self.checkin).total_seconds() / 3600 )
    

    def total(self):
       """ método para calcular o total, valor da hora multiplicado por horas_total"""
       return self.valor_hora * self.horas_total()

    def __str__(self):
        return self.veiculo.proprietario.nome + ' - ' + self.veiculo.placa



class Mensalista(models.Model):
    """classe de veiculos mensalistas no estacionamento"""
    veiculo = models.ForeignKey(Veiculo,on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.veiculo) + ' - ' + str(self.inicio)


class MovMensalista(models.Model):
    """movimentação dos veciulos mensalistas"""
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    data_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.mensalista) + ' - ' + str(self.total)