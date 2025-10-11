
## Detailed Workflows


check workflows 7 and 8 

# Further Details on De-Id Routines

The de-identification procedures of raw BIDS data largely covers the following groups of files:

* Standard BIDS metadata text sources such as `scans.tsv`, `session.tsv`, JSON files  
    * In motion files, any JSON fields with `PatientName` or `PatientBirthDate` are deleted  
    * In scans/sessions tsv/json files, the site information is replaced with anonymized site IDs based on a site mapping file.  
    * All other JSON files known to contain site IDs have `InstitutionAddress`, `InstitutionalDepartmentName`, and `InstitutionName` deleted  
* EEG `eventlogs.txt` sourcedata files: Custom routines anonymize entries for `DataFile.Basename`, `DCCID`, and `Subject` columns  
* EEG .set files  
    * Custom routines recursively search through nested fields and replaces DCCIDs/PSCIDs with Release Candidate IDs  
    * Certain fields likely to contain manually entered information such as DCCID/PSCID have their text replaced with ‘Anonymized’  
    * Other fields likely to contain manually entered information have values outside of a pre-approved list of strings replaced with ‘Anonymized’  
* **MRS Nifti files:** Fields `InstitutionName`, `InstitutionAddress`, `PatientSex`, and `PatientWeight` are removed from nifti headers using spec2nii


Some files are not currently supported by de-identification routines and have thus far not been copied to any of the de-identified data stores. This includes files from the EEG sourcedata directory (i.e. `sub-{ID}/ses-{V0X}/eeg/sourcedata`): `eventlogs.edat3` and `eeg_flags.json` files