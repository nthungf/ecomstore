from django.shortcuts import render


# Create your views here.
def home(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    return render(request, 'index.html', locals())
