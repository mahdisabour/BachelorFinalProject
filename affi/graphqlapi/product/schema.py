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



class ProductQuery(ObjectType):
    # product_image = PlainTextNode.Field(ImageNode)
    all_product_image = DjangoFilterConnectionField(ImageNode)

    # dimension = PlainTextNode.Field(DimensionNode)
    all_dimension = DjangoFilterConnectionField(DimensionNode)

    # download = PlainTextNode.Field(DownloadNode)
    all_download = DjangoFilterConnectionField(DownloadNode)

    # tag = PlainTextNode.Field(TagNode)
    all_tag = DjangoFilterConnectionField(TagNode)

    # review = PlainTextNode.Field(ReviewNode)
    all_review = DjangoFilterConnectionField(ReviewNode)

    # product = PlainTextNode.Field(ProductNode)
    all_product = DjangoFilterConnectionField(ProductNode)
