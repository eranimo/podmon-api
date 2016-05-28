from podmon.api.serializers import ReferenceUserSerializer

def token_payload(token, user=None, request=None):
    return {
        'token': token,
        'user': ReferenceUserSerializer(user, context={'request': request}).data
    }
