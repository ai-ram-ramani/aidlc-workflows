# Infrastructure Design Plan — Calculator

## Context
- **Unit**: calculator (single unit)
- **AWS Services**: S3, CloudFront, API Gateway, Lambda
- **IaC**: AWS CDK (TypeScript), single stack
- **Security Extensions**: Disabled

## Design Plan

- [x] Define S3 bucket configuration for static site
- [x] Define CloudFront distribution configuration
- [x] Define Lambda function configuration
- [x] Define API Gateway REST API configuration
- [x] Define IAM roles and policies
- [x] Define CDK stack outputs
- [x] Generate infrastructure-design.md
- [x] Generate deployment-architecture.md
- [x] Validate design completeness

---

## Infrastructure Questions

## Question 1
What AWS region should the stack be deployed to?

A) us-east-1 (N. Virginia — best for CloudFront integration)
B) us-west-2 (Oregon)
C) eu-west-1 (Ireland)
D) Other (please describe after [Answer]: tag below)

[Answer]: A

## Question 2
Should the CDK stack include an automated frontend deployment (S3 BucketDeployment construct to upload HTML/CSS/JS during `cdk deploy`)?

A) Yes — automatically deploy frontend files as part of CDK stack deployment
B) No — deploy frontend files separately (manual S3 sync or CI/CD pipeline)
C) Other (please describe after [Answer]: tag below)

[Answer]: A

