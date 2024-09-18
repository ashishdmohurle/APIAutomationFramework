# APIConstants - Class which contain all the endpoints.
# Keep the URLs

class APIConstants(object):

    @staticmethod
    def url_create_booking():
        return "/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    # Update, PUT, PATCH, DELETE - bookingId
    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)

