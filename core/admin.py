from django.contrib import admin
import nested_admin

# Register your models here.
from core.models import Company, ActivePause, Activity, Prevent, Video


class PreventAdminInline(nested_admin.NestedTabularInline):
    model = Prevent
    extra = 0
    suit_classes = 'suit-tab suit-tab-prevents'


class ActivityAdminInline(nested_admin.NestedTabularInline):
    model = Activity
    extra = 0
    suit_classes = 'suit-tab suit-tab-activities'


class VideoAdminInline(nested_admin.NestedTabularInline):
    model = Video
    extra = 0
    suit_classes = 'suit-tab suit-tab-videos'


class ActivePauseAdminInline(nested_admin.NestedStackedInline):
    model = ActivePause
    extra = 0
    suit_classes = 'suit-tab suit-tab-pauses'
    exclude = ('slug',)
    inlines = (ActivityAdminInline, PreventAdminInline, VideoAdminInline)


@admin.register(Company)
class CompanyAdmin(nested_admin.NestedModelAdmin):
    list_display = ('id', 'owner', 'name', 'logo', 'mascot', 'primary_color', 'secondary_color')
    list_filter = ('owner',)
    search_fields = ('name',)
    inlines = (ActivePauseAdminInline,)


'''
@admin.register(ActivePause)
class ActivePauseAdmin(nested_admin.NestedModelAdmin):
    list_display = ('id', 'company', 'name', 'icon_svg', 'number_of_exercises', 'duration')
    list_filter = ('company', )
    search_fields = ('name', )
    inlines = (ActivityAdminInline, PreventAdminInline)
'''
