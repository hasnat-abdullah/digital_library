from rest_framework import viewsets
from rest_framework import serializers


class CustomModelViewSet(viewsets.ModelViewSet):
    """
    Mixed permission base model allowing for action level
    permission control. Subclasses may define their permissions
    by creating a 'permission_classes_by_action' variable.

    Example:
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAdmin]}
    """

    permission_classes_by_action = {}
    serializer_classes_by_action = {}

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


    def get_serializer_class(self):
        """
        A class which inhertis this mixins should have variable
        `serializer_action_classes`.

        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:

        class SampleViewSet(viewsets.ViewSet):
            serializer_class = SomethingDetailsSerializer
            serializer_action_classes = {
               'upload': UploadDocumentSerializer,
               'list': SomethingListSerializer,
            }
            def list():
                ...

            @action
            def upload:
                ...

        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.
        """
        try:
            return self.serializer_classes_by_action[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()


class CustomModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields_by_action` argument that
    controls which fields should be displayed.
    """

    def create(self, validated_data):
        try:
            self.Meta.model._meta.get_field('created_by')
            validated_data['created_by'] = self.context['request'].user
        except Exception:
            pass
        return super().create(validated_data)

    def update(self, instance, validated_data):
        try:
            self.Meta.model._meta.get_field('updated_by')
            validated_data['updated_by'] = self.context['request'].user
        except Exception:
            pass
        return super().update(instance, validated_data)
