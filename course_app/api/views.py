from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from ..models import Course

from .serlizer import Course_Ser

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def getall(request):
    if request.method == 'GET':
       
        # courses = Course.objects.all()
        # jsoncourses = Course_Ser(courses, many=True)
        return Response(
            # data={'courses': Course_Ser(courses, many=True).data},
            data={'courses': Course_Ser.serlize_all()},
            status=status.HTTP_200_OK
    )

    else:
        # get data from request
        jsondata = request.data
        # convert json to course_ser deserializer
        courseserobj = Course_Ser(data=jsondata)
        #validate data
        if courseserobj.is_valid():
            # save data
            courseserobj.save()
            return Response(
                data = courseserobj.data,
                status=status.HTTP_201_CREATED
            )
        #else return error
        else:
            return Response(
                data = {'error': courseserobj.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        
@api_view(['GET', 'PUT', 'DELETE','Patch'])
def getbyid_update_delete(request, id):
    if request.method == 'GET':
        return Response(
            data = Course_Ser.get_by_id(id),
            status=status.HTTP_200_OK
        )
    elif request.method=='DELETE':
        if (Course_Ser.delete(id)):
            return Response(
                data = {'message': 'Deleted Successfully'},
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                data = {'message': 'Not Found'},
                status=status.HTTP_404_NOT_FOUND
            )
    if request.method=='PUT':
        #get new data
        jsondata = request.data
        #get old model object
        #serialize new data
        serobj = Course_Ser.getundpatedcourse(id,jsondata)
        #validate new data
        if serobj.is_valid():
            #save new data
            serobj.save()
            return Response(
                data = serobj.data,
                status=status.HTTP_200_OK
            )
        #else return error
        else:
            return Response(
                data = {'error': serobj.errors},
                status=status.HTTP_400_BAD_REQUEST
            )