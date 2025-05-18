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

document.addEventListener("DOMContentLoaded", function () {
    // Wait for Mermaid to finish rendering
    setTimeout(() => {
        const tooltipText = "Montreal Consortium for Innovation in Neuroinformatics";

        // Find the Mermaid node by label text
        const nodes = document.querySelectorAll('.mermaid g.node');
        nodes.forEach(node => {
            const textElements = node.querySelectorAll('tspan');
            textElements.forEach(t => {
                if (t.textContent.includes("MCIN Assoc Dir")) {
                    node.setAttribute("title", tooltipText);
                    node.style.cursor = "help";
                }
            });
        });
    }, 500); // Wait for render — adjust delay if needed
});

