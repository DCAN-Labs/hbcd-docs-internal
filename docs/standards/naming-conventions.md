<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

# LORIS Naming Conventions

Table Naming conventions as they appear in Lasso are documented on the HBCD Release Data Docs site under [Metadata & Naming Conventions](https://docs.hbcdstudy.org/latest/access/metadata/) > [Naming Conventions](https://docs.hbcdstudy.org/latest/access/metadata/#naming-conventions).

## Domain

Differences in the `domain` values in LORIS (vs Lasso as outlined [here](https://docs.hbcdstudy.org/latest/access/metadata/#domain-source)) include:

 - Additional domain `sens` for 'Biosensor' tables (note: `sens` does not have an equivalent NBDC data dictionary domain)
 - For MRI data, `mri` is used in place of `img` within LORIS

## Source

As outlined in the Release Docs site, the `source` naming convention component corresponds with `source` in the NBDC Data Dictionary (e.g. child vs birth parent). Note that `source` may either indicates the subject (who the protocol element is about) or, in some cases, the respondent (who completed the assessment). For example, `mri_ra_prep` refers to MRI-related data entered by a research assistant (RA), representing procedural details as opposed to direct input from a child or caregiver.

Additional potential values for `source`, other than `bm` (Biological Mother), `cg` (Caregiver), and `ch` (Child) shown [here](https://docs.hbcdstudy.org/latest/access/metadata/#domain-source), `source` values in LORIS and/or for variables to be included in a future release include:

 - `si` - Sibling
 - `te` - Teacher
 - `cl` - Clinician
 - `ra` - RA (research assistant)
 - `ld` - Linked Data
 - `fd` - Family Data


### Correspondence to JSON Metadata

The `domain` and `source` are also included in the JSON metadata and are typically derived from the corresponding sections of the instrument name. However, in some cases, data are collected directly into fields or tables that do not follow the standard naming convention. In those instances, the domain and source values are added later during the Data Release process.

**This applies to:**

 - BioSpecimens
 - Imaging file based data & derivatives
 - Some session-level elements (e.g. `informantID`)
 - Participant-level data
