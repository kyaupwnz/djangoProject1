from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ProductDetailView, RecordListView, RecordCreateView, RecordUpdateView, RecordDeleteView, RecordDetailView, \
    ProductUpdateWithVersionView, ModeratorProductUpdateView, CategoryListView

app_name = CatalogConfig.name


urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    #path('products/', products, name='products'),
    path('products/', login_required(ProductListView.as_view()), name='product_list'),
    path('category_list/', login_required(CategoryListView.as_view()), name='category_list'),
    path('create/', login_required(ProductCreateView.as_view()), name='create'),
    path('update/<int:pk>/', cache_page(60)(login_required(ProductUpdateWithVersionView.as_view())), name='update'),
    path('moderate/<int:pk>/', login_required(ModeratorProductUpdateView.as_view()), name='moderate'),
    path('delete/<int:pk>/', login_required(ProductDeleteView.as_view()), name='delete'),
    path('detail/<int:pk>/', cache_page(60)(login_required(ProductDetailView.as_view())), name='detail'),
    path('records/', RecordListView.as_view(), name='record_list'),
    path('create_record/', RecordCreateView.as_view(), name='create_record'),
    path('update/<slug:slug>/', RecordUpdateView.as_view(), name='update_record'),
    path('delete/<slug:slug>/', RecordDeleteView.as_view(), name='delete_record'),
    path('detail/<slug:slug>/', RecordDetailView.as_view(), name='record_detail')
]