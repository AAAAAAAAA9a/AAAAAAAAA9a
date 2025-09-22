# API Endpoints Reference

This document provides a complete reference for all API endpoints in the AI Customer Service Platform.

## Authentication Endpoints

### POST /auth/register
Register a new user account.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "firstName": "John",
  "lastName": "Doe",
  "company": "Example Corp"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "user": {
      "id": "uuid",
      "email": "user@example.com",
      "firstName": "John",
      "lastName": "Doe",
      "company": "Example Corp",
      "createdAt": "2024-01-15T10:30:00Z"
    },
    "session": {
      "accessToken": "jwt-token",
      "refreshToken": "refresh-token",
      "expiresAt": "2024-01-15T11:30:00Z"
    }
  }
}
```

### POST /auth/login
Authenticate an existing user.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "user": {
      "id": "uuid",
      "email": "user@example.com",
      "firstName": "John",
      "lastName": "Doe",
      "company": "Example Corp"
    },
    "session": {
      "accessToken": "jwt-token",
      "refreshToken": "refresh-token",
      "expiresAt": "2024-01-15T11:30:00Z"
    }
  }
}
```

### POST /auth/logout
Logout the current user.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Response:**
```json
{
  "success": true,
  "message": "Logout successful"
}
```

### GET /auth/me
Get current user information.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Response:**
```json
{
  "success": true,
  "data": {
    "user": {
      "id": "uuid",
      "email": "user@example.com",
      "firstName": "John",
      "lastName": "Doe",
      "company": "Example Corp",
      "createdAt": "2024-01-15T10:30:00Z",
      "lastLogin": "2024-01-15T10:30:00Z",
      "organizations": [
        {
          "id": "org-uuid",
          "name": "Example Corp",
          "role": "owner"
        }
      ]
    }
  }
}
```

### PUT /auth/profile
Update user profile information.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Request:**
```json
{
  "firstName": "John",
  "lastName": "Doe",
  "company": "Updated Corp",
  "phone": "+48123456789"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "user": {
      "id": "uuid",
      "email": "user@example.com",
      "firstName": "John",
      "lastName": "Doe",
      "company": "Updated Corp",
      "phone": "+48123456789",
      "updatedAt": "2024-01-15T10:30:00Z"
    }
  }
}
```

## Organization Endpoints

### POST /organizations
Create a new organization.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Request:**
```json
{
  "name": "Example Company",
  "field": "Technology",
  "website": "https://example.com",
  "description": "A technology company based in Kielce",
  "contactEmail": "contact@example.com",
  "contactPhone": "+48123456789",
  "address": {
    "street": "ul. Sienkiewicza 1",
    "city": "Kielce",
    "postalCode": "25-001",
    "country": "Poland"
  },
  "settings": {
    "timezone": "Europe/Warsaw",
    "language": "pl",
    "currency": "PLN"
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "organization": {
      "id": "org-uuid",
      "name": "Example Company",
      "field": "Technology",
      "website": "https://example.com",
      "description": "A technology company based in Kielce",
      "contactEmail": "contact@example.com",
      "contactPhone": "+48123456789",
      "address": {
        "street": "ul. Sienkiewicza 1",
        "city": "Kielce",
        "postalCode": "25-001",
        "country": "Poland"
      },
      "settings": {
        "timezone": "Europe/Warsaw",
        "language": "pl",
        "currency": "PLN"
      },
      "knowledgeBase": {
        "files": [],
        "customData": null
      },
      "createdAt": "2024-01-15T10:30:00Z",
      "updatedAt": "2024-01-15T10:30:00Z",
      "ownerId": "user-uuid"
    }
  }
}
```

### GET /organizations
Get all organizations for the current user.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Query Parameters:**
- `page` (optional): Page number (default: 1)
- `limit` (optional): Items per page (default: 10)
- `search` (optional): Search by name or field

**Response:**
```json
{
  "success": true,
  "data": {
    "organizations": [
      {
        "id": "org-uuid",
        "name": "Example Company",
        "field": "Technology",
        "website": "https://example.com",
        "description": "A technology company based in Kielce",
        "logo": "https://storage.example.com/logos/org-uuid.png",
        "createdAt": "2024-01-15T10:30:00Z",
        "role": "owner"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 10,
      "total": 1,
      "pages": 1
    }
  }
}
```

### GET /organizations/:id
Get detailed information about a specific organization.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Response:**
```json
{
  "success": true,
  "data": {
    "organization": {
      "id": "org-uuid",
      "name": "Example Company",
      "field": "Technology",
      "website": "https://example.com",
      "description": "A technology company based in Kielce",
      "contactEmail": "contact@example.com",
      "contactPhone": "+48123456789",
      "address": {
        "street": "ul. Sienkiewicza 1",
        "city": "Kielce",
        "postalCode": "25-001",
        "country": "Poland"
      },
      "settings": {
        "timezone": "Europe/Warsaw",
        "language": "pl",
        "currency": "PLN"
      },
      "knowledgeBase": {
        "files": [
          {
            "id": "file-uuid",
            "name": "company-info.json",
            "type": "json",
            "size": 1024,
            "url": "https://storage.example.com/files/file-uuid.json",
            "processed": true,
            "vectorized": true,
            "uploadedAt": "2024-01-15T10:30:00Z"
          }
        ],
        "customData": {
          "faq": [
            {
              "question": "What are your business hours?",
              "answer": "We are open Monday to Friday, 9 AM to 5 PM"
            }
          ]
        }
      },
      "createdAt": "2024-01-15T10:30:00Z",
      "updatedAt": "2024-01-15T10:30:00Z",
      "ownerId": "user-uuid"
    }
  }
}
```

### PUT /organizations/:id
Update organization information.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Request:**
```json
{
  "name": "Updated Company Name",
  "field": "Software Development",
  "website": "https://updated-example.com",
  "description": "Updated description",
  "contactEmail": "new-contact@example.com",
  "settings": {
    "timezone": "Europe/Warsaw",
    "language": "en",
    "currency": "EUR"
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "organization": {
      "id": "org-uuid",
      "name": "Updated Company Name",
      "field": "Software Development",
      "website": "https://updated-example.com",
      "description": "Updated description",
      "contactEmail": "new-contact@example.com",
      "updatedAt": "2024-01-15T11:00:00Z"
    }
  }
}
```

### DELETE /organizations/:id
Delete an organization and all associated data.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Response:**
```json
{
  "success": true,
  "message": "Organization deleted successfully"
}
```

### POST /organizations/:id/upload
Upload knowledge files to organization.

**Headers:**
```
Authorization: Bearer <jwt-token>
Content-Type: multipart/form-data
```

**Request Body (Form Data):**
- `files`: Array of files (JSON, Markdown, PDF, TXT)
- `description` (optional): Description of the files

**Response:**
```json
{
  "success": true,
  "data": {
    "uploadedFiles": [
      {
        "id": "file-uuid",
        "name": "company-info.json",
        "type": "json",
        "size": 1024,
        "url": "https://storage.example.com/files/file-uuid.json",
        "processed": false,
        "vectorized": false,
        "uploadedAt": "2024-01-15T10:30:00Z"
      }
    ],
    "processingStatus": "pending"
  }
}
```

## MasterAI Endpoints

### POST /masterai/research
Initiate deep research for an organization.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Request:**
```json
{
  "organizationId": "org-uuid",
  "researchScope": {
    "includeWebResearch": true,
    "includeSocialMedia": true,
    "includeCompetitorAnalysis": true,
    "includeLocalMarket": true,
    "customKeywords": ["technology", "innovation", "customer service"]
  },
  "priority": "high"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "researchId": "research-uuid",
    "status": "initiated",
    "estimatedCompletion": "2024-01-15T11:00:00Z",
    "stages": [
      {
        "name": "data_collection",
        "status": "pending",
        "estimatedDuration": "5 minutes"
      },
      {
        "name": "analysis",
        "status": "pending",
        "estimatedDuration": "10 minutes"
      },
      {
        "name": "report_generation",
        "status": "pending",
        "estimatedDuration": "3 minutes"
      }
    ]
  }
}
```

### GET /masterai/research/:researchId/status
Get current status of research process.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Response:**
```json
{
  "success": true,
  "data": {
    "researchId": "research-uuid",
    "status": "in_progress",
    "progress": 65,
    "currentStage": "analysis",
    "stages": [
      {
        "name": "data_collection",
        "status": "completed",
        "completedAt": "2024-01-15T10:35:00Z",
        "results": {
          "websitesAnalyzed": 3,
          "socialMediaProfiles": 2,
          "competitorsFound": 5
        }
      },
      {
        "name": "analysis",
        "status": "in_progress",
        "progress": 80,
        "estimatedCompletion": "2024-01-15T10:40:00Z"
      },
      {
        "name": "report_generation",
        "status": "pending"
      }
    ],
    "estimatedCompletion": "2024-01-15T10:45:00Z"
  }
}
```

### GET /masterai/reports
Get all research reports for user's organizations.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Query Parameters:**
- `organizationId` (optional): Filter by organization
- `status` (optional): Filter by status (completed, failed, in_progress)
- `page` (optional): Page number
- `limit` (optional): Items per page

**Response:**
```json
{
  "success": true,
  "data": {
    "reports": [
      {
        "id": "report-uuid",
        "organizationId": "org-uuid",
        "organizationName": "Example Company",
        "status": "completed",
        "createdAt": "2024-01-15T10:30:00Z",
        "completedAt": "2024-01-15T11:00:00Z",
        "summary": {
          "companySize": "small",
          "industry": "technology",
          "marketPosition": "emerging",
          "keyStrengths": ["innovation", "customer focus"],
          "recommendations": 5
        }
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 10,
      "total": 1,
      "pages": 1
    }
  }
}
```

### GET /masterai/reports/:reportId
Get detailed research report.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Response:**
```json
{
  "success": true,
  "data": {
    "report": {
      "id": "report-uuid",
      "organizationId": "org-uuid",
      "status": "completed",
      "createdAt": "2024-01-15T10:30:00Z",
      "completedAt": "2024-01-15T11:00:00Z",
      "executiveSummary": {
        "companyOverview": "Example Company is a technology startup based in Kielce, Poland...",
        "keyFindings": [
          "Strong local market presence",
          "Innovative product portfolio",
          "Growing customer base"
        ],
        "recommendations": [
          "Implement AI-powered customer service",
          "Expand digital marketing efforts",
          "Develop mobile-first solutions"
        ]
      },
      "detailedAnalysis": {
        "companyProfile": {
          "size": "small",
          "industry": "technology",
          "founded": "2020",
          "employees": "10-50",
          "revenue": "€100K-€500K"
        },
        "marketAnalysis": {
          "localMarket": {
            "kielcePresence": "strong",
            "competitors": 3,
            "marketShare": "15%"
          },
          "industryTrends": [
            "AI adoption increasing",
            "Digital transformation accelerating",
            "Customer experience focus"
          ]
        },
        "digitalPresence": {
          "website": {
            "url": "https://example.com",
            "traffic": "moderate",
            "seoScore": 75,
            "mobileFriendly": true
          },
          "socialMedia": {
            "facebook": "active",
            "linkedin": "active",
            "instagram": "inactive"
          }
        },
        "competitorAnalysis": {
          "directCompetitors": [
            {
              "name": "Competitor A",
              "strengths": ["market share", "brand recognition"],
              "weaknesses": ["customer service", "innovation"]
            }
          ],
          "competitiveAdvantages": [
            "Personalized service",
            "Local expertise",
            "Technology innovation"
          ]
        }
      },
      "knowledgeBase": {
        "extractedFacts": [
          "Company founded in 2020",
          "Specializes in web development",
          "Serves local businesses in Kielce",
          "Offers 24/7 customer support"
        ],
        "faqSuggestions": [
          {
            "question": "What services do you offer?",
            "answer": "We provide web development, mobile apps, and digital marketing services"
          },
          {
            "question": "Do you serve clients outside Kielce?",
            "answer": "Yes, we work with clients throughout Poland and internationally"
          }
        ],
        "chatbotPersonality": {
          "tone": "professional_friendly",
          "expertise": "technology_consulting",
          "localKnowledge": "kielce_focused"
        }
      },
      "recommendations": {
        "customerService": [
          "Implement AI chatbot for 24/7 support",
          "Create comprehensive FAQ section",
          "Develop self-service portal"
        ],
        "businessGrowth": [
          "Expand digital marketing efforts",
          "Develop mobile-first solutions",
          "Partner with local businesses"
        ],
        "technology": [
          "Adopt cloud-based solutions",
          "Implement analytics tracking",
          "Enhance website performance"
        ]
      }
    }
  }
}
```

### POST /masterai/chat
Chat with MasterAI for system customization and business advice.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Request:**
```json
{
  "organizationId": "org-uuid",
  "message": "How can I improve my customer service chatbot?",
  "context": {
    "currentChatbotConfig": {
      "personality": "professional",
      "responseTime": "fast",
      "knowledgeBase": "basic"
    }
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "response": "Based on your company profile and industry analysis, I recommend several improvements for your customer service chatbot:\n\n1. **Enhanced Personality**: Given your local Kielce focus, consider a more approachable, community-oriented personality that reflects Polish business culture.\n\n2. **Expanded Knowledge Base**: Your current knowledge base is basic. I suggest adding:\n   - Detailed service descriptions\n   - Local business hours and contact information\n   - Common technical support scenarios\n   - Pricing and package information\n\n3. **Multi-language Support**: Consider adding Polish language support for local customers.\n\n4. **Integration Opportunities**: Based on your tech focus, integrate with your existing systems for real-time data access.\n\nWould you like me to help you implement any of these suggestions?",
    "suggestions": [
      {
        "type": "personality_update",
        "title": "Update Chatbot Personality",
        "description": "Make the chatbot more community-focused and approachable",
        "priority": "high"
      },
      {
        "type": "knowledge_expansion",
        "title": "Expand Knowledge Base",
        "description": "Add detailed service and support information",
        "priority": "high"
      },
      {
        "type": "language_support",
        "title": "Add Polish Language Support",
        "description": "Enable Polish language for local customers",
        "priority": "medium"
      }
    ],
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

## Chatbot Endpoints

### GET /chatbot/config
Get chatbot configuration for an organization.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Query Parameters:**
- `organizationId` (required): Organization ID

**Response:**
```json
{
  "success": true,
  "data": {
    "config": {
      "id": "chatbot-uuid",
      "organizationId": "org-uuid",
      "name": "Example Company Assistant",
      "description": "AI-powered customer service chatbot",
      "appearance": {
        "primaryColor": "#007bff",
        "secondaryColor": "#6c757d",
        "accentColor": "#28a745",
        "fontFamily": "Inter, sans-serif",
        "borderRadius": 8,
        "position": "bottom-right",
        "size": "medium"
      },
      "personality": {
        "tone": "professional",
        "expertise": "technology consulting",
        "language": "en",
        "responseStyle": "conversational",
        "humor": "light"
      },
      "behavior": {
        "greetingMessage": "Hello! I'm here to help you with any questions about our services.",
        "fallbackMessage": "I'm sorry, I don't have information about that. Let me connect you with a human agent.",
        "typingIndicator": true,
        "responseDelay": 1000,
        "maxResponseLength": 500,
        "enableSuggestions": true,
        "enableFileUpload": false
      },
      "knowledge": {
        "sources": ["company-info", "faq", "policies"],
        "confidenceThreshold": 0.7,
        "enableWebSearch": false,
        "customResponses": [
          {
            "id": "response-uuid",
            "trigger": "pricing",
            "response": "Our pricing varies based on your needs. Let me connect you with our sales team for a personalized quote.",
            "conditions": {
              "intent": "pricing_inquiry"
            }
          }
        ]
      },
      "integration": {
        "websiteUrl": "https://example.com",
        "allowedDomains": ["example.com", "www.example.com"],
        "enableAnalytics": true,
        "enableChatLogging": true
      },
      "status": "active",
      "createdAt": "2024-01-15T10:30:00Z",
      "updatedAt": "2024-01-15T10:30:00Z"
    }
  }
}
```

### PUT /chatbot/config
Update chatbot configuration.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Request:**
```json
{
  "name": "Updated Assistant Name",
  "appearance": {
    "primaryColor": "#ff6b6b",
    "secondaryColor": "#4ecdc4",
    "accentColor": "#45b7d1",
    "fontFamily": "Roboto, sans-serif",
    "borderRadius": 12,
    "position": "bottom-left",
    "size": "large"
  },
  "personality": {
    "tone": "friendly",
    "expertise": "customer service",
    "language": "pl",
    "responseStyle": "detailed",
    "humor": "moderate"
  },
  "behavior": {
    "greetingMessage": "Cześć! Jak mogę Ci pomóc?",
    "fallbackMessage": "Przepraszam, nie mam informacji na ten temat. Połączę Cię z naszym agentem.",
    "typingIndicator": true,
    "responseDelay": 1500,
    "maxResponseLength": 750,
    "enableSuggestions": true,
    "enableFileUpload": true
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "config": {
      "id": "chatbot-uuid",
      "name": "Updated Assistant Name",
      "appearance": {
        "primaryColor": "#ff6b6b",
        "secondaryColor": "#4ecdc4",
        "accentColor": "#45b7d1",
        "fontFamily": "Roboto, sans-serif",
        "borderRadius": 12,
        "position": "bottom-left",
        "size": "large"
      },
      "personality": {
        "tone": "friendly",
        "expertise": "customer service",
        "language": "pl",
        "responseStyle": "detailed",
        "humor": "moderate"
      },
      "behavior": {
        "greetingMessage": "Cześć! Jak mogę Ci pomóc?",
        "fallbackMessage": "Przepraszam, nie mam informacji na ten temat. Połączę Cię z naszym agentem.",
        "typingIndicator": true,
        "responseDelay": 1500,
        "maxResponseLength": 750,
        "enableSuggestions": true,
        "enableFileUpload": true
      },
      "updatedAt": "2024-01-15T11:00:00Z"
    }
  }
}
```

### POST /chatbot/customize
Apply predefined customization templates.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Request:**
```json
{
  "template": "tech_startup",
  "customizations": {
    "companyName": "Example Tech",
    "primaryColor": "#007bff",
    "language": "en"
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "config": {
      "id": "chatbot-uuid",
      "name": "Example Tech Assistant",
      "appearance": {
        "primaryColor": "#007bff",
        "secondaryColor": "#6c757d",
        "accentColor": "#28a745",
        "fontFamily": "Inter, sans-serif",
        "borderRadius": 8,
        "position": "bottom-right",
        "size": "medium"
      },
      "personality": {
        "tone": "professional",
        "expertise": "technology innovation",
        "language": "en",
        "responseStyle": "conversational",
        "humor": "light"
      },
      "behavior": {
        "greetingMessage": "Hi! I'm here to help you explore our innovative technology solutions.",
        "fallbackMessage": "I'm not sure about that. Let me connect you with our technical team.",
        "typingIndicator": true,
        "responseDelay": 1000,
        "maxResponseLength": 500,
        "enableSuggestions": true,
        "enableFileUpload": false
      }
    }
  }
}
```

### GET /chatbot/widget-code
Get widget integration code for website embedding.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Query Parameters:**
- `organizationId` (required): Organization ID
- `format` (optional): Code format (html, react, vue, angular)

**Response:**
```json
{
  "success": true,
  "data": {
    "widgetCode": {
      "html": "<script src=\"https://widget.aichatbot-kielce.com/embed.js\" data-org-id=\"org-uuid\" data-theme=\"custom\"></script>",
      "react": "import { ChatbotWidget } from '@aichatbot-kielce/react-widget';\n\nfunction App() {\n  return (\n    <div>\n      <ChatbotWidget organizationId=\"org-uuid\" theme=\"custom\" />\n    </div>\n  );\n}",
      "vue": "<template>\n  <div>\n    <ChatbotWidget :organization-id=\"orgId\" theme=\"custom\" />\n  </div>\n</template>\n\n<script>\nimport { ChatbotWidget } from '@aichatbot-kielce/vue-widget';\n\nexport default {\n  components: { ChatbotWidget },\n  data() {\n    return {\n      orgId: 'org-uuid'\n    };\n  }\n};\n</script>",
      "angular": "import { Component } from '@angular/core';\nimport { ChatbotWidgetComponent } from '@aichatbot-kielce/angular-widget';\n\n@Component({\n  selector: 'app-root',\n  template: '<chatbot-widget [organizationId]=\"orgId\" theme=\"custom\"></chatbot-widget>',\n  imports: [ChatbotWidgetComponent]\n})\nexport class AppComponent {\n  orgId = 'org-uuid';\n}"
    },
    "customization": {
      "css": ".aichatbot-widget {\n  --primary-color: #007bff;\n  --secondary-color: #6c757d;\n  --accent-color: #28a745;\n  --font-family: 'Inter', sans-serif;\n  --border-radius: 8px;\n}",
      "config": {
        "position": "bottom-right",
        "size": "medium",
        "greetingMessage": "Hello! I'm here to help you with any questions about our services."
      }
    }
  }
}
```