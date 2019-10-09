from django.urls import path
from . import views 

app_name = 'core' 

urlpatterns = [
    path('', views.home ,name='home'),

    # PESSOA CRUD
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('core/pessoa_nova/', views.pessoa_nova, name='pessoa_nova'),
    path('core/pessoa_update/<int:id>/', views.pessoa_update, name='pessoa_update'),
    path('core/pessoa_delete/<int:id>/', views.pessoa_delete, name='pessoa_delete'),

    # VEICULO CRUD
    path('veiculos/', views.lista_veiculos, name='lista_veiculos'),
    path('core/veiculo_novo/', views.veiculo_novo,name='veiculo_novo'),
    path('core/veiculo_update/<int:id>/', views.veiculo_update, name='veiculo_update'),
    path('core/veiculo_delete/<int:id>/', views.veiculo_delete, name='veiculo_delete'),

    # MOVROTATIVO CRUD
    path('movimentosRotativos/', views.lista_movrotativos, 
    name='lista_movrotativos'),
    path('core/novo_rotativo/', views.novo_rotativo, name='novo_rotativo'),
    path('core/rotativo_update/<int:id>/', views.rotativo_update, name='rotativo_update'),
    path('core/rotativo_delete/<int:id>/', views.rotativo_delete, name='rotativo_delete'),

    # MENSALISTA CRUD
    path('mensalistas/', views.lista_mensalistas, name='lista_mensalistas'),
    path('core/mensalista_novo', views.mensalista_novo, name='mensalista_novo'),
    path('core/mensalista_update/<int:id>/', views.mensalista_update, name='mensalista_update'),
    path('core/mensalista_delete/<int:id>', views.mensalista_delete, name='mensalista_delete'),

    # MOVMENSAL CRUD
    path('movimentosMensais/', views.lista_movMensal, name='lista_movMensal'),
    path('core/movMensal_novo/', views.movMensal_novo, name='movMensal_novo'),
    path('core/movMensal_update/<int:id>/', views.movMensal_update, name='movMensal_update'),
    path('core/movMensal_delete/<int:id>/', views.movMensal_delete, name='movMensal_delete'),
    # os caminhos que tem core/caminho são os caminhos que não tem template proprios
    # estes caminhos saem de um template e vão para o core, sem o core/ o django não os identifica
    
]