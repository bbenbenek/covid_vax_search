# CVS COVID-19 Vaccine Availabilty Search

This will search the CVS Vaccine website for availability of appointments. It will send a text message via Twilio (free account) to you or any other verified phone number when availability opens up in the specified State and Cities of interest. It refreshes and re-searches every 5 minutes (300 seconds) and collects the json data file that contains updated information. This is not perfect, but should give you an idea of when appointments become available so you can anticipate when you should do a more robust manual effort. 

This script WILL NOT find specific appointment times for you. That is up to you to do manually. This script will simply identify the general availabilty, which can come and go very quickly as spots are filled.

CVS is updating their bot-fighting power, so there is a chance that this does not work as more sophisicated defenses are implements, but the only issue I've had with this is hitting the max number of refreshes to the CVS site over the course of ~24 hours.
