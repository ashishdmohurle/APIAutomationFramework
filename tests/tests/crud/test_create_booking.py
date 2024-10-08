import os

import allure
import pytest

from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import verify_http_status_code, verify_json_key_for_not_null, \
    verify_response_key_should_not_be_none, verify_create_booking_response_schema, verify_the_response
from src.utils.logging_util import logger, log_with_delimiter  # Import the configured logger
from src.utils.utils import Utils


class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should not be null and status code should be "
        "200 for the correct payload")
    def test_create_booking_positive(self):

        try:
            logger.info("Starting test: test_create_booking_positive")

            response = post_request(
                url=os.getenv("QA_BASE_URL") + APIConstants.url_create_booking(),
                auth=None,
                headers=Utils().common_headers_json(),
                payload=payload_create_booking(),
                in_json=False
            )

            logger.info(f"Request URL: {os.getenv("QA_BASE_URL") + APIConstants.url_create_booking()}")
            logger.info(f"Request Headers: {Utils().common_headers_json()}")
            logger.info(f"Response Status Code: {response.status_code}")
            logger.info(f"Response Data: {response.json()}")

            # Perform verifications
            verify_http_status_code(response_data=response, expect_data=200)
            verify_create_booking_response_schema(response.json())
            verify_the_response(response.json())
            verify_json_key_for_not_null(response.json().get("bookingid"))
            verify_response_key_should_not_be_none(response.json().get("bookingid"))

            log_with_delimiter(logger, "Test completed successfully.")

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
                url=os.getenv("QA_BASE_URL") + APIConstants.url_create_booking(),
                auth=None,
                headers=Utils().common_headers_json(),
                payload={},
                in_json=False
            )
            logger.info(f"Request URL: {os.getenv("QA_BASE_URL") + APIConstants.url_create_booking()}")
            logger.info(f"Request Headers: {Utils().common_headers_json()}")
            logger.info(f"Response Status Code: {response.status_code}")

            verify_http_status_code(response_data=response, expect_data=500)
            log_with_delimiter(logger, "Test completed successfully.")

        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise
