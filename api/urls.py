from django.urls import path, include
from .views import city, region, poi, province, user, image, tag, social_media, day_and_hour, precompiled_itinerary, geoapify, \
    poi_opening_hour, generated_itinerary, nearby_poi
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'region', region.RegionViewSet, basename='region')  # 1
router.register(r'province', province.ProvinceViewSet, basename='province')  # 2
router.register(r'city', city.CityViewSet, basename='city')  # 3
router.register(r'user', user.UserViewSet, basename='user')  # 4
router.register(r'image', image.ImageViewSet, basename='image')  # 5
router.register(r'tag', tag.TagViewSet, basename='tag')  # 6
router.register(r'poi', poi.PoiViewSet, basename='poi')  # 7
router.register(r'poi_opening_hour', poi_opening_hour.PoiOpeningHourViewSet, basename='poi_opening_hour')  # 8
router.register(r'social_media', social_media.SocialMediaViewSet, basename='social_media')  # 9
router.register(r'day_and_hour', day_and_hour.DayAndHourViewSet, basename='day_and_hour')  # 10
# router.register(r'register_backuser', backuser.RegisterBackUser, basename='register_backuser')  # 10
router.register(r'accommodations', geoapify.AccommodationView, basename='accommodations')  # 10
router.register(r'caterings', geoapify.CateringView, basename='caterings')  # 10
router.register(r'nearby_poi', nearby_poi.nearbyPoi, basename='nearby_poi')  # 10
router.register(r'precompiled_itinerary', precompiled_itinerary.PrecompiledItineraryViewSet, basename='precompiled_itinerary')  # 10
router.register(r'generated_itinerary', generated_itinerary.GeneratedItineraryViewSet, basename='generated_itinerary')  # 10

# router.register(r'itinerary',itinerary.ItineraryViewSet, basename='itinerary')
# router.register(r'accommodation',geoapify.AccommodationViewSet, basename='accommodation')


# urlpatterns = router.urls


urlpatterns = [
    #path(r'accommodation/', geoapify.AccommodationView.as_view(), name='accommodation'),
    # path(r'catering/', geoapify.CateringView.as_view(), name='catering'),
    # path(r'itinerary/generated/', itinerary.ItineraryViewSet.as_view({'get': 'get'}), name='itinerary'),
    # path(r'itinerary/precompiled/', itinerary.ItineraryViewSet.as_view({'get': 'get_precompiled'}), name='itinerary_precompiled'),
    # path(r'nearby_poi/', poi.nearbyPoi.as_view(), name='nearby_poi'),
    # path(r'register_backuser/', backuser.RegisterBackUser.as_view(), name='register_backuser'),

    # path('', include(router.urls)),
    # path('itinerary', itinerary.ItineraryView.as_view, name='itinerary'),
    # path('region', views.region),
    # path('region/<str:pk>', views.region_id),
]

urlpatterns += router.urls
