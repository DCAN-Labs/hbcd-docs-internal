# Known Issues

### ⚠️ #1 - Deleted EEG Data
EEG files were ingested and disappeared from the bucket post ingestion, resulting in 404 errors when users try to download all the EEG data (HBCD).

**Impact on Users**: Any download including EEG files will fail.       
**Target Release for Fix**: BR 14.6. 

### ⚠️ #2 - Partial EEG Sessions in Buckets
Some EEG sessions were skipped because they do not contain an acquisition file (set) but only impedance, electrodes, and coordsystem. Those sessions correspond to the ones that failed MADE processing. Electrodes, coordystems, and impedance files were also recently added in the release (HBCD).

**Impact on Users**: End user will not see those files in the UI.          
**Target Release for Fix**: TDB - ETA required from HDCC.  

### ⚠️ #3 - Empty Label Column in HBCD Data Dictionary
The field dictionary "label" has been renamed "Description," diverging from ABCD convention. To fix this, in Lasso, the DD column will be renamed to Description (and save the ABCD Label DD field as ‘Description.’) 

**Impact on Users**: In the HBCD DD, the Label column is empty.         
**Target Release for Fix**: First release after 14.6. 

### ⚠️ #4 - Issue With `nibabies.toml` Files
Lasso bug: FE import with duplicated ID impacting the Nibabies file type `bids/derivatives/nibabies/sub-<label>/ses-<label>/log/20250125-071817_f14585f4-03b1-48ef-8cdc-edc3eb0be744/nibabies.toml`.

**Impact on Users**: These files are temporarily not available for download.        
**Target Release for Fix**: Lasso ETA is March 10.

### ⚠️ #5 - Incompatible Format of M-CRIB-S and FreeSurfer Data
M-CRIB-S and FreeSurfer do not follow the BIDS subdirectory convention of other derivatives, using `sub-<label>_ses-<label>` instead of `sub-<label>/ses-<label>`. As a result, import failed because we cannot extract the subject/session.  

**Impact on Users**: These files are temporarily not available for download.       
**Target Release for Fix**: TBD - ETA needed from HDCC.




