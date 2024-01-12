from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializer import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


def get_json_data(query, serializer, count=None, many=False):
    if count:
        query = query[:count]
    else:
        query = query.order_by('-id')[:count]
    if many:
        data = serializer(query, many=True).data
    else:
        data = serializer(query).data
    return data


@api_view(['GET'])
def get_banner(request):
    return Response(get_json_data(Banner.objects.last(), BannerSerializer))


@api_view(['GET'])
def get_about(request):
    return Response(get_json_data(AboutUs.objects.last(), AboutUs))


@api_view(['GET'])
def get_mini_about(request):
    return Response(get_json_data(Feature.objects.all(), FeatureSerializer, 4, True))


@api_view(['GET'])
def get_products_for_main(request):
    return Response(get_json_data(Product.objects.all(), ProductSerializer, 8, True))


@api_view(['GET'])
def get_service(request):
    return Response(get_json_data(Service, ServiceSerializer, 'all', 4))


@api_view(['GET'])
def get_category_for_main(request):
    return Response(get_json_data(Category, CategorySerializer, 'all', 10))


@api_view(['GET'])
def get_feedback(request):
    return Response(get_json_data(Feedback, FeatureSerializer, 'all'))


@api_view(['GET'])
def get_about_us_number(request):
    return Response(get_json_data(AboutUs, AboutUsSerializer, 'all', 4))


@api_view(['GET'])
def get_blog(request):
    return Response(get_json_data(Blog, BlogSerializer, 'all', 2))


@api_view(['GET'])
def get_faq(request):
    return Response(get_json_data(Faq, FaqSerializer, 'all', 8))


@api_view(['GET'])
def get_category(request):
    return Response(get_json_data(Category, CategorySerializer, 'all'))


@api_view(['GET'])
def get_description(request, number):
    query = Description.objects.filter(choice=number)
    return Response(DescriptionSerializer(query, many=True).data)


@api_view(['GET'])
def get_product_detail(request, pk):
    query = Product.objects.get(id=pk)
    return Response(DescriptionSerializer(query).data)


@api_view(['GET'])
def get_product_detail(request, pk):
    query = Product.objects.get(id=pk)
    return Response(DescriptionSerializer(query).data)


@api_view(['GET'])
def get_portfolio(request):
    return Response(get_json_data(Portfolio, PortfolioSerializer, 'all'))


@api_view(['GET'])
def get_service(request):
    return Response(get_json_data(Service, ServiceSerializer, 'all', 10))


@api_view(['GET'])
def get_service_extra(request):
    query = Service.objects.all().order_by('-id')[10:]
    return Response(ServiceSerializer(query, many=True).data)


@api_view(['GET'])
def get_partner(request):
    return Response(get_json_data(Partner, PartnerSerializer, 'all'))


@api_view(['GET'])
def get_production(request):
    return Response(get_json_data(Production, ProductionSerializer, 'last'))


@api_view(['GET'])
def get_jobs(request):
    return Response(get_json_data(Job, JobSerializer, 'all'))


@api_view(['GET'])
def get_history(request):
    return Response(get_json_data(History, HistorySerializer, 'last'))


@api_view(['GET'])
def get_blog(request):
    return Response(get_json_data(Blog, BlogSerializer, 'all'))


@api_view(['GET'])
def get_contact(request):
    return Response(get_json_data(Contact, ContactSerializer, 'last'))


@api_view(['GET'])
def get_faq(request):
    return Response(get_json_data(Faq, FaqSerializer, 'all'))


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def add_cart(request):
    user = request.user
    product_id = request.POST.get("product")
    quantity = request.POST.get("quantity")
    product = Product.objects.get(id=product_id)
    price = product.bonus if product.bonus else product.price
    Cart.objects.create(user=user, product=product, quantity=quantity, price=price)
    return Response({"message": True})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    data = CartSerializer(cart, many=True).data
    return Response(data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def remove_cart(request, pk):
    user = request.user
    cart = Cart.objects.get(id=pk)
    if user == cart.user:
        cart.delete()
    return Response({'message': True})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_order(request, pk):
    user = request.user
    order = Order.objects.create(
        full_name=request.POST.get('full_name'),
        inn=request.POST.get('inn'),
        phone=request.POST.get('phone'),
        email=request.POST.get('email'),
        status=request.POST.get('status'),
        address=request.POST.get('address'),
        comment=request.POST.get('comment'),
    )
    for i in Cart.objects.filter(user=user):
        OrderItem.objects.create(order=order, product=i.product, quantity=i.quantity, price=i.product.bonus if i.product.bonus else i.product.price)
    Cart.objects.filter(user=user).delete()
    return Response({'message': True})


@api_view(['POST'])
def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            token, create = Token.objects.get_or_create(user=user)
            data = {
                "sucess": True,
                "user_id": user.id,
                "username": user.username,
                'token': token.key
            }
        else:
            data = {
                "success": False,
                "message": 'Password is wrong'
            }
    except Exception as e:
        data = {
            "success": False,
            "message": f'{e}'
        }
    return data