from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeSerializer, RegisterSerializer

# Create your views here.

class RegisterView(APIView):

    def post(self,request):

        serializer = RegisterSerializer(data=request.data)
        print("Dataaaa---->>>>>>>>", request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User registered successfully"})

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class EmployeeListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        employees = Employee.objects.filter(user=request.user)
        serializer = EmployeeSerializer(employees, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class EmployeeDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id, user):
        try:
            return Employee.objects.get(id=id,user=user)
        except Employee.DoesNotExist:
            return Response({'message': 'Record Doest Not found'}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, id):
        employee = self.get_object(id, request.user)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self,request,id):
        employee = self.get_object(id,request.user)
        serializer = EmployeeSerializer(employee,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)


    def delete(self,request,id):
        employee = self.get_object(id,request.user)
        employee.delete()
        return Response({"message":"Deleted"})