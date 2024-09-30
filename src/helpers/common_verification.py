# Common Verification
# HTTP Status Code
# Headers
# Data Verification
# JSON schema
import json
from jsonschema import validate, ValidationError


def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, "Failed ER!=AR"


def verify_response_key(key, expected_data):
    assert key == expected_data


def verify_json_key_for_not_null(key):
    assert key != 0, "Failed - Key is non Empty" + key
    assert key > 0, "Failed - Key is grater than zero"


def verify_json_key_for_not_null_token(key):
    assert key != 0, "Failed - Key is non Empty" + key


def verify_response_key_should_not_be_none(key):
    assert key is not None


def verify_response_delete(response):
    assert "Created" in response


def verify_create_booking_response_schema(response,
                                          schema_path=r"C:\Users\ashis\PycharmProjects\API_Automation_Framework\src\resources\create_booking_response_schema.json"):
    with open(schema_path, 'r') as f:
        response_schema = json.load(f)

    try:
        validate(instance=response, schema=response_schema)
        return True
    except Exception as e:
        print(e)


def verify_the_response(response,
                        expected_response=r"C:\Users\ashis\PycharmProjects\API_Automation_Framework\src\resources\expected_response_json.json"):
    with open(expected_response) as f:
        expt_response = json.load(f)

    expt_response.pop('bookingid', None)
    response.pop('bookingid', None)
    try:
        assert expt_response == response, f"Response does not match the expected output.\nExpected: {expt_response}\nActual: {response}"
        return True
    except AssertionError as e:
        raise AssertionError(f"Assertion Error: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {expected_response}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from {expected_response}: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")