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
The API contains endpoints for CRUD operations on vendor model and Purhase_order model. Here are some examples, on using API endpoints. API endpoints for vendors are as follows -

| Task | Endpoint |
| --- | --- |
| Listing all Vendors | GET api/vendors/ |
| Creating a new Vendor | POST api/vendors/ |
| Retrieving a specific Vendor | GET api/vendor/{vendor_id}/ |
| Updating vendor | PUT api/vendor/{vendor_id}/ |
| Deleting Vendor | DELETE api/vendor/{vendor_id} |
| Performance matrix of specified vendor | GET api/vendors/{vendor_id}/performance |


API endpoints for Purchase_order are as follows -
| Task | Endpoint |
| --- | --- |
| Listing all Purchase Orders | GET api/purchase_orders / |
| Creating a new Purchase order | POST api/purchase_orders/ |
| Retrieving a specific Purchase order | GET api/purchase_order/{po_id}/ |
| Updating a specific Purchase order | PUT api/purchase_order/{po_id}/ |
| Deleting a specific Purchase orde | DELETE api/purchase_order/{po_id}/ |

