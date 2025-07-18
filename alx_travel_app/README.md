## API Endpoints

- Listings: `/api/listings/`
- Bookings: `/api/bookings/`
- Reviews: `/api/reviews/`

## Models

- **Listing**: Vacation properties available for booking
- **Booking**: Reservations made by guests
- **Review**: Guest feedback on listings
  


  ## Chapa Payment Integration

### Steps Covered:
- Payment Model
- Initiate and Verify Endpoints
- Chapa Sandbox Testing
- Celery-based Email Notifications

### Endpoints
- POST `/api/payment/initiate/`
- GET `/api/payment/verify/<tx_ref>/`

### .env
