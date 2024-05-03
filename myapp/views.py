from django.shortcuts import render, redirect
from myapp.forms import ClienteForm, ImovelForm
from .models import Imovel, ImovelImagem
from .forms import RegistroLocacaoForm
from django.db.models import Q

# Create your views here.
def lista_locacao(request):
    imoveis = Imovel.objects.filter(alugado=False)
    context = {
        'imoveis': imoveis
    }
    return render(request, 'lista_locacao.html', context)

def form_cliente(request):
    form = ClienteForm() 
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_locacao')   
    return render(request, 'form_cliente.html', {'form': form})

def form_imovel(request):
    form = ImovelForm()
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES)
        if form.is_valid():
            imovel = form.save()
            files = request.FILES.getlist('imovel') ## pega todas as imagens
            if files:
                for f in files:
                    ImovelImagem.objects.create( # cria instance para imagens
                        imovel=imovel, 
                        image=f)
            return redirect('lista_locacao')  
    return render(request, 'form_imovel.html', {'form': form})

def form_locacao(request, id):
    obter_localidade = Imovel.objects.get(id=id) ## pega objeto
    form = RegistroLocacaoForm()  
    if request.method == 'POST':
        form = RegistroLocacaoForm(request.POST)
        if form.is_valid():
            locacao_form = form.save(commit=False)
            locacao_form.imovel = obter_localidade ## salva id do imovel 
            locacao_form.save() 
            
	## muda status do imovel para "Alugado"
            alugado = Imovel.objects.get(id=id)
            alugado.alugado = True ## passa ser True
            alugado.save() 
      
            return redirect('lista_locacao') # Retorna para lista
    context = {
        'form': form, 
        'locacao': obter_localidade
        }
    return render(request, 'form_locacao.html', context)

#Relatórios

def relatorios(request):
    imoveis = Imovel.objects.all() 
    cliente = request.GET.get('cliente')
    tipo_item = request.GET.get('tipo_item')
    alugado = request.GET.get('alugado')
    data_inicio = request.GET.get('data_inicio')
    data_final = request.GET.get('data_final')
    
    if data_inicio and data_final: ## Por data
        imovel = Imovel.objects.filter(
						reg_locacaon__create_at__range=[data_inicio,data_final])
    
    if cliente: ## Filtra por nome e email do cliente
        imoveis = imoveis.filter(
            Q(reg_locacao__cliente__nome__icontains=cliente) | 
            Q(reg_locacao__cliente__email__icontains=cliente)
        )
    
    if tipo_item: ## Tipo de Imovel
        imoveis = imoveis.filter(tipo_item=tipo_item) 
        
    if alugado: ## Imovel foi locado ou não
        imoveis = imoveis.filter(alugado=alugado) 
        
    return render(request, 'relatorios.html', {'imoveis': imoveis})
