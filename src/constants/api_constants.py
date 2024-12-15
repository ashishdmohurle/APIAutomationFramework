class APIConstants:
    # Base URLs
    CREATE_BOOKING = "/booking"
    CREATE_TOKEN = "/auth"

    # Dynamic URL for specific booking ID
    @staticmethod
    def PATCH_PUT_DELETE(booking_id):
        return f"{APIConstants.CREATE_BOOKING}/{booking_id}"
