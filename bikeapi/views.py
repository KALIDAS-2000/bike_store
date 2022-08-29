from django.shortcuts import render
from rest_framework.views import  APIView
from  rest_framework.response import  Response
from bikeapi.serializers import BikeSerializers,BikeModelserializer
from bikeapi.models import Bikes


            #api/v1/vech/bikes/     -GET
            #api/v1/vech/bikes/     -POST

class BikesView(APIView):
    def get(self,request,*args,**kwargs):
        bks=Bikes.objects.all()
        serializer=BikeSerializers(bks,many=True)
        return  Response(data=serializer.data)



    def post(self,request,*args,**kwargs):
        serializer=BikeSerializers(data=request.data)
        if serializer.is_valid():
            Bikes.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return  Response(serializer.errors)


        # api/v1/vech/bikes/2   -GET
        # api/v1/vech/bikes/2   -PUT
        # api/v1/vech/bikes/2   -DELETE
class BikeDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        bks=Bikes.objects.get(id=id)
        serializer=BikeSerializers(bks)
        return  Response(data=serializer.data)


    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        bk=Bikes.objects.get(id=id)
        bk.delete()
        return Response({"msg":"deleted"})


    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        bk=Bikes.objects.filter(id=id)
        serializer=BikeSerializers(instance=bk,data=request.data)
        if serializer.is_valid():
            bk.update(**serializer.validated_data)
            return  Response({'msg':'updated'})
        else:
            return Response(data=serializer.errors)

            #api/v2/vech/bikes/     -GET
            #api/v2/vech/bikes/     -POST
class BikeModelViews(APIView):
    def get(self,request,*args,**kwargs):
        bk=Bikes.objects.all()
        serializer=BikeModelserializer(bk,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=BikeModelserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


        # api/v1/vech/bikes/2   -GET
        # api/v1/vech/bikes/2   -PUT
        # api/v1/vech/bikes/2   -DELETE
class BikeModelDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        bk=Bikes.objects.get(id=id)
        serializer=BikeModelserializer(bk)
        return  Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        bk=Bikes.objects.get(id=id)
        serializer=BikeModelserializer(instance=bk,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(data=serializer.data)
        else:
            return  Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        bk=Bikes.objects.get(id=id)
        bk.delete()
        return  Response({"msg":"deleted"})
