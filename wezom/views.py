from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import *
import requests


URL_API_VIN = "http://atlanticexpress.com.ua/api/v1/vehicle/decodevin/"


class BrandView(APIView):
    """

    """
    def get(self, request):
        brand = Brand.objects.all()
        serializer = BrandSerializer(brand, many=True)
        return Response(serializer.data)


class CreateBrand(APIView):
    def get(self, request):
        brand_list = requests.get("https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json")
        if brand_list.status_code == 200:
            list_save =[x['Make_Name'] for x in brand_list.json()["Results"]]
            list_save = [Brand(name=n) for n in list_save]
            Brand.objects.bulk_create(list_save)


class AutoLostCreate(generics.CreateAPIView):
    serializer_class = LostAutoCreateSerializer
    """

    """
    def post(self, request):
        review = LostAutoCreateSerializer(data=request.data)
        if request.data.get("user") and request.data.get("number") and request.data.get("vin_code") and request.data.get("color"):

        # print(request.data)
        # if review.is_valid():
            vin_code = request.data.get("vin_code")
            request_api = requests.get(f"{URL_API_VIN}{vin_code}")
            if request_api.status_code == 200:
                request_api_json = request_api.json()
                brand_api = request_api_json[6].get('Value')
                model = request_api_json[8].get('Value')
                brand = Brand.objects.get_or_create(name=brand_api)
                model = Model.objects.get_or_create(name=model, brand=brand[0])
            lost_auto = LostAuto.objects.create(user=request.data.get("user"), vin_code=request.data.get("vin_code"), number=request.data.get("number"), color=request.data.get("color"),
                                                brand=brand[0], model=model[0])
        return Response(status=201)


class AutoLostView(APIView):
    def get(self, request):
        list_lost_auto = LostAuto.objects.all()
        serializer = LostAutoSerializer(list_lost_auto, many=True)
        return Response(serializer.data)


class ModelView(APIView):
    def get(self, request):
        model = Model.objects.all()
        serializer = BrandSerializer(model, many=True)
        return Response(serializer.data)