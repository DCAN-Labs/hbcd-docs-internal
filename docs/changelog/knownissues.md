# Known Issues

### ⚠️ #1 - Partial EEG Sessions in Buckets
Some EEG sessions were skipped because they do not contain an acquisition file (set) but only impedance, electrodes, and coordsystem. Those sessions correspond to the ones that failed MADE processing. Electrodes, coordystems, and impedance files were also recently added in the release (HBCD).

**Impact on Users**: End user will not see those files in the UI.          
**Target Release for Fix**: TDB - ETA required from HDCC.  

### ⚠️ #2 - Empty Label Column in HBCD Data Dictionary
The field dictionary "label" has been renamed "Description," diverging from ABCD convention. To fix this, in Lasso, the DD column will be renamed to Description (and save the ABCD Label DD field as ‘Description.’) 

**Impact on Users**: In the HBCD DD, the Label column is empty.         
**Target Release for Fix**: BR15. 

### ⚠️ #3 - Issue With `nibabies.toml` Files
Lasso bug: FE import with duplicated ID impacting the Nibabies file type `bids/derivatives/nibabies/sub-<label>/ses-<label>/log/20250125-071817_f14585f4-03b1-48ef-8cdc-edc3eb0be744/nibabies.toml`.

**Impact on Users**: These files are temporarily not available for download.        
**Target Release for Fix**: Lasso ETA is March 10.

### ⚠️ #4 - Incompatible Format of M-CRIB-S and FreeSurfer Data
M-CRIB-S and FreeSurfer do not follow the BIDS subdirectory convention of other derivatives, using `sub-<label>_ses-<label>` instead of `sub-<label>/ses-<label>`. As a result, import failed because we cannot extract the subject/session. To address this issue, the data will be reorganized in the prerelease bucket to follow the BIDS convention.  

**Impact on Users**: These files are temporarily not available for download.       
**Target Release for Fix**: BR14.6.

### ⚠️ #5 - Missing Labels For 'Levels' On Multi-Select To Checkbox Items
There are some unresolved issues with the conversion of multi-select fields to checkboxes for values derived from the Ripple Pregnancy Check up and pushed to the derived Basic Demographics (`sed_basic_demographics`) directly. The values for the checkbox 'levels' are missing, and only the expected labels (TRUE/FALSE) are available in the Data Dictionary.

**Impact on Users**: Missing labels for 'levels' on multi-select to checkbox items in `sed_basic_demographics`.       
**Target Release for Fix**: BR14.7.

### ⚠️ #6 -  Missing Administrative Variables (Gestational and Candidate Age) for BioSpecimen, MRI/EEG & Derived categories
**Target Release for Fix**: BR14.7.

### ⚠️ #7 - BrainSwipes Erroneously Included
BrainSwipes should have not been included, and this was an oversight on removing the files generated from the S3 bucket before de-identification.
     
**Target Release for Fix**: TBD

### ⚠️ #8 - Missing Shadow Matrices
Shadow matrices are missing for BrainSwipes (should not be considered yet) and the BioSpecimen data, which follows a different process and for which we currently do not have a clear way to populate blank fields.
   
**Target Release for Fix**: TBD








