
from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.unlock_screen()
    bot.get_sales()
    bot.get_deals()
