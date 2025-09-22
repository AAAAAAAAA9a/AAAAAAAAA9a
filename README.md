# AI Customer Service Platform - Kielce

A comprehensive AI-powered customer service platform designed for companies in Kielce, Poland. This platform provides intelligent chatbots, company research capabilities, and customizable customer service solutions.

## 🚀 Project Overview

This platform consists of several key components:

1. **Marketing Landing Page** - Simple demo page with authentication
2. **User Dashboard** - Main panel with organization management and AI chat
3. **MasterAI** - Research and knowledge management system
4. **Customer Service Chatbot** - Customizable AI for customer support
5. **Widget Integration** - Easy embedding for company websites
6. **Analytics & Logging** - Comprehensive data tracking

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Marketing     │    │   User          │    │   Customer      │
│   Landing Page  │───▶│   Dashboard     │───▶│   Service       │
│                 │    │                 │    │   Chatbot       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Authentication│    │   MasterAI      │    │   Widget        │
│   System        │    │   Research      │    │   Integration   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 ▼
                    ┌─────────────────┐
                    │   Supabase      │
                    │   Database      │
                    │   + Vector DB   │
                    └─────────────────┘
```

## 📚 Documentation Structure

- [API Documentation](./docs/api/README.md) - Complete API reference
- [Authentication](./docs/auth/README.md) - User management and security
- [Organization Management](./docs/organization/README.md) - Company setup and configuration
- [MasterAI System](./docs/masterai/README.md) - Research and knowledge management
- [Chatbot Customization](./docs/chatbot/README.md) - Customer service AI configuration
- [Widget Integration](./docs/widget/README.md) - Website embedding guide
- [Analytics](./docs/analytics/README.md) - Data tracking and insights
- [Deployment Guide](./docs/deployment/README.md) - Production setup

## 🛠️ Technology Stack

- **Frontend**: React/Next.js with TypeScript
- **Backend**: Node.js/Express or Python/FastAPI
- **Database**: Supabase (PostgreSQL + Vector Database)
- **AI Framework**: LangChain or similar
- **Authentication**: Supabase Auth
- **File Storage**: Supabase Storage
- **Deployment**: Vercel/Netlify (Frontend), Railway/Heroku (Backend)

## 🚀 Quick Start

1. Clone the repository
2. Install dependencies: `npm install`
3. Set up environment variables
4. Run development server: `npm run dev`
5. Access the application at `http://localhost:3000`

## 📖 Getting Started

For detailed setup instructions and API usage, please refer to the specific documentation sections above.

## 🤝 Contributing

This project is in the planning stage. Please refer to the documentation for understanding the architecture and planned features.

## 📄 License

[License information to be added]