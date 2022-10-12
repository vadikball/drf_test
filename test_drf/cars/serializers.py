from rest_framework import serializers
from django.db.models import Sum

from cars.models import Color, Brand, CarModel, Order


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = '__all__'


class ReadOnlyCarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        exclude = ('brand', )


class OrderSerializer(serializers.ModelSerializer):

    car_model = serializers.PrimaryKeyRelatedField(write_only=True, queryset=CarModel.objects.all())
    color = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Color.objects.all())

    model = serializers.SerializerMethodField(read_only=True)
    brand = serializers.SerializerMethodField(read_only=True)
    color_type = serializers.SerializerMethodField(read_only=True)

    def get_model(self, obj: Order):
        return ReadOnlyCarModelSerializer(instance=obj.car_model).data

    def get_color_type(self, obj: Order):
        return ColorSerializer(instance=obj.color).data

    def get_brand(self, obj: Order):
        return BrandSerializer(instance=obj.car_model.brand).data

    class Meta:
        model = Order
        fields = '__all__'


class OrderedColorSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField(read_only=True)
    amount = serializers.SerializerMethodField(read_only=True)

    def get_color(self, obj):
        return ColorSerializer(instance=obj).data

    def get_amount(self, obj):
        ordered_amount = Order.objects.filter(
            color=obj.id
        ).aggregate(ordered_amount=Sum('amount'))['ordered_amount']
        if ordered_amount is None:
            ordered_amount = 0
        return ordered_amount

    class Meta:
        model = Color
        fields = ('color', 'amount', )


class OrderedBrandSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField(read_only=True)
    amount = serializers.SerializerMethodField(read_only=True)

    def get_brand(self, obj):
        return BrandSerializer(instance=obj).data

    def get_amount(self, obj):
        ordered_amount = Order.objects.filter(
            car_model__brand=obj.id
        ).aggregate(ordered_amount=Sum('amount'))['ordered_amount']
        if ordered_amount is None:
            ordered_amount = 0
        return ordered_amount

    class Meta:
        model = Brand
        fields = ('brand', 'amount', )
