# coding=utf-8
"""View for presentation's search functionality"""
from django.http import JsonResponse
from django.views.generic import View

from prezi.mixins import AjaxViewMixin
from prezi.mixins import MethodRestrictionViewMixin

from search.models import Presentation


class PresentationsView(AjaxViewMixin, MethodRestrictionViewMixin, View):
    """View that receives a search request and returns result in json format"""

    allowed_http_methods = ['post']

    def post(self, request, *args, **kwargs):

        # get filters to query db
        filters = self.get_filters(request)

        # Querying db
        records = Presentation.objects.filter(**filters).order_by("-date_added")

        # Serializing records
        records = self.custom_slots_serializer(records)

        return JsonResponse(records, safe=False)

    def custom_slots_serializer(self, records):
        """Searializer method to convert query object into normal json format"""
        response = [{
            'id': record.custom_id,
            'title': record.title,
            'thumbnail': record.thumbnail,
            'creator_name': record.creator_name,
            'creator_profile_url': record.creator_profile_url,
            'date_added': record.date_added,
            'last_updated': record.last_updated,
        } for record in records]

        return response

    def get_filters(self, request):
        """Method to get request and return a filter dict."""
        filters = dict()

        title = request.POST.get('title', None)

        if title:
            filters['title__contains'] = title

        return filters
