# from django import forms
# from django.db.models import Sum
#
# from .models import BookSummary
#
#
# class YourModelForm(forms.ModelForm):
#
#     total = forms.IntegerField()
#
#     def save(self, commit=True):
#         total = self.cleaned_data.get('extra_field', None)
#         total = BookSummary.objects.aggregate(Sum("price"))
#         # ...do something with extra_field here...
#         return super(YourModelForm, self).save(commit=commit)
#
#     class Meta:
#         model = BookSummary
#         fields = '__all__'