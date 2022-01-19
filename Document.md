<div  align="center">

<img  src="https://user-images.githubusercontent.com/43369148/150193017-54a57e44-64b6-4020-b832-4f344239eedb.png" />

</div>

  
  

<div  align="center">

  

<h1>User Management Screen</h1>

  

</div>

  

## Table of Contents

  

- [Requirements](#requirements)

  

- [Functions](#functions)

  

- [Components](#components)

  

- [Behaviours](#behaviours)

  

- [Errors](#errors)

  
  

## Requirements
  
- **Backend Integration** : USER table access with CRUD for data attainments

- **UI Materials Kit** : To be uniform with the related pages using same libraries e.g Bootstrap,Material UI

## Functions
User Management Screen relies on creation and display of users.

- Creating User: Initiate with a button Create User --> get related info through form --> conclude to commit from button Save User.
- Displaying Users : Getting the view only includes the table with columns of : ID, User Name, Email, Enabled
- Filtering : Hide Disable User --> Returns only users with Enabled = True
- Sorting : Sorting is included in table column names view. ID sorts decending only , UserName , Email and Enabled sorts both decending and ascending alphabetically. Can be handled in both frontend or backend
  
## Components

### Web Page Layout 
#### 2 Rows with Containers

  ##### First Container 
  - Components included : Create User Button + Radio Button + Save User Button 
  
  ![pi_ui_buttons](https://user-images.githubusercontent.com/43369148/150200059-baa616c4-d658-4f12-a4cd-6dc2d0216231.png)
  
  - Second Container --> Table + Form (2 Columns are in same width which is 50%)

![pi_ui_form](https://user-images.githubusercontent.com/43369148/150200039-92968d1f-7fbf-44ab-926c-ebab41ca3880.png)
![pi_ui_table](https://user-images.githubusercontent.com/43369148/150200074-0d25e4ce-d5f4-406a-a14d-f2f96621e3f3.png)
  

## Behaviours



## Errors


