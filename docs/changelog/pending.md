# Pending Updates

## Upcoming - BR20.1/20.2

### General Data Updates

- **Data Dictionary adjustments** *Based on flagged cases*
    * Validation script  
    * Lasso flags  
    * SME/WG reported: *Current Employment; Household Chemical Exposures*  
- **Multiple Birth/PNR**: Cleanup and Inclusion/Exclusion lists  
- **BioSpecimen**  
    * Data Ingestion of USDTL Nails, Urine & Blood Spot Card into LORIS database  
    * For `biosample_urine_bio_c_cot_u`, ensure missings values are not reported as '0'  
- **Basic Demographics**  
    * Remove `child_ethnoracial_acs_by_multi_race` from Basic Demographics (`sed_basic_demographics`)  
    * Child ACS race/ethnicity present at V01 (Change to `Unknown` for all V01)  
    * Remove ‘Hawaiian’ as an option for `screen_mother_race`  
    * Replace “defined by Ripple” with “(ACS item)” for `child_ethnicity` & `child_race`  
    * Replace “LORIS” with “RedCAP at V01” for `rc_mother_education` & `rc_mother_income`  
    * Replace “LORIS” mention with “Mother’s race/ethnicity (ACS item at enrollment)” for `screen_mother_race` & `screen_mother_ethnicity`  
    * Update label for Multiracial option (non-Black)   
    * Change description to indicate that 'Sex' refers to child for `sed_basic_demographics_sex` - Change to "Child sex (Male, Female)"  
- **Visit Data**  
    * Remove SU flags (`par_visit_data_su_flag_bio_barb`; `par_visit_data_su_flag_bio_benzo`; `par_visit_data_su_flag_bio_mscrlx`) from Visit Data
    * Set BioSpecimen SU flags at V02 as blank (Urine not collected at V02)

### File based data

* **Genomics Data files**  
* **Geocoding** - *Concatenated data tables*  
* **Study Navigator** - *Concatenated data tables*

### Instruments specific changes

- **Demographics**
    - 'Income' data levels merge (Go from 10 levels down to 6 levels)  
    - 'Education' data levels merge (Go from 21 levels down to 6 levels)  
    - Add selected ‘Roster’ fields; change label from “gender” to “sex” for selected roster fields
    - Remove the variable names in parentheses that are a part of the description for `sed_bm_demo_roster_001_i_00` & `sed_bm_demo_child_i_roster_002_i_02_i_00` to `sed_bm_demo_child_i_roster_020_i_02_i_00`  
    - Add '(other biological parent)' to description for `sed_bm_demo_herit_i_oth` fields 

- **Anthropometrics:** Review broken age calculations
- **APA:**
    - Remove level 2 data for participants not meeting level 1 threshold
    - Add ‘t-score’ and ‘total score’ fields for 'Anger' subscale  
- **BioSensor:** Change instrument name to include 'Novel Tech' (nt) domain
- **CDI:** Change DD from 'static' to 'character' with levels
- **EPDS:** Remove `pex_bm_epds_score`
- **Pex Health Illness:** ICD labels not imported for `pex_bm_health_preg_i_illness` codes (n=5)
- **SPM-2:** Missing 'Status score' for each sub scale.(Currently only provided for one sub scale)
- **TLFB:** Correct ages (Adjusted age and gestational age)
- **Vancouver Index of Acculturation:** Swap sub-scores

### Imaging/EEG

* **EEG MADE derivatives**  
* **Derivatives** - NiBabies & X-CPD  
* **Re-ID of tabular data**

### Other

* Review incorrect 'age_adjusted' values for specific cases  
* Add new 'Administrative' (or other) domain for exceptional forms (e.g. 'Visit Start', 'Clinical Alert')  
* Change 'type_var' to 'administrative for 'age' fields  
* Review cases where 'Missingness' reason is showing as 'Logic Skipped'  
* FamilyID Inclusion (TBD)

## Upcoming - Post-Release (2.0/3.0)

* **Brain Rating associated fields**  
* **Add ‘Unit’ information** - Audit of 'Unit' fields & include 'Unit' information (Ongoing - case by case basis review)   
* **PEX Medication breakdown** - Incorporate breakdown of medication labels  
* **Shadow Matrix - QC Flags** - Add logic to populate Shadow Matrix for:   
    * 'Blank' fields related to 'QC Flagged' cases (fields with validations)  
    * ‘Blank' fields related to other 'QC Flagged' cases  
* **Upgrade ‘Instructions’ extraction**


<br>