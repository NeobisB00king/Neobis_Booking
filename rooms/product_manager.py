from .models import Reservation


def proccess_reservation(obj, differ_obj, change_status):
    if obj.status == Reservation.BUILDING or obj.status == Reservation.REQUESTED: # Need to testing again
        return
    if obj.status == Reservation.ACCEPTED: # Need to testing again
        accepted_reservation(obj, differ_obj, change_status)
    elif obj.status == Reservation.DENIED: # Need to testing again
        denied_reservation(obj, differ_obj, change_status)
    elif obj.status == Reservation.BORROWED: # Need to testing again
        borrowed_reservation(obj, differ_obj, change_status)
    elif obj.status == Reservation.RETURNED: # Need to testing again
        returned_reservation(obj, differ_obj, change_status)


def denied_reservation(instance, differ_obj, change_status):
    pass


def accepted_reservation(instance, differ_obj, change_status):
    pass


def borrowed_reservation(instance, differ_obj, change_status):
    not_borrowed = []
    if change_status:
        query = instance.product_set.filter(borrowed=True)
    else:
        query = instance.product_set.filter(pk__in=differ_obj, borrowed=True)
        not_borrowed = instance.product_set.filter(
            pk__in=differ_obj, borrowed=False)
    for product in query:
        ref_obj = product.content_object
        setattr(ref_obj, product.amount_field,
                getattr(ref_obj, product.amount_field) - product.amount)
        ref_obj.save()

    for product in not_borrowed:
        ref_obj = product.content_object
        setattr(ref_obj, product.amount_field,
                getattr(ref_obj, product.amount_field) + product.amount)
        ref_obj.save()


def returned_reservation(instance, differ_obj, change_status):

    if change_status:
        query = instance.product_set.filter(borrowed=True)
    else:
        query = instance.product_set.filter(pk_in=differ_obj, borrowed=True)

    for product in query:
        ref_obj = product.content_object
        setattr(ref_obj, product.amount_field, getattr(
            ref_obj, product.amount_field) + product.amount)
        ref_obj.save()