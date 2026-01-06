<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<thead>
  <tr>
    <th>Phase</th>
    <th>Step #</th>
    <th>High Level Org in HBCD</th>
    <th>Responsible Group</th>
    <th>Activity</th>
    <th>Inputs</th>
    <th>Outputs / Artifacts</th>
    <th>System of Record</th>
  </tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Instrument coding Specification</td>
<td style="word-wrap: break-word; white-space: normal;">1a</td>
<td style="word-wrap: break-word; white-space: normal;">HCAC</td>
<td style="word-wrap: break-word; white-space: normal;">Work Group (WG)</td>
<td style="word-wrap: break-word; white-space: normal;">Provide instrument specifications and scoring requirements</td>
<td style="word-wrap: break-word; white-space: normal;">Email, PDF, scoring docs</td>
<td style="word-wrap: break-word; white-space: normal;">Instrument spec + scoring rules</td>
<td style="word-wrap: break-word; white-space: normal;">Confluence</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">HDCC-Biostats Authoring</td>
<td style="word-wrap: break-word; white-space: normal;">1b</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC-Biostats</td>
<td style="word-wrap: break-word; white-space: normal;">Receive instrument from WG; author scoring code and perform initial validation</td>
<td style="word-wrap: break-word; white-space: normal;">WG instrument specs</td>
<td style="word-wrap: break-word; white-space: normal;">Validated scoring code + example outputs</td>
<td style="word-wrap: break-word; white-space: normal;">Git (code) + Confluence</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Provenance Capture</td>
<td style="word-wrap: break-word; white-space: normal;">1c</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC-Biostats</td>
<td style="word-wrap: break-word; white-space: normal;">Store scoring code, examples, and validation notes</td>
<td style="word-wrap: break-word; white-space: normal;">Scoring code, test cases</td>
<td style="word-wrap: break-word; white-space: normal;">Versioned code + validation record</td>
<td style="word-wrap: break-word; white-space: normal;">Git + Confluence</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Instrument Build</td>
<td style="word-wrap: break-word; white-space: normal;">1d</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC-LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Implement instrument and scoring logic in data capture system</td>
<td style="word-wrap: break-word; white-space: normal;">Approved specs + scoring logic</td>
<td style="word-wrap: break-word; white-space: normal;">Coded instrument and scoring</td>
<td style="word-wrap: break-word; white-space: normal;">LORIS</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Instrument Code Validation (WG)</td>
<td style="word-wrap: break-word; white-space: normal;">1e</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC-Biostats</td>
<td style="word-wrap: break-word; white-space: normal;">Validate coded instrument and scoring implementation and put ticket into LORIS ticket centre</td>
<td style="word-wrap: break-word; white-space: normal;">LORIS instrument</td>
<td style="word-wrap: break-word; white-space: normal;">QC feedback / approval</td>
<td style="word-wrap: break-word; white-space: normal;">LORIS</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Formal Instrument Approval</td>
<td style="word-wrap: break-word; white-space: normal;">1g</td>
<td style="word-wrap: break-word; white-space: normal;">HCAC</td>
<td style="word-wrap: break-word; white-space: normal;">WG</td>
<td style="word-wrap: break-word; white-space: normal;">Final sign-off on coded instrument and put tickets into HDCC-QC Lasso Ticket Centre with any issues</td>
<td style="word-wrap: break-word; white-space: normal;">Instrument Validated by WG</td>
<td style="word-wrap: break-word; white-space: normal;">Instrument approval</td>
<td style="word-wrap: break-word; white-space: normal;">LORIS</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Approval Provenance</td>
<td style="word-wrap: break-word; white-space: normal;">1h</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC-WG Liason</td>
<td style="word-wrap: break-word; white-space: normal;">Publish signed approvals and version info</td>
<td style="word-wrap: break-word; white-space: normal;">WG + Biostats sign-off</td>
<td style="word-wrap: break-word; white-space: normal;">Immutable approval record</td>
<td style="word-wrap: break-word; white-space: normal;">Confluence</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Collection</td>
<td style="word-wrap: break-word; white-space: normal;">2</td>
<td style="word-wrap: break-word; white-space: normal;">HCAC</td>
<td style="word-wrap: break-word; white-space: normal;">HCAC: Site Staff</td>
<td style="word-wrap: break-word; white-space: normal;">Begin data collection using approved instrument</td>
<td style="word-wrap: break-word; white-space: normal;">Approved instrument</td>
<td style="word-wrap: break-word; white-space: normal;">Raw study data</td>
<td style="word-wrap: break-word; white-space: normal;">LORIS</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Ongoing QC &ndash; Data Availability</td>
<td style="word-wrap: break-word; white-space: normal;">3</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC-QC Lasso</td>
<td style="word-wrap: break-word; white-space: normal;">Data becomes available in ongoing QC environment</td>
<td style="word-wrap: break-word; white-space: normal;">Collected data</td>
<td style="word-wrap: break-word; white-space: normal;">QC-ready dataset</td>
<td style="word-wrap: break-word; white-space: normal;">Lasso Ongoing QC</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Continuous HDCC Biostats QC</td>
<td style="word-wrap: break-word; white-space: normal;">3b</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC-Biostats</td>
<td style="word-wrap: break-word; white-space: normal;">Run scheduled HDCC-Biostats QC scripts per instrument. Included in QC scripts will be HDCC-Biostats group running scoring algorithm over item level data and comparing to scored fields in Lasso and put tickets into HDCC-QC Lasso Ticket Centre with any issues. Dump run outputs into common repository.</td>
<td style="word-wrap: break-word; white-space: normal;">Live data</td>
<td style="word-wrap: break-word; white-space: normal;">QC metrics, flags, logs</td>
<td style="word-wrap: break-word; white-space: normal;">Git (code) + Lasso HDCC-QC</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Ongoing QC- WG Review (<a class="in-cell-link" href="https://hbcdstudy.atlassian.net/wiki/spaces/SOPS/overview#Work-Group-and-SME-SOP-V.9" target="_blank">see SME QC SOP</a>)</td>
<td style="word-wrap: break-word; white-space: normal;">3c</td>
<td style="word-wrap: break-word; white-space: normal;">HCAC</td>
<td style="word-wrap: break-word; white-space: normal;">Work Group (WG)</td>
<td style="word-wrap: break-word; white-space: normal;">Perform ongoing QC in Lasso and put tickets into HDCC-QC Lasso Ticket Centre with any issues</td>
<td style="word-wrap: break-word; white-space: normal;">QC datasets</td>
<td style="word-wrap: break-word; white-space: normal;">QC feedback</td>
<td style="word-wrap: break-word; white-space: normal;">Lasso HDCC-QC</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">HDCC ticket review and corrections</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC-LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">All issues are logged in Mondays and reviewed, managed, and corrected weekly at Monday Release Meeting with all release asociated staff</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC-QC tickets, WG, and HDCC inputs</td>
<td style="word-wrap: break-word; white-space: normal;">Corrected and closed tickets</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Pre-release - BR Data Available</td>
<td style="word-wrap: break-word; white-space: normal;">4a</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC-LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Prepare Beta Release (BR) and filtered datasets (validate against HDCC biostats Ongoing scoring) against gold standard (Dump run outputs into common repository put there by hdcc-biostats group)</td>
<td style="word-wrap: break-word; white-space: normal;">QC-reviewed data</td>
<td style="word-wrap: break-word; white-space: normal;">BR dataset</td>
<td style="word-wrap: break-word; white-space: normal;">Lasso HDCC-QC</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Pre-Release HDCC Biostats QC</td>
<td style="word-wrap: break-word; white-space: normal;">4c</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC-Biostats</td>
<td style="word-wrap: break-word; white-space: normal;">QC BR dataset and publish release-specific QC R scripts and put tickets into Git with any issues reported in HDCC-QC Lasso Ticket Centre</td>
<td style="word-wrap: break-word; white-space: normal;">BR dataset</td>
<td style="word-wrap: break-word; white-space: normal;">Release-tagged QC code</td>
<td style="word-wrap: break-word; white-space: normal;">Git (per-instrument folders)</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Pre-Release WG QC</td>
<td style="word-wrap: break-word; white-space: normal;">4d</td>
<td style="word-wrap: break-word; white-space: normal;">HCAC</td>
<td style="word-wrap: break-word; white-space: normal;">Work Group (WG)</td>
<td style="word-wrap: break-word; white-space: normal;">QC data in Pre-Release environment</td>
<td style="word-wrap: break-word; white-space: normal;">BR dataset</td>
<td style="word-wrap: break-word; white-space: normal;">Final QC feedback</td>
<td style="word-wrap: break-word; white-space: normal;">Lasso HDCC-QC</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Final Provenance Capture</td>
<td style="word-wrap: break-word; white-space: normal;">4e</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC</td>
<td style="word-wrap: break-word; white-space: normal;">HDCC-WG Liason</td>
<td style="word-wrap: break-word; white-space: normal;">Publish WG sign-off for BR</td>
<td style="word-wrap: break-word; white-space: normal;">Final approvals</td>
<td style="word-wrap: break-word; white-space: normal;">Release provenance record</td>
<td style="word-wrap: break-word; white-space: normal;">Confluence</td>
</tr>
</tbody>
</table>