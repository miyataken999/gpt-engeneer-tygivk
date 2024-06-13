from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Shop
from .serializers import ShopSerializer

class ShopView(APIView):
    def get(self, request):
        shops = Shop.objects.filter(
            Q(category__icontains='Fluorescence') |
            Q(category__icontains='Carat') |
            Q(category__icontains='Color Grade') |
            Q(category__icontains='Cutting Style') |
            Q(name__icontains='FLUORESCENCE') |
            Q(category__icontains='Round Brilliant') |
            Q(subcategory__icontains='CUT PROPORTION') |
            Q(subcategory__icontains='CUT GRADE') |
            Q(subcategory__icontains='POLISH') |
            Q(subcategory__icontains='SYMMETRY') |
            Q(subcategory__icontains='THIN-MEDIUM') |
            Q(subcategory__icontains='MEDIUM WHITISH BLUE')
        ).filter(price__gte=0, price__lte=4.41)
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)