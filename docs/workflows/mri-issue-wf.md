<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 <br> 
Finalize from source doc <a href="https://docs.google.com/document/d/1EYMx3GtJ7oSoum69PHD7lqbE_JUgyvEk/edit?usp=sharing&ouid=113306241090115436408&rtpof=true&sd=true">here</a></p>

# HBCD MR Radiology Workflow: From Site to Radiologist

## 1. Initial Site Notification

* Site emails the following core contacts: Chris, Chad, Ron, Don, Cecile, Samir.  
* Radiologists (Bob/Josh) are included only when data is nearly ready for review.

## 2. Urgent Ticket Creation

* Site opens an urgent LORIS ticket to formally log the request and track progress.  
* Default Assignee: Ron  
* Default Watchers: Cecile, Chris, Chad, Don and Samir.

## 3. Data Location Verification

* Ron update ticket to ‘Acknowledged’  
* Ron checks pipeline systems to verify the current location of the MR data.  
  * FIONA 🡪 LORIS 🡪 AMBRA 🡪

## 4. Data Transfer: Imaging Pipeline

* Standard flow: FIONA → LORIS → AMBRA.  
* For urgent cases, Ron pushes from FIONA directly to UCSD, skipping QC.  
* UCSD ingests the data into their S3 bucket.

## 5. Push to AMBRA

* A sync pushes data from UCSD/S3 to AMBRA (cronjob run every 15 minutes). We will ensure.

## 6. Readiness Checkpoint

* Once data is confirmed as present in AMBRA (and accessible to the radiology team), the designated contact updates the LORIS ticket.  
* [Standard ticketing workflow](https://docs.google.com/document/d/1pKg5lPRdE1h_rz0xILFxpCQgqmyT3--NN_iwTXqVEKw/edit?tab=t.0#heading=h.1nf1t4ccbhdx) ensues (Acknowledged, Assigned, Feedback status updates as necessary).

## 7. Radiologist Notification

* Radiologists (Bob, Josh) included as Watchers and are notified MR is in AMBRA and ready for review.  
* Radiologists perform the read in AMBRA and email the site with the report.  
* Ticket update to ‘Resolved’ and assigned back to initial ‘Reporter’ (site).  
* Site reviews and closes ticket (if no further action required).

### **8. Documentation**

* All communication and actions are logged in the LORIS ticket for traceability.

<br>

<img class="center" src="../images/urgent-mri-wf.jpeg" width="70%" height="auto">
