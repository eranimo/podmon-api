from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from podmon.api.serializers import ReferenceAccountSerializer, UpdateAccountSerializer
from podmon.api.permissions import IsObjectOwner
from ..models import Account
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route
import evelink

class AccountView(viewsets.GenericViewSet):
    "Account view"
    queryset = Account.objects.all()
    serializer_class = ReferenceAccountSerializer

    @permission_classes((IsAuthenticated,))
    def create(self, request):
        """
        Create an account
        ---
        request_serializer: UpdateAccountSerializer
        response_serializer: ReferenceAccountSerializer
        """
        user = request.user
        serializer = UpdateAccountSerializer(data=request.data)
        if serializer.is_valid():
            account = Account(
                owner=user,
                key_id=serializer.data.get('key_id'),
                v_code=serializer.data.get('v_code')
            )
            account.save()
            account_serializer = self.get_serializer(account)
            return Response(account_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes((IsObjectOwner,))
    def retrieve(self, request, pk):
        """
        Get an account
        ---
        response_serializer: ReferenceAccountSerializer
        """
        account = self.get_object()
        account_serializer = self.get_serializer(account)

        account = self.get_object()
        api = evelink.api.API(api_key=(account.key_id, account.v_code))
        account_d = evelink.account.Account(api)
        return Response({
            'info': account_serializer.data,
            'characters': account_d.characters().result,
            'status': account_d.status().result
        })



    @permission_classes((IsObjectOwner,))
    def update(self, request, pk):
        """
        Update an account
        ---
        request_serializer: UpdateAccountSerializer
        response_serializer: ReferenceAccountSerializer
        parameters:
            - name: name
              description: Account name
              requried: false
              type: string
            - name: key_id
              description: API Key ID
              required: false
              type: string
            - name: v_code
              description: Verification Code
              requried: false
              type: string
        """
        user = request.user
        account = self.get_object()
        name = request.data.get('name')
        key_id = request.data.get('key_id')
        v_code = request.data.get('v_code')

        if name is not None:
            account.name = name
        if key_id is not None:
            account.key_id = key_id
        if v_code is not None:
            account.v_code = v_code
        account.save()
        account_serializer = self.get_serializer(account)
        return Response(account_serializer.data)
