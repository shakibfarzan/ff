import os
from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from categories.models import Category, SubCategory
from .models import Photo
from .serializers import PhotoSerializer

class PhotoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        queryset = Photo.objects.all()
        slug = self.request.query_params.get('slug')
        if slug is not None:
            queryset = Photo.objects.filter(category__slug=slug)
            sub = self.request.query_params.get('sub')
            if sub is not None:
                queryset = Photo.objects.filter(category__slug=slug, sub_category__slug=sub)
        return queryset
    
    def post(self, request, *args, **kwargs):
        src = request.data['src']
        name = request.data['name']
        category = Category.objects.get(pk=request.data['category'])
        sub_category = SubCategory.objects.get(pk=request.data['sub_category'])
        Photo.objects.create(name=name, category=category, src=src, sub_category=sub_category)
        return Response({"message": "Uploaded"})
    

class PhotoUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    lookup_field = 'pk'


        
class PhotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        os.remove(instance.src.path)