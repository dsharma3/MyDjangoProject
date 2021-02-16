from django.shortcuts import render
from django.http import HttpResponse
from pollapp.forms import ContactForm
# Create your views here.
def index(request):
    my_dict = {'topic': Topic.objects.all()}
    
    return render(request, 'pollapp/modelBinding.html',context=my_dict)
    
def get_topic(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'pollapp/form-example.html', {'form': form})
 
def yourname(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['contactname']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            print(name)
            print(email)
            print(message)

            return HttpResponse('Thanks for visiting '+name)
        return HttpResponse('Data was not valid')
        
    else:
        return HttpResponse('Thanks for visiting')
