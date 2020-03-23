***************************
Rooms structure information
***************************

Adding rooms
************

| You can add new rooms by adding "/room/add/" to initial URL
| so that it looks like this:
| **localhost:8000/room/add/**
|
| This page can be accessed only if you are a superuser or user
| with admin rights.
| 
| On this page there is a form that consists of:
| Name, Capacity, Category, Volume and Images.

Viewing rooms
*************

| You can view all the existing rooms by adding "/room/list/"
| to initial URL so tha it looks like this:
| **localhost:8000/room/list/**
| 
| This page can be accessed by anyone

Searching rooms
***************

| To search for rooms add "/room/search/" to initial URL
| so that it looks like this:
| **localhost:8000/room/search/**
|
| This page can be accessed by anyone
|
| On that page there is 3 fields to choose from (or use all 3).
| Search by name (of part of the name).
| Search rooms with capaticy more than entered.
| Search rooms with capatich less then entered.