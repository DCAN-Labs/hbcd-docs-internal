<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

# LORIS Naming Conventions

Table Naming conventions as they appear in Lasso are documented on the HBCD Release Data Docs site under [Metadata & Naming Conventions](https://docs.hbcdstudy.org/latest/access/metadata/) > [Naming Conventions](https://docs.hbcdstudy.org/latest/access/metadata/#naming-conventions).

## Domain

 - For MRI data, `mri` is used in place of `img` within LORIS

## Correspondence to JSON Metadata

The `domain` and `source` are also included in the JSON metadata and are typically derived from the corresponding sections of the instrument name. However, in some cases, data are collected directly into fields or tables that do not follow the standard naming convention. In those instances, the domain and source values are added later during the Data Release process.

**This applies to:**

 - BioSpecimens
 - Imaging file based data & derivatives
 - Some session-level elements (e.g. `informantID`)
 - Participant-level data

## REDCap Naming Convention: `_i_` 

Table names in Lasso using single ( `_` ) and double ( `__` ) underscores, as explained [here](https://docs.hbcdstudy.org/latest/access/metadata/#double-underscores). Note that, in REDCap, `_i_` is used in place of double underscores and used in LORIS for instruments and fieldnames to denote hierarchies for scales and sub-scales in the instrument name and field counters. For the Data Release, the `i` is removed, resulting in `__` instead of `_i_`. This naming convention conversion occurs when the data is transferred from LORIS to Lasso.
