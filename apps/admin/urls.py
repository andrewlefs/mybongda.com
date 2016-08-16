from  django.conf.urls import url
from .views import (
    dashboard, country, tournament,
    season, team, fixture, match, category,
    video, post, relax, user, channel, clip, page
)

urlpatterns = [
    url(r'^$', dashboard.DashboardView.as_view(), name='dashboard'),
    url(r'^profile/$', dashboard.ChangePasswordView.as_view(),
        name='profile'),
    url(r'^login/$', dashboard.LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/admincp/login/'}, name='logout'),

    # Url for country
    url(r'^country/$', country.ListCountryView.as_view(), name='list_country'),
    url(r'^country/create/$', country.CreateCountryView.as_view(),
        name='create_country'),
    url(r'^country/update/(?P<pk>[0-9]+)/$',
        country.UpdateCountryView.as_view(), name='update_country'),
    url(r'^country/delete/(?P<pk>[0-9]+)/$',
        country.DeleteCountryView.as_view(), name='delete_country'),

    # Url for tournament 
    url(r'^tournament/$', tournament.ListTournamentView.as_view(),
        name='list_tournament'),
    url(r'^tournament/search/$', tournament.SearchTournamentByCountryView.as_view(),
        name='search_tournament'),
    url(r'^tournament/create/$', tournament.CreateTournamentView.as_view(),
        name='create_tournament'),
    url(r'^tournament/update/(?P<pk>[0-9]+)/$',
        tournament.UpdateTournamentView.as_view(), name='update_tournament'),
    url(r'^tournament/delete/(?P<pk>[0-9]+)/$',
        tournament.DeleteTournamentView.as_view(), name='delete_tournament'),

    # Url for season 
    url(r'^season/$', season.ListSeasonView.as_view(),
        name='list_season'),
    url(r'^season/create/$', season.CreateSeasonView.as_view(),
        name='create_season'),
    url(r'^season/update/(?P<pk>[0-9]+)/$',
        season.UpdateSeasonView.as_view(), name='update_season'),
    url(r'^season/delete/(?P<pk>[0-9]+)/$',
        season.DeleteSeasonView.as_view(), name='delete_season'),

    # Url for team 
    url(r'^team/$', team.ListTeamView.as_view(),
        name='list_team'),
    url(r'^team/create/$', team.CreateTeamView.as_view(),
        name='create_team'),
    url(r'^team/update/(?P<pk>[0-9]+)/$',
        team.UpdateTeamView.as_view(), name='update_team'),
    url(r'^team/delete/(?P<pk>[0-9]+)/$',
        team.DeleteTeamView.as_view(), name='delete_team'),

    # Url for fixture 
    url(r'^fixture/$', fixture.ListFixtureView.as_view(),
        name='list_fixture'),
    url(r'^fixture/search/$', fixture.SearchFixtureView.as_view(),
        name='search_fixture'),
    url(r'^fixture/create/$', fixture.CreateFixtureView.as_view(),
        name='create_fixture'),
    url(r'^fixture/update/(?P<pk>[0-9]+)/$',
        fixture.UpdateFixtureView.as_view(), name='update_fixture'),
    url(r'^fixture/delete/(?P<pk>[0-9]+)/$',
        fixture.DeleteFixtureView.as_view(), name='delete_fixture'),
    url(r'^fixture/delete-multiple/$',
        fixture.DeleteMultipleFixtureView.as_view(), name='delete_multiple_fixture'),

    # Url for match
    url(r'^match/update/(?P<pk>[0-9]+)/$',
        match.UpdateMatchView.as_view(), name='update_match'),

    # Url for category
    url(r'^category/$', category.ListCategoryView.as_view(), name='list_category'),
    url(r'^category/create/$', category.CreateCategoryView.as_view(),
        name='create_category'),
    url(r'^category/update/(?P<pk>[0-9]+)/$',
        category.UpdateCategoryView.as_view(), name='update_category'),
    url(r'^category/delete/(?P<pk>[0-9]+)/$',
        category.DeleteCategoryView.as_view(), name='delete_category'),

    # Url for channel
    url(r'^channel/$', channel.ListChannelView.as_view(), name='list_channel'),
    url(r'^channel/create/$', channel.CreateChannelView.as_view(),
        name='create_channel'),
    url(r'^channel/update/(?P<pk>[0-9]+)/$',
        channel.UpdateChannelView.as_view(), name='update_channel'),
    url(r'^channel/delete/(?P<pk>[0-9]+)/$',
        channel.DeleteChannelView.as_view(), name='delete_channel'),

    # Url for video 
    url(r'^video/$', video.ListVideoView.as_view(),
        name='list_video'),
    url(r'^video/create/$', video.CreateVideoView.as_view(),
        name='create_video'),
    url(r'^video/update/(?P<pk>[0-9]+)/$',
        video.UpdateVideoView.as_view(), name='update_video'),
    url(r'^video/delete/(?P<pk>[0-9]+)/$',
        video.DeleteVideoView.as_view(), name='delete_video'),

    # Url for clip
    url(r'^clip/$', clip.ListClipView.as_view(),
        name='list_clip'),
    url(r'^clip/auto/$', clip.AutoGetClipView.as_view(),
        name='auto_clip'),
    url(r'^clip/delete/(?P<pk>[0-9]+)/$',
        clip.DeleteClipView.as_view(), name='delete_clip'),

    # Url for relax
    url(r'^relax/$', relax.ListRelaxView.as_view(),
        name='list_relax'),
    url(r'^relax/create/$', relax.CreateRelaxView.as_view(),
        name='create_relax'),
    url(r'^relax/update/(?P<pk>[0-9]+)/$',
        relax.UpdateRelaxView.as_view(), name='update_relax'),
    url(r'^relax/delete/(?P<pk>[0-9]+)/$',
        relax.DeleteRelaxView.as_view(), name='delete_relax'),

    # Url for post 
    url(r'^post/$', post.ListPostView.as_view(),
        name='list_post'),
    url(r'^post/create/$', post.CreatePostView.as_view(),
        name='create_post'),
    url(r'^post/update/(?P<pk>[0-9]+)/$',
        post.UpdatePostView.as_view(), name='update_post'),
    url(r'^post/delete/(?P<pk>[0-9]+)/$',
        post.DeletePostView.as_view(), name='delete_post'),

    # Url for page
    url(r'^page/$', page.ListPageView.as_view(),
        name='list_page'),
    url(r'^page/create/$', page.CreatePageView.as_view(),
        name='create_page'),
    url(r'^page/update/(?P<pk>[0-9]+)/$',
        page.UpdatePageView.as_view(), name='update_page'),
    url(r'^page/delete/(?P<pk>[0-9]+)/$',
        page.DeletePageView.as_view(), name='delete_page'),

    # Url for user
    url(r'^user/$', user.ListUserProfileView.as_view(),
        name='list_user'),
    url(r'^user/create/$', user.CreateUserProfileView.as_view(),
        name='create_user'),
    url(r'^user/update/(?P<pk>[0-9]+)/$',
        user.UpdateUserProfileView.as_view(), name='update_user'),
    url(r'^user/delete/(?P<pk>[0-9]+)/$',
        user.DeleteUserProfileView.as_view(), name='delete_user'),
]
