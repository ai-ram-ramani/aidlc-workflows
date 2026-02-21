# Code Generation Plan — Calculator

## Unit Context
- **Unit**: calculator (single unit)
- **Project Type**: Greenfield
- **Workspace Root**: .
- **Code Location**: Workspace root (NEVER aidlc-docs/)

## Project Structure
```
calculator-app/
+-- frontend/                  # Static web files (deployed to S3)
|   +-- index.html             # Calculator HTML structure
|   +-- style.css              # Minimal/clean styling
|   +-- app.js                 # Calculator logic and API calls
+-- lambda/                    # Lambda function code
|   +-- handler.py             # Lambda entry point + calculation logic
+-- infra/                     # CDK infrastructure
|   +-- bin/
|   |   +-- app.ts             # CDK app entry point
|   +-- lib/
|   |   +-- calculator-stack.ts # Main stack definition
|   +-- cdk.json
|   +-- package.json
|   +-- tsconfig.json
+-- tests/                     # Tests
|   +-- test_handler.py        # Lambda unit tests
+-- README.md
```

## Dependencies
- None (single unit, no external service dependencies)

## Code Generation Steps

### Step 1: Project Structure Setup
- [x] Create directory structure: `frontend/`, `lambda/`, `infra/bin/`, `infra/lib/`, `tests/`

### Step 2: Lambda Function — Business Logic
- [x] Create `lambda/handler.py` with:
  - `handler(event, context)` — Lambda entry point, parses body, calls validate + calculate, returns response
  - `validate_request(body)` — Validates operand1, operand2, operator fields and types
  - `calculate(operand1, operand2, operator)` — Performs add/subtract/multiply/divide
  - Error handling for division by zero, invalid input, malformed JSON
  - CORS headers in response

### Step 3: Lambda Unit Tests
- [x] Create `tests/test_handler.py` with:
  - Tests for all 4 operations (add, subtract, multiply, divide)
  - Test division by zero error
  - Test invalid operator error
  - Test missing fields error
  - Test non-numeric operands error
  - Test malformed JSON body

### Step 4: Lambda Code Summary
- [x] Create `aidlc-docs/construction/calculator/code/lambda-summary.md`

### Step 5: Frontend — HTML Structure
- [x] Create `frontend/index.html` with:
  - Calculator display area
  - Digit buttons (0-9, decimal point)
  - Operator buttons (+, −, ×, ÷)
  - Equals and Clear buttons
  - `data-testid` attributes on all interactive elements
  - Script and stylesheet references

### Step 6: Frontend — CSS Styling
- [x] Create `frontend/style.css` with:
  - Minimal/clean design, light theme
  - CSS Grid layout for button grid
  - Responsive sizing
  - Display area styling

### Step 7: Frontend — JavaScript Logic
- [x] Create `frontend/app.js` with:
  - API_URL constant (placeholder, updated after first deploy)
  - `handleDigit(digit)`, `handleOperator(op)`, `handleEquals()`, `handleClear()`
  - `sendCalculation(operand1, operand2, operator)` — fetch POST to API
  - `updateDisplay(value)` — DOM update
  - Event listeners for all buttons
  - Error display handling

### Step 8: Frontend Code Summary
- [x] Create `aidlc-docs/construction/calculator/code/frontend-summary.md`

### Step 9: CDK Infrastructure — Package Setup
- [x] Create `infra/package.json` with CDK dependencies
- [x] Create `infra/tsconfig.json`
- [x] Create `infra/cdk.json`

### Step 10: CDK Infrastructure — Stack Definition
- [x] Create `infra/lib/calculator-stack.ts` with:
  - S3 bucket (blocked public access, auto-delete, removal policy DESTROY)
  - CloudFront distribution (OAC to S3, HTTPS redirect, PriceClass 100)
  - Lambda function (Python 3.12, ARM64, 128MB, 10s timeout)
  - API Gateway REST API (POST /calculate, Lambda proxy, CORS)
  - BucketDeployment (frontend/ → S3, CloudFront invalidation)
  - Stack outputs (CloudFront URL, API endpoint)

### Step 11: CDK Infrastructure — App Entry Point
- [x] Create `infra/bin/app.ts` with CDK app instantiation

### Step 12: Infrastructure Code Summary
- [x] Create `aidlc-docs/construction/calculator/code/infrastructure-summary.md`

### Step 13: README
- [x] Create `README.md` with:
  - Project overview
  - Prerequisites (Node.js, Python, AWS CDK, AWS CLI)
  - Deployment instructions
  - API URL configuration steps
  - Cleanup instructions

### Step 14: Final Validation
- [x] Verify all files created at correct paths (not in aidlc-docs/)
- [x] Verify no duplicate files
- [x] Verify all plan steps marked [x]
