from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from podmon.api.serializers import ReferenceAccountSerializer, UpdateAccountSerializer
from podmon.api.permissions import IsObjectOwner
from ..models import Account
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from rest_framework_extensions.mixins import NestedViewSetMixin
import evelink
from django.http import JsonResponse
from django.conf.urls import url
from podmon.api.utils.eve_data import get_stations, get_types

def fetch_char_from_api(account_id, char_id):
    print("Getting character {} from account {}".format(char_id, account_id))
    account = Account.objects.get(pk=account_id)
    api = evelink.api.API(api_key=(account.key_id, account.v_code))
    character_api = evelink.char.Char(char_id, api)
    return character_api


def get_character_info(request, account_id, char_id):
    "Get a character by an ID"
    character_api = fetch_char_from_api(account_id, char_id)
    return JsonResponse(character_api.character_sheet(), safe=False)

def get_character_skills(request, account_id, char_id):
    "Get a character skills"
    character_api = fetch_char_from_api(account_id, char_id)
    return JsonResponse(character_api.skills(), safe=False)

def get_character_wallet(request, account_id, char_id):
    "Get a character skills"
    character_api = fetch_char_from_api(account_id, char_id)
    return JsonResponse(character_api.wallet_info(), safe=False)

def get_character_assets(request, account_id, char_id):
    "Get a character assets"

    character_api = fetch_char_from_api(account_id, char_id)
    assets = character_api.assets()
    stations = get_stations()
    types = get_types()

    result = []
    for location_id, data in assets[0].items():
        print(location_id, type(location_id))
        if int(location_id) in stations:
            contents = []
            for item in data.get('contents'):
                if item['id'] in types:
                    item['item_name'] = types[item['id']]
                contents.append(item)
            result.append({
                'station': {
                    'name': stations.get(int(location_id)),
                    'location_id': location_id
                },
                'data': contents
            })
        # else:
        #     raise Exception('Station {} not found!'.format(location_id))
    return JsonResponse(result, safe=False)


character_urls = [
    url(r'^skills/', get_character_skills),
    url(r'^wallet/', get_character_wallet),
    url(r'^assets/', get_character_assets),
    url(r'^', get_character_info),
]
