from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils

import allure
import pytest
import openpyxl
import pytest
import os
from dotenv import load_dotenv


@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIConstants().url_create_token(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload_create_token(),
        in_json=False
    )
    verify_http_status_code(response_data=response, expect_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(url=APIConstants().url_create_booking(),
                            auth=None,
                            headers=Utils().common_headers_json(),
                            payload=payload_create_booking(),
                            in_json=False)

    booking_id = response.json()["bookingid"]

    verify_http_status_code(response_data=response, expect_data=200)
    verify_json_key_for_not_null(booking_id)
    return booking_id


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="qa", help="Environment to run tests against (e.g., qa, staging)"
    )


@pytest.fixture(scope="session", autouse=True)
def load_environment(pytestconfig):
    # Load the .env file
    load_dotenv()

    # Get the selected environment from the command line
    selected_env = pytestconfig.getoption("env").lower()

    # Dynamically select the environment variables based on the selected environment
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
