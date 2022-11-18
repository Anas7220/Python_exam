from rest_framework import serializers
#For Api Creation
class HotelSerializer(serializers.Serializer):
    hname=serializers.CharField(max_length=80)
    cname=serializers.CharField(max_length=80)
    cno=serializers.IntegerField()
    cin=serializers.DateTimeField()
    cout=serializers.DateTimeField()
