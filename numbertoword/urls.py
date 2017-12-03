from django.conf.urls import include, url
from django.contrib import admin
from numword import views
from numword.extra_views import numbersubmit

urlpatterns = [
    # Examples:
    # url(r'^$', 'numbertoword.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^submit/', views.convert, name='submit'),
    url(r'^submit_intercool/', numbersubmit.SearchSubmitView.as_view(),name='search-ajax-submit')

]
