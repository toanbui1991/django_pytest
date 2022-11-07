import pytest
from core.app1.models import Product

"""
what is parametrize:
    - parametrize help to build test cases
    - test cases will help test with the same code with multiple test case
@pytest.mark.parametrize is a decorator which create a suit of test which allow us to test the same code with multiple suit
"""

@pytest.mark.parametrize(
    "title, category, description, slug, regular_price, discount_price, validity",
    [
        ("NewTitle", 1, "NewDescription", "slug", "4.99", "3.99", True),
        ("NewTitle", 1, "NewDescription", "slug", "", "3.99", False),
    ],
)
def test_product_instance(
    db, product_factory, title, category, description, slug, regular_price, discount_price, validity
):

    test = product_factory(
        title=title,
        category_id=category,
        description=description,
        slug=slug,
        regular_price=regular_price,
        discount_price=discount_price,
    )

    item = Product.objects.all().count()
    print(item)
    assert item == validity