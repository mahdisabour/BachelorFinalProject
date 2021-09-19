class ReviewStatus:
    APPROVED = "approved"
    HOLD = "hold"
    SPAM = "spam"
    UNSPAM = "unspam"
    TRASH = "trash"
    UNTRASH = "untrash"

    CHOICES = [
        (APPROVED, "approved"),
        (HOLD, "hold"),
        (SPAM, "spam"),
        (UNSPAM, "unspam"),
        (TRASH, "trash"),
        (UNTRASH, "untrash"),
    ]


class ProductType:
    SIMPLE = "simple"
    GROUNDED = "grounded"
    EXTERNAL = "external"
    VARIABLE = "variable"

    CHOICES = [
        (SIMPLE, "simple"),
        (GROUNDED, "grounded"),
        (EXTERNAL, "external"),
        (VARIABLE, "variable"),
    ]


class ProductStatus:
    DRAFT = "draft"
    PENDING = "pending"
    PRIVATE = "private"
    PUBLISH = "publish"

    CHOICES = [
        (DRAFT, "draft"),
        (PENDING, "pending"),
        (PRIVATE, "private"),
        (PUBLISH, "publish"),
    ]


class CatalogVisibilityType:
    VISIBLE = "visible"
    CATALOG = "catalog"
    SEARCH = "search"
    HIDDEN = "hidden"

    CHOICES = [
        (VISIBLE, "visible"),
        (CATALOG, "catalog"),
        (SEARCH,"search"),
        (HIDDEN, "hidden"),
    ]


class TaxStatus:
    TAXABLE = "taxable"
    SHIPPING = "shipping"
    NONE = "none"

    CHOICES = [
        (TAXABLE, "taxable"),
        (SHIPPING, "shipping"),
        (NONE, "none"),
    ]


class StockStatus:
    INSTOCK = "instock"
    OUTOFSTOCK = "outofstock"
    ONBACKORDER = "onbackorder"

    CHOICES = [
        (INSTOCK, "instock"),
        (OUTOFSTOCK, "outofstock"),
        (ONBACKORDER, "onbackorder"),
    ]