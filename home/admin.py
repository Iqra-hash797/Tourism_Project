from django.contrib import admin

# Register your models here.
from home.models import Contact,Destination,TicketBooking

admin.site.register(Contact)
admin.site.register(Destination)
admin.site.register(TicketBooking)