from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


@api_view(["GET","POST"])
def category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category,many =True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)


@api_view(["PUT"])
def category_update(request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": 'Not found'},status=404)
        serializer = CategorySerializer(category,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

@api_view(["DELETE"])
def category_delete(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"error":'not found'},status=404)
    category.delete()
    return Response(status=204)





@api_view(["GET", "POST"])
def product(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


@api_view(["PUT"])
def product_update(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    serializer = ProductSerializer(product, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(["DELETE"])
def product_delete(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    product.delete()
    return Response(status=204)
