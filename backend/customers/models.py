from django.db import models, connection

# Create your models here.
def create_dynamic_customer_model(fields):
    attrs = {field_name: models.TextField(blank=True,null=True) for field_name in fields}
    attrs['create_at'] = models.DateField(auto_now_add=True)
    attrs['__module__']=__name__

    Customer = type('Customer',(models.Model,),attrs)

    table_name = Customer._meta.db_table
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT to_regclass('{table_name}');")
        if cursor.fetchone()[0] is None:
            with connection.schema_editor() as schema_editor:
                schema_editor.create_model(Customer)

    return Customer