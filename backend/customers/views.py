from django.shortcuts import render
import pandas as pd
from .forms import FileUploadForm
from .models import create_dynamic_customer_model

# Create your views here.

def process_file(file):
    if file.name.endswith('.xlsx'):
        data  = pd.read_excel(file)
    else:
        data = pd.read_csv(file)
    return data

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            file = request.FILES.get('file')
            if file:
                data = process_file(file)
                fields = data.columns.tolist()

                Customer = create_dynamic_customer_model(fields)


                for _, row in data.iterrows():
                    customer_instance = Customer()
                    for field in fields:
                        setattr(customer_instance,field,row[field])
                    customer_instance.save()

                return render(request,'customers/upload_success.html',{'fields':fields})
    else:
        form = FileUploadForm()

    return render(request, 'customers/upload.html',{'form':form})


def customer_analysis(request):
    if request.method =='POST':
        file = request.FILES['file']
        data = process_file(file)
        fields = data.columns.tolist()

        Customer = create_dynamic_customer_model(fields)

        for _, row, in data.iterrows():
            customer_instance = Customer()
            for field in fields:
                setattr(customer_instance,field,row[field])
            customer_instance.save()

        customer_count = Customer.objects.count()

        return render(request, 'customers/customer_analysis.html',{'customer_count':customer_count})
    
    return render(request,'customers/upload.html')
            

def view_customers(request):
    fields = request.session.get('upload_fields',[])
    
    Customer = create_dynamic_customer_model(fields)

    customers = Customer.objects.all()

    return render(request,'customer/view_customers.html',{'customers.html':customers,'fields':fields})


