from rest_framework.serializers import ModelSerializer
from .models import Expenses

class  ExpenseSerializers(ModelSerializer):
    class Meta:
        model=Expenses
        fields = "__all__"