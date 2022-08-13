#
import os
from django_api_sample.settings import BASE_DIR
from django.utils.datastructures import MultiValueDictKeyError
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from action_code.models import ActionCode
from action_code.serializers import ActionCodeSerializer


def arg_next(action_code,
             tel_on, tel_message, tel_list,
             mail_on, mail_message,
             created_at, updated_at):
    print('-----------')
    print('ActionCode=', action_code)
    try:
        file_dir = os.path.join(BASE_DIR, 'agent_file.log')
        agent_str = 'agent-test->' + action_code
        with open(file_dir, 'w') as fp:
            fp.write(agent_str)
    except IOError as e:
        pass

    if tel_on:
        # push_tel()
        print('tel-ON:', tel_message)
        print('tel-list:', tel_list)
    if mail_on:
        print('mail-ON', mail_message)
    print('created_at=', created_at)
    print('updated_at', updated_at)
    print('===========')


class Apiv1APIView(viewsets.ReadOnlyModelViewSet):
    queryset = ActionCode.objects.all()
    serializer_class = ActionCodeSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'
    http_method_names = ['get', ]

    def list(self, request, *args, **kwargs):
        queryset = ActionCode.objects.all()
        serializer = ActionCodeSerializer(queryset, many=True)
        query_list = request.query_params
        ret = serializer.data

        try:
            action_code = query_list['action_code']
        except MultiValueDictKeyError:
            action_code = False
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        for dat in serializer.data:
            if dat['action_code'] == query_list['action_code']:
                arg_next(dat['action_code'],
                         dat['tel_on'], dat['tel_message'], dat['tel_list'],
                         dat['mail_on'], dat['mail_message'],
                         dat['created_at'], dat['updated_at'])
                res_dat = dat
                stat = {'status': 202}
                ret = {**stat, **res_dat}
                return Response(ret, status=status.HTTP_202_ACCEPTED)
            else:
                stat = {'status': 400}
                return Response(stat, status=status.HTTP_400_BAD_REQUEST)
        return Response(ret, status=status.HTTP_202_ACCEPTED)
