# Services

## Service: Calculation API

- **Name**: Calculation API
- **Type**: REST API (API Gateway + Lambda)
- **Purpose**: Provide a single HTTP endpoint for performing arithmetic calculations
- **Orchestration**: Synchronous request-response pattern
  1. Client sends POST /calculate with JSON body
  2. API Gateway validates request and forwards to Lambda
  3. Lambda validates input, performs calculation, returns result
  4. API Gateway returns response to client

### Service Interface

| Attribute | Value |
|---|---|
| Protocol | HTTPS (REST) |
| Method | POST |
| Path | /calculate |
| Content-Type | application/json |
| Authentication | None (public) |
| Rate Limiting | API Gateway default throttling |
| CORS | Allowed from CloudFront domain |

### Service Behavior

- Stateless — no session or state between requests
- Synchronous — client waits for response
- Idempotent — same inputs always produce same output
- No side effects — no data written or stored
