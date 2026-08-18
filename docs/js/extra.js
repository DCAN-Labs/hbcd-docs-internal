// Collapsible content - new logic
function toggleNotificationCollapse(banner) {
  const content = banner.nextElementSibling;
  if (content && content.classList.contains('open-collapsible-content')) {
    content.classList.toggle('open');
  }
}

// Collapsed content: toggles open class AND rotate class to ON when arrow is clicked to expand/collapse the section.
function toggleCollapse(element) {
  const collapsibleContent = element.nextElementSibling;
  const arrow = element.querySelector(['.arrow']);

  if (collapsibleContent.classList.contains('open')) {
    collapsibleContent.classList.remove('open');
    arrow.classList.remove('rotate');
  } else {
    collapsibleContent.classList.add('open');
    arrow.classList.add('rotate');
  }
}

// Utility function to expand a collapsible section by ID
function expandCollapsibleById(id) {
  const element = document.getElementById(id);
  
  if (element && (element.classList.contains('table-banner') ||
                  element.classList.contains('source-banner') ||
                  element.classList.contains('ingestion-banner') ||
                  element.classList.contains('preproc-banner') ||
                  element.classList.contains('proc-banner') ||
                  element.classList.contains('pre-release-banner'))) {
    const collapsibleContent = element.nextElementSibling;
    const arrow = element.querySelector(['.arrow']);

    if (collapsibleContent && !collapsibleContent.classList.contains('open')) {
      collapsibleContent.classList.add('open');
      if (arrow) arrow.classList.add('rotate');
    }
    element.scrollIntoView({ behavior: 'smooth' });
  }
}

// Auto-expand banners if navigated via external link
document.addEventListener('DOMContentLoaded', function () {
  const hash = window.location.hash.substring(1);
  if (hash) {
    expandCollapsibleById(hash);
  }
});


// Expand only collapsible sections with arrows that have the "open-arrow" class
document.addEventListener('DOMContentLoaded', function () {
  const openArrows = document.querySelectorAll('.open-arrow');

  openArrows.forEach(arrow => {
    arrow.classList.add('rotate');

    // Find the related collapsible content (assumes it is the next sibling or nearby)
    const content = arrow.closest('.collapsible-header')?.nextElementSibling;

    if (content && content.classList.contains('collapsible-content')) {
      content.classList.add('open');
    }
  });

  // Auto-expand specific banner if navigated via external link
  const hash = window.location.hash.substring(1);
  if (hash) {
    expandCollapsibleById(hash);
  }
});

// Listen for hash changes to expand collapsible sections
window.addEventListener('hashchange', () => {
  const hash = window.location.hash.substring(1);
  if (hash) {
    expandCollapsibleById(hash);
  }
});