from graphene import ObjectType 
from graphene_django.filter import DjangoFilterConnectionField

from .types import (
    PlainTextNode, 
    ImageNode, 
    DimensionNode,
    DownloadNode,
    TagNode, 
    ReviewNode, 
    ProductNode
)
from .filters import ProductFilter



class ProductQuery(ObjectType):
    all_product_image = DjangoFilterConnectionField(ImageNode)
    all_dimension = DjangoFilterConnectionField(DimensionNode)
    all_download = DjangoFilterConnectionField(DownloadNode)
    all_tag = DjangoFilterConnectionField(TagNode)
    all_review = DjangoFilterConnectionField(ReviewNode)
    all_product = DjangoFilterConnectionField(ProductNode, filterset_class=ProductFilter)

    
