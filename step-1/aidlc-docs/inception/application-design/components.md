# Components

## Component 1: Calculator UI (Frontend)

- **Name**: calculator-ui
- **Type**: Static Web Application (HTML/CSS/JS)
- **Purpose**: Provide a web-based calculator interface for users to input operands, select operations, and view results
- **Responsibilities**:
  - Render calculator display and button grid
  - Capture user input (digits, operators, clear, equals)
  - Build and manage the current expression state
  - Send computation requests to the backend API
  - Display results or error messages from the API
  - Handle UI state (input mode, result display, error display)
- **Hosting**: S3 bucket served via CloudFront CDN

## Component 2: Calculation Service (Backend)

- **Name**: calculation-service
- **Type**: AWS Lambda Function (Python)
- **Purpose**: Receive calculation requests, validate inputs, perform arithmetic, and return results
- **Responsibilities**:
  - Parse and validate incoming JSON request body
  - Validate operand types (must be numeric)
  - Validate operator (must be one of: add, subtract, multiply, divide)
  - Perform the requested arithmetic operation
  - Handle division by zero with appropriate error response
  - Return JSON response with result or error

## Component 3: Infrastructure (CDK Stack)

- **Name**: calculator-stack
- **Type**: AWS CDK Stack (TypeScript)
- **Purpose**: Define and provision all AWS resources as a single CloudFormation stack
- **Responsibilities**:
  - Create S3 bucket for static site hosting
  - Create CloudFront distribution pointing to S3 origin
  - Create Lambda function with Python runtime
  - Create API Gateway REST API with single POST endpoint
  - Configure CORS on API Gateway
  - Set up IAM roles and policies
  - Output CloudFront URL and API endpoint
