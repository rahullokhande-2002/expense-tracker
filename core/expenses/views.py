from rest_framework.viewsets import ModelViewSet
from .models import Expenses
from .serializers import ExpenseSerializers
from rest_framework.permissions import IsAuthenticated

class ExpenseViewSet(ModelViewSet):
    
    
    
    serializer_class=ExpenseSerializers
    permission_classes = [IsAuthenticated]
    queryset = Expenses.objects.all()   
    
    
    def get_queryset(self):
        return Expenses.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
     serializer.save(user=self.request.user)
