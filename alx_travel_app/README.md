Project Components Overview
📂 Models – Database Structure
Define how your application's data is stored and related within the database.
What we will build
User – Using Django’s built-in User model


Conversation – Represents a chat thread between two or more users


Message – Represents individual messages within a conversation


🔄 Serializers – Data Conversion
Convert between Python objects and JSON so your API can send and receive data.
Serializers we will create
UserSerializer – Handles user data


ConversationSerializer – Handles conversation data


MessageSerializer – Handles message data

🌱 Seeders – Sample Data
Populate the database with test data for development and testing.
Seeders will create
Sample users


Example conversations


Sample messages


You can implement seeders using:
Django management commands


Custom Python scripts placed inside your Django app



📚 Django Chat Application — Models, Serializers & Seeders
This project implements a simple chat application using Django and Django REST Framework.
 It includes data models, serializers for API communication, and seeders for generating sample data during development.

🧱 Models – Database Structure
Models define how your application stores and structures data inside the database.
Included Models
User
 Using Django’s built-in User model for authentication and user details.
Conversation
 Represents a chat thread between users. A conversation can include two or more participants.


Message
 Represents individual messages sent inside a conversation.
🔄 Serializers – Data Conversion
Serializers convert Python/Django objects into JSON and vice-versa, enabling clean API communication.
Included Serializers
UserSerializer
 Handles the conversion of user data for API responses.


ConversationSerializer
 Responsible for converting conversation data, including linked participants.


MessageSerializer
 Converts message objects, including the sender and timestamp.



🌱 Seeders – Sample Data Population
Seeders help populate the database with sample data for development and testing.
Seeders Will Create
Sample users


Sample conversations


Sample messages


You can create seeders using:
Django management commands


Standalone Python scripts inside your Django app


These seeders make it easy to test the chat functionality without manually entering data.

 Summary
This project demonstrates how to:
Structure chat-related data with Django models


Use serializers for clean API response formatting
## Chapa Payment Integration

This project integrates Chapa API for secure payment processing.

### Payment Flow
1. User initiates booking
2. Payment is initialized via Chapa
3. User completes payment on Chapa checkout
4. Payment is verified
5. Status updated (Pending → Completed / Failed)
6. Confirmation email sent via Celery

### Environment Variables
- CHAPA_SECRET_KEY
- CHAPA_PUBLIC_KEY

### Testing
Chapa sandbox environment used.
