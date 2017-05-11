'''

Copyright (c) 2017 Vanessa Sochat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

from django.views.generic.base import (
    TemplateView,
    RedirectView
)
from django.conf.urls import include, url
import notifications.urls
import docfish.apps.base.views as base_views

favicon_view = RedirectView.as_view(url='/static/img/favicon/favicon.ico', 
                                    permanent=True)

urlpatterns = [
    url(r'^$', base_views.index_view, name="index"),
    url(r'^about$', base_views.about_view, name="about"),
    url(r'^data$', base_views.data_view, name="data"),
    url(r'^guide$', base_views.user_guide_view, name="user_guide"),
    url(r'^favicon\.ico$', favicon_view),
    url(r'^notifications/', include(notifications.urls,namespace='notifications')),
#    url(r'^saml.xml$', base_views.saml_metadata_view, name="samlxml")
]
