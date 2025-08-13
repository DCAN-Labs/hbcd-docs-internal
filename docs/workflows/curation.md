# Curation Procedures: Naming Conventions

Variable naming conventions for the release data are described on the HBCD Release Data Docs site on the *Metadata & Naming Conventions* under [Naming Conventions](https://docs.hbcdstudy.org/latest/access/metadata/#naming-conventions). The naming convention is applied when data is transferred from LORIS to Lasso for release staging.

## Source Data Naming Schemes

Prior to staging in Lasso, instrument and fieldname conventions generally follow the REDCap naming standardization scheme, but may differ based on the source of the data, including:

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <thead>
        <tr>
            <th>Data Source</th>
            <th>Naming Convention Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="word-wrap: break-word; white-space: normal;"><b>REDCap surveys</b></td>
            <td style="word-wrap: break-word; white-space: normal;">
                Variables are named according to the conventions defined in REDCap and imported into LORIS via the REDCap Data Dictionary (DD). 
                These variable names generally match those in the REDCap DD, as LORIS instruments are created directly from that dictionary.
            </td>
        </tr>
        <tr>
            <td style="word-wrap: break-word; white-space: normal;"><b>LORIS native forms</b></td>
            <td style="word-wrap: break-word; white-space: normal;">
                Initially coded using a flexible scheme, these instruments were later adapted to align with the REDCap naming convention. 
                Field and instrument names now generally follow the REDCap standard, with only minor deviations in some cases.
            </td>
        </tr>
       <tr>
            <td style="word-wrap: break-word; white-space: normal;"><b>LORIS Core Fields</b></td>
            <td style="word-wrap: break-word; white-space: normal;">
                These fields are not associated with instruments and have their own pre-established names that may or may not be be adapted for the Data Release.
            </td>
        </tr>
        <tr>
            <td style="word-wrap: break-word; white-space: normal;"><b>Third-party instruments</b></td>
            <td style="word-wrap: break-word; white-space: normal;">
                Collected externally and imported into LORIS via parsing scripts, these instruments function like LORIS native forms and 
                follow the same naming convention, typically adhering to the standardized REDCap scheme.
            </td>
        </tr>
        <tr>
            <td style="word-wrap: break-word; white-space: normal;"><b>Ripple / ETL fields</b></td>
            <td style="word-wrap: break-word; white-space: normal;">
                Fields related to screening, demographics, or other study metadata, such as <i>Transition in Care (TIC)</i>, 
                <i>Alternate Caregiver (ACG)</i>, <i>Geocoding</i>, or <i>Study Navigator (SN)</i>, are collected or calculated in Ripple or via ETL then transferred to LORIS. These fields may not fully follow the REDCap naming convention and are usually stored at the 
                participant or session level.
            </td>
        </tr>
    </tbody>
</table>

## Curation Procedures

When data are transferred to Lasso for release staging, the variable names are updated to follow the naming conventions, mentioned above, described on the central HBCD Data Release Docs site [here](https://docs.hbcdstudy.org/latest/access/metadata/#naming-conventions). Here we describe certain aspects of how the naming conventions are instituted.

### REDCap Naming Convention: `_i_` 

Table names in Lasso using single ( `_` ) and double ( `__` ) underscores, as explained [here](https://docs.hbcdstudy.org/latest/access/metadata/#subcomponents). In REDCap and subsequently LORIS, `_i_` is used in place of double underscores for instruments and fieldnames to denote hierarchies for scales and sub-scales in the instrument name and field counters. For the Data Release, the `i` is removed, resulting in `__` instead of `_i_`. This naming convention conversion occurs when the data is transferred from LORIS to Lasso.

### Update JSON Metadata

The `domain` and `source` are included in the JSON metadata and are typically derived from the corresponding sections of the instrument name. However, in some cases, data are collected directly into fields or tables that do not follow the standard naming convention. In those instances, the domain and source values are added later during the Data Release process.

**This applies to:**

 - BioSpecimens
 - Imaging file based data & derivatives
 - Some session-level elements (e.g. `informantID`)
 - Participant-level data

## Known Issues 

Below is a running list of variables that need to be updated to conform to naming conventions aligned with ABCD (see outline of current naming standards [here](https://docs.hbcdstudy.org/latest/access/metadata/#naming-conventions)). Note that variable names are fairly internally consistent within tables (as they are often dictated by the conventions of the source platform), so the issues and examples below will generally apply to all of the variable names within a given instrument (which should make implementing changes towards standardization a more straightforward process). 

See [this spreadsheet](https://docs.google.com/spreadsheets/d/1AM7BJiKpZIDdcCFdkZnFg4jr6ZN48ZPtbFMevfNrPWo/edit?usp=sharing) for additional notes and details.

### Issue 1: Scale should be a subcomponent of table

As described [here](https://docs.hbcdstudy.org/latest/access/metadata/#naming-conventions), `scale` is currently included in the Release 1.0 variables as a main naming component (separated by single underscores): 

<p style="font-size: 1.2em; font-weight: bold; padding: 10px;" align="center">
<code>domain_source_table_<span style="color: teal;">{scale}</span>_item</code>
</p>

This perhaps follows this [REDCap standardization documentation](https://docs.google.com/document/d/1_xj8TPDRmb5-fQAQ3KZW87yzft-bA5Kt8HLNwMwm_MA/edit?tab=t.0#heading=h.6j8c7yy6p6t4). However, it makes the number of naming components across variables inconsistent (i.e. a mixture of 4 or 5), because not all variables have scales. It is also inconsistent with [ABCD naming conventions](https://docs.abcdstudy.org/latest/documentation/curation/naming.html), which uses double underscores to make `scale` a subcomponent of `table`, resulting in 4 consistent main components across variables:

<p style="font-size: 1.2em; font-weight: bold; padding: 10px;" align="center">
<code>domain_source_table_item</code>
</p>

A rough estimate from a simple parsing script shows the majority of variables in R1.0 currently follow the convention that includes `scale` as a main component (3531 vs. 965). Below are impacted instruments with examples variables and fixes:

<table class="compact-table">
<thead>
<tr>
<th style="width: 10%">Domain</th>
<th style="width: 10%;">Table</th>
<th style="width: 20%">Table Name</th>
<th style="width: 20%">Example Variable</th>
<th style="width: 10%">Example Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">BCGI</td>
<td style="word-wrap: break-word; white-space: normal;">IBQ-R (VSF)+BI</td>
<td style="word-wrap: break-word; white-space: normal;">mh_cg_ibqr</td>
<td style="word-wrap: break-word; white-space: normal;">mh_cg_ibqr_efrt_011</td>
<td style="word-wrap: break-word; white-space: normal;">__efrt</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">NCL</td>
<td style="word-wrap: break-word; white-space: normal;">SPM-2</td>
<td style="word-wrap: break-word; white-space: normal;">ncl_cg_spm2__inf</td>
<td style="word-wrap: break-word; white-space: normal;">ncl_cg_spm2__inf_soc_001</td>
<td style="word-wrap: break-word; white-space: normal;">__soc</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">PH</td>
<td style="word-wrap: break-word; white-space: normal;">Growth</td>
<td style="word-wrap: break-word; white-space: normal;">ph_ch_anthro</td>
<td style="word-wrap: break-word; white-space: normal;">ph_ch_anthro_head_001__01</td>
<td style="word-wrap: break-word; white-space: normal;">__head</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">PEX</td>
<td style="word-wrap: break-word; white-space: normal;">ALL preg health tables, eg Chronic conditions:</td>
<td style="word-wrap: break-word; white-space: normal;">pex_bm_health_preg__chroncond</td>
<td style="word-wrap: break-word; white-space: normal;">pex_bm_health_preg__chroncond_001___1</td>
<td style="word-wrap: break-word; white-space: normal;">__preg</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">PEX</td>
<td style="word-wrap: break-word; white-space: normal;">FAM MH</td>
<td style="word-wrap: break-word; white-space: normal;">pex_bm_psych</td>
<td style="word-wrap: break-word; white-space: normal;">pex_bm_psych_bf_001</td>
<td style="word-wrap: break-word; white-space: normal;">__bf</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">PEX</td>
<td style="word-wrap: break-word; white-space: normal;">ASSISTV1/2/3</td>
<td style="word-wrap: break-word; white-space: normal;">pex_bm_assistv1</td>
<td style="word-wrap: break-word; white-space: normal;">pex_bm_assistv1_lt__use_001</td>
<td style="word-wrap: break-word; white-space: normal;">__lt</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">SED</td>
<td style="word-wrap: break-word; white-space: normal;">BFY</td>
<td style="word-wrap: break-word; white-space: normal;">sed_bm_bfy</td>
<td style="word-wrap: break-word; white-space: normal;">sed_bm_bfy_econstr_008</td>
<td style="word-wrap: break-word; white-space: normal;">__econstr</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">SED</td>
<td style="word-wrap: break-word; white-space: normal;">Demographics</td>
<td style="word-wrap: break-word; white-space: normal;">sed_bm_demo</td>
<td style="word-wrap: break-word; white-space: normal;">sed_bm_demo_herit_002__06___2</td>
<td style="word-wrap: break-word; white-space: normal;">__herit</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">SED</td>
<td style="word-wrap: break-word; white-space: normal;">PROMIS</td>
<td style="word-wrap: break-word; white-space: normal;">sed_bm_strsup</td>
<td style="word-wrap: break-word; white-space: normal;">sed_bm_strsup_socspprt_001</td>
<td style="word-wrap: break-word; white-space: normal;">__socspprt</td>
</tr>
</tbody>
</table>

<br>

### Issue 2: Scale should be a subcomponent of table (*Issue 1*) + Add double underscores for item components

The following are table variables that have `scale` as a separate main component and also require additional double underscores in order to nest the item subcomponents:

<table class="compact-table">
<thead>
<tr>
<th style="width: 10%">Domain</th>
<th style="width: 10%;">Table</th>
<th style="width: 20%">Table Name</th>
<th style="width: 20%">Example Variable</th>
<th style="width: 10%">Example Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>NT</td>
<td>Infant Questionnaire</td>
<td>nt_ch_sens__qtn_1</td>
<td>nt_ch_sens__qtn_1_beh_002</td>
<td>__1__</td>
</tr>
<tr>
<td>PEX</td>
<td>APA 1/2</td>
<td>pex_bm_apa</td>
<td>pex_bm_apa_1_depr_001</td>
<td>__1__</td>
</tr>
<tr>
<td>PEX</td>
<td>TLFB</td>
<td>pex_ch_tlfb</td>
<td>pex_ch_tlfb_alc_wk_01</td>
<td>__alc_wk__</td>
</tr>
<tr>
<td>Biospec</td>
<td>Nails</td>
<td>bio_bm_biosample_nails_results</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Biospec</td>
<td>Nails</td>
<td>bio_bm_biosample_nails_type</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Biospec</td>
<td>Urine</td>
<td>bio_bm_biosample_urine</td>
<td>bio_bm_biosample_urine_bio_c_pcp_u</td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>

<br>

### Issue 3: Admin and summary score variables - Replace frequent single underscores 

Admin and summary score variables often have single underscores that should be replaced by double underscores, e.g., `date_taken`, `candidate_age`, `gestational_age`, `adjusted_age`, `summary_score`, `total_score`, etc. See [HBCD Docs](https://docs.hbcdstudy.org/latest/access/metadata/#administrative-summary-score-variables) for additional details.
