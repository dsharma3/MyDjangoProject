from django.shortcuts import render
from crud_app.forms import EmployeeForm
from django.http import HttpResponse
from crud_app.models import EmployeeModel

# Create your views here.
def employee(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmployeeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            try:
                form.save()
                print("saved")
            except Exception as ex:
                print("Exception", ex)
                pass

        else:
            form = EmployeeForm()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmployeeForm(request.GET)
    return render(request, 'crud_app/employee.html', {'form': form})


def employee_list(request):
    data = {'employees': EmployeeModel.objects.all()}
    return render(request, 'crud_app/employee_list.html', context=data)
