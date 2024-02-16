from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .admin import AutomobileResource, CountryResource, ManufacturerResource, CommentariesResource
from .models import (Country,
                     Manufacturer,
                     Automobile,
                     Commentaries)
from .serializers import (CountryListSerializer,
                          CountrySerializer,
                          ManufacturerListSerializer,
                          ManufacturerSerializer,
                          AutomobileListSerializer,
                          AutomobileSerializer,
                          CommentListSerializer,
                          CommentSerializer)


def export_auto(request):
    if request.GET.get("format"):
        dataset = AutomobileResource().export()
        format = request.GET.get("format")
        ds = ""
        if format == "xls":
            ds = dataset.xls
        elif format == "csv":
            ds = dataset.csv

        response = HttpResponse(ds, content_type=f"{format}")
        response["Content-Disposition"] = f"attachment; filename=auto.{format}"
        return response
    return HttpResponse("Добавьте GET запрос к адресу браузера ?format=xls или csv")


def export_country(request):
    if request.GET.get("format"):
        dataset = CountryResource().export()
        format = request.GET.get("format")
        if format == "xls":
            ds = dataset.xls
        elif format == "csv":
            ds = dataset.csv
        response = HttpResponse(ds, content_type=f"{format}")
        response["Content-Disposition"] = f"attachment; filename=country.{format}"
        return response
    return HttpResponse("Добавьте GET запрос к адресу браузера ?format=xls или csv")


def export_manufacturer(request):
    if request.GET.get("format"):
        dataset = ManufacturerResource().export()
        format = request.GET.get("format")
        if format == "xls":
            ds = dataset.xls
        elif format == "csv":
            ds = dataset.csv
        response = HttpResponse(ds, content_type=f"{format}")
        response["Content-Disposition"] = f"attachment; filename=manufacturer.{format}"
        return response
    return HttpResponse("Добавьте GET запрос к адресу браузера ?format=xls или csv")


def export_commentaries(request):
    if request.GET.get("format"):
        dataset = CommentariesResource().export()
        format = request.GET.get("format")
        if format == "xls":
            ds = dataset.xls
        elif format == "csv":
            ds = dataset.csv

        response = HttpResponse(ds, content_type=f"{format}")
        response["Content-Disposition"] = f"attachment; filename=commentaries.{format}"
        return response
    return HttpResponse("Добавьте GET запрос к адресу браузера ?format=xls или csv")


class CountryListView(ListAPIView):
    queryset = Country.objects.order_by('title')
    serializer_class = CountryListSerializer


class CountryView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        country = Country.objects.filter(pk=pk)
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method 'PUT' not allowed"}, status=403)
        try:
            instance = Country.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"}, status=400)

        serializer = CountrySerializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=202)
        else:
            return Response(status=400)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method 'DELETE' not allowed"}, status=403)
        try:
            instance = Country.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"}, status=400)
        instance.delete()
        return Response("Deleted")


class ManufacturerListView(ListAPIView):
    queryset = Manufacturer.objects.order_by('title')
    serializer_class = ManufacturerListSerializer


class ManufacturerView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        manufacturer = Manufacturer.objects.filter(pk=pk)
        serializer = ManufacturerSerializer(manufacturer, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method 'PUT' not allowed"}, status=403)
        try:
            instance = Manufacturer.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"}, status=400)

        serializer = ManufacturerSerializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=202)
        else:
            return Response(status=400)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method 'DELETE' not allowed"}, status=403)
        try:
            instance = Manufacturer.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"}, status=400)
        instance.delete()
        return Response("Deleted")


class AutomobilesListView(ListAPIView):
    queryset = Automobile.objects.order_by('title')
    serializer_class = AutomobileListSerializer


class AutomobileView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = [TokenAuthentication,]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        automobile = Automobile.objects.filter(pk=pk)
        serializer = AutomobileSerializer(automobile, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AutomobileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method 'PUT' not allowed"}, status=403)
        try:
            instance = Automobile.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"}, status=400)

        serializer = AutomobileSerializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=202)
        else:
            return Response(status=400)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method 'DELETE' not allowed"}, status=403)
        try:
            instance = Automobile.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"}, status=400)
        instance.delete()
        return Response("Deleted")


class CommentListView(ListAPIView):
    queryset = Commentaries.objects.all()
    serializer_class = CommentListSerializer


class CommentView(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        comment = Commentaries.objects.filter(pk=pk)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pk = kwargs.get("pk", None)
            if not pk:
                return Response({"error": "Method 'PUT' not allowed"}, status=403)
            try:
                instance = Commentaries.objects.get(pk=pk)
            except:
                return Response({"error": "Object does not exist"}, status=400)

            serializer = CommentSerializer(data=request.data, instance=instance)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(status=202)
            else:
                return Response(status=400)
        else:
            return Response(status=403)

    def delete(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pk = kwargs.get("pk ", None)
            if not pk:
                return Response({"error": "Method 'DELETE' not allowed"}, status=403)
            try:
                instance = Commentaries.objects.get(pk=pk)
            except:
                return Response({"error": "Object does not exist"}, status=400)
            instance.delete()
            return Response("Deleted")
        else:
            return Response(status=403)