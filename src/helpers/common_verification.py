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


def verify_create_booking_response_schema(response, schema_path=r'C:\Users\ashis\PycharmProjects'
                                                                r'\API_Automation_Framework\src\resources'
                                                                r'\create_booking_response_schema.json'):
    """
    Validates the JSON response against the schema loaded from the specified file path.

    :param response: The JSON response to validate.
    :param schema_path: The file path to the JSON schema.
    :raises AssertionError: If the validation fails.
    """
    try:
        # Load the schema from the specified file path
        with open(schema_path) as f:
            response_schema = json.load(f)

        # Validate the response against the schema
        validate(instance=response, schema=response_schema)
        return True

    except FileNotFoundError:
        raise AssertionError(f"Schema file not found at path: {schema_path}")

    except ValidationError as e:
        raise AssertionError(f"JSON schema validation failed: {e}")
