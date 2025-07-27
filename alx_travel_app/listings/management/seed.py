from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        # Create sample users
        user1 = User.objects.create_user(username='user1', password='password')
        user2 = User.objects.create_user(username='user2', password='password')

        # Create sample listings
        listing1 = Listing.objects.create(
            title='Cozy Cottage',
            description='A cozy cottage in the woods.',
            price=100.00,
            owner=user1
        )
        listing2 = Listing.objects.create(
            title='Beach House',
            description='A beautiful beach house.',
            price=200.00,
            owner=user2
        )

        # Create sample bookings
        Booking.objects.create(
            listing=listing1,
            user=user2,
            start_date='2023-10-01',
            end_date='2023-10-05'
        )

        # Create sample reviews
        Review.objects.create(
            listing=listing1,
            user=user2,
            rating=5,
            comment='Amazing stay!'
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with sample data.'))
