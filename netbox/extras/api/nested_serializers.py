from rest_framework import serializers

from extras import choices, models
from netbox.api.fields import ChoiceField
from netbox.api.serializers import NestedTagSerializer, WritableNestedSerializer
from users.api.nested_serializers import NestedUserSerializer

__all__ = [
    'NestedConfigContextSerializer',
    'NestedConfigTemplateSerializer',
    'NestedCustomFieldSerializer',
    'NestedCustomLinkSerializer',
    'NestedExportTemplateSerializer',
    'NestedImageAttachmentSerializer',
    'NestedJobResultSerializer',
    'NestedJournalEntrySerializer',
    'NestedSavedFilterSerializer',
    'NestedTagSerializer',  # Defined in netbox.api.serializers
    'NestedWebhookSerializer',
]


class NestedWebhookSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='extras-api:webhook-detail')

    class Meta:
        model = models.Webhook
        fields = ['id', 'url', 'display', 'name']


class NestedCustomFieldSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='extras-api:customfield-detail')

    class Meta:
        model = models.CustomField
        fields = ['id', 'url', 'display', 'name']


class NestedCustomLinkSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='extras-api:customlink-detail')

    class Meta:
        model = models.CustomLink
        fields = ['id', 'url', 'display', 'name']


class NestedConfigContextSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='extras-api:configcontext-detail')

    class Meta:
        model = models.ConfigContext
        fields = ['id', 'url', 'display', 'name']


class NestedConfigTemplateSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='extras-api:configtemplate-detail')

    class Meta:
        model = models.ConfigTemplate
        fields = ['id', 'url', 'display', 'name']


class NestedExportTemplateSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='extras-api:exporttemplate-detail')

    class Meta:
        model = models.ExportTemplate
        fields = ['id', 'url', 'display', 'name']


class NestedSavedFilterSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='extras-api:savedfilter-detail')

    class Meta:
        model = models.SavedFilter
        fields = ['id', 'url', 'display', 'name', 'slug']


class NestedImageAttachmentSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='extras-api:imageattachment-detail')

    class Meta:
        model = models.ImageAttachment
        fields = ['id', 'url', 'display', 'name', 'image']


class NestedJournalEntrySerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='extras-api:journalentry-detail')

    class Meta:
        model = models.JournalEntry
        fields = ['id', 'url', 'display', 'created']


class NestedJobResultSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='extras-api:jobresult-detail')
    status = ChoiceField(choices=choices.JobResultStatusChoices)
    user = NestedUserSerializer(
        read_only=True
    )

    class Meta:
        model = models.JobResult
        fields = ['url', 'created', 'completed', 'user', 'status']
