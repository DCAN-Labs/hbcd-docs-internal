
# 8



<p><strong>Process:</strong></p>
<ul>
  <li>For each subject/session/pipeline, compare <code>LastModified</code> (de-ID) and <code>cbrain-timestamp</code> (re-ID) values between:
    <ul>
      <li><code>s3://midb-hbcd-main-deid/derivatives</code></li>
      <li><code>s3://midb-hbcd-main-pr/reid_derivatives</code></li>
    </ul>
  </li>
  <li>If the number of files or timestamps differ, delete the corresponding re-identified data from <code>s3://midb-hbcd-main-pr</code>.</li>
</ul>

<p><strong>Contacts:</strong> Sriharshitha Anuganti, Monalisa Bilas, Erik Lee<br>
<strong>Frequency:</strong> Daily<br>
<strong>Inputs:</strong> <code>s3://midb-hbcd-main-pr/reid_derivatives</code> and <code>s3://midb-hbcd-main-deid/derivatives</code><br>
<strong>Outputs:</strong> None<br>
<strong>Notes:</strong> Ensures only synchronized derivatives remain in LORIS and prevents outdated or mismatched data from being used.</p>
