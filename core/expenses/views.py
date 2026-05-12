from rest_framework.viewsets import ModelViewSet
from .models import Expenses
from .serializers import ExpenseSerializers

class ExpenseViewSet(ModelViewSet):
    
    queryset=Expenses.objects.all()
    serializer_class=ExpenseSerializers
