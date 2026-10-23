# Curation Procedures: Naming Conventions

Variable naming conventions for the release data are described on the HBCD Release Data Docs site under [Naming Conventions](https://docs.hbcdstudy.org/latest/standards/naming-conventions/). The naming convention is applied when data is transferred from LORIS to Lasso for release staging.

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
            <td><b>REDCap surveys</b></td>
            <td>
                Variables are named according to the conventions defined in REDCap and imported into LORIS via the REDCap Data Dictionary (DD). 
                These variable names generally match those in the REDCap DD, as LORIS instruments are created directly from that dictionary.
            </td>
        </tr>
        <tr>
            <td><b>LORIS native forms</b></td>
            <td>
                Initially coded using a flexible scheme, these instruments were later adapted to align with the REDCap naming convention. 
                Field and instrument names now generally follow the REDCap standard, with only minor deviations in some cases.
            </td>
        </tr>
       <tr>
            <td><b>LORIS Core Fields</b></td>
            <td>
                These fields are not associated with instruments and have their own pre-established names that may or may not be be adapted for the Data Release.
            </td>
        </tr>
        <tr>
            <td><b>Third-party instruments</b></td>
            <td>
                Collected externally and imported into LORIS via parsing scripts, these instruments function like LORIS native forms and 
                follow the same naming convention, typically adhering to the standardized REDCap scheme.
            </td>
        </tr>
        <tr>
            <td><b>Ripple / ETL fields</b></td>
            <td>
                Fields related to screening, demographics, or other study metadata, such as <i>Transition in Care (TIC)</i>, 
                <i>Alternate Caregiver (ACG)</i>, <i>Geocoding</i>, or <i>Study Navigator (SN)</i>, are collected or calculated in Ripple or via ETL then transferred to LORIS. These fields may not fully follow the REDCap naming convention and are usually stored at the 
                participant or session level.
            </td>
        </tr>
    </tbody>
</table>

## Naming Curation Procedures

When data are transferred to Lasso for release staging, the variable names are updated to follow the naming conventions. Table names in Lasso using single ( `_` ) and double ( `__` ) underscores. In REDCap and subsequently LORIS, `_i_` is used in place of double underscores for instruments and fieldnames to denote hierarchies for scales and sub-scales in the instrument name and field counters. For the Data Release, the `i` is removed, resulting in `__` instead of `_i_`. This naming convention conversion occurs when the data is transferred from LORIS to Lasso.

## Divergence from ABCD conventions

`scale` is one of the main naming components, separated by single underscore (<code>domain_source_table_<span style="color: teal;">{scale}</span>_item</code>). Not all measures have scales, making the number of naming components across variables inconsistent (i.e. a mixture of 4 or 5). This is inconsistent with [ABCD naming conventions](https://docs.abcdstudy.org/latest/documentation/curation/naming.html), which uses double underscores to make `scale` a subcomponent of `table`, resulting in 4 consistent main components across variables (`domain_source_table_item` if no scale present and `domain_source_table__scale_item` if scale is present).

## Minor Known Inconsistencies 
There are some table variables with minor inconsistencies that diverge from the naming convention. For instance, the following variables are missing double underscores required to nest item subcomponents consistently:

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



<!-- ### Correspondence to JSON Metadata

The `domain` and `source` are included in the JSON metadata and are typically derived from the corresponding sections of the instrument name. However, in some cases, data are collected directly into fields or tables that do not follow the standard naming convention. In those instances, the domain and source values are added later during the Data Release process.

**This applies to:**

 - BioSpecimens
 - Imaging file based data & derivatives
 - Some session-level elements (e.g. `informantID`)
 - Participant-level data -->