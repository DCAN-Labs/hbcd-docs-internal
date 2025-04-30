  - mermaid2:
      version: 10.0.2
      javascript: https://unpkg.com/mermaid@10.4.0/dist/mermaid.esm.min.mjs



      version: "11.6.0"
      arguments:
        startOnLoad: true
      javascript_url: https://cdn.jsdelivr.net/npm/mermaid@latest/dist/mermaid.min.js

plugins:
  - search
  - mermaid2:
      version: "11.6.0"
      arguments:
        startOnLoad: true
      javascript_url: https://cdn.jsdelivr.net/npm/mermaid@latest/dist/mermaid.min.js
  - git-revision-date-localized:
      type: date