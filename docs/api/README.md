# API Documentation

This document provides comprehensive documentation for all public APIs in the AI Customer Service Platform.

## Base URL

```
Production: https://api.aichatbot-kielce.com
Development: http://localhost:3001/api
```

## Authentication

All API endpoints require authentication using JWT tokens obtained from Supabase Auth. Include the token in the Authorization header:

```
Authorization: Bearer <your-jwt-token>
```

## Response Format

All API responses follow a consistent format:

```json
{
  "success": true,
  "data": {},
  "message": "Operation completed successfully",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

Error responses:

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {}
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

## API Endpoints Overview

### Authentication & User Management
- [POST /auth/register](#post-authregister)
- [POST /auth/login](#post-authlogin)
- [POST /auth/logout](#post-authlogout)
- [GET /auth/me](#get-authme)
- [PUT /auth/profile](#put-authprofile)

### Organization Management
- [POST /organizations](#post-organizations)
- [GET /organizations](#get-organizations)
- [GET /organizations/:id](#get-organizationsid)
- [PUT /organizations/:id](#put-organizationsid)
- [DELETE /organizations/:id](#delete-organizationsid)
- [POST /organizations/:id/upload](#post-organizationsidupload)

### MasterAI Research
- [POST /masterai/research](#post-masterairesearch)
- [GET /masterai/reports](#get-masteraireports)
- [GET /masterai/reports/:id](#get-masteraireportsid)
- [POST /masterai/chat](#post-masteraichat)

### Customer Service Chatbot
- [GET /chatbot/config](#get-chatbotconfig)
- [PUT /chatbot/config](#put-chatbotconfig)
- [POST /chatbot/customize](#post-chatbotcustomize)
- [GET /chatbot/widget-code](#get-chatbotwidget-code)

### Chat & Analytics
- [POST /chat/send](#post-chatsend)
- [GET /chat/history](#get-chathistory)
- [GET /analytics/dashboard](#get-analyticsdashboard)
- [GET /analytics/chat-stats](#get-analyticschat-stats)

### Widget Integration
- [GET /widget/:organizationId](#get-widgetorganizationid)
- [POST /widget/chat](#post-widgetchat)

## Rate Limiting

API requests are rate-limited to prevent abuse:

- **Authentication endpoints**: 5 requests per minute
- **General API endpoints**: 100 requests per minute
- **Chat endpoints**: 30 requests per minute
- **File upload endpoints**: 10 requests per minute

Rate limit headers are included in responses:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1642248000
```

## Error Codes

| Code | Description |
|------|-------------|
| `VALIDATION_ERROR` | Invalid input data |
| `AUTHENTICATION_ERROR` | Invalid or missing authentication |
| `AUTHORIZATION_ERROR` | Insufficient permissions |
| `NOT_FOUND` | Resource not found |
| `RATE_LIMIT_EXCEEDED` | Too many requests |
| `INTERNAL_ERROR` | Server error |
| `AI_SERVICE_ERROR` | AI service unavailable |
| `FILE_UPLOAD_ERROR` | File upload failed |

## SDKs and Libraries

### JavaScript/TypeScript
```bash
npm install @aichatbot-kielce/sdk
```

### Python
```bash
pip install aichatbot-kielce
```

### React Hook
```bash
npm install @aichatbot-kielce/react-hooks
```

## Webhooks

The platform supports webhooks for real-time notifications:

- `organization.created` - New organization created
- `research.completed` - MasterAI research finished
- `chatbot.updated` - Chatbot configuration changed
- `chat.message` - New chat message received

Webhook payload format:
```json
{
  "event": "organization.created",
  "data": {
    "organizationId": "uuid",
    "userId": "uuid",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

## Testing

Use the provided Postman collection or test with curl:

```bash
# Test authentication
curl -X POST https://api.aichatbot-kielce.com/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "password"}'
```

## Support

For API support and questions:
- Email: api-support@aichatbot-kielce.com
- Documentation: https://docs.aichatbot-kielce.com
- Status Page: https://status.aichatbot-kielce.com