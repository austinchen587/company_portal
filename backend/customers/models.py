from django.db import models

# Create your models here.
def create_dynamic_customer_model(fields):
    attrs = {field_name: models.CharField(max_length=255, blank=True,null=True) for field_name in fields}
    attrs['create_at'] = models.DateField(auto_now_add=True)
    return type('Customer',(models.Model,),attrs)

 