# Calculator App

A web-based calculator with an AWS serverless backend. Users enter basic arithmetic operations in the browser, which are computed by a Python Lambda function via API Gateway.

## Architecture

- **Frontend**: HTML/CSS/JS served via CloudFront + S3
- **Backend**: API Gateway + Lambda (Python 3.12)
- **Infrastructure**: AWS CDK (TypeScript)

## Prerequisites

- [Node.js](https://nodejs.org/) >= 18
- [Python](https://www.python.org/) >= 3.12
- [AWS CLI](https://aws.amazon.com/cli/) configured with credentials
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) (`npm install -g aws-cdk`)

## Deployment

### 1. Install CDK dependencies

```bash
cd infra
npm install
```

### 2. Bootstrap CDK (first time only)

```bash
cdk bootstrap aws://ACCOUNT_ID/us-east-1
```

### 3. Deploy the stack

```bash
cdk deploy
```

Note the outputs:
- **CloudFrontURL** — the calculator UI URL
- **ApiEndpoint** — the API Gateway base URL

### 4. Update the API URL in the frontend

Edit `frontend/app.js` and replace the `API_URL` placeholder with the **ApiEndpoint** output (without trailing slash):

```javascript
const API_URL = "https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod";
```

### 5. Redeploy to update the frontend

```bash
cdk deploy
```

The calculator is now accessible at the **CloudFrontURL**.

## Running Tests

```bash
# From project root
pip install pytest
PYTHONPATH=. pytest tests/ -v
```

Note: The test imports use `lambda_` (with underscore) as the module name since `lambda` is a Python reserved word. Create a symlink or rename if needed:

```bash
ln -s lambda lambda_
```

## Cleanup

```bash
cd infra
cdk destroy
```

This removes all AWS resources including S3 bucket contents.
