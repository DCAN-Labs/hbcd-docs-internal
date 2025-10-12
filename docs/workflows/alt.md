
  <span class="table-text">LORIS Ingestion of Re-Identified Derivatives</span>

<p>LORIS updates their database from <code>s3://midb-hbcd-main-pr/derivatives</code> by:</p>
<ol>
<li>Removing any database entries related to derivative outputs that no longer exist</li>
<li>Looking for cases where there are newer derivative outputs than what exists in LORIS records and replacing the old records with the new data</li>
<li>Adding in records for any new subjects/sessions</li>
</ol>


<a href=\"../data-proc-wf/#copy-to-release\" target=\"_top\"><i>Click for Details</i></a>

<a href=\"../data-proc-wf/#copy-to-release\" target=\"_top\"><i>Click for Details</i></a>