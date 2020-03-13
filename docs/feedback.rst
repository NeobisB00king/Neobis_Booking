********************
Feedback information
********************

The "feedback" is a pretty straight forward part of the website,
it takes the info from "forms", edits it a little and sends to the
admin email witch is set in admin panel.

| It can be accessed by adding "feedback" to the URL, for example:
| **localhost:8000/feedback**

The form looks something like this:

+--------+--------+
|name    |   -    |
+--------+--------+
|email   |   -    |
+--------+--------+
|subject |   -    |
+--------+--------+
|message |   -    |
+--------+--------+

After user fills up the form it is edited to look like this for
admin when recieving the emai:

+--------------------+
|name, email, subject|
+--------------------+
|message             |
+--------------------+