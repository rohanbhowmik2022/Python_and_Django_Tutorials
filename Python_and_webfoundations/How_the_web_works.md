🖥️ Client
A client is the application that requests data
Examples:
Web browser (Chrome, Firefox)
Mobile app
API client (Postman, curl)

🖧 Server
A server is a machine or service that:
Stores data
Processes requests
Sends responses

🔄 Basic Flow
### Client sends a request > Server processes it > Server sends back a response
👉 This model allows multiple clients to communicate with one server efficiently.

2️⃣ HTTP & HTTPS
📡 HTTP (HyperText Transfer Protocol)
>>> Application-layer protocol
>>> Used for communication between client and server
>>> Stateless by design
Example:
GET /index.html HTTP/1.1
Host: example.com

🔐 HTTPS (HTTP Secure)
HTTP + SSL/TLS encryption
Encrypts:
URL path, Headers, Body (data)

HTTP uses port 80 by default and HTTPS uses 443 by default

📌 HTTPS protects against: Man-in-the-middle attacks, Data theft, Credential leaks



3️⃣ Request–Response Lifecycle

### Step-by-step lifecycle
--------------------------------
1️⃣ URL entered
https://api.example.com/users

2️⃣ DNS Resolution
Domain → IP address

3️⃣ TCP + TLS handshake
Secure connection established (for HTTPS)

4️⃣ HTTP Request Sent
GET /users HTTP/1.1
Authorization: Bearer token

5️⃣ Server Processing
Auth check
Business logic
Database query

6️⃣ HTTP Response Returned
200 OK
Content-Type: application/json

[
  {"id": 1, "name": "Rohan"}
]

7️⃣ Connection closed or reused

---------------------------------------------------------------------------------------------------------------

4️⃣ REST Principles

🔹 What is REST?
REST (Representational State Transfer) is an architectural style for designing APIs using HTTP.

🔸 Core REST Principles
1️⃣ Statelessness
Server does not remember client state
Every request contains all required info

❌ Bad:
Server remembers logged-in user

✅ Good:
Authorization: Bearer <token>

📌 Benefits:
1. Scalability
2. Reliability
3. Easier debugging



2️⃣ Resources


Everything is treated as a resource


Identified using URLs

Users -> /users
Single User -> /users/5
Orders -> /orders

3️⃣ HTTP Methods (Verbs)

Methods
GET -> Read
POST -> Create
PUT -> Update (full)
PATCH -> Update (partial)
DELETE -> Remove

Example:
POST /users


4️⃣ Representation
Resource can be represented in:
1. JSON (most common)
2. XML
3. HTML

{
  "id": 1,
  "name": "Rohan"
}


5️⃣ Status Codes
Code
200 -> OK
201 -> Created
400 -> Bad Request
401 -> Unauthorized
404 -> Not Found
500 -> Server Error

5️⃣ REST API Concepts (In Practice)
Example REST API Flow
GET /api/products

Response:
[
  {"id":101,"name":"Laptop","price":70000}
]

✔ Clean URLs
✔ Stateless requests
✔ Proper status codes
✔ JSON response

6️⃣ MDN Web Docs (Recommended Reference)
📘 MDN Web Docs is the gold standard for web fundamentals.

Key MDN Sections:
1. HTTP Overview
2. Request methods
3. Headers
4. Status codes
5. CORS
6. Caching
7. Security

💡 MDN explains what browsers actually implement, not just theory.

7️⃣ Big Picture Summary

Client → HTTP/HTTPS → Server → Response

Client–Server = separation of concerns

HTTP/HTTPS = communication rules

REST = design philosophy

Statelessness = scalability

Resources = clean API design



