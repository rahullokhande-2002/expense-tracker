from rest_framework.viewsets import ModelViewSet
from .models import Expenses
from .serializers import ExpenseSerializers
from rest_framework.permissions import IsAuthenticated

class ExpenseViewSet(ModelViewSet):
    
    queryset=Expenses.objects.all()
    serializer_class=ExpenseSerializers
    
    permission_classes = [IsAuthenticated]
