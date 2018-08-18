from rest_framework.routers import DefaultRouter, APIRootView


class TwitterCloneRootView(APIRootView):
    """
    Twitter Clone API

    Serviço que disponibiliza, através de uma interface REST,
    os dados do Twitter Clone para serem consumidos via browser ou
    programaticamente

    """
    pass


class TwitterCloneRouter(DefaultRouter):
    """
    TwitterCloneRouter

    O TwitterCloneRouter torna opcional o uso de uma barra "/" no final da url
    E adiciona a documentação do API Root
    """

    APIRootView = TwitterCloneRootView

    def __init__(self, *args, **kwargs):
        super(DefaultRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = '/?'
