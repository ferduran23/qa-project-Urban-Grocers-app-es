# Urban Grocers API Testing

## Description

This project contains automated tests for the Urban Grocers API, specifically for the endpoint responsible for creating kits for a user.

The goal is to validate different input scenarios for the `name` field and verify that the API behaves according to the documentation.

## Test Coverage

The following scenarios are covered:

* Valid name with 1 character
* Valid name with 511 characters
* Empty name (should return an error)
* Name exceeding the maximum allowed length (512 characters)
* Use of special characters
* Use of spaces in the name
* Numeric values provided as text
* Missing `name` parameter
* Incorrect data type (`number` instead of `string`)

## Technologies Used

* Python
* Pytest
* Requests

## Running the Tests

1. Install dependencies:

```bash
pip install pytest requests
```

2. Run the test suite:

```bash
pytest create_kit_name_kit_test.py
```

## Project Structure

* `configuration.py` → API URLs and endpoints
* `data.py` → Request payloads
* `sender_stand_request.py` → Functions for sending requests
* `create_kit_name_kit_test.py` → Test cases
* `README.md` → Project documentation
* `.gitignore` → Ignored files

