# Requirements Verification Questions

Please answer the following questions to help clarify the requirements for the Web UI Calculator App with AWS Cloud Backend.

## Question 1
What mathematical operations should the calculator support?

A) Basic arithmetic only (addition, subtraction, multiplication, division)
B) Basic arithmetic plus advanced operations (exponents, square roots, modulo)
C) Scientific calculator (trigonometry, logarithms, factorials, etc.)
D) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 2
What frontend technology should be used for the Web UI?

A) React (JavaScript/TypeScript)
B) Vue.js
C) Plain HTML/CSS/JavaScript (no framework)
D) Angular
E) Other (please describe after [Answer]: tag below)

[Answer]: C

## Question 3
What AWS services should power the backend computation?

A) API Gateway + Lambda (serverless)
B) API Gateway + ECS/Fargate (containerized)
C) API Gateway + EC2 (traditional server)
D) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 4
How should the frontend be hosted?

A) AWS S3 + CloudFront (static hosting with CDN)
B) AWS Amplify Hosting
C) Served from the same backend service
D) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 5
Does the app require user authentication (login/signup)?

A) No authentication needed — open calculator for anyone
B) Yes — basic authentication (username/password)
C) Yes — social login (Google, GitHub, etc.) via Amazon Cognito
D) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 6
Should the app persist calculation history?

A) No — calculations are stateless, no history stored
B) Yes — store history per browser session (local storage)
C) Yes — store history server-side per user (requires authentication)
D) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 7
What Infrastructure as Code tool should be used for AWS resource provisioning?

A) AWS CDK (TypeScript)
B) AWS CloudFormation (YAML/JSON)
C) Terraform
D) AWS SAM (Serverless Application Model)
E) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 8
What backend programming language should be used?

A) Python
B) Node.js (TypeScript)
C) Java
D) Go
E) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 9
What is the expected scale and performance requirement?

A) Low traffic — personal/demo project (< 100 users)
B) Medium traffic — team or small business use (100–10,000 users)
C) High traffic — public-facing production app (10,000+ users)
D) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 10: Security Extensions
Should security extension rules be enforced for this project?

A) Yes — enforce all SECURITY rules as blocking constraints (recommended for production-grade applications)
B) No — skip all SECURITY rules (suitable for PoCs, prototypes, and experimental projects)
C) Other (please describe after [Answer]: tag below)

[Answer]: B
