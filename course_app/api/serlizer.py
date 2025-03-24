from rest_framework import serializers
from ..models import Course
from django.shortcuts import get_object_or_404
class Course_Ser(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=300)


    @classmethod
    def serlize_all(cls):
        return cls(Course.get_all_courses(), many=True).data
    
    def create(self, validated_data):
        objmodel = Course(name=validated_data['name'], description=validated_data['description'])
        objmodel.save()
        return objmodel
    
    @classmethod
    def get_by_id(cls, id):
        return cls(get_object_or_404(Course, pk=id)).data
    
    @classmethod
    def delete(cls, id):
        # obj = Course.objects.get(id=id).delete()
        obj = get_object_or_404(Course, pk=id)
        obj.delete()
        return True
        
    @classmethod
    def getundpatedcourse(cls,id,data):
        oldcourse = Course.get_by_id(id)
        return Course_Ser(oldcourse, data=data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.save()
        return instance