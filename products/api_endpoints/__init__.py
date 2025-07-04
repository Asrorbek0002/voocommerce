from .ProductsList import *
from .ProductCreate import *
from .ProductDelete import *
from .ProductUpdate import *

from .CategoryList import *
from .CategoryDelete import *
from .CategoryUpdate import *
from .CategoryCreate import *

from .BrandList import *
from .BrandDelete import *
from .BrandUpdate import *
from .BrandCreate import *

from .Color import *

from .Size import *

from .ReviewComment import *

from .Story import *

__all__ = [
    "BrandCreateAPIView",
    "BrandListAPIView",
    "BrandUpdateAPIView",
    "BrandDeleteAPIView",
    "BrandRetrieveAPIView",
    "CategoryListAPIView",
    "CategoryCreateAPIView",
    "CategoryUpdateAPIView",
    "CategoryDeleteAPIView",
    "CategoryRetrieveAPIView",
    "ProductCreateAPIView",
    "ProductListAPIView",
    "ProductUpdateAPIView",
    "ProductDeleteAPIView",
    "ProductRetrieveAPIView",
    "SizeListCreateAPIView",
    "SizeRetrieveUpdateDestroyView",
    "ColorListCreateView",
    "ColorRetrieveUpdateDestroyView",
    "ReviewCreateAPIView",
    "UserReviewsListAPIView",
    "ReviewDeleteAPIView",
    "CommentCreateAPIView",
    "UserCommentListAPIView",
    "CommentDeleteAPIView",
    "StoryCreateAPIView",
    "StoryListAPIView",
    "StoryRetrieveAPIView",
    "StoryUpdateAPIView",
    "StoryDeleteAPIView",
]




