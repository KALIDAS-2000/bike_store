from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from bike.models import bikes

class BikesView(APIView):
    def get(self,request,*args,**kwargs):
        all_bike=bikes
        if 'brand' in request.query_params:
            bnd=request.query_params.get('brand')
            all_bike=[bk for bk in bikes if bk.get('brand')==bnd].pop()
        if 'colour' in request.query_params:
            clr=request.query_params.get('colour')
            all_bike=[bk for bk in bikes if bk.get('colour')==clr].pop()
        return Response ({"bikes":all_bike})


    # def post(self,request,*args,**kwargs):
    #     data=request.data
    #     return Response ({'msg':data})


class BikesDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        rs=[ b for b in bikes if b.get('id')==id]
        return Response ({'details':rs})

    def put(self, request, *args, **kwargs):
        id=kwargs.get('id')
        data=request.data
        instance = [bk for bk in bikes if bk.get('id') == id].pop()
        instance.update(data)
        return Response({'data': instance})

    def delete(self,request,*args,**kwargs):
        id=kwargs.get('id')
        instance=[bk for bk in bikes if bk.get('id')==id].pop()
        bikes.remove(instance)
        return Response ({'delete':instance})
