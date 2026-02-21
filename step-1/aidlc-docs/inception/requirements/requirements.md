# Requirements Document — Web UI Calculator App

## Intent Analysis Summary

- **User Request**: Build a Web UI calculator app with AWS cloud backend for basic mathematical computations
- **Request Type**: New Project (Greenfield)
- **Scope**: Multiple Components (Frontend + Backend API + Infrastructure)
- **Complexity**: Moderate (simple business logic, multi-tier architecture)
- **Clarity**: Clear — all ambiguities resolved via clarifying questions

---

## Functional Requirements

### FR-01: Calculator User Interface
- The app SHALL provide a web-based calculator UI built with plain HTML, CSS, and JavaScript (no framework)
- The UI SHALL display a numeric input/display area and operation buttons
- The UI SHALL include buttons for digits 0–9, decimal point, and clear

### FR-02: Supported Operations
- The app SHALL support addition (+)
- The app SHALL support subtraction (−)
- The app SHALL support multiplication (×)
- The app SHALL support division (÷)
- The app SHALL display an error message for division by zero

### FR-03: Computation via Backend API
- The UI SHALL send computation requests to an AWS backend API
- The API SHALL accept two operands and an operator
- The API SHALL return the computed result
- The API SHALL return appropriate error responses for invalid inputs

### FR-04: Stateless Operation
- The app SHALL NOT persist calculation history
- Each computation SHALL be independent and stateless
- No user authentication is required

---

## Non-Functional Requirements

### NFR-01: Architecture
- **Frontend**: Static HTML/CSS/JS hosted on AWS S3 with CloudFront CDN
- **Backend**: AWS API Gateway + AWS Lambda (serverless)
- **Infrastructure as Code**: AWS CDK (TypeScript)
- **Backend Language**: Python (Lambda function)

### NFR-02: Performance
- Target: Low traffic (< 100 users), personal/demo project
- Lambda cold start latency acceptable for this use case
- No caching layer required

### NFR-03: Availability
- Standard AWS Lambda/API Gateway availability (no multi-region or HA requirements)

### NFR-04: Security
- Security extension rules are NOT enforced (demo/prototype project)
- CORS configured on API Gateway to allow requests from the CloudFront domain
- Input validation on Lambda to prevent malformed requests

### NFR-05: Cost
- Serverless architecture minimizes cost for low-traffic usage
- S3 + CloudFront + Lambda all fall within AWS Free Tier for expected usage

---

## Technical Architecture Overview

```
+-------------------+       +-------------------+       +-------------------+
|                   |       |                   |       |                   |
|   CloudFront      +------>+   API Gateway     +------>+   Lambda          |
|   (CDN)           |       |   (REST API)      |       |   (Python)        |
|                   |       |                   |       |                   |
+--------+----------+       +-------------------+       +-------------------+
         |
         |
+--------+----------+
|                   |
|   S3 Bucket       |
|   (Static Site)   |
|                   |
+-------------------+
```

- User accesses the calculator via CloudFront URL
- Static assets (HTML/CSS/JS) served from S3 via CloudFront
- Calculator sends API requests to API Gateway
- API Gateway routes to Lambda function for computation
- Lambda returns result to frontend

---

## Constraints and Assumptions

- No database or persistent storage required
- No user authentication or session management
- Single AWS region deployment
- AWS CDK used for all infrastructure provisioning
- Python 3.12+ for Lambda runtime
