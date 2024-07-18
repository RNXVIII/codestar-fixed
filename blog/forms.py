from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date']  

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if Booking.objects.filter(date=date, booked=True).exists():
            raise forms.ValidationError("This date is already booked.")
        return date