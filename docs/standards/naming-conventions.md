<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

# Naming Conventions

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
            <td><b>REDCap surveys</b></td>
            <td style="word-wrap: break-word; white-space: normal;">
                Variables are named according to the conventions defined in REDCap and imported into LORIS via the REDCap Data Dictionary (DD). 
                These variable names generally match those in the REDCap DD, as LORIS instruments are created directly from that dictionary.
            </td>
        </tr>
        <tr>
            <td><b>LORIS native forms</b></td>
            <td style="word-wrap: break-word; white-space: normal;">
                Initially coded using a flexible scheme, these instruments were later adapted to align with the REDCap naming convention. 
                Field and instrument names now generally follow the REDCap standard, with only minor deviations in some cases.
            </td>
        </tr>
       <tr>
            <td><b>LORIS Core Fields</b></td>
            <td style="word-wrap: break-word; white-space: normal;">
                These fields are not associated with instruments and have their own pre-established names that may or may not be be adapted for the Data Release.
            </td>
        </tr>
        <tr>
            <td><b>Third-party instruments</b></td>
            <td style="word-wrap: break-word; white-space: normal;">
                Collected externally and imported into LORIS via parsing scripts, these instruments function like LORIS native forms and 
                follow the same naming convention, typically adhering to the standardized REDCap scheme.
            </td>
        </tr>
        <tr>
            <td><b>Ripple / ETL fields</b></td>
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

### Update JSON Metadata

The `domain` and `source` are included in the JSON metadata and are typically derived from the corresponding sections of the instrument name. However, in some cases, data are collected directly into fields or tables that do not follow the standard naming convention. In those instances, the domain and source values are added later during the Data Release process.

**This applies to:**

 - BioSpecimens
 - Imaging file based data & derivatives
 - Some session-level elements (e.g. `informantID`)
 - Participant-level data

## REDCap Naming Convention: `_i_` 

Table names in Lasso using single ( `_` ) and double ( `__` ) underscores, as explained [here](https://docs.hbcdstudy.org/latest/access/metadata/#subcomponents). In REDCap and subsequently LORIS, `_i_` is used in place of double underscores for instruments and fieldnames to denote hierarchies for scales and sub-scales in the instrument name and field counters. For the Data Release, the `i` is removed, resulting in `__` instead of `_i_`. This naming convention conversion occurs when the data is transferred from LORIS to Lasso.
