# coding=utf-8
"""Mixins can be used in all apps"""
from django import http


class AjaxViewMixin(object):
    """AjaxViewMixin
    Only allows ajax requests in whatever view this is mixed into.
    """

    def dispatch(self, request, *args, **kwargs):
        request_meta = request.META

        if 'HTTP_X_REQUESTED_WITH' not in request_meta or not request.is_ajax():
            raise http.Http404("Only AJAX requests are allowed to this view")

        return super(AjaxViewMixin, self).dispatch(request, *args, **kwargs)


class MethodRestrictionViewMixin(object):
    """MethodRestrictionViewMixin
    Only allows defined requests in whatever view this is mixed into.
    """
    allowed_http_methods = ['post', 'get']

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() not in self.allowed_http_methods:
            raise http.Http404("Method not allowed")

        return super(MethodRestrictionViewMixin, self).dispatch(request, *args, **kwargs)
