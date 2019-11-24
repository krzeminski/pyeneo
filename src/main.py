from src.CeneoAPIHandler import CeneoAPIHandler
from src.models.item_query import ItemQuery
from datetime import datetime

from src.processors.product_offers_processor import ProductOffersProcessor
from src.processors.search_results_processor import SearchResultsProcessor

item_query = ItemQuery("pralka wsad 7 kg", 1, 1000, 1600, datetime.now())

print(item_query.create_url())

api_handler = CeneoAPIHandler()
item_query_html = api_handler.send_search_request(item_query).text

search_processor = SearchResultsProcessor(item_query_html, item_query)
item = search_processor.get_first_item_with_multiple_sellers()

print(item.create_url())

item_html = api_handler.send_product_request(item).text
product_processor = ProductOffersProcessor(item_html, item)

product_processor.get_offers_list()
