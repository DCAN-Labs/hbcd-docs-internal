# Known Issues

## Lasso Interface
### ⚠️ Help Center Down for Maintenance
The Help Center is down for maintenance until next week - please email Aarushi Chaudhry (achaudhry@lassoinformatics.com) if you run into issues.

### ⚠️ Query Tool: No Rows Displayed on Toggling Between File-Based and Tabular Data Tabs
On toggling between file-based and tabular data tabs in the Dictionary Query Tool, users can expect to see an error where no rows are displayed. Please reload the page to populate the tabular data. We will fix this very soon.

---------------

## BR14.8 Target Release for Fix

### ⚠️ Duplicated Rows in Basic Demographics
**Impact on Users**: Data can still be queried, but the number of sessions cannot be accurately tallied from this table.
**How to Fix**: Remove duplicate entries
**Details**: The number of rows/sessions included in Basic Demographics (`sed_basic_demographics`) are duplicated, which increases the number of reported V02 and V03 sessions in the Basic Demographics. The data can still be consistently queried by using the first entry for a given participant, so the only issue is that the number of sessions should not be tallied from this table. We will be addressing this as soon as possible for BR14.8 or earlier if possible.

### ⚠️ Missing `par-visit-dat` File (sub-858XXXXXXX)
**Impact on Users**: This participant is absent from the database (DW queries), but is present in phenotype files.      
**How to Fix**: Lasso needs the proper entry to be added in par-visit-data.tsv.         
**Details**: This was hacked by the Lasso team to not block ingestion, but in a real scenario, ingestion would not be possible.

### ⚠️ Biospecimen Data: Missing Shadow Matrix
**Details**: Shadow matrix is not currently available for biospecimen data. LORIS will populate the shadow matrix with a place holder for the next release and work with the WG to discern reasons for missingness. The target release for fix is TBD until the reason for missingness is assessed. In the meantime, for BR14.7, placeholder text will be added to populate the shadow matrix.

-------

## TBD Target Release for Fix
### ⚠️ Partial EEG Sessions in Buckets
**Impact on Users**: End user will not see those files in the UI.  
**How to Fix**: Remove EEG sessions with partial data (ETA required from HDCC).        
**Details**: The V03 acquisitions for 5 participants errored in MADE and had various issues, therefore the EEG Workgroup asked for those files to be removed from the release. The EEG files were removed from BR14 and BR14.5 post-ingestion, which lead to 404 file not found errors when users queried file-based data in BR14 - this has since been resolved (see [BR14.6 Resolved Known Issues > ⚠️ Deleted EEG Data Causing 404 Errors](versions/BR14.6.md/#deleted-eeg-data-causing-404-errors)). However, the file removal caused a separate issue where some EEG companion files were left over after the deletion process (the sessions contain an acquisition file (SET) but only impedance, electrodes, and coordsystem), so the EEG sessions were skipped. This is not causing a major problem, but for the purpose of the release, those files should ideally be removed as well.

### ⚠️ Missing Shadow Matrices
**How to Fix**: TBD (Review required from LORIS).       
**Details**: Shadow matrices are missing for BrainSwipes (should not be considered yet) and the BioSpecimen data, which follows a different process and for which we currently do not have a clear way to populate blank fields.








