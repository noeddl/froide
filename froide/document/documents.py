from django_elasticsearch_dsl import DocType, fields

from froide.helper.search import (
    get_index, get_text_analyzer, get_search_analyzer
)

from filingcabinet.models import Page


index = get_index('documentpage')
analyzer = get_text_analyzer()
search_analyzer = get_search_analyzer()


@index.doc_type
class PageDocument(DocType):
    document = fields.IntegerField(attr='document_id')

    title = fields.TextField(
        analyzer=analyzer,
        search_analyzer=search_analyzer,
    )
    description = fields.TextField(
        analyzer=analyzer,
        search_analyzer=search_analyzer,
    )

    tags = fields.ListField(fields.KeywordField())
    created_at = fields.DateField()

    publicbody = fields.IntegerField(attr='document.publicbody_id')
    jurisdiction = fields.IntegerField(attr='document.publicbody.jurisdiction_id')
    foirequest = fields.IntegerField(attr='document.foirequest_id')
    campaign = fields.IntegerField(attr='document.foirequest.campaign_id')

    user = fields.IntegerField(attr='document.user_id')
    team = fields.IntegerField(attr='document.team_id')

    public = fields.BooleanField()

    number = fields.IntegerField()
    content = fields.TextField(
        analyzer=analyzer,
        search_analyzer=search_analyzer,
        index_options='offsets',
    )

    class Meta:
        model = Page
        queryset_chunk_size = 50

    def get_queryset(self):
        """Not mandatory but to improve performance we can select related in one sql request"""
        return super().get_queryset().select_related(
            'document',
        )

    def prepare_title(self, obj):
        if obj.number == 1:
            return obj.document.title
        return ''

    def prepare_description(self, obj):
        if obj.number == 1:
            return obj.document.description
        return ''

    def prepare_tags(self, obj):
        return [tag.id for tag in obj.document.tags.all()]

    def prepare_created_at(self, obj):
        return obj.document.created_at

    def prepare_public(self, obj):
        return obj.document.is_public()

    def prepare_team(self, obj):
        if obj.document.team_id:
            return obj.document.team_id
        return None
