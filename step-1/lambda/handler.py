"""Calculator Lambda function — performs basic arithmetic operations."""

import json


def handler(event, context):
    """Lambda entry point. Parses request, validates, calculates, returns response."""
    cors_headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
    }

    # Handle CORS preflight
    if event.get("httpMethod") == "OPTIONS":
        return {"statusCode": 200, "headers": cors_headers, "body": ""}

    try:
        body = json.loads(event.get("body", "{}"))
    except (json.JSONDecodeError, TypeError):
        return {
            "statusCode": 400,
            "headers": cors_headers,
            "body": json.dumps({"error": "Invalid JSON in request body"}),
        }

    try:
        operand1, operand2, operator = validate_request(body)
    except ValueError as e:
        return {
            "statusCode": 400,
            "headers": cors_headers,
            "body": json.dumps({"error": str(e)}),
        }

    try:
        result = calculate(operand1, operand2, operator)
    except ZeroDivisionError:
        return {
            "statusCode": 400,
            "headers": cors_headers,
            "body": json.dumps({"error": "Division by zero is not allowed"}),
        }

    return {
        "statusCode": 200,
        "headers": cors_headers,
        "body": json.dumps({"result": result}),
    }


def validate_request(body):
    """Validate request body fields and types.

    Returns:
        tuple: (operand1, operand2, operator)

    Raises:
        ValueError: If validation fails.
    """
    if "operand1" not in body:
        raise ValueError("Missing required field: operand1")
    if "operand2" not in body:
        raise ValueError("Missing required field: operand2")
    if "operator" not in body:
        raise ValueError("Missing required field: operator")

    try:
        operand1 = float(body["operand1"])
    except (TypeError, ValueError):
        raise ValueError("operand1 must be a number")

    try:
        operand2 = float(body["operand2"])
    except (TypeError, ValueError):
        raise ValueError("operand2 must be a number")

    valid_operators = ("add", "subtract", "multiply", "divide")
    operator = body["operator"]
    if operator not in valid_operators:
        raise ValueError(
            f"Invalid operator. Must be one of: {', '.join(valid_operators)}"
        )

    return operand1, operand2, operator


def calculate(operand1, operand2, operator):
    """Perform arithmetic operation.

    Returns:
        float: The calculation result.

    Raises:
        ZeroDivisionError: If dividing by zero.
    """
    if operator == "add":
        return operand1 + operand2
    elif operator == "subtract":
        return operand1 - operand2
    elif operator == "multiply":
        return operand1 * operand2
    elif operator == "divide":
        if operand2 == 0:
            raise ZeroDivisionError("Division by zero")
        return operand1 / operand2
