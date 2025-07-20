# File Based Data Processing Workflow

### Site Capture & BIDS Conversion

Data is collected from sites into LORIS (EEG, Axtivity, and GABI) or FIONA (for MRI and MRS). LORIS data is subsequently transferred directly into the central S3 main PR bucket, which subsequently is sourced for CBRAIN processing. MRI and MRS must first be converted to BIDS format and MRI data also undergoes extensive raw data QC ([see details](https://docs.hbcdstudy.org/latest/instruments/mri/qc/#raw-mr-data-qc)).

![](images/capture.svg)

\*<i>S3 Key</i>:   

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <tbody>
    <tr>
        <td></td>
        <td><strong>MRS BIDS</strong></td>
        <td><code>s3://midb-hbcd-main-pr-mrs/</code></td>
    </tr>
    <tr>
        <td></td>
        <td><strong>JCVI DICOMs</strong></td>
        <td><code>s3://midb-hbcd-ucsd-main-pr-dicoms/</code></td>
    </tr>
</tbody>
</table>