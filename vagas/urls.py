from django.urls import path
from . import views

urlpatterns = [
    path('nova_vaga/', views.nova_vaga, name="nova_vaga"),
    path('vaga/<int:id>', views.vaga, name="vaga"),
    path('nova_tarefa/<int:id_vaga>', views.nova_tarefa, name='nova_tarefa'),
    path('realizar_tarefa/<int:id>', views.realizar_tarefa, name='realizar_tarefa'),
    path('envia_email/<int:id_vaga>', views.envia_email, name="envia_email"),
    path('exclui_email/<int:id>', views.exclui_email, name="exclui_email"),
    path('atualizar_status/<int:id_vaga>', views.atualizar_status, name="atualizar_status"),
    path('editar_tecnologias_domino/<int:id_domino>/<int:id_vaga>', views.editar_tecnologias_domino, name="editar_tecnologias_domino"),
    path('editar_tecnologias_estudar/<int:id_estudar>/<int:id_vaga>', views.editar_tecnologias_estudar, name="editar_tecnologias_estudar"),
]