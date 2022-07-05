from TwitterClone.models import Tweet, Perfil
from TwitterClone.serializers import TweetSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class FeedViewSet(viewsets.ViewSet):
    """
    # Endpoint de Feed

    Nesse endpoint é possível visualizar o feed do usuário logado

    O Feed é composto dos próprios tweets e dos usuários que está seguindo

    Note que apenas é possível visualizar o próprio feed

    **Métodos e ações possíveis:**

    - **GET**
        - /feed
            - Lista o feed do usuário
    """

    permission_classes = (IsAuthenticated,)

    def list(self, request):
        seguidores_e_user_ids = list(
            Perfil.objects.prefetch_related("segue")
            .get(usuario_id=request.user.id)
            .segue.all()
            .values_list("id", flat=True)
        )
        seguidores_e_user_ids.append(request.user.id)

        queryset = (
            Tweet.objects.filter(usuario_id__in=seguidores_e_user_ids)
            .order_by("id")
            .reverse()
        )
        serializer = TweetSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)
