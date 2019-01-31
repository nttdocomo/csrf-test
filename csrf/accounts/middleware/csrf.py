"""
Cross Site Request Forgery Middleware.
This module provides a middleware that implements protection
against request forgeries from other sites.
"""
from __future__ import unicode_literals

class DisableCSRFMiddleware(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)