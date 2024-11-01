# Day-12: Serialization, Deserialization, Mixins, and Decorators

## DRF Component Overview:
### The connection between serializers.py, views.py, and urls.py in Django REST Framework (DRF) 


**Model**: Represents the structure of database tables, with each model class corresponding to a table and fields as columns. It defines and handles the database interactions.

**Serializer**: Manages data conversion and validation. It transforms model data to JSON for API responses and ensures incoming data meets validation rules before saving.

**View**: Contains the main logic of each API endpoint. Views use serializers to validate and serialize data, determining what data to send or receive and how to process it for each request type (GET, POST, etc.).

**URL**: Routes requests to the appropriate views, defining endpoints for each view. It connects specific views to web addresses, allowing clients to access API resources.

### How They Connect:
- **URL** directs requests to Views.

- **Views** process requests, using Serializers to validate/serialize data.

- **Serializers** interact with Models for database operations.

