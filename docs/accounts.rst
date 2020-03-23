******************************
Accounts structure information
******************************

Authorization
*************

| Basicaly executed by adding /accounts/login/ to the URL
| so the URL should lookig somewhat like that: **http://localhost:8000/accounts/login/**
| 
| And on that page will be the regular login form

+---------+---------+
|Username |         |
+---------+---------+
|Password |         |
+---------+---------+

Accounts
********

| The only way to get an account is for superuser to create one with admin-panel
| which means **there is no registration system**.
| 
| Created accounts then can be granted permissions like:
| Access the admin panel
| Add, change, delete, view chosen activities like accounts, rooms, bookings etc.
| (It's pretty straightforward there in the admin panel)