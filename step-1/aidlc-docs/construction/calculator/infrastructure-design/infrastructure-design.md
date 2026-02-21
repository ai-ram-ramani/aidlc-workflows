# Infrastructure Design — Calculator

## Overview

Single CDK stack deployed to us-east-1 containing all AWS resources. Frontend files auto-deployed via CDK BucketDeployment construct.

## AWS Region
- **Primary Region**: us-east-1 (N. Virginia)
- **Rationale**: Optimal for CloudFront integration, broadest AWS service availability

## Resource Definitions

### 1. S3 Bucket — Frontend Static Assets

| Property | Value |
|---|---|
| Purpose | Host HTML, CSS, JS files |
| Public Access | Blocked (all public access denied) |
| Access | CloudFront OAC only |
| Versioning | Disabled (not needed for demo) |
| Encryption | S3-managed (SSE-S3, default) |
| Removal Policy | DESTROY (demo project, easy cleanup) |
| Auto Empty | Yes (allow CDK to delete non-empty bucket) |

### 2. CloudFront Distribution — CDN

| Property | Value |
|---|---|
| Purpose | Serve frontend with low latency |
| Origin | S3 bucket via Origin Access Control (OAC) |
| Default Root Object | index.html |
| Price Class | PriceClass.PRICE_CLASS_100 (cheapest — NA/EU only) |
| Viewer Protocol Policy | REDIRECT_TO_HTTPS |
| Cache Policy | CachePolicy.CACHING_OPTIMIZED |
| Error Pages | 403/404 → /index.html (SPA-style fallback) |

### 3. Lambda Function — Calculation Service

| Property | Value |
|---|---|
| Runtime | Python 3.12 |
| Handler | handler.handler |
| Memory | 128 MB |
| Timeout | 10 seconds |
| Architecture | ARM64 (Graviton — cost efficient) |
| Code Location | `lambda/` directory in project root |
| Environment Variables | None required |

### 4. API Gateway REST API

| Property | Value |
|---|---|
| Type | REST API (not HTTP API) |
| Endpoint Type | REGIONAL |
| Resource | /calculate |
| Method | POST |
| Integration | Lambda proxy integration |
| CORS | Enabled — allow CloudFront domain and localhost |
| Throttling | Default (10,000 req/s burst, 5,000 req/s steady) |
| Stage | prod |

### 5. S3 BucketDeployment — Frontend Auto-Deploy

| Property | Value |
|---|---|
| Source | `frontend/` directory in project root |
| Destination | S3 frontend bucket |
| Distribution | CloudFront distribution (triggers cache invalidation) |
| Distribution Paths | /* (invalidate all on deploy) |

### 6. IAM Roles

**Lambda Execution Role**:
- Managed Policy: AWSLambdaBasicExecutionRole (CloudWatch Logs)
- No additional policies needed (no database, no S3 access)

**CloudFront OAC**:
- S3 bucket policy grants CloudFront read access via OAC principal

## CDK Stack Outputs

| Output | Value | Purpose |
|---|---|---|
| CloudFrontURL | Distribution domain name | Access the calculator UI |
| ApiEndpoint | API Gateway invoke URL | API base URL (used by frontend) |

## Extension Compliance
| Extension | Status | Rationale |
|---|---|---|
| Security Baseline | N/A | Disabled per user choice (demo/prototype project) |
