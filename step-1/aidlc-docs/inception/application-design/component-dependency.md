# Component Dependencies

## Dependency Matrix

| Component | Depends On | Communication Pattern |
|---|---|---|
| Calculator UI | Calculation Service (API) | HTTPS REST (POST /calculate) |
| Calculator UI | CloudFront / S3 | Static asset delivery |
| Calculation Service | None | Standalone compute |
| API Gateway | Calculation Service (Lambda) | Lambda proxy integration |
| CloudFront | S3 Bucket | Origin Access Control (OAC) |

## Data Flow

```
+-------------------+     HTTPS POST      +-------------------+     Lambda Proxy    +-------------------+
|                   |    /calculate        |                   |    Integration      |                   |
|   Calculator UI   +-------------------->+   API Gateway     +-------------------->+   Lambda          |
|   (Browser)       |                     |   (REST API)      |                     |   (Python)        |
|                   +<--------------------+                   +<--------------------+                   |
|                   |     JSON Response   |                   |     JSON Response   |                   |
+-------------------+                     +-------------------+                     +-------------------+

Static Assets Flow:
+-------------------+     HTTPS GET       +-------------------+     OAC             +-------------------+
|                   |                     |                   |                     |                   |
|   Browser         +-------------------->+   CloudFront     +-------------------->+   S3 Bucket       |
|                   |                     |   (CDN)           |                     |   (Static Files)  |
|                   +<--------------------+                   +<--------------------+                   |
|                   |     HTML/CSS/JS     |                   |     HTML/CSS/JS     |                   |
+-------------------+                     +-------------------+                     +-------------------+
```

## Dependency Notes

- Calculator UI has a runtime dependency on the Calculation Service API endpoint URL
- The API URL will be injected into the frontend JS at build/deploy time (or configured as a constant)
- No circular dependencies exist
- Lambda has no external dependencies (pure computation, no database or external service calls)
