# ALX Travel App

## Setup Instructions

1. Clone the repository
2. Create and activate virtual environment
3. Install requirements: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Seed database: `python manage.py seed`
6. Run server: `python manage.py runserver`

## API Endpoints

- Listings: `/api/listings/`
- Bookings: `/api/bookings/`
- Reviews: `/api/reviews/`

## Models

- **Listing**: Vacation properties available for booking
- **Booking**: Reservations made by guests
- **Review**: Guest feedback on listings

## Seed Command

Populates database with:
- 1 host user (host@example.com)
- 1 guest user (guest@example.com)
- 10 sample listings