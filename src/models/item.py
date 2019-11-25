from functools import reduce
from typing import List

from src.constants import Ceneo
from src.models.item_query import ItemQuery
from src.models.offer import Offer


class Item:
    """ Class reflecting a specific item"""

    prod_id: str = ""
    # TODO: consider leaving item_query as "parent" to item
    parent_item_query: ItemQuery = None
    offers: List[Offer] = []

    def __init__(self, prod_id: str, parent_item_query: ItemQuery = None):
        self.prod_id = prod_id
        self.parent_item_query = parent_item_query

    def create_url(self) -> str:
        """ Create URL for and item with specific ID sorted by lowest price (delivery included) """
        return f"{Ceneo.URI}{self.prod_id};0284-0.htm"

    def add_seller(self, name: str, price: float):
        """ Method to append seller with their price to prices """
        self.offers.append(Offer(name, price))

    def get_mean_price(self) -> float:
        return reduce(lambda value, acc: value+acc, map(lambda offer: offer.price, self.offers)) / len(self.offers)

    def set_offers(self, offers: List[Offer]):
        # TODO: consider raising an exception when this list is empty -- just for security?
        self.offers = offers
