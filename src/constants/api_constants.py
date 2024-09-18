# APIConstants - Class which contain all the endpoints.
# Keep the URLs


class APIConstants(object):

    @staticmethod
    def url_create_booking():
        return "/booking"

    @staticmethod
    def url_create_token():
        return "/auth"

    # Update, PUT, PATCH, DELETE - bookingId
    @staticmethod
    def url_patch_put_delete(booking_id):
        return "/booking/" + str(booking_id)

