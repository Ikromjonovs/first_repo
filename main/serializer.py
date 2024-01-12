from rest_framework.serializers import ModelSerializer
from .models import *


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"


class FeatureSerializer(ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class DescriptionSerializer(ModelSerializer):
    class Meta:
        model = Description
        fields = "__all__"


class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class ProductPhotoSerializer(ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = "__all__"


class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"


class AboutUsNumberSerializer(ModelSerializer):
    class Meta:
        model = AboutUsNumber
        fields = "__all__"


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class FaqSerializer(ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"


class SubscriberSerializer(ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"


class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"


class ProductionSerializer(ModelSerializer):
    class Meta:
        model = Production
        fields = "__all__"


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class HistorySerializer(ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"


class HistoryInfoSerializer(ModelSerializer):
    class Meta:
        model = HistoryInfo
        fields = "__all__"


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class WorkingHoursSerializer(ModelSerializer):
    class Meta:
        model = WorkingHours
        fields = "__all__"


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

