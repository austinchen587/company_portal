from django.shortcuts import render
import pandas as pd
from .forms import FileUploadForm
from .models import create_dynamic_customer_model

# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)
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
    return render(request,'customers/upload.html',{'from':form})

def customer_analysis(request):
    if request.method == 'POST':
        file = request.FILES['file']

        try:
            data = pd.read_csv(file)
        except Exception as e:
            date = pd.read_excel(file)

        fields = data.columns.tolist()

        Customer = create_dynamic_customer_model(fields)

        for index, row in data.iterrows():
            customer_instance = Customer(**row.to_dict())
            customer_instance.save()

        customer_count = Customer.objects.count()

        return render(request,'customers/customer_analysis.html',{'customer_count':customer_count,})


    return render(request,'customers/upload.html')




