# Infrastructure Code Summary

## Files
- `infra/lib/calculator-stack.ts` — Single CDK stack with S3, CloudFront, Lambda, API Gateway, BucketDeployment
- `infra/bin/app.ts` — CDK app entry point, deploys to us-east-1
- `infra/package.json` — CDK dependencies (aws-cdk-lib, constructs)
- `infra/tsconfig.json` — TypeScript configuration
- `infra/cdk.json` — CDK app configuration

## Stack Resources
- S3 Bucket (block public access, auto-delete, DESTROY removal policy)
- CloudFront Distribution (OAC to S3, HTTPS redirect, PriceClass 100, error page fallbacks)
- Lambda Function (Python 3.12, ARM64, 128MB, 10s timeout)
- API Gateway REST API (POST /calculate, Lambda proxy, CORS enabled)
- BucketDeployment (frontend/ → S3, CloudFront cache invalidation)

## Outputs
- CloudFrontURL — Calculator UI URL
- ApiEndpoint — API Gateway base URL
