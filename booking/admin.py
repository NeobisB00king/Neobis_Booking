import json
from importlib.resources import path

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count, Sum
from django.db.models.functions import TruncDay
from django.http import JsonResponse

from .forms import YourModelForm
from .models import *


class BookingAdmin(admin.ModelAdmin):
    list_display = ('clientEmail', 'room', 'date_from',
                    'date_to', 'book_status')
    list_filter = ('book_status', 'room', 'book_date')


# admin.site.register(Client)
admin.site.register(Room)
admin.site.register(Booking, BookingAdmin)
admin.site.register(CategoryRoom)
admin.site.register(VolumeRoom)


# admin.site.register(RoomImages)


@admin.register(BookSummary)
class SaleSummaryAdmin(admin.ModelAdmin):
    # pass
    # change_list_template = 'admin/sale_summary_change_list.html'
    form = YourModelForm

    fieldsets = (
        (None, {
            'fields': ('room_category_stats', 'book_date', 'clientName', 'total'),
        }),
    )
    date_hierarchy = 'book_date'
    list_display = ('room_category_stats', 'book_date', 'clientName', 'totalsum')
    list_filter = ('room_category_stats', 'book_date', 'clientName')
    search_fields = ['book_date']

    # def changelist_view(self, request, extra_context=None):
    #     chart_data = self.chart_data()
    #     as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
    #     extra_context = extra_context or {"chart_data": as_json}
    #     return super().changelist_view(request, extra_context=extra_context)

    # def get_urls(self):
    #     urls = super().get_urls()
    #     extra_urls = [
    #         path("chart_data/", self.admin_site.admin_view(self.chart_data_endpoint))
    #     ]
    #     # NOTE! Our custom urls have to go before the default urls, because they
    #     # default ones match anything.
    #     return extra_urls + urls

    # JSON endpoint for generating chart data that is used for dynamic loading
    # via JS.
    # def chart_data_endpoint(self, request):
    #     chart_data = self.chart_data()
    #     return JsonResponse(list(chart_data), safe=False)
    #
    # def chart_data(self):
    #     return (
    #         Booking.objects.annotate(date=TruncDay("book_date"))
    #             .values("date")
    #             .annotate(y=Count("id"))
    #             .order_by("-date")
    #     )
    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(
    #         request,
    #         extra_context=extra_context,
    #     )
    #     try:
    #         qs = response.context_data['cl'].queryset
    #     except (AttributeError, KeyError):
    #         return response
    #     metrics = {
    #         'total': Count('id'),
    #         'total_sales': Sum('totalsum'),
    #     }
    #     response.context_data['summary'] = list(
    #         qs
    #         .values('room_category_stats')
    #         .annotate(**metrics)
    #         .order_by('-total_sales')
    #     )
    #     return response
