"""Admin classes for the ``paypal_pyconsg`` app."""
from django.contrib import admin

from .models import CheckoutChoices


class CheckoutChoicesAdmin(admin.ModelAdmin):
    model = CheckoutChoices
    list_display = [
        'id', 'user', 'user__email', 'transaction', 'transaction__status',
        'is_student', 'has_conference_ticket', 'tutorial_morning',
        'tutorial_afternoon', 'tshirt_size', 'food_choice', ]
    list_filter = [
        'transaction__status', 'has_conference_ticket', 'is_student',
        'food_choice', 'tshirt_size', ]
    search_fields = [
        'id', 'user__email', 'user__first_name', 'user__last_name',
        'transaction__transaction_id', 'tutorial_morning__title',
        'tutorial_afternoon__title']
    raw_id_fields = ['user', 'transaction', ]

    def user__email(self, obj):
        return obj.user.email

    def transaction__status(self, obj):
        return obj.transaction.status


admin.site.register(CheckoutChoices, CheckoutChoicesAdmin)
