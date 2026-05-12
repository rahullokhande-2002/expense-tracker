from rest_framework.serializers import ModelSerializer
from .models import Expenses

class  ExpenseSerializers(ModelSerializer):
    class Meta:
        model=Expenses
        field='__all__'