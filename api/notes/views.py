from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
@extend_schema(description="Verify api status Online.")
def healthcheck(request):
    return Response({"data": "Online"})


class NotesViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `destroy()` and `list()` actions.
    """

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @extend_schema(responses=NoteSerializer)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(responses=NoteSerializer)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(responses=NoteSerializer)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(responses=NoteSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(responses=NoteSerializer)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
