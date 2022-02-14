from django.db import models
from django.urls import reverse

class Cliente (models.Model):
    cpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    dt_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (("pode_manipular", "Manipula o cadastro"),)

    """ Retorna a URL para acessar os detalhes deste contas. """
    def get_absolute_url(self):
        return reverse('cliente-detalhes', args=[str(self.id)])
    def __str__(self):
        return self.nome

class Filme (models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    produtora = models.CharField(max_length=100)

    class Meta:
        permissions = (("pode_manipular", "Manipula o cadastro"),)

    """ Retorna a URL para acessar os detalhes deste filme. """
    def get_absolute_url(self):
        return reverse('filme-detalhes', args=[str(self.id)])
    def __str__(self):
        return self.titulo


class Locacao (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete= models.CASCADE)
    data_locacao = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)

    def get_absolute_url(self):
        return reverse('locacao-detalhes', args=[str(self.id)])