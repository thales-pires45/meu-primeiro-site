from django.urls import path
from contas import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/', views.ClienteListView.as_view(), name='cliente'),
    path('cliente/<int:pk>', views.ClienteDetailView.as_view(), name='cliente-detalhes'),
    path('cliente/create/', views.ClienteCreateView.as_view(), name='cliente-create'),
    path('cliente/<int:pk>/delete/', views.ClienteDelete.as_view(), name='cliente-delete'),
    path('cliente/<int:pk>/update/', views.ClienteUpdate.as_view(), name='cliente-update'),
    #Filmes
    path('filme/', views.FilmeListView.as_view(), name='filme'),
    path('filme/<int:pk>', views.FilmeDetailView.as_view(), name='filme-detalhes'),
    path('filme/create/', views.FilmeCreateView.as_view(), name='filme-create'),
    path('filme/<int:pk>/delete/', views.FilmeDelete.as_view(), name='filme-delete'),
    path('filme/<int:pk>/update/', views.FilmeUpdate.as_view(), name='filme-update'),
    #locacao
    path('locacao/', views.LocacaoListView.as_view(), name='locacao'),
    path('locacao/<int:pk>', views.LocacaoDetailView.as_view(), name='locacao-detalhes'),
    path('locacao/create/', views.LocacaoCreateView.as_view(), name='locacao-create'),
    path('locacao/<int:pk>/delete/', views.LocacaoDelete.as_view(), name='locacao-delete'),
    path('locacao/<int:pk>/update/', views.LocacaoUpdate.as_view(), name='locacao-update'),
]

