from podmon.api.serializers import ReferenceUserSerializer
from rest_framework_jwt.utils import jwt_decode_handler

def token_payload(token, user=None, request=None):
    decoded = jwt_decode_handler(token)
    return {
        'token': token,
        'orig_iat': decoded.get('orig_iat'),
        'user': ReferenceUserSerializer(user, context={'request': request}).data
    }
