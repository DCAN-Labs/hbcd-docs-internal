# Clinical Data Validation Procedure

<div class="pill-center">
  <a href="../../#data-quality-checks" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip">
        <i class="fa-solid fa-clipboard-check" style="color: #6300d3;"></i>
        <span class="tooltiptext">Data quality checks<br><i>Click to learn more</i></span>
      </span>
    </span>
  </a>
  <a href="../../#project-management" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip">
        <i class="fa-solid fa-diagram-project" style="color: #6300d3;"></i>
        <span class="tooltiptext">Project Management<br><i>Click to learn more</i></span>
      </span>
    </span>
  </a>
  <a href="../../#reproducibility" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip">
        <i class="fa-solid fa-code-compare" style="color: #6300d3;"></i>
        <span class="tooltiptext">Reproducibility<br><i>Click to learn more</i></span>
      </span>
    </span>
  </a>
</div>
<p></p>

*Validation procedures for Electronic Health Records (EHR) data are performed as follows:*

<img src="../images/EHR-wf.png">

1. Load EHR data from the site into the Landing Zone within the Secure Computing Environment  
2. Run a script to validate that the Landing Zone data was loaded correctly that checks for the following issues and coordinate with the site to correct these issues:  
    - Dates only sent when expecting date / time  
    - Time only sent when expecting date / time  
    - Date / time format was unknown to import script so it was imported as a varchar (requires changes to import script)  
    - Headers not sent so the column names are based on the first row of the data  
    - Rows are all NULL values because the file had rows with no data  
3. Run the Landing Zone to OMOP mapping scripts for each site  
    - Correct any known site-specific issues that can be automatically corrected in the scripts  
    - Let the site know of any issues with their data preventing mapping of their data  
    - Move data that passes QA into the central HBCD Clinical Data Repository (versioned for each year)  
4. Generate two reports back to each site  
    [1] EHR data received by participant study ID  
    [2] Summary Table 1 for the site


<div id="table1" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Example Table 1 Summary (Birth Parent)</span>
  <a class="anchor-link" href="#table1" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
    <thead>
      <tr>
        <th style="width: 5%;">Characteristic</th>
        <th style="width: 5%;">Total</th>
      </tr>
    </thead>
    <tbody>
      <tr>
      <td><b>N</b></td>
      <td>870</td>
      </tr>
      <tr>
      <td><b>Demographics</b></td>
      <td>&nbsp;</td>
      </tr>
      <tr>
      <td>Mean age (&plusmn; SD)</td>
      <td>31.69 (5.69)</td>
      </tr>
      <tr>
      <td>Sex|FEMALE</td>
      <td>870 (100.0)</td>
      </tr>
      <tr>
      <td>Sex|MALE</td>
      <td>0 (0.0)</td>
      </tr>
      <tr>
      <td>Sex|No matching concept</td>
      <td>0 (0.0)</td>
      </tr>
      <tr>
      <td>Race|American Indian or Alaska Native</td>
      <td>10 (1.1)</td>
      </tr>
      <tr>
      <td>Race|Asian</td>
      <td>39 (4.5)</td>
      </tr>
      <tr>
      <td>Race|Black or African American</td>
      <td>197 (22.6)</td>
      </tr>
      <tr>
      <td>Race|Native Hawaiian or Other Pacific Islander</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Race|No matching concept</td>
      <td>105 (12.1)</td>
      </tr>
      <tr>
      <td>Race|White</td>
      <td>517 (59.4)</td>
      </tr>
      <tr>
      <td>Ethnicity|Hispanic or Latino</td>
      <td>122 (14.0)</td>
      </tr>
      <tr>
      <td>Ethnicity|Not Hispanic or Latino</td>
      <td>748 (86.0)</td>
      </tr>
      <tr>
      <td>Ethnicity|No Matching Concept</td>
      <td>0 (0.0)</td>
      </tr>
      <tr>
      <td><b>Conditions</b></td>
      <td>&nbsp;</td>
      </tr>
      <tr>
      <td>Major depression, single episode</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Second trimester pregnancy</td>
      <td>127 (14.6)</td>
      </tr>
      <tr>
      <td>Third trimester pregnancy</td>
      <td>117 (13.4)</td>
      </tr>
      <tr>
      <td>First trimester pregnancy</td>
      <td>88 (10.1)</td>
      </tr>
      <tr>
      <td>Disorder of pregnancy</td>
      <td>87 (10.0)</td>
      </tr>
      <tr>
      <td>Complication occurring during pregnancy</td>
      <td>66 (7.6)</td>
      </tr>
      <tr>
      <td>Anxiety disorder</td>
      <td>66 (7.6)</td>
      </tr>
      <tr>
      <td>Depressive disorder</td>
      <td>64 (7.4)</td>
      </tr>
      <tr>
      <td>Fetal condition affecting obstetrical care of mother</td>
      <td>52 (6.0)</td>
      </tr>
      <tr>
      <td>Gestation period, 36 weeks</td>
      <td>50 (5.7)</td>
      </tr>
      <tr>
      <td>Anemia of pregnancy</td>
      <td>47 (5.4)</td>
      </tr>
      <tr>
      <td>Mental disorders during pregnancy, childbirth and the puerperium</td>
      <td>46 (5.3)</td>
      </tr>
      <tr>
      <td>Finding related to pregnancy</td>
      <td>34 (3.9)</td>
      </tr>
      <tr>
      <td>Uncomplicated asthma</td>
      <td>28 (3.2)</td>
      </tr>
      <tr>
      <td>Disease of the respiratory system complicating pregnancy, childbirth and/or the puerperium</td>
      <td>28 (3.2)</td>
      </tr>
      <tr>
      <td>Poor fetal growth affecting management</td>
      <td>27 (3.1)</td>
      </tr>
      <tr>
      <td>Maternal obesity complicating pregnancy, childbirth and the puerperium, antepartum</td>
      <td>24 (2.8)</td>
      </tr>
      <tr>
      <td>Generalized anxiety disorder</td>
      <td>18 (2.1)</td>
      </tr>
      <tr>
      <td>Posttraumatic stress disorder</td>
      <td>14 (1.6)</td>
      </tr>
      <tr>
      <td>High risk pregnancy</td>
      <td>11 (1.3)</td>
      </tr>
      <tr>
      <td><b>Lab Results</b></td>
      <td>&nbsp;</td>
      </tr>
      <tr>
      <td>Body temperature (degree Celsius)</td>
      <td>36.69 (0.18)</td>
      </tr>
      <tr>
      <td>Systolic blood pressure (millimeter mercury column)</td>
      <td>119.48 (9.42)</td>
      </tr>
      <tr>
      <td>Diastolic blood pressure (millimeter mercury column)</td>
      <td>72.49 (5.62)</td>
      </tr>
      <tr>
      <td>Heart rate (counts per minute)</td>
      <td>91.58 (8.91)</td>
      </tr>
      <tr>
      <td>No matching concept (nanogram per milliliter)</td>
      <td>358.33 (1243.37)</td>
      </tr>
      <tr>
      <td>Pain severity - 0-10 verbal numeric rating [Score] - Reported</td>
      <td>1.77 (1.01)</td>
      </tr>
      <tr>
      <td>Hematocrit [Volume Fraction] of Blood by Automated count (percent)</td>
      <td>34.81 (3.19)</td>
      </tr>
      <tr>
      <td>MCV [Entitic volume] by Automated count (femtoliter)</td>
      <td>88.14 (6.84)</td>
      </tr>
      <tr>
      <td>MCH [Entitic mass] by Automated count (picogram)</td>
      <td>29.53 (2.52)</td>
      </tr>
      <tr>
      <td>Erythrocyte distribution width [Ratio] by Automated count (percent)</td>
      <td>13.65 (1.58)</td>
      </tr>
      <tr>
      <td>Respiratory rate (counts per minute)</td>
      <td>17.35 (0.54)</td>
      </tr>
      <tr>
      <td>Platelet mean volume [Entitic volume] in Blood by Automated count (femtoliter)</td>
      <td>10.52 (1.09)</td>
      </tr>
      <tr>
      <td>Body temperature (degree Fahrenheit)</td>
      <td>97.87 (0.26)</td>
      </tr>
      <tr>
      <td>Erythrocyte distribution width [Entitic volume] by Automated count (femtoliter)</td>
      <td>43.61 (8.49)</td>
      </tr>
      <tr>
      <td>No matching concept (milligram per deciliter)</td>
      <td>98.85 (122.08)</td>
      </tr>
      <tr>
      <td>Hemoglobin [Mass/volume] in Blood (gram per deciliter)</td>
      <td>11.64 (1.14)</td>
      </tr>
      <tr>
      <td>Oxygen saturation in Arterial blood by Pulse oximetry (percent)</td>
      <td>97.99 (1.05)</td>
      </tr>
      <tr>
      <td>Body weight (kilogram)</td>
      <td>83.74 (25.21)</td>
      </tr>
      <tr>
      <td>Body height (centimeter)</td>
      <td>163.48 (6.62)</td>
      </tr>
      <tr>
      <td><b>Procedures</b></td>
      <td>&nbsp;</td>
      </tr>
      <tr>
      <td>Ultrasound scan for fetal growth</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Antenatal screening</td>
      <td>12 (1.4)</td>
      </tr>
      <tr>
      <td>Monitoring of Products of Conception, Cardiac Rate, External Approach</td>
      <td>10 (1.1)</td>
      </tr>
      <tr>
      <td>Fetal biophysical profile</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasonography for antepartum monitoring of fetus</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasound scan - obstetric</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasound scan for fetal nuchal translucency</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasonography in first trimester</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Delivery of Products of Conception, External Approach</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasonography of Third Trimester, Single Fetus</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>X-ray of chest anteroposterior view</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Extraction of Products of Conception, Low, Open Approach</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Drainage of Amniotic Fluid, Therapeutic from Products of Conception, Via Natural or Artificial Opening</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasonography of Second Trimester, Single Fetus</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Diagnostic radiography of chest, combined PA and lateral</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Counseling</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasonography of cervix uteri</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Insertion of Other Device into Products of Conception, Via Natural or Artificial Opening</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Repair Perineum Muscle, Open Approach</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td><b>Medications</b></td>
      <td>&nbsp;</td>
      </tr>
      <tr>
      <td>sodium chloride</td>
      <td>142 (16.3)</td>
      </tr>
      <tr>
      <td>ibuprofen</td>
      <td>132 (15.2)</td>
      </tr>
      <tr>
      <td>potassium chloride</td>
      <td>125 (14.4)</td>
      </tr>
      <tr>
      <td>calcium chloride</td>
      <td>124 (14.3)</td>
      </tr>
      <tr>
      <td>lactate</td>
      <td>124 (14.3)</td>
      </tr>
      <tr>
      <td>acetaminophen</td>
      <td>85 (9.8)</td>
      </tr>
      <tr>
      <td>ondansetron</td>
      <td>79 (9.1)</td>
      </tr>
      <tr>
      <td>sennosides, USP</td>
      <td>63 (7.2)</td>
      </tr>
      <tr>
      <td>oxycodone</td>
      <td>62 (7.1)</td>
      </tr>
      <tr>
      <td>folic acid</td>
      <td>60 (6.9)</td>
      </tr>
      <tr>
      <td>docusate</td>
      <td>57 (6.6)</td>
      </tr>
      <tr>
      <td>ketorolac</td>
      <td>54 (6.2)</td>
      </tr>
      <tr>
      <td>glucose</td>
      <td>53 (6.1)</td>
      </tr>
      <tr>
      <td>oxytocin</td>
      <td>47 (5.4)</td>
      </tr>
      <tr>
      <td>famotidine</td>
      <td>45 (5.2)</td>
      </tr>
      <tr>
      <td>simethicone</td>
      <td>43 (4.9)</td>
      </tr>
      <tr>
      <td>gabapentin</td>
      <td>25 (2.9)</td>
      </tr>
      <tr>
      <td>buprenorphine</td>
      <td>11 (1.3)</td>
      </tr>
</tbody>
</table>
</div>

<br>
