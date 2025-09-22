# Usage Examples & Integration Guides

This document provides practical examples and integration guides for implementing the AI Customer Service Platform.

## Quick Start Examples

### 1. Basic HTML Integration

The simplest way to add the chatbot to your website:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Company Website</title>
</head>
<body>
    <h1>Welcome to Your Company</h1>
    <p>Your website content goes here...</p>
    
    <!-- Add the chatbot widget -->
    <script src="https://widget.aichatbot-kielce.com/embed.js" 
            data-org-id="your-organization-id" 
            data-theme="custom"
            data-position="bottom-right"
            data-size="medium">
    </script>
</body>
</html>
```

### 2. React Integration

For React applications:

```bash
npm install @aichatbot-kielce/react-widget
```

```typescript
import React from 'react';
import { ChatbotWidget } from '@aichatbot-kielce/react-widget';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Your Company</h1>
        <p>Welcome to our website</p>
      </header>
      
      <main>
        {/* Your main content */}
      </main>
      
      {/* Chatbot Widget */}
      <ChatbotWidget 
        organizationId="your-organization-id"
        theme="custom"
        position="bottom-right"
        size="medium"
        onMessage={(message) => {
          console.log('New message:', message);
        }}
        onSessionStart={(session) => {
          console.log('Chat session started:', session);
        }}
      />
    </div>
  );
}

export default App;
```

### 3. Vue.js Integration

For Vue.js applications:

```bash
npm install @aichatbot-kielce/vue-widget
```

```vue
<template>
  <div id="app">
    <header>
      <h1>Your Company</h1>
      <p>Welcome to our website</p>
    </header>
    
    <main>
      <!-- Your main content -->
    </main>
    
    <!-- Chatbot Widget -->
    <ChatbotWidget 
      :organization-id="orgId" 
      theme="custom"
      position="bottom-right"
      size="medium"
      @message="handleMessage"
      @session-start="handleSessionStart"
    />
  </div>
</template>

<script>
import { ChatbotWidget } from '@aichatbot-kielce/vue-widget';

export default {
  name: 'App',
  components: {
    ChatbotWidget
  },
  data() {
    return {
      orgId: 'your-organization-id'
    };
  },
  methods: {
    handleMessage(message) {
      console.log('New message:', message);
    },
    handleSessionStart(session) {
      console.log('Chat session started:', session);
    }
  }
};
</script>
```

## Complete Implementation Examples

### 1. E-commerce Website Integration

For an online store in Kielce:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sklep Internetowy - Kielce</title>
    <style>
        .chatbot-custom {
            --primary-color: #e74c3c;
            --secondary-color: #34495e;
            --accent-color: #f39c12;
            --font-family: 'Arial', sans-serif;
        }
    </style>
</head>
<body>
    <header>
        <h1>Sklep Internetowy</h1>
        <nav>
            <a href="/produkty">Produkty</a>
            <a href="/o-nas">O nas</a>
            <a href="/kontakt">Kontakt</a>
        </nav>
    </header>
    
    <main>
        <section class="hero">
            <h2>Witamy w naszym sklepie!</h2>
            <p>Najlepsze produkty w Kielcach</p>
        </section>
        
        <section class="products">
            <!-- Product listings -->
        </section>
    </main>
    
    <footer>
        <p>&copy; 2024 Sklep Internetowy. Wszystkie prawa zastrzeżone.</p>
    </footer>
    
    <!-- Chatbot Widget with Polish customization -->
    <script src="https://widget.aichatbot-kielce.com/embed.js" 
            data-org-id="your-organization-id"
            data-theme="custom"
            data-position="bottom-right"
            data-size="medium"
            data-language="pl"
            data-primary-color="#e74c3c"
            data-secondary-color="#34495e"
            data-accent-color="#f39c12"
            data-greeting-message="Cześć! Jak mogę Ci pomóc z zakupami?"
            data-typing-indicator="true"
            data-analytics="true">
    </script>
</body>
</html>
```

### 2. Professional Services Website

For a law firm or consulting company:

```typescript
import React, { useState, useEffect } from 'react';
import { ChatbotWidget } from '@aichatbot-kielce/react-widget';

interface ChatbotConfig {
  organizationId: string;
  theme: string;
  position: string;
  size: string;
  language: string;
  customColors: {
    primary: string;
    secondary: string;
    accent: string;
  };
}

function ProfessionalWebsite() {
  const [chatbotConfig, setChatbotConfig] = useState<ChatbotConfig>({
    organizationId: 'your-organization-id',
    theme: 'custom',
    position: 'bottom-right',
    size: 'medium',
    language: 'pl',
    customColors: {
      primary: '#2c3e50',
      secondary: '#7f8c8d',
      accent: '#3498db'
    }
  });

  const handleChatbotMessage = (message: any) => {
    // Track chatbot interactions for analytics
    console.log('Chatbot message:', message);
    
    // You can integrate with your analytics system
    if (window.gtag) {
      window.gtag('event', 'chatbot_message', {
        event_category: 'engagement',
        event_label: message.type
      });
    }
  };

  const handleSessionStart = (session: any) => {
    console.log('Chat session started:', session);
    
    // Track session start
    if (window.gtag) {
      window.gtag('event', 'chatbot_session_start', {
        event_category: 'engagement'
      });
    }
  };

  return (
    <div className="professional-website">
      <header className="header">
        <div className="container">
          <h1>Kancelaria Prawna</h1>
          <nav>
            <a href="/uslugi">Usługi</a>
            <a href="/zespol">Zespół</a>
            <a href="/kontakt">Kontakt</a>
          </nav>
        </div>
      </header>
      
      <main className="main">
        <section className="hero">
          <div className="container">
            <h2>Profesjonalne usługi prawne w Kielcach</h2>
            <p>Doświadczony zespół prawników gotowy do pomocy</p>
            <button className="cta-button">Skontaktuj się z nami</button>
          </div>
        </section>
        
        <section className="services">
          <div className="container">
            <h2>Nasze usługi</h2>
            <div className="services-grid">
              <div className="service-card">
                <h3>Prawo cywilne</h3>
                <p>Kompleksowa obsługa spraw cywilnych</p>
              </div>
              <div className="service-card">
                <h3>Prawo rodzinne</h3>
                <p>Rozwiązywanie spraw rodzinnych</p>
              </div>
              <div className="service-card">
                <h3>Prawo pracy</h3>
                <p>Ochrona praw pracowniczych</p>
              </div>
            </div>
          </div>
        </section>
      </main>
      
      <footer className="footer">
        <div className="container">
          <p>&copy; 2024 Kancelaria Prawna. Wszystkie prawa zastrzeżone.</p>
        </div>
      </footer>
      
      {/* Professional Chatbot Widget */}
      <ChatbotWidget 
        organizationId={chatbotConfig.organizationId}
        theme={chatbotConfig.theme}
        position={chatbotConfig.position}
        size={chatbotConfig.size}
        language={chatbotConfig.language}
        customColors={chatbotConfig.customColors}
        onMessage={handleChatbotMessage}
        onSessionStart={handleSessionStart}
        behavior={{
          greetingMessage: "Dzień dobry! Jestem tutaj, aby odpowiedzieć na Państwa pytania prawne.",
          fallbackMessage: "Przepraszam, nie mogę odpowiedzieć na to pytanie. Proszę skontaktować się z naszym biurem.",
          typingIndicator: true,
          responseDelay: 1500
        }}
      />
    </div>
  );
}

export default ProfessionalWebsite;
```

### 3. Healthcare Website Integration

For a medical practice or clinic:

```vue
<template>
  <div id="healthcare-website">
    <header class="header">
      <div class="container">
        <h1>Przychodnia Medyczna</h1>
        <nav>
          <a href="/uslugi">Usługi medyczne</a>
          <a href="/lekarze">Lekarze</a>
          <a href="/kontakt">Kontakt</a>
          <a href="/rejestracja">Rejestracja online</a>
        </nav>
      </div>
    </header>
    
    <main class="main">
      <section class="hero">
        <div class="container">
          <h2>Opieka medyczna na najwyższym poziomie</h2>
          <p>Zespół doświadczonych lekarzy w Kielcach</p>
          <button class="cta-button" @click="openRegistration">
            Umów wizytę
          </button>
        </div>
      </section>
      
      <section class="services">
        <div class="container">
          <h2>Nasze usługi</h2>
          <div class="services-grid">
            <div class="service-card" v-for="service in services" :key="service.id">
              <h3>{{ service.name }}</h3>
              <p>{{ service.description }}</p>
            </div>
          </div>
        </div>
      </section>
      
      <section class="emergency">
        <div class="container">
          <h2>Pilne przypadki</h2>
          <p>W przypadku pilnych problemów zdrowotnych, proszę skontaktować się z nami natychmiast.</p>
          <div class="emergency-contacts">
            <a href="tel:+48123456789" class="emergency-phone">
              📞 +48 123 456 789
            </a>
          </div>
        </div>
      </section>
    </main>
    
    <footer class="footer">
      <div class="container">
        <p>&copy; 2024 Przychodnia Medyczna. Wszystkie prawa zastrzeżone.</p>
      </div>
    </footer>
    
    <!-- Healthcare Chatbot Widget -->
    <ChatbotWidget 
      :organization-id="orgId"
      theme="custom"
      position="bottom-right"
      size="medium"
      language="pl"
      :custom-colors="healthcareColors"
      :behavior="healthcareBehavior"
      @message="handleMessage"
      @session-start="handleSessionStart"
    />
  </div>
</template>

<script>
import { ChatbotWidget } from '@aichatbot-kielce/vue-widget';

export default {
  name: 'HealthcareWebsite',
  components: {
    ChatbotWidget
  },
  data() {
    return {
      orgId: 'your-organization-id',
      services: [
        {
          id: 1,
          name: 'Medycyna rodzinna',
          description: 'Kompleksowa opieka medyczna dla całej rodziny'
        },
        {
          id: 2,
          name: 'Pediatria',
          description: 'Specjalistyczna opieka nad dziećmi'
        },
        {
          id: 3,
          name: 'Kardiologia',
          description: 'Diagnostyka i leczenie chorób serca'
        }
      ],
      healthcareColors: {
        primary: '#27ae60',
        secondary: '#2c3e50',
        accent: '#3498db'
      },
      healthcareBehavior: {
        greetingMessage: 'Dzień dobry! Jestem tutaj, aby pomóc Państwu z pytaniami dotyczącymi naszych usług medycznych.',
        fallbackMessage: 'Przepraszam, nie mogę odpowiedzieć na to pytanie medyczne. Proszę skontaktować się z naszym biurem lub w przypadku pilnych problemów zadzwonić pod numer +48 123 456 789.',
        typingIndicator: true,
        responseDelay: 2000,
        enableEmergencyContact: true
      }
    };
  },
  methods: {
    openRegistration() {
      // Open registration modal or redirect
      console.log('Opening registration...');
    },
    handleMessage(message) {
      console.log('Healthcare chatbot message:', message);
      
      // Track healthcare-specific interactions
      if (message.intent === 'emergency') {
        this.showEmergencyAlert();
      }
    },
    handleSessionStart(session) {
      console.log('Healthcare chat session started:', session);
    },
    showEmergencyAlert() {
      alert('W przypadku pilnych problemów zdrowotnych, proszę zadzwonić pod numer +48 123 456 789');
    }
  }
};
</script>

<style scoped>
.healthcare-website {
  font-family: 'Arial', sans-serif;
}

.header {
  background-color: #27ae60;
  color: white;
  padding: 1rem 0;
}

.hero {
  background: linear-gradient(135deg, #27ae60, #2ecc71);
  color: white;
  padding: 4rem 0;
  text-align: center;
}

.emergency {
  background-color: #e74c3c;
  color: white;
  padding: 2rem 0;
  text-align: center;
}

.emergency-phone {
  display: inline-block;
  background-color: white;
  color: #e74c3c;
  padding: 1rem 2rem;
  border-radius: 5px;
  text-decoration: none;
  font-weight: bold;
  margin-top: 1rem;
}

.emergency-phone:hover {
  background-color: #f8f9fa;
}
</style>
```

## Advanced Integration Examples

### 1. Custom Chatbot with Analytics

```typescript
import React, { useState, useEffect } from 'react';
import { ChatbotWidget } from '@aichatbot-kielce/react-widget';

interface AnalyticsEvent {
  event: string;
  category: string;
  label?: string;
  value?: number;
}

function AdvancedChatbotIntegration() {
  const [chatbotConfig, setChatbotConfig] = useState({
    organizationId: 'your-organization-id',
    theme: 'custom',
    position: 'bottom-right',
    size: 'medium',
    language: 'pl'
  });

  const [analytics, setAnalytics] = useState({
    totalMessages: 0,
    totalSessions: 0,
    averageSessionDuration: 0
  });

  // Track analytics events
  const trackEvent = (event: AnalyticsEvent) => {
    // Google Analytics
    if (window.gtag) {
      window.gtag('event', event.event, {
        event_category: event.category,
        event_label: event.label,
        value: event.value
      });
    }

    // Custom analytics
    console.log('Analytics event:', event);
  };

  // Handle chatbot messages
  const handleMessage = (message: any) => {
    setAnalytics(prev => ({
      ...prev,
      totalMessages: prev.totalMessages + 1
    }));

    trackEvent({
      event: 'chatbot_message',
      category: 'engagement',
      label: message.type
    });

    // Handle specific message types
    if (message.intent === 'pricing') {
      trackEvent({
        event: 'pricing_inquiry',
        category: 'conversion',
        label: 'chatbot'
      });
    }
  };

  // Handle session start
  const handleSessionStart = (session: any) => {
    setAnalytics(prev => ({
      ...prev,
      totalSessions: prev.totalSessions + 1
    }));

    trackEvent({
      event: 'chatbot_session_start',
      category: 'engagement'
    });
  };

  // Handle session end
  const handleSessionEnd = (session: any) => {
    const duration = session.duration || 0;
    
    setAnalytics(prev => ({
      ...prev,
      averageSessionDuration: (prev.averageSessionDuration + duration) / 2
    }));

    trackEvent({
      event: 'chatbot_session_end',
      category: 'engagement',
      value: duration
    });
  };

  return (
    <div className="advanced-integration">
      <header>
        <h1>Advanced Chatbot Integration</h1>
        <div className="analytics-summary">
          <div className="metric">
            <span className="label">Total Messages:</span>
            <span className="value">{analytics.totalMessages}</span>
          </div>
          <div className="metric">
            <span className="label">Total Sessions:</span>
            <span className="value">{analytics.totalSessions}</span>
          </div>
          <div className="metric">
            <span className="label">Avg Duration:</span>
            <span className="value">{Math.round(analytics.averageSessionDuration)}s</span>
          </div>
        </div>
      </header>
      
      <main>
        {/* Your main content */}
      </main>
      
      <ChatbotWidget 
        organizationId={chatbotConfig.organizationId}
        theme={chatbotConfig.theme}
        position={chatbotConfig.position}
        size={chatbotConfig.size}
        language={chatbotConfig.language}
        onMessage={handleMessage}
        onSessionStart={handleSessionStart}
        onSessionEnd={handleSessionEnd}
        analytics={{
          enabled: true,
          trackEvents: true,
          customEvents: ['pricing_inquiry', 'contact_request', 'service_inquiry']
        }}
      />
    </div>
  );
}

export default AdvancedChatbotIntegration;
```

### 2. Multi-language Support

```typescript
import React, { useState, useEffect } from 'react';
import { ChatbotWidget } from '@aichatbot-kielce/react-widget';

function MultiLanguageWebsite() {
  const [language, setLanguage] = useState('pl');
  const [chatbotConfig, setChatbotConfig] = useState({
    organizationId: 'your-organization-id',
    theme: 'custom',
    position: 'bottom-right',
    size: 'medium'
  });

  const languageConfigs = {
    pl: {
      language: 'pl',
      greetingMessage: 'Cześć! Jak mogę Ci pomóc?',
      fallbackMessage: 'Przepraszam, nie mogę odpowiedzieć na to pytanie. Proszę skontaktować się z nami.',
      primaryColor: '#e74c3c',
      secondaryColor: '#2c3e50',
      accentColor: '#f39c12'
    },
    en: {
      language: 'en',
      greetingMessage: 'Hello! How can I help you?',
      fallbackMessage: 'Sorry, I cannot answer that question. Please contact us.',
      primaryColor: '#3498db',
      secondaryColor: '#2c3e50',
      accentColor: '#e74c3c'
    },
    de: {
      language: 'de',
      greetingMessage: 'Hallo! Wie kann ich Ihnen helfen?',
      fallbackMessage: 'Entschuldigung, ich kann diese Frage nicht beantworten. Bitte kontaktieren Sie uns.',
      primaryColor: '#27ae60',
      secondaryColor: '#2c3e50',
      accentColor: '#f39c12'
    }
  };

  const currentConfig = languageConfigs[language];

  const handleLanguageChange = (newLanguage: string) => {
    setLanguage(newLanguage);
    setChatbotConfig(prev => ({
      ...prev,
      language: newLanguage
    }));
  };

  return (
    <div className="multi-language-website">
      <header>
        <h1>Multi-language Website</h1>
        <div className="language-selector">
          <button 
            className={language === 'pl' ? 'active' : ''}
            onClick={() => handleLanguageChange('pl')}
          >
            Polski
          </button>
          <button 
            className={language === 'en' ? 'active' : ''}
            onClick={() => handleLanguageChange('en')}
          >
            English
          </button>
          <button 
            className={language === 'de' ? 'active' : ''}
            onClick={() => handleLanguageChange('de')}
          >
            Deutsch
          </button>
        </div>
      </header>
      
      <main>
        {/* Your main content */}
      </main>
      
      <ChatbotWidget 
        organizationId={chatbotConfig.organizationId}
        theme={chatbotConfig.theme}
        position={chatbotConfig.position}
        size={chatbotConfig.size}
        language={currentConfig.language}
        customColors={{
          primary: currentConfig.primaryColor,
          secondary: currentConfig.secondaryColor,
          accent: currentConfig.accentColor
        }}
        behavior={{
          greetingMessage: currentConfig.greetingMessage,
          fallbackMessage: currentConfig.fallbackMessage,
          typingIndicator: true,
          responseDelay: 1000
        }}
      />
    </div>
  );
}

export default MultiLanguageWebsite;
```

## Testing and Debugging

### 1. Development Testing

```typescript
import React from 'react';
import { ChatbotWidget } from '@aichatbot-kielce/react-widget';

function DevelopmentTesting() {
  const [testMode, setTestMode] = useState(false);
  const [testMessages, setTestMessages] = useState([]);

  const handleTestMessage = (message: any) => {
    if (testMode) {
      setTestMessages(prev => [...prev, message]);
      console.log('Test message received:', message);
    }
  };

  const runTests = () => {
    // Test chatbot functionality
    const tests = [
      {
        name: 'Greeting Test',
        message: 'Hello',
        expectedIntent: 'greeting'
      },
      {
        name: 'Pricing Test',
        message: 'What are your prices?',
        expectedIntent: 'pricing_inquiry'
      },
      {
        name: 'Contact Test',
        message: 'How can I contact you?',
        expectedIntent: 'contact_inquiry'
      }
    ];

    tests.forEach(test => {
      console.log(`Running test: ${test.name}`);
      // Send test message to chatbot
      // Verify response
    });
  };

  return (
    <div className="development-testing">
      <header>
        <h1>Development Testing</h1>
        <div className="test-controls">
          <button onClick={() => setTestMode(!testMode)}>
            {testMode ? 'Disable' : 'Enable'} Test Mode
          </button>
          <button onClick={runTests}>Run Tests</button>
        </div>
      </header>
      
      {testMode && (
        <div className="test-results">
          <h3>Test Messages:</h3>
          <ul>
            {testMessages.map((msg, index) => (
              <li key={index}>
                <strong>{msg.type}:</strong> {msg.content}
              </li>
            ))}
          </ul>
        </div>
      )}
      
      <ChatbotWidget 
        organizationId="your-organization-id"
        theme="custom"
        position="bottom-right"
        size="medium"
        debug={testMode}
        onMessage={handleTestMessage}
      />
    </div>
  );
}

export default DevelopmentTesting;
```

### 2. Performance Monitoring

```typescript
import React, { useState, useEffect } from 'react';
import { ChatbotWidget } from '@aichatbot-kielce/react-widget';

function PerformanceMonitoring() {
  const [performance, setPerformance] = useState({
    responseTime: 0,
    messageCount: 0,
    errorCount: 0,
    uptime: 0
  });

  const [startTime] = useState(Date.now());

  useEffect(() => {
    const interval = setInterval(() => {
      setPerformance(prev => ({
        ...prev,
        uptime: Date.now() - startTime
      }));
    }, 1000);

    return () => clearInterval(interval);
  }, [startTime]);

  const handleMessage = (message: any) => {
    const responseTime = message.responseTime || 0;
    
    setPerformance(prev => ({
      ...prev,
      responseTime: (prev.responseTime + responseTime) / 2,
      messageCount: prev.messageCount + 1
    }));
  };

  const handleError = (error: any) => {
    setPerformance(prev => ({
      ...prev,
      errorCount: prev.errorCount + 1
    }));
    
    console.error('Chatbot error:', error);
  };

  return (
    <div className="performance-monitoring">
      <header>
        <h1>Performance Monitoring</h1>
        <div className="performance-metrics">
          <div className="metric">
            <span className="label">Response Time:</span>
            <span className="value">{Math.round(performance.responseTime)}ms</span>
          </div>
          <div className="metric">
            <span className="label">Messages:</span>
            <span className="value">{performance.messageCount}</span>
          </div>
          <div className="metric">
            <span className="label">Errors:</span>
            <span className="value">{performance.errorCount}</span>
          </div>
          <div className="metric">
            <span className="label">Uptime:</span>
            <span className="value">{Math.round(performance.uptime / 1000)}s</span>
          </div>
        </div>
      </header>
      
      <main>
        {/* Your main content */}
      </main>
      
      <ChatbotWidget 
        organizationId="your-organization-id"
        theme="custom"
        position="bottom-right"
        size="medium"
        onMessage={handleMessage}
        onError={handleError}
        performance={{
          enabled: true,
          trackResponseTime: true,
          trackErrors: true
        }}
      />
    </div>
  );
}

export default PerformanceMonitoring;
```

## Best Practices

### 1. Security Considerations

```typescript
// Implement proper security measures
const secureChatbotConfig = {
  organizationId: process.env.REACT_APP_ORGANIZATION_ID,
  allowedDomains: ['yourdomain.com', 'www.yourdomain.com'],
  enableCSP: true,
  enableSRI: true,
  rateLimit: {
    enabled: true,
    maxRequests: 100,
    windowMs: 900000 // 15 minutes
  }
};
```

### 2. Accessibility

```typescript
// Ensure chatbot is accessible
const accessibleChatbotConfig = {
  organizationId: 'your-organization-id',
  theme: 'custom',
  position: 'bottom-right',
  size: 'medium',
  accessibility: {
    enableKeyboardNavigation: true,
    enableScreenReader: true,
    highContrast: false,
    fontSize: 'medium'
  }
};
```

### 3. Performance Optimization

```typescript
// Optimize chatbot performance
const optimizedChatbotConfig = {
  organizationId: 'your-organization-id',
  theme: 'custom',
  position: 'bottom-right',
  size: 'medium',
  performance: {
    lazyLoad: true,
    preload: false,
    cache: true,
    compression: true
  }
};
```

This comprehensive guide provides practical examples for implementing the AI Customer Service Platform in various scenarios. Choose the approach that best fits your needs and customize it according to your requirements.