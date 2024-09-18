from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils

import pytest
import os
from dotenv import load_dotenv
from src.utils.logging_util import logger, log_with_delimiter


@pytest.fixture(scope="session")
def create_token():
    try:
        logger.info("Create Token")
        response = post_request(
            url=os.getenv('QA_BASE_URL') + APIConstants.url_create_token(),
            headers=Utils().common_headers_json(),
            auth=None,
            payload=payload_create_token(),
            in_json=False
        )
        logger.info(f"Request URL: {os.getenv('QA_BASE_URL') + APIConstants.url_create_token()}")
        logger.info(f"Request Headers: {Utils().common_headers_json()}")
        logger.info(f"Response Status Code: {response.status_code}")
        logger.info(f"Response Data: {response.json()}")
        log_with_delimiter(logger, "Test completed successfully.")

        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null_token(response.json()["token"])


    except Exception as e:
        logger.error(f"Test failed: {e}")
        raise

    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    try:
        logger.info("Create Booking")
        response = post_request(
            url=os.getenv('QA_BASE_URL') + APIConstants.url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )

        booking_id = response.json()["bookingid"]
        logger.info(f"Request URL: {os.getenv('QA_BASE_URL') + APIConstants.url_create_booking()}")
        logger.info(f"Request Headers: {Utils().common_headers_json()}")
        logger.info(f"Response Status Code: {response.status_code}")
        logger.info(f"Response Data: {response.json()}")
        log_with_delimiter(logger, "Test completed successfully.")

        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

    except Exception as e:
        logger.info(f"Test Failed: {e}")
        raise

    return booking_id


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="qa", help="Environment to run tests against (e.g., qa, staging)"
    )


@pytest.fixture(scope="session", autouse=True)
def load_environment(pytestconfig):
    load_dotenv()
    selected_env = pytestconfig.getoption("env").lower()

    if selected_env == "qa":
        os.environ["BASE_URL"] = os.getenv("QA_BASE_URL")
        os.environ["API_KEY"] = os.getenv("QA_API_KEY")
        os.environ["ENV"] = os.getenv("QA_ENV")
    elif selected_env == "prod":
        os.environ["BASE_URL"] = os.getenv("PROD_BASE_URL")
        os.environ["API_KEY"] = os.getenv("PROD_API_KEY")
        os.environ["ENV"] = os.getenv("PROD_ENV")
    else:
        raise ValueError(f"Unknown environment: {selected_env}")

    print(f"Running tests in {selected_env} environment")