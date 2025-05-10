// Mermaid diagram formatting
document.addEventListener("DOMContentLoaded", function () {
  // Open external links in new tab
  const externalLinks = document.querySelectorAll('a[href^="http"]:not([target="_blank"])');
  externalLinks.forEach(function(link) {
    link.setAttribute('target', '_blank'); 
    link.setAttribute('rel', 'noopener noreferrer');
  });

  // Initialize Mermaid with ELK layout
  mermaid.initialize({
    startOnLoad: true,
    theme: "default",
    flowchart: {
      defaultRenderer: "elk"
    },
    layout: "elk"
  });
});
