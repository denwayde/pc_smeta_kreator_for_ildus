from dadata import Dadata
from setenv import token, secret


dadata = Dadata(token, secret)
result = dadata.suggest("address", 'ЖЕЛЕЗНОДОРОЖНАЯ')

# print(result[10]['data']['street_with_type'])
import time
try:
    print(result[0]['data']['street_with_type'])
    time.sleep(.3)
except IndexError:
    print("Нет результата")

obj = {
    'value': 'г Москва, ул Железнодорожная', 'unrestricted_value': 'г Москва, Молжаниновский р-н, ул Железнодорожная',
    'data': {'postal_code': None, 'country': 'Россия', 'country_iso_code': 'RU', 'federal_district': 'Центральный', 'region_fias_id': '0c5b2444-70a0-4932-980c-b4dc0d3f02b5', 'region_kladr_id': '7700000000000', 'region_iso_code': 'RU-MOW', 'region_with_type': 'г Москва', 'region_type': 'г', 'region_type_full': 'город', 'region': 'Москва', 'area_fias_id': None, 'area_kladr_id': None, 'area_with_type': None, 'area_type': None, 'area_type_full': None, 'area': None, 'city_fias_id': '0c5b2444-70a0-4932-980c-b4dc0d3f02b5', 'city_kladr_id': '7700000000000', 'city_with_type': 'г Москва', 'city_type': 'г', 'city_type_full': 'город', 'city': 'Москва', 'city_area': 'Северный', 'city_district_fias_id': None, 'city_district_kladr_id': None, 'city_district_with_type': None, 'city_district_type': None, 'city_district_type_full': None, 'city_district': None, 'settlement_fias_id': None, 'settlement_kladr_id': None, 'settlement_with_type': None, 'settlement_type': None, 'settlement_type_full': None, 'settlement': None, 'street_fias_id': 'e79cc02a-9278-4d9b-b8dc-e1aa2b42332b', 'street_kladr_id': '77000000000748100', 'street_with_type': 'ул Железнодорожная', 'street_type': 'ул', 'street_type_full': 'улица', 'street': 'Железнодорожная', 'stead_fias_id': None, 'stead_cadnum': None, 'stead_type': None, 'stead_type_full': None, 'stead': None, 'house_fias_id': None, 'house_kladr_id': None, 'house_cadnum': None, 'house_type': None, 'house_type_full': None, 'house': None, 'block_type': None, 'block_type_full': None, 'block': None, 'entrance': None, 'floor': None, 'flat_fias_id': None, 'flat_cadnum': None, 'flat_type': None, 'flat_type_full': None, 'flat': None, 'flat_area': None, 'square_meter_price': None, 'flat_price': None, 'room_fias_id': None, 'room_cadnum': None, 'room_type': None, 'room_type_full': None, 'room': None, 'postal_box': None, 'fias_id': 'e79cc02a-9278-4d9b-b8dc-e1aa2b42332b', 'fias_code': None, 'fias_level': '7', 'fias_actuality_state': '0', 'kladr_id': '77000000000748100', 'geoname_id': '524901', 'capital_marker': '0', 'okato': '45277584000', 'oktmo': '45343000', 'tax_office': '7743', 'tax_office_legal': '7743', 'timezone': None, 'geo_lat': '55.75396', 'geo_lon': '37.620393', 'beltway_hit': None, 'beltway_distance': None, 'metro': None, 'divisions': None, 'qc_geo': '4', 'qc_complete': None, 'qc_house': None, 'history_values': None, 'unparsed_parts': None, 'source': None, 'qc': None}}