from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import BuscaEan
from .tasks import pesquisa_google

# Create your views here.
def teste_view(request):
    form = BuscaEan()
    context = {
        'form': form
    }
    return render(request, 'template.html', context)


class Home(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        form = BuscaEan()
        context = {
            'form': form,
            'produto' : 123
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = BuscaEan(request.POST, request.FILES)
        context = {
            'form': form,
            'produto': request.POST['ean']
        }
        pesquisa_google.delay(request.POST['ean'])

        if not form.is_valid():
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)
