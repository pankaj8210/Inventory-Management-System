# Inventory-Management-System

### Objective:
Develop a backend API for an Inventory Management System that supports CRUD
operations on inventory items, integrated with JWT-based authentication for secure
access. The system should use Django Rest Framework (DRF) for the API framework,
PostgreSQL for the database, Redis for caching, and include unit tests to ensure
functionality. Implement proper error handling with appropriate error codes and integrate a
logger for debugging and monitoring.
#### Background:
An inventory management system allows a business to manage its stock of products
efficiently. The system must provide endpoints to create, read, update, and delete (CRUD)
items in the inventory. To improve performance, frequently accessed items should be
cached using Redis. Additionally, JWT authentication will be used to secure access to the
API.
