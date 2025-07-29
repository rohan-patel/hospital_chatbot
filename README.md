# 🏥 Role-Based AI Chatbot for HMIS

A secure, role-aware AI chatbot integrated directly into a hospital's HMIS system. Developed by **Xcelcode Innovations**, this chatbot enables staff to access real-time information using natural language — no need to navigate complex menus or run manual reports.

---

## ✨ Key Features

- 🔒 **Role-Based Access Control (RBAC)**  
  Each user's permissions are dynamically enforced. If a user asks something outside their access level, the bot responds clearly:
  > “You don’t have access to this module.”

- 💬 **Natural Language Interface**  
  Staff can ask questions like:
  > “How many patients have appointments today?”

  And receive:
  - Friendly, human-readable text answers
  - Tabular responses
  - CSV downloads for large datasets (10+ records)
  - PDF export for structured results (coming soon)

- 🔁 **Session Context**  
  Supports follow-up questions within the same session, enabling smoother, more natural conversations.

- 🧠 **AI-Powered by Azure OpenAI**  
  Leverages GPT models to understand and respond to everyday hospital queries.

- 📦 **HMIS Modules Supported**
  - User & Role Management
  - Patient Registration
  - Doctor/Nurse OPD Queues
  - Vital Collection
  - Prescription Management
  - Pharmacy
  - Payments

- 🕵️ **Audit Logging**  
  All interactions are logged with timestamps and user IDs for full traceability.

- ⚡ **Fast, Real-Time Access**  
  Response times are targeted to be under 5 seconds.  
  > Note: Caching is **disabled** to ensure all data is live and accurate.

- 🛡️ **Read-Only Operation**  
  The chatbot never modifies any data — it only reads and formats based on access rights.

---

## 🧩 Architecture

- 🧠 AI Engine: Azure OpenAI (GPT)
- ⚙️ Backend: Python FastAPI
- 🗃️ Database: MongoDB
- 🔐 Auth: OAuth2 with role enforcement
- 📡 API: Exposed via REST microservice
- 🧩 Integration: Compatible with MERN-stack HMIS

---

## 🔭 Future Enhancements

- 🎙️ Voice input/output
- 💡 Suggested follow-up prompts
- 📝 PDF download support for all responses
- 🌐 Multi-language support

---

## 🧑‍💼 Why This Matters

This chatbot is designed to be:
- **Simple** for non-technical staff
- **Fast** for operational agility
- **Secure** for handling sensitive medical data

By reducing clicks and complexity, it helps hospital staff focus on care instead of navigating software.

---
