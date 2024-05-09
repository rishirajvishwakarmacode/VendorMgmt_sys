# Vendor Management System using Django Rest Framework

## Table of Contents
1. Models and Serializers
2. API endpoints
3. Database
4. CRUD operations using Django's generic API views
5. Django Signals for performance calculations

## Models and Serializers
Models are implemented using django models class. Models are interlinked or related using vendor model as the foreign_key for both Purchase_order and Performance model. Serializers are implemented using djangoRESTframework's modelSerializers. Using modelSerializers not only saves the hassel to declare each and every field but also consumes a lot lesser time. 

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


## CRUD operations using genericAPI views
For Implementing CRUD operations on models I used, generic views built in the Django REST framework. Reducing the time required to write code. Details of implementation in the views.py file in vendor application.

## Django Signals for performance calculations
To measure the performance parameters of each of vendors I used model signals and defined the signal functions within the models.py file in vendor application. With trigger methods of post_save, post_delete and sender being PurchaseOrder model the update_peformance function triggers with any updates in any of the PurchaseOrder instance either save, update or delete. Updates in PurchaseOrder model triggers update_performance function which in turn triggers four functions to calculate performance parameters and updates them into database. Once these parameters are updated Performance models sends signals to vendor model that in turn updates all vendor performance measures in vendor model. 
