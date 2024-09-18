import allure
import pytest
from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import verify_http_status_code, verify_json_key_for_not_null
from src.utils.logging_util import logger  # Import the configured logger
from src.utils.utils import Utils


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        try:
            logger.info("Starting test: test_create_booking_positive")

            response = post_request(
                url=APIConstants().url_create_booking(),
                auth=None,
                headers=Utils().common_headers_json(),
                payload=payload_create_booking(),
                in_json=False
            )

            logger.info(f"Request URL: {APIConstants().url_create_booking()}")
            logger.info(f"Request Headers: {Utils().common_headers_json()}")
            logger.info(f"Response Status Code: {response.status_code}")
            logger.info(f"Response Data: {response.json()}")

            # Perform verifications
            verify_http_status_code(response_data=response, expect_data=200)
            verify_json_key_for_not_null(response.json().get("bookingid"))

            logger.info("Test completed successfully.")

        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    @pytest.mark.negative
    @allure.title("Verify that Create Booking doesn't work with no payload")
    @allure.description(
        "Creating a Booking with no payload and verify that booking id")
    def test_create_booking_negative(self):
        try:
            logger.info("Starting test: test_create_booking_negative")
            response = post_request(
                url=APIConstants().url_create_booking(),
                auth=None,
                headers=Utils().common_headers_json(),
                payload={},
                in_json=False
            )
            logger.info(f"Request URL: {APIConstants().url_create_booking()}")
            logger.info(f"Request Headers: {Utils().common_headers_json()}")
            logger.info(f"Response Status Code: {response.status_code}")

            verify_http_status_code(response_data=response, expect_data=500)
            logger.info("Test completed successfully.")

        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise
