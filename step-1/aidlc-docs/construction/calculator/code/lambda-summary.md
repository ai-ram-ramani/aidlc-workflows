# Lambda Code Summary

## Files
- `lambda/handler.py` — Lambda entry point with `handler()`, `validate_request()`, and `calculate()` functions

## Functions
- `handler(event, context)` — Parses JSON body, validates, calculates, returns response with CORS headers. Handles OPTIONS preflight.
- `validate_request(body)` — Validates presence and types of operand1, operand2, operator. Returns tuple or raises ValueError.
- `calculate(operand1, operand2, operator)` — Performs add/subtract/multiply/divide. Raises ZeroDivisionError for divide-by-zero.

## Tests
- `tests/test_handler.py` — 19 unit tests covering all operations, error cases, CORS, and input validation.
