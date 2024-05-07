from django.db import models
from datetime import datetime


# Cadastro de Clientes.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    fone = models.CharField(max_length=15)
    
    def __str__(self):
        return "{} - {}".format(self.nome, self.email)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-id']


class TipoImovel(models.TextChoices):
    Apartamento = 'APARTAMENTO','APARTAMENTO'
    Kitnet = 'KITNET','KITNET'
    Casa = 'CASA', 'CASA'
    Chacara = 'CHACARA', 'CHACARA'
    
## Cadastro dos Imóveis

class Imovel(models.Model):
    codigo = models.CharField(max_length=100, verbose_name='Código do Imóvel')
    tipo_item = models.CharField(max_length=100, choices=TipoImovel.choices, verbose_name='Tipo do Imóvel')
    endereco = models.TextField(verbose_name='Endereço')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    alugado = models.BooleanField(default=False, verbose_name='Alugado?')
    
    def __str__(self):
        return "{} - {}".format(self.codigo, self.tipo_item)
    
    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'
        ordering = ['-id']
        

## Cadastrar as Imagens do Imóvel
class ImovelImagem(models.Model):
    image = models.ImageField('Images', upload_to='images')
    imovel = models.ForeignKey(Imovel, related_name='imovel_imagem', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.imovel.codigo
    
## Registrar Locação
class Registro(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='reg_locacao')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField('Início')
    data_final = models.DateTimeField('fim')
    criacao = models.DateField(default=datetime.now, blank=True)
    
    def __str__(self):
        return"{} - {}".format(self.cliente, self.imovel)
    
    class Meta:
        verbose_name = "Registrar Locação"
        verbose_name_plural = "Registrar Locação"
        ordering = ['-id']
        
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subrscribed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    
class Sobre(models.Model):
    titulo = models.CharField(max_length=255)
    texto = models.TextField(blank=False, null=False)
    ativado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Página Sobre Nós"
        verbose_name_plural = "Sobre"