from django.shortcuts import render
from django.views import generic
from .models import Servicos
from .models import Publicacoes
from .models import Depoimentos
# from .models import nomeDoModels
from .models import Parceiros

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse  
from django.urls import reverse_lazy 
from templated_email import send_templated_mail

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def post (self,request, *args, **kwargs):
        nome=request.POST.get('nome')
        assunto=request.POST.get('assunto')
        email=request.POST.get('email')
        mmensagem=request.POST.get('mensagem')
        send_templated_mail(
        template_name='email',
        from_email= email,
        recipient_list=['clientejosealcantara@gmail.com'],
        context={
            'nome':nome,
            'assunto':assunto,
            'email':email,
            'mensagem':mmensagem
        },)
        return HttpResponseRedirect(reverse_lazy("index"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicos"] = Servicos.objects.all()
        context["parceiros"] = Parceiros.objects.all()
        context["publicacoes"] = Publicacoes.objects.all()
        context["depoimentos"] = Depoimentos.objects.all()
        return context