# Organization Management

This document covers the organization management system, including company setup, file uploads, and configuration for the AI Customer Service Platform.

## Overview

Organizations represent companies using the platform. Each organization has its own knowledge base, chatbot configuration, and analytics. Users can create and manage multiple organizations, with proper access control and data isolation.

## Organization Data Model

```typescript
interface Organization {
  id: string;
  name: string;
  field: string; // Business field/industry
  website: string;
  description: string;
  logo?: string;
  contactEmail: string;
  contactPhone?: string;
  address?: {
    street: string;
    city: string;
    postalCode: string;
    country: string;
  };
  settings: {
    timezone: string;
    language: string;
    currency: string;
  };
  knowledgeBase: {
    files: KnowledgeFile[];
    customData: any;
  };
  createdAt: string;
  updatedAt: string;
  ownerId: string;
}

interface KnowledgeFile {
  id: string;
  name: string;
  type: 'json' | 'markdown' | 'pdf' | 'txt';
  size: number;
  url: string;
  processed: boolean;
  vectorized: boolean;
  uploadedAt: string;
}
```

## API Endpoints

### POST /organizations

Create a new organization.

**Headers:**
```
Authorization: Bearer <jwt-token>
Content-Type: application/json
```

**Request Body:**
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
  },
  "message": "Organization created successfully"
}
```

**Error Responses:**
- `400` - Validation error (missing required fields)
- `409` - Organization name already exists
- `500` - Server error

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

**Error Responses:**
- `403` - Access denied (not owner/admin)
- `404` - Organization not found

### PUT /organizations/:id

Update organization information.

**Headers:**
```
Authorization: Bearer <jwt-token>
Content-Type: application/json
```

**Request Body:**
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
  },
  "message": "Organization updated successfully"
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

**Error Responses:**
- `403` - Access denied (not owner)
- `404` - Organization not found
- `409` - Organization has active chatbots (cannot delete)

## File Upload Management

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
  },
  "message": "Files uploaded successfully. Processing will begin shortly."
}
```

### GET /organizations/:id/files

Get all knowledge files for an organization.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Response:**
```json
{
  "success": true,
  "data": {
    "files": [
      {
        "id": "file-uuid",
        "name": "company-info.json",
        "type": "json",
        "size": 1024,
        "url": "https://storage.example.com/files/file-uuid.json",
        "processed": true,
        "vectorized": true,
        "uploadedAt": "2024-01-15T10:30:00Z",
        "processingStatus": "completed"
      }
    ]
  }
}
```

### DELETE /organizations/:id/files/:fileId

Delete a knowledge file.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Response:**
```json
{
  "success": true,
  "message": "File deleted successfully"
}
```

## Knowledge Base Management

### POST /organizations/:id/knowledge

Add custom knowledge data (FAQ, policies, etc.).

**Headers:**
```
Authorization: Bearer <jwt-token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "type": "faq",
  "data": [
    {
      "question": "What are your business hours?",
      "answer": "We are open Monday to Friday, 9 AM to 5 PM"
    },
    {
      "question": "How can I contact support?",
      "answer": "You can reach us at support@example.com or call +48123456789"
    }
  ]
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "knowledgeId": "knowledge-uuid",
    "type": "faq",
    "itemsCount": 2,
    "createdAt": "2024-01-15T10:30:00Z"
  },
  "message": "Knowledge data added successfully"
}
```

### GET /organizations/:id/knowledge

Get all custom knowledge data.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Response:**
```json
{
  "success": true,
  "data": {
    "knowledge": [
      {
        "id": "knowledge-uuid",
        "type": "faq",
        "data": [
          {
            "question": "What are your business hours?",
            "answer": "We are open Monday to Friday, 9 AM to 5 PM"
          }
        ],
        "createdAt": "2024-01-15T10:30:00Z"
      }
    ]
  }
}
```

## File Processing Status

### GET /organizations/:id/processing-status

Get processing status of uploaded files.

**Headers:**
```
Authorization: Bearer <jwt-token>
```

**Response:**
```json
{
  "success": true,
  "data": {
    "files": [
      {
        "id": "file-uuid",
        "name": "company-info.json",
        "status": "processing",
        "progress": 75,
        "stage": "vectorization",
        "estimatedCompletion": "2024-01-15T10:35:00Z"
      }
    ]
  }
}
```

## Usage Examples

### JavaScript/TypeScript

```typescript
import { OrganizationClient } from '@aichatbot-kielce/sdk';

const orgClient = new OrganizationClient({
  baseUrl: 'https://api.aichatbot-kielce.com',
  token: 'jwt-token'
});

// Create organization
const organization = await orgClient.create({
  name: 'Example Company',
  field: 'Technology',
  website: 'https://example.com',
  description: 'A technology company based in Kielce',
  contactEmail: 'contact@example.com'
});

// Upload files
const formData = new FormData();
formData.append('files', file1);
formData.append('files', file2);

const uploadResult = await orgClient.uploadFiles(organization.id, formData);

// Add custom knowledge
await orgClient.addKnowledge(organization.id, {
  type: 'faq',
  data: [
    {
      question: 'What are your business hours?',
      answer: 'We are open Monday to Friday, 9 AM to 5 PM'
    }
  ]
});
```

### React Hook

```typescript
import { useOrganization } from '@aichatbot-kielce/react-hooks';

function OrganizationForm() {
  const { createOrganization, loading, error } = useOrganization();

  const handleSubmit = async (formData) => {
    try {
      const org = await createOrganization(formData);
      console.log('Organization created:', org);
    } catch (err) {
      console.error('Failed to create organization:', err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Organization form fields */}
    </form>
  );
}
```

## File Upload Guidelines

### Supported File Types

- **JSON**: Company data, product catalogs, structured information
- **Markdown**: Documentation, policies, procedures
- **PDF**: Reports, manuals, brochures
- **TXT**: Plain text documents, FAQs

### File Size Limits

- Maximum file size: 10MB
- Maximum total files per organization: 50
- Maximum total storage per organization: 100MB

### File Processing

1. **Upload**: Files are uploaded to secure storage
2. **Validation**: File format and content validation
3. **Extraction**: Text extraction from files
4. **Chunking**: Content is split into manageable chunks
5. **Vectorization**: Text is converted to embeddings
6. **Indexing**: Vectors are stored in Supabase vector database

### Best Practices

1. **File Organization**: Use descriptive filenames
2. **Content Quality**: Ensure files contain relevant, accurate information
3. **Regular Updates**: Keep knowledge base current
4. **File Formats**: Prefer structured formats (JSON) for better processing
5. **Size Optimization**: Keep files focused and concise

## Error Handling

Common error scenarios:

```json
{
  "success": false,
  "error": {
    "code": "FILE_UPLOAD_ERROR",
    "message": "File upload failed",
    "details": {
      "reason": "file_too_large",
      "maxSize": "10MB"
    }
  }
}
```

Error codes:
- `FILE_TOO_LARGE` - File exceeds size limit
- `UNSUPPORTED_FORMAT` - File type not supported
- `PROCESSING_FAILED` - File processing error
- `STORAGE_QUOTA_EXCEEDED` - Organization storage limit reached
- `INVALID_FILE_CONTENT` - File content cannot be processed