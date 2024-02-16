from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *


class CountryListSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = [
            "id",
            "title",
            "manufacturer"
        ]


class ManufacturerListSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            "id",
            "title",
            "country",
            "automobile"
        ]


class AutomobileListSerializer(ModelSerializer):
    class Meta:
        model = Automobile
        fields = [
            "id",
            "title",
            "manufacturer",
            "start_year",
            "end_year",
        ]


class CommentListSerializer(ModelSerializer):

    class Meta:
        model = Commentaries
        fields = [
            "id",
            "email",
            "automobile",
            "create_data",
            "comment",
        ]


class CountrySerializer(ModelSerializer):
    manufacturers = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = [
            "id",
            "title",
            "manufacturers",
        ]

    def get_manufacturers(self, instance):
        result = [{manufacturer.id: manufacturer.title}
                  for manufacturer in Manufacturer.objects.filter(country=instance.id)]
        return result

    def create(self, validated_data):
        country = Country.objects.update_or_create(
            title=validated_data.get("title", None),
        )
        return country

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.save()

        return instance


class ManufacturerSerializer(ModelSerializer):
    automobiles = serializers.SerializerMethodField()

    class Meta:
        model = Manufacturer
        fields = [
            "id",
            "title",
            "country",
            "automobiles",
        ]

    def get_automobiles(selfs, instance):
        result = [{auto.title: [{"commentaries":
            len(Commentaries.objects.select_related("automobile").filter(
                automobile_id=auto.id))}]}
            for auto in Automobile.objects.select_related("manufacturer")
            if auto.manufacturer.id == instance.pk]
        return result

    def create(self, validated_data):
        manufacturer = Manufacturer.objects.update_or_create(
            title=validated_data.get("title", None),
            country=validated_data.get("country", None),
        )
        return manufacturer

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.country = validated_data.get("country", instance.country)
        instance.save()

        return instance


class AutomobileSerializer(ModelSerializer):
    title = serializers.CharField(max_length=100)
    start_year = serializers.IntegerField(max_value=9999, min_value=0)
    end_year = serializers.IntegerField(max_value=9999, min_value=0)
    comment_count = serializers.SerializerMethodField()
    commentaries = serializers.SerializerMethodField()

    class Meta:
        model = Automobile
        fields = [
            "id",
            "title",
            "manufacturer",
            "start_year",
            "end_year",
            "comment_count",
            "commentaries",
        ]

    def get_comment_count(self, instance):
        return (len(Commentaries.objects.filter(automobile=instance.id)))

    def get_commentaries(self, instance):
        result = [{com.id: com.comment} for com in
                  Commentaries.objects.filter(automobile=instance.id)]
        return result

    def create(self, validated_data):
        automobile = Automobile.objects.update_or_create(
            title=validated_data.get("title", None),
            manufacturer=validated_data.get("manufacturer", None),
            start_year=validated_data.get("start_year"),
            end_year=validated_data.get("end_year")

        )
        return automobile

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.manufacturer = validated_data.get("manufacturer", instance.manufacturer)
        instance.start_year = validated_data.get("start_year", instance.start_year)
        instance.end_year    = validated_data.get("end_year", instance.end_year)
        instance.save()

        return instance


class CommentSerializer(ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = Commentaries
        fields = [
            "id",
            "email",
            "automobile",
            "create_data",
            "comment",
        ]

    def create(self, validated_data):
        comment = Commentaries.objects.update_or_create(
            email=validated_data.get("email"),
            automobile=validated_data.get("automobile", None),
            comment=validated_data.get("comment")

        )
        return comment

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.email = validated_data.get("email", instance.email)
        instance.automobile = validated_data.get("automobile", instance.automobile)
        instance.create_data = validated_data.get("create_data", instance.create_data)
        instance.comment = validated_data.get("comment", instance.comment)
        instance.save()

        return instance
