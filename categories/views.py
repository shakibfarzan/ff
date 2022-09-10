from rest_framework import generics, permissions, authentication
from .models import Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        slug = serializer.validated_data.get('slug')
        if slug is None:
            list_str = name.split(' ')
            slug = '-'.join(list_str).lower()
        serializer.save(slug=slug)


class CategoryDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class CategoryUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        slug = serializer.validated_data.get('slug')
        if slug is None:
            list_str = name.split(' ')
            slug = '-'.join(list_str).lower()
        serializer.save(slug=slug)


class CategoryDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class SubCategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = SubCategory.objects.all()
        parent = self.request.query_params.get('parent')
        if parent is not None:
            queryset = SubCategory.objects.filter(parent_category=parent)
        return queryset
    
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        slug = serializer.validated_data.get('slug')
        if slug is None:
            list_str = name.split(' ')
            slug = '-'.join(list_str).lower()
        serializer.save(slug=slug)

class SubCategoryUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        slug = serializer.validated_data.get('slug')
        if slug is None:
            list_str = name.split(' ')
            slug = '-'.join(list_str).lower()
        serializer.save(slug=slug)


class SubCategoryDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
