from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer
from .validators import validate_create


class ProductListAPIView(ListAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    pagination_class = PageNumberPagination
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def post(self, request):
        is_valid, error_message = validate_create(request.data)
        if not is_valid:
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        product = Product.objects.create(
            title=request.data.get("title"),
            content=request.data.get("content"),
            image=request.data.get("image"),
            seller=request.user
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, productId):
        return get_object_or_404(Product, id=productId)

    def get(self, request, productId):
        product = self.get_object(productId)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, productId):
        product = self.get_object(productId)
        if product.seller == request.user:
            serializer = ProductSerializer(
                product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error_message": "수정 권한이 없습니다."}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, productId):
        product = self.get_object(productId)
        if product.seller == request.user:
            product.delete()
            data = f"{productId}번 게시물 삭제"
            return Response(data)
        else:
            return Response({"error_message": "수정 권한이 없습니다."}, status=status.HTTP_401_UNAUTHORIZED)
