# Vendor Management System using Django Rest Framework

## Table of Contents
1. Models and Serializers
2. API endpoints
3. Database
4. CRUD operations using Django's generic API views

## Models and Serializers
Models are implemented using django models class. Models are interlinked or related using vendor model as the foreign_key for both Purchase_order and Performance model. Serializers are implemented using djangoRESTframework's modelSerializers. Using modelSerializers not only saves the hassel to declare each and every field but also consumes a lot lesser time. 

### Data Validation in Serializers

## API Endpoints.
The API contains endpoints for CRUD operations on vendor model and Purhase_order model. Here are some examples, on using API endpoints.
