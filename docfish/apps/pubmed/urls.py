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

from django.conf.urls import url
from django.views.generic.base import TemplateView
import docfish.apps.pubmed.views as pmc_views
import docfish.apps.pubmed.actions as actions

urlpatterns = [

    # Pubmed search
    url(r'^search$', pmc_views.search_view, name="search_pubmed"),
    url(r'^searching$', pmc_views.searching_view, name="searching_pubmed"),
    url(r'^searching/(?P<page>\d+)/$', pmc_views.searching_view, name="searching_pubmed"),

    # Adding to collections
    url(r'^collection/(?P<cid>\d+)/add$',actions.add_papers,name='collection_add_papers'),

]
