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
  - Height : 10%
  - Components included : 
	  - Create User Button
		 - Height : 10px
		 - Width : 20px 
	     - Background Color :  Dark Blue 
	     - Symbol : '+'  Before Text
	     - Text : 'New User'
	     - Text Color : White
	     - Padding : 0px 5px
	  -  Hide Disabled User Checkbox
		  - Text : 'Hide Disabled User'
	     - Text Color : Black
	  -  Save User Button 
	 	 - Height : 10px
		 - Width : 20px 
	     - Background Color :  Light Blue 
	     - Symbol : None
	     - Text : 'Save User'
	     - Text Color : White
	     - Padding : 0px 5px
  - Allignment:
	  - Create User Button + Hide Disabled User Checkbox alligns to left in this order
	  - Save User Button alligns right
	  
  - Padding
	  -  Bottom 1 rem
	  
- Mock Up:

 ![pi_ui_buttons](https://user-images.githubusercontent.com/43369148/150200059-baa616c4-d658-4f12-a4cd-6dc2d0216231.png)
##### Second Container
  - Height: auto
  - Components included:
	  - Table
		  - Column Names Background Color : Dark Blue
		  - Column Names Text Color : White
		  - Text Allign : Left
		  - Column Names Icons : 
			  - ID :   Up Arrow + Filter
			  - User Name : Up and Down Arrow + Filter
			  - Email : Up and Down Arrow + Filter
			  - Enabled : Up and Down Arrow + Filter
			  - Icon Allign : Right (in the same order written)
			  - Icon Color : White
		  - Row Color : White and Light Blue Alternating
		  - Data Text Color : Black
		  - Background Color : White
		  - Border Color : Light Grey
		  - Mock Up :
		  
		  ![pi_ui_table](https://user-images.githubusercontent.com/43369148/150200074-0d25e4ce-d5f4-406a-a14d-f2f96621e3f3.png)
	 
	  - Form
		  - Title Text : 'New User'
		  - Title Background : Light Grey
		  - Title Height : 15%
		  - Title Text Color : Black
		  - Title Text Size : 20px
		  - Inputs (In Order):
			  -  Username 		(Textbox)
			  -  Display Name 	(Textbox)
			  -  Phone 				(Textbox)
			  -  Email 				(Textbox)
			  - User Roles			(Dropbox)
			  - Enabled 				(Checkbox)
		  - User Roles Dropbox Options : Guest, Admin, SuperAdmin
		  - User Roles Dropbox Text Before Selection : 'Select User Roles'
		  - Input Title Text Color : Black
		  - Input Title Text Size : 10px
		  - Input Title Text Padding : Left 3px
		  - Input Title Text Column Width : 20%
		  - Input Width : 80%
		  - Mock Up:
		  
![pi_ui_form](https://user-images.githubusercontent.com/43369148/150200039-92968d1f-7fbf-44ab-926c-ebab41ca3880.png)

- Allignment
	- 2 Columns are in same width which is 45%
	- Table alligns left with padding right 1 rem 
	-  Form alligns right 

## Behaviours
- Form is not visible before clicking '+New User' button
- After click Form is visible in the second container's column in right
- All User Data is fetched and viewed in page landing
- Hide Disabled User Checkbox is active in default
- All inputs are checked while submitting the form
- If the form is fulfilled correctly after clicking 'Save User' button pop-up appears saying 'User Saved'
- While sorted if any other arrow button is clicked sorts again according to the related area
## Errors
- Error pops up if inputs are in false format and trying to submit 
- Error pops up if any of the input area is blank and trying to submit 
- Error pops up if selected inputs are not unique (etc. Username, ... exists) and trying to submit

