"""Unit tests for the calculator Lambda function."""

import json
import pytest
from lambda_.handler import handler, validate_request, calculate


def _make_event(body):
    """Helper to create an API Gateway proxy event."""
    return {
        "httpMethod": "POST",
        "body": json.dumps(body) if isinstance(body, dict) else body,
    }


class TestCalculate:
    """Tests for the calculate function."""

    def test_add(self):
        assert calculate(5, 3, "add") == 8

    def test_subtract(self):
        assert calculate(10, 4, "subtract") == 6

    def test_multiply(self):
        assert calculate(3, 7, "multiply") == 21

    def test_divide(self):
        assert calculate(10, 2, "divide") == 5.0

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            calculate(10, 0, "divide")

    def test_add_negative_numbers(self):
        assert calculate(-5, -3, "add") == -8

    def test_multiply_by_zero(self):
        assert calculate(5, 0, "multiply") == 0

    def test_divide_decimals(self):
        assert calculate(7, 2, "divide") == 3.5


class TestValidateRequest:
    """Tests for the validate_request function."""

    def test_valid_request(self):
        result = validate_request({"operand1": 5, "operand2": 3, "operator": "add"})
        assert result == (5.0, 3.0, "add")

    def test_missing_operand1(self):
        with pytest.raises(ValueError, match="Missing required field: operand1"):
            validate_request({"operand2": 3, "operator": "add"})

    def test_missing_operand2(self):
        with pytest.raises(ValueError, match="Missing required field: operand2"):
            validate_request({"operand1": 5, "operator": "add"})

    def test_missing_operator(self):
        with pytest.raises(ValueError, match="Missing required field: operator"):
            validate_request({"operand1": 5, "operand2": 3})

    def test_non_numeric_operand1(self):
        with pytest.raises(ValueError, match="operand1 must be a number"):
            validate_request({"operand1": "abc", "operand2": 3, "operator": "add"})

    def test_non_numeric_operand2(self):
        with pytest.raises(ValueError, match="operand2 must be a number"):
            validate_request({"operand1": 5, "operand2": "xyz", "operator": "add"})

    def test_invalid_operator(self):
        with pytest.raises(ValueError, match="Invalid operator"):
            validate_request({"operand1": 5, "operand2": 3, "operator": "modulo"})

    def test_string_numbers_accepted(self):
        result = validate_request({"operand1": "5", "operand2": "3", "operator": "add"})
        assert result == (5.0, 3.0, "add")


class TestHandler:
    """Tests for the Lambda handler function."""

    def test_successful_addition(self):
        event = _make_event({"operand1": 5, "operand2": 3, "operator": "add"})
        response = handler(event, None)
        assert response["statusCode"] == 200
        body = json.loads(response["body"])
        assert body["result"] == 8

    def test_successful_division(self):
        event = _make_event({"operand1": 10, "operand2": 4, "operator": "divide"})
        response = handler(event, None)
        assert response["statusCode"] == 200
        body = json.loads(response["body"])
        assert body["result"] == 2.5

    def test_division_by_zero_error(self):
        event = _make_event({"operand1": 10, "operand2": 0, "operator": "divide"})
        response = handler(event, None)
        assert response["statusCode"] == 400
        body = json.loads(response["body"])
        assert body["error"] == "Division by zero is not allowed"

    def test_invalid_operator_error(self):
        event = _make_event({"operand1": 5, "operand2": 3, "operator": "power"})
        response = handler(event, None)
        assert response["statusCode"] == 400
        body = json.loads(response["body"])
        assert "Invalid operator" in body["error"]

    def test_malformed_json(self):
        event = {"httpMethod": "POST", "body": "not-json"}
        response = handler(event, None)
        assert response["statusCode"] == 400
        body = json.loads(response["body"])
        assert body["error"] == "Invalid JSON in request body"

    def test_missing_fields(self):
        event = _make_event({"operand1": 5})
        response = handler(event, None)
        assert response["statusCode"] == 400

    def test_cors_headers_present(self):
        event = _make_event({"operand1": 1, "operand2": 2, "operator": "add"})
        response = handler(event, None)
        assert response["headers"]["Access-Control-Allow-Origin"] == "*"

    def test_options_preflight(self):
        event = {"httpMethod": "OPTIONS"}
        response = handler(event, None)
        assert response["statusCode"] == 200
