import json
from django.urls import path

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count, Sum, DateTimeField, Min, Max
from django.db.models.functions import TruncDay, Trunc
# from django.http import JsonResponse, request, response
import requests
# from .forms import YourModelForm
from .models import *
from admin_totals.admin import ModelAdminTotals
from django.db.models import Sum, Avg
from django.db.models.functions import Coalesce


class BookingAdmin(admin.ModelAdmin):
    list_display = ('clientEmail', 'room', 'date_from',
                    'date_to', 'book_status')
    list_filter = ('book_status', 'room', 'book_date')


# admin.site.register(Client)
admin.site.register(Room)
admin.site.register(Booking, BookingAdmin)
admin.site.register(CategoryRoom)
admin.site.register(VolumeRoom)
admin.site.register(BookStatus)
admin.site.register(BookPayStatus)


# admin.site.register(RoomImages)


@admin.register(BookSummary)
class SaleSummaryAdmin(ModelAdminTotals):
    # pass
    date_hierarchy = 'book_date'
    list_display = ('room_category_stats', 'book_status', 'book_date', 'clientName', 'totalsum', 'book_pay_status')

    list_filter = ('room_category_stats', 'book_date', 'clientName', 'book_status', 'book_pay_status')
    search_fields = ['book_date']
    fieldsets = (
        (None, {
            'fields': ('room_category_stats', 'book_date', 'clientName', 'total'),
        }),
    )
    save_as = True
    save_on_top = True
    list_totals = [('totalsum', lambda totalsum: Coalesce(Sum(totalsum), 0))]
    # ('book_status', lambda book_status: Coalesce())]

    # change_list_template = 'sale_summary_change_list.html'

    # form = YourModelForm
    # def get_next_in_date_hierarchy(self, date_hierarchy):
    #     if date_hierarchy and '__day' in requests.get:
    #         return 'hour'
    #     if date_hierarchy and '__month' in requests.get:
    #         return 'day'
    #     if date_hierarchy and '__year' in requests.get:
    #         return 'week'
    #     return 'month'

    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(
    #         request,
    #         extra_context=extra_context,
    #     )
    #
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
    #             .values('book_status')
    #             .annotate(**metrics)
    #             .order_by('-total_sales')
    #     )
    #     response.context_data['totalsum'] = dict(
    #         qs.aggregate(**metrics)
    #     )
    #
    #     summary_over_time = qs.annotate(
    #         period=Trunc(
    #             'book_date',
    #             'day',
    #             output_field=DateTimeField(),
    #         ),
    #     ).values('period').annotate(total=Sum('totalsum')).order_by('period')
    #     summary_range = summary_over_time.aggregate(
    #         low=Min('total'),
    #         high=Max('total'),
    #     )
    #     high = summary_range.get('high', 0)
    #     low = summary_range.get('low', 0)
    #     response.context_data['summary_over_time'] = [{
    #         'period': x['period'],
    #         'total': x['total'] or 0,
    #         'pct': ((x['total'] or 0) - low) / (high - low) * 100
    #         if high > low else 0,
    #     } for x in summary_over_time]
    #     period = self.get_next_in_date_hierarchy(request)
    #     response.context_data['period'] = period
    #     summary_over_time = qs.annotate(
    #         period=Trunc('created', period, output_field=DateTimeField()),
    #     ).values('period').annotate(total=Sum('price')).order_by('period')
    #     return response

    # def changelist_view(self, request, extra_context=None):
    #     chart_data = self.chart_data()
    #     as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
    #     extra_context = extra_context or {"chart_data": as_json}
    #     return super().changelist_view(request, extra_context=extra_context)
    #
    # def get_urls(self):
    #     urls = super().get_urls()
    #     extra_urls = [
    #         path("chart_data/", self.admin_site.admin_view(self.chart_data_endpoint))
    #     ]
    #     # NOTE! Our custom urls have to go before the default urls, because they
    #     # default ones match anything.
    #     return extra_urls + urls
    #
    # # JSON endpoint for generating chart data that is used for dynamic loading
    # # via JS.
    # def chart_data_endpoint(self, request):
    #     chart_data = self.chart_data()
    #     return JsonResponse(list(chart_data), safe=False)
    #
    # def chart_data(self):
    #     return (
    #         BookSummary.objects.annotate(date=TruncDay("book_date"))
    #         .values("date")
    #         .annotate(y=Count("id"))
    #         .order_by("-date")
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
    #             .values('room_category_stats')
    #             .annotate(**metrics)
    #             .order_by('-total_sales')
    #     )
    #     return response
