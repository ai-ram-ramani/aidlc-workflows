# Application Design — Web UI Calculator

## Overview

A stateless web calculator application with three components: a static HTML/CSS/JS frontend served via CloudFront, a Python Lambda backend for arithmetic computation, and a CDK infrastructure stack provisioning all AWS resources.

## Architecture

```
+-------------------+     HTTPS POST      +-------------------+     Lambda Proxy    +-------------------+
|                   |    /calculate       |                   |    Integration      |                   |
|   Calculator UI   +-------------------->+   API Gateway     +-------------------->+   Lambda          |
|   (Browser)       |                     |   (REST API)      |                     |   (Python 3.12)   |
|                   +<--------------------+                   +<--------------------+                   |
|                   |     JSON Response   |                   |     JSON Response   |                   |
+--------+----------+                     +-------------------+                     +-------------------+
         |
         | Static Assets (HTML/CSS/JS)
         |
+--------+----------+                     +-------------------+
|                   |        OAC          |                   |
|   CloudFront      +-------------------->+   S3 Bucket       |
|   (CDN)           |                     |   (Static Files)  |
+-------------------+                     +-------------------+
```

## Components

### 1. Calculator UI (Frontend)
- **Technology**: Plain HTML, CSS, JavaScript
- **Style**: Minimal/clean — simple grid of buttons, light theme
- **Hosting**: S3 bucket via CloudFront CDN
- **Responsibilities**: Render UI, capture input, call API, display results
- **Key Functions**: handleDigit, handleOperator, handleEquals, handleClear, sendCalculation

### 2. Calculation Service (Backend)
- **Technology**: Python 3.12 on AWS Lambda
- **Responsibilities**: Validate input, perform arithmetic, return result
- **Key Functions**: handler (entry point), calculate, validate_request
- **Operations**: add, subtract, multiply, divide
- **Error Handling**: Invalid input (400), division by zero (400)

### 3. Infrastructure (CDK Stack)
- **Technology**: AWS CDK (TypeScript)
- **Organization**: Single stack containing all resources
- **Resources**: S3 Bucket, CloudFront Distribution, API Gateway REST API, Lambda Function, IAM Roles

## API Contract

**POST /calculate**

Request:
```json
{ "operand1": 5, "operand2": 3, "operator": "add" }
```

Success (200):
```json
{ "result": 8 }
```

Error (400):
```json
{ "error": "Division by zero is not allowed" }
```

Valid operators: `add`, `subtract`, `multiply`, `divide`

## Design Decisions

| Decision | Choice | Rationale |
|---|---|---|
| API Format | Single POST endpoint with JSON body | Simple, RESTful, easy to extend |
| UI Style | Minimal/clean | Matches demo project scope, fast to implement |
| CDK Organization | Single stack | Small project, no need for stack separation |
| Frontend Framework | None (vanilla JS) | Minimal dependencies, simple requirements |
| Backend Language | Python | User preference, good Lambda support |
| CORS | Enabled for CloudFront domain | Required for cross-origin API calls |

## Extension Compliance
| Extension | Status | Rationale |
|---|---|---|
| Security Baseline | N/A | Disabled per user choice (demo/prototype project) |
