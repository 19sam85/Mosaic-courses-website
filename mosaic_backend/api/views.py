import random
import string

from blog.models import Post, Tag
from booking.models import Booking
from carousel.models import MainCarouselItem
from crm_app.models import GiftCert
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from marketplace.models import Artwork
from masterclass.models import Masterclass, MasterclassType
from rest_framework import filters, mixins, status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from school.models import School

from api.filters import ArtworksFilter, PostsFilter
from api.serializers import (ArtworkSerializer, BookingSerializer,
                             EmailMainSerializer, GiftCertSerializer,
                             MainCarouselSerializer, MasterclassSerializer,
                             MasterclassTypeSerializer, PostSerializer,
                             RequestSerializer, SchoolSerializer,
                             TagReadOnlySerializer)


def generate_cert_id(size=6, chars=string.ascii_uppercase + string.digits):
    """generates an unique 6 letters/digits code"""
    return ''.join(random.choice(chars) for _ in range(size))


class RequestCreateOnlyViewSet(mixins.CreateModelMixin,
                               viewsets.GenericViewSet):
    serializer_class = RequestSerializer
    permission_classes = [AllowAny, ]


class TagReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagReadOnlySerializer
    permission_classes = [AllowAny, ]


class ArtworkReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    # add get serializer class
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    pagination_class = LimitOffsetPagination
    filterset_class = ArtworksFilter
    permission_classes = [AllowAny, ]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, ]


class EmailCreateOnlyViewSet(mixins.CreateModelMixin,
                             viewsets.GenericViewSet):
    serializer_class = EmailMainSerializer
    permission_classes = [AllowAny, ]


class MasterclassReadOnlyViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = MasterclassSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return Masterclass.objects.all().annotate(
            num_of_guests=Count('bookings__guest'))


class MasterclassTypeReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MasterclassTypeSerializer
    queryset = MasterclassType.objects.all()
    permission_classes = [AllowAny, ]


class AbstractView(
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    pass


class BookingViewSet(AbstractView):
    """Viewset for user profile and course/masterclass bookings
    that process get, post and delete requests.
    Only authorized user can book a course. For non-authorized users there is
    a redirect to the 'call me back' page (or it will be done if not yet."""
    queryset = Booking.objects.all()  # TODO после авторизации
    serializer_class = BookingSerializer
    # permission_classes = TODO


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]
    pagination_class = LimitOffsetPagination
    filterset_class = PostsFilter
    filter_backends = [DjangoFilterBackend, ]


class SchoolReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [AllowAny, ]


class MainCarouselReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MainCarouselItem.objects.all()
    serializer_class = MainCarouselSerializer
    permission_classes = [AllowAny, ]


class CertificatePostPatchViewSet(viewsets.GenericViewSet,
                                  mixins.DestroyModelMixin,
                                  mixins.CreateModelMixin):
    queryset = GiftCert.objects.all()
    serializer_class = GiftCertSerializer
    permission_classes = [AllowAny, ]

    def perform_create(self, serializer):
        """Standard behaviour except for calling a method to
        generate a 6-symbols (digits and letters) code as the cert ID"""
        cert_id = generate_cert_id()
        serializer.save(id=cert_id)
        return cert_id

    def create(self, request, *args, **kwargs):
        """Returns the certificate's ID among the other data"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            cert_id = self.perform_create(serializer)
            serializer_id = {'certificate_id': f'{cert_id}'}
            serializer_id.update(serializer.data)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer_id,
                            status=status.HTTP_201_CREATED,
                            headers=headers)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
