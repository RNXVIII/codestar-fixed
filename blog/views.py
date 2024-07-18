from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from .models import Booking


@login_required
def index(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.booked = True  # Ensure the booking is marked as booked
            booking.save()
            messages.success(request, 'Booking successfully created.')
            return redirect('home')
        else:
            messages.error(request, 'There was an error with your booking.')
    else:
        form = BookingForm()

    bookings = Booking.objects.all().order_by('date')
    context = {
        'bookings': bookings,
        'form': form,
    }
    return render(request, 'blog/index.html', context)

# Create your views here.
# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1)
#     template_name = "blog/index.html"
#     paginate_by = 6


# def post_detail(request, slug):

#     queryset = Post.objects.filter(status=1)
#     post = get_object_or_404(queryset, slug=slug)

#     return render(
#         request,
#         "blog/post_detail.html",
#         {"post": post,
#          "coder": "Matt Rudge"},
#     )

    
