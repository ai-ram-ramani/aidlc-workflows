# Deployment Architecture — Calculator

## Architecture Diagram

```
                          Internet
                             |
                             v
                  +---------------------+
                  |    CloudFront CDN    |
                  |  (HTTPS, us-east-1) |
                  +----------+----------+
                             |
              +--------------+--------------+
              |                             |
              v                             v
   +-------------------+        +-------------------+
   |   S3 Bucket       |        |   API Gateway     |
   |   (Static Files)  |        |   (REST API)      |
   |   - index.html    |        |   POST /calculate |
   |   - style.css     |        |   CORS enabled    |
   |   - app.js        |        +--------+----------+
   +-------------------+                 |
                                         v
                              +-------------------+
                              |   Lambda Function  |
                              |   (Python 3.12)    |
                              |   ARM64 / 128MB    |
                              +-------------------+
```

## Project Directory Structure

```
calculator-app/
+-- frontend/                  # Static web files (deployed to S3)
|   +-- index.html
|   +-- style.css
|   +-- app.js
+-- lambda/                    # Lambda function code
|   +-- handler.py
+-- infra/                     # CDK infrastructure
|   +-- bin/
|   |   +-- app.ts             # CDK app entry point
|   +-- lib/
|   |   +-- calculator-stack.ts # Main stack definition
|   +-- cdk.json
|   +-- package.json
|   +-- tsconfig.json
+-- README.md
```

## Deployment Flow

1. Developer runs `cdk deploy` from `infra/` directory
2. CDK creates/updates CloudFormation stack in us-east-1:
   - Provisions S3 bucket, CloudFront, API Gateway, Lambda
   - BucketDeployment uploads `frontend/` files to S3
   - CloudFront cache invalidation triggered
3. Stack outputs display CloudFront URL and API endpoint
4. API endpoint URL must be configured in `frontend/app.js` before deployment

## API URL Configuration Strategy

The frontend needs to know the API Gateway endpoint URL. Since CDK BucketDeployment deploys frontend files as part of the stack:

- **Approach**: Use a two-phase deployment or a config injection pattern
  - **Option A (Simple)**: First deploy creates the API. Copy the API URL into `app.js`. Redeploy to update frontend.
  - **Option B (Automated)**: CDK custom resource writes a `config.js` file to S3 after stack creation with the API URL.
  
- **Chosen**: Option A (simple approach) — suitable for demo project. The API URL is set as a constant in `app.js` and updated after first deployment.

## Cleanup

```bash
cd infra
cdk destroy
```

This removes all AWS resources including the S3 bucket contents (auto-delete enabled).
