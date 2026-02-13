from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa


def lista_tarefas(request):
    tarefas = Tarefa.objects.all().order_by('-criada_em')
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})


def criar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        if titulo:
            Tarefa.objects.create(titulo=titulo)
    return redirect('lista_tarefas')


def concluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect('lista_tarefas')


def deletar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('lista_tarefas')
