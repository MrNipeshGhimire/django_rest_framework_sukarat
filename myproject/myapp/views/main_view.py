from rest_framework.response import Response
from ..models import Student
from ..serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST','GET'])
def student_view(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Student added successfully",'data':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # for GET method 
    if request.method == "GET":
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT','DELETE','GET'])
def student_view_detail(request,id):
    try:
        student = Student.objects.get(id=id)
    except Exception as e:
        print(e)
        return Response({"error":"Cannot found data"})
    
    if request.method == 'DELETE':
        student.delete()
        return Response({'msg':"Student data deleted successfully"},status=status.HTTP_200_OK)
    

