# Component Methods

## Calculator UI (Frontend)

### Methods / Functions

| Function | Purpose | Input | Output |
|---|---|---|---|
| `handleDigit(digit)` | Append digit to current input | `string` (0-9, .) | Updates display |
| `handleOperator(op)` | Store first operand and selected operator | `string` (add, subtract, multiply, divide) | Updates UI state |
| `handleEquals()` | Send calculation request to API | None (reads UI state) | Displays result or error |
| `handleClear()` | Reset calculator to initial state | None | Clears display and state |
| `sendCalculation(operand1, operand2, operator)` | POST request to backend API | `number, number, string` | `Promise<{result: number} \| {error: string}>` |
| `updateDisplay(value)` | Update the calculator display | `string` | Updates DOM |

## Calculation Service (Backend Lambda)

### Methods / Functions

| Function | Purpose | Input | Output |
|---|---|---|---|
| `handler(event, context)` | Lambda entry point, routes to calculate | API Gateway event | API Gateway response (JSON) |
| `calculate(operand1, operand2, operator)` | Perform arithmetic operation | `float, float, str` | `float` |
| `validate_request(body)` | Validate request body fields and types | `dict` | `tuple(float, float, str)` or raises `ValueError` |

### API Contract

**Endpoint**: `POST /calculate`

**Request Body**:
```json
{
  "operand1": 5,
  "operand2": 3,
  "operator": "add"
}
```

**Valid operators**: `add`, `subtract`, `multiply`, `divide`

**Success Response** (200):
```json
{
  "result": 8
}
```

**Error Response** (400 — validation error):
```json
{
  "error": "Invalid operator. Must be one of: add, subtract, multiply, divide"
}
```

**Error Response** (400 — division by zero):
```json
{
  "error": "Division by zero is not allowed"
}
```

## Infrastructure (CDK Stack)

### Constructs

| Construct | Purpose | Key Configuration |
|---|---|---|
| `S3 Bucket` | Host static frontend files | Block public access, website hosting not needed (CloudFront OAC) |
| `CloudFront Distribution` | CDN for frontend delivery | S3 origin with OAC, default root object: index.html |
| `Lambda Function` | Run calculation logic | Python 3.12, 128MB memory, 10s timeout |
| `API Gateway REST API` | HTTP endpoint for calculations | Single POST /calculate route, CORS enabled |
| `IAM Roles` | Least-privilege access | Lambda execution role, CloudFront OAC policy |
