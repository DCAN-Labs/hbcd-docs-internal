# Known Issues

### ⚠️ #1 - Partial EEG Sessions in Buckets
**Impact on Users**: End user will not see those files in the UI.          
**Target Release for Fix**: TDB - ETA required from HDCC.  
**Details**: The V03 acquisitions for 5 participants errored in MADE and had various issues, therefore the EEG Workgroup asked for those files to be removed from the release. The EEG files were removed from BR14 and BR14.5 post-ingestion, which lead to 404 file not found errors when users queried file-based data in BR14 - this has since been resolved (see [BR14.6 Resolved Known Issues > ⚠️ #4 - Deleted EEG Data Causing 404 Errors](versions/BR14.6.md/#4-deleted-eeg-data-causing-404-errors)). However, the file removal caused a separate issue where some EEG companion files were left over after the deletion process (the sessions contain an acquisition file (SET) but only impedance, electrodes, and coordsystem), so the EEG sessions were skipped. This is not causing a major problem, but for the purpose of the release, those files should ideally be removed as well.

### ⚠️ #2 - Incompatible Format of M-CRIB-S and FreeSurfer Data
**Impact on Users**: These files are temporarily not available for download.       
**Target Release for Fix**: BR14.7.     
**Details**: M-CRIB-S and FreeSurfer do not follow the BIDS subdirectory convention of other derivatives, using `sub-<label>_ses-<label>` instead of `sub-<label>/ses-<label>`. As a result, import failed because we cannot extract the subject/session. To address this issue, the data will be reorganized in the prerelease bucket to follow the BIDS convention.  

### ⚠️ #3 - Missing Labels For 'Levels' On Multi-Select To Checkbox Items
**Impact on Users**: Missing labels for 'levels' on multi-select to checkbox items in `sed_basic_demographics`.       
**Target Release for Fix**: BR14.7.     
**Details**: There are some unresolved issues with the conversion of multi-select fields to checkboxes for values derived from the Ripple Pregnancy Check up and pushed to the derived Basic Demographics (`sed_basic_demographics`) directly. The values for the checkbox 'levels' are missing, and only the expected labels (TRUE/FALSE) are available in the Data Dictionary.

### ⚠️ #4 -  Missing Administrative Variables (Gestational and Candidate Age) for BioSpecimen, MRI/EEG & Derived categories
**Target Release for Fix**: BR14.7.

### ⚠️ #5 - BrainSwipes Erroneously Included
**Target Release for Fix**: BR15.            
**Details**: BrainSwipes should have not been included, and this was an oversight on removing the files generated from the S3 bucket before de-identification. The BrainSwipes data is not ready for release and should not be considered yet.   

### ⚠️ #6 - Missing Shadow Matrices
**Target Release for Fix**: TBD (Review required from LORIS).       
**Details**: Shadow matrices are missing for BrainSwipes (should not be considered yet) and the BioSpecimen data, which follows a different process and for which we currently do not have a clear way to populate blank fields.
   









