# Known Issues

## Lasso Interface
### ⚠️ Help Center Down for Maintenance
The Help Center is down for maintenance until next week - please email Aarushi Chaudhry (achaudhry@lassoinformatics.com) if you run into issues.

### ⚠️ Query Tool: No Rows Displayed on Toggling Between File-Based and Tabular Data Tabs
On toggling between file-based and tabular data tabs in the Dictionary Query Tool, users can expect to see an error where no rows are displayed. Please reload the page to populate the tabular data. We will fix this very soon.

---------------

## TBD Target Release for Fix
### ⚠️ Partial EEG Sessions in Buckets
**Impact on Users**: End user will not see those files in the UI.  
**How to Fix**: Remove EEG sessions with partial data (ETA required from HDCC).        
**Details**: The V03 acquisitions for 5 participants errored in MADE and had various issues, therefore the EEG Workgroup asked for those files to be removed from the release. The EEG files were removed from BR14 and BR14.5 post-ingestion, which lead to 404 file not found errors when users queried file-based data in BR14 - this has since been resolved (see [BR14.6 Resolved Known Issues > ⚠️ Deleted EEG Data Causing 404 Errors](versions/BR14.6.md/#deleted-eeg-data-causing-404-errors)). However, the file removal caused a separate issue where some EEG companion files were left over after the deletion process (the sessions contain an acquisition file (SET) but only impedance, electrodes, and coordsystem), so the EEG sessions were skipped. This is not causing a major problem, but for the purpose of the release, those files should ideally be removed as well.










