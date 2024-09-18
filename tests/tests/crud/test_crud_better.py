# Create Token
# Create Booking Id
# Update the Booking(Put) - BookingID, Token
# Delete the Booking
import os

# Verify that created booking id when we update we are able to update it and delete it also


import allure
import pytest
import logging
from src.utils.logging_util import logger, log_with_delimiter
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


class TestCRUDBooking(object):
    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description("Verify that Full Update with the booking ID and Token is working.")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        try:
            logger.info("Starting test: test_update_booking_id_token")
            booking_id = get_booking_id
            token = create_token
            put_url = os.getenv('QA_BASE_URL') + APIConstants.url_patch_put_delete(booking_id=booking_id)
            response = put_requests(
                url=put_url,
                headers=Utils().common_header_put_delete_patch_cookie(token=token),
                payload=payload_create_booking(),
                auth=None,
                in_json=False
            )
            logger.info(f"Request URL: {put_url}")
            logger.info(f"Request Headers: {Utils().common_headers_json()}")
            logger.info(f"Response Status Code: {response.status_code}")
            logger.info(f"Response Data: {response.json()}")

            verify_response_key(response.json()["firstname"], "Amit")
            verify_response_key(response.json()["lastname"], "Brown")
            verify_http_status_code(response_data=response, expect_data=200)

            log_with_delimiter(logger, "Test completed successfully.")

        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    @allure.title("Test CRUD operation Delete(delete)")
    @allure.description("Verify booking gets deleted with the booking ID and Token.")
    def test_delete_booking_id(self, create_token, get_booking_id):
        try:
            logger.info("Starting test: test_delete_booking_id")
            booking_id = get_booking_id
            token = create_token
            delete_url = os.getenv('QA_BASE_URL') + APIConstants.url_patch_put_delete(booking_id=booking_id)
            response = delete_requests(
                url=delete_url,
                headers=Utils().common_header_put_delete_patch_cookie(token=token),
                auth=None,
                in_json=False
            )
            logger.info(f"Request URL: {delete_url}")
            logger.info(f"Request Headers: {Utils().common_headers_json()}")
            logger.info(f"Response Status Code: {response.status_code}")
            logger.info(f"Response Data: {response.text}")


            verify_response_delete(response=response.text)
            verify_http_status_code(response_data=response, expect_data=201)

            log_with_delimiter(logger, "Test completed successfully.")

        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise
