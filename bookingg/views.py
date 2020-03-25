import datetime

# from dateutil import parser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, TemplateView

from .filter import RoomFilter
from .forms import CreateRoomForm, SearchRoomForm, BookingForm
from .models import Room, Booking


class MakeReservationView(View):
    """Book a particular room for a selected day."""

    def get(self, request, id):
        room = get_object_or_404(Room, pk=id)
        theroom = Room.objects.get(id=id)
        template_name = 'make_reservation.html'
        form = BookingForm()
        price = theroom.price
        return render(request, template_name, {'form': form, 'price': price, 'room': room})

    def post(self, request, id):
        room = get_object_or_404(Room, pk=id)
        template_name = 'make_reservation.html'
        form = BookingForm(request.POST)

        if form.is_valid():
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']
            comment = form.cleaned_data['comment']
            has_child = form.cleaned_data['has_child']
            clientName = form.cleaned_data['clientName']
            clientSurname = form.cleaned_data['clientSurname']
            clientEmail = form.cleaned_data['clientEmail']
            clientPhone = form.cleaned_data['clientPhone']

            minimal_date = datetime.datetime.now().date()

            if request.POST.get('book'):
                if date_from < minimal_date:
                    messages.error(request, f'Дата должна быть сегодня или позже, не вчера или раньше!')
                    return redirect('home')
                elif date_from >= minimal_date:
                    bookingForm = Booking.objects.create(
                        date_from=date_from,
                        date_to=date_to,
                        room=room,
                        comment=comment,
                        has_child=has_child,
                        clientName=clientName,
                        clientSurname=clientSurname,
                        clientEmail=clientEmail,
                        clientPhone=clientPhone,
                        )

        messages.success(request, f'Комната успешно забронирована!')
        return redirect('home')


class CreateRoomView(LoginRequiredMixin, View):
    """Add a new room to the database."""
    raise_exception = True
    def get(self, request):
        template_name = 'create_room.html'
        form = CreateRoomForm
        return render(request, template_name, {'form': form})

    def post(self, request):
        template_name = 'create_room.html'
        form = CreateRoomForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            capacity = form.cleaned_data['capacity']
            category = form.cleaned_data['category']
            volume = form.cleaned_data['volume']
            images = form.cleaned_data['images']

            if not Room.objects.filter(name=form.cleaned_data['name']).exists():
                new_room = Room.objects.create(
                    name=name, capacity=capacity, category=category, volume=volume, images=images)
                new_room.save()
                ctx = {'msg': 'New room has been added successfuly to our database',
                       'form': form}
            else:
                ctx = {'msg': 'That room already exists in our database'}

        return redirect('home', messages.success(request, 'Profile details updated.'))


class RoomDetailsView(View):
    """Display data of particular room."""

    def get(self, request, id):
        room = get_object_or_404(Room, pk=id)
        theroom = Room.objects.get(id=id)
        price = theroom.price
        template_name = 'room_details.html'

        ctx = {
            'room': room,
            'price': price,
        }
        return render(request, template_name, ctx)


class UpdateRoomView(LoginRequiredMixin, View):
    """Edit data of existing model instance."""
    raise_exception = True
    def get(self, request, id):
        room = get_object_or_404(Room, pk=id)
        template_name = 'update_room.html'
        form = CreateRoomForm(instance=room)
        ctx = {
            'room': room,
            'form': form,
        }
        return render(request, template_name, ctx)

    def post(self, request, id):
        room = get_object_or_404(Room, pk=id)
        form = CreateRoomForm(request.POST, instance=room)

        if form.is_valid():
            obj = form.save()
            obj.save()

        return redirect('room_details', id=room.id)


class AllRoomsView(View):
    """View to display all existing rooms within their booking status."""

    def get(self, request):
        rooms = Room.objects.all().order_by('name')
        template_name = 'all_rooms.html'
        today = datetime.date.today()
        status = ''

        ctx = {
            'rooms': rooms,
            'status': status,
        }

        return render(request, template_name, ctx)


class DeleteRoomView(LoginRequiredMixin, View):
    """Delete chosen room."""
    raise_exception = True

    def get(self, request, id):
        room = get_object_or_404(Room, pk=id)
        msg = f"You are about to delete a following room: {room.name}"
        template_name = 'delete_room.html'
        ctx = {
            'room': room,
            'msg': msg,
        }
        return render(request, template_name, ctx)

    def post(self, request, id):

        room_to_del = get_object_or_404(Room, pk=id)

        if request.POST.get('delete'):
            room_to_del.delete()
            return redirect('deleted_room')

        elif request.POST.get('no_delete'):
            return redirect('/')


class DeletedRoomView(LoginRequiredMixin, View):
    """A view deleting a model instance."""

    def get(self, request):
        template_name = 'deleted_room_view.html'
        return render(request, template_name)



class HomeView(TemplateView):
    template_name = 'home.html'


class SearchRoomView(ListView):
    model = Room
    template_name = 'search_room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RoomFilter(self.request.GET, queryset=self.get_queryset())
        return context
