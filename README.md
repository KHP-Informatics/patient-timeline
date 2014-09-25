# Patient Record Timeline

## Overview
Using a json file/request to display the patient data in a timeline page.

## Original purposal 
One of the biggest issues clinicians have with the move to an electronic health record system at SLaM is that it is no longer possible to pick up a patient's record and flick through the documents in it, to get an overview of their case, or of recent events, or just to find a document you're looking for. Instead, in the existing system one must open up documents one by one and read through them, which is time consuming. It would be very useful to have a scrollable timeline of all of the documents, potentially just one long concatenated document, or alternatively something that made it easy to get a summary / preview of each document as you scrolled, without having to download it and open in on your local machine. In general, better ways of visualising the key points of a patient's record and drilling down to specifics in a user-friendly way would be extremely useful.


### reference
using jQuery Timliner library: https://github.com/technotarek/timeliner


#### testing:

python server.py

http://hostname:5000/static/timeliner.html
