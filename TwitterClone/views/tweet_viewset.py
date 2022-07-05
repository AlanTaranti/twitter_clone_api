import django_filters
from TwitterClone.serializers import TweetSerializer
from rest_framework import viewsets
from TwitterClone.models import Tweet


class TweetFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        field_name="usuario", lookup_expr="username__exact"
    )

    class Meta:
        model = Tweet
        fields = ("username",)


class TweetViewSet(viewsets.ModelViewSet):
    """
    # Endpoint de Tweets

    Nesse endpoint é possível manipular os tweets

    Note que apenas é possível um usuário editar seus próprios tweets

    **Métodos e ações possíveis:**

    - **GET**
        - /tweets
            - Lista todos os tweets
            - Parâmetros:
                - Filtragem:
                    - username: filtra os tweets de um usuário
                - Busca:
                    - search: busca tweets por texto
        - /tweets/<id\>
            - Consulta um tweets específico
    - **POST**
        - /tweets
            - Cria um novo tweet
    -  **PUT/PATCH**
        - /tweets/<id\>
            - Atualiza um tweet específico
    -  **DELETE**
        - /tweets/<id\>
            - Deleta um tweet específico
    """

    serializer_class = TweetSerializer
    filter_class = TweetFilter
    search_fields = ("texto",)

    def get_queryset(self):
        queryset = Tweet.objects.all()
        # Configurar "carregamento ansioso" (o invés do lazy loading do Django) para evitar selects N+1
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset

    def perform_create(self, serializer):
        serializer.validated_data["usuario"] = self.request.user
        super().perform_create(serializer)
