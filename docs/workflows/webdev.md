# Web Development Workflow & Versioning

The repository for HBCD Docs is housed under the NBDC Data Hub organization ([https://github.com/nbdc-datahub](https://github.com/nbdc-datahub)) on GitHub, which is where the website repos as well as additional ABCD/ABCC- and HBCD-specific utilities are housed: [https://github.com/nbdc-datahub/hbcd-docs](https://github.com/nbdc-datahub/hbcd-docs)

The branch `dev` is used for development purposes, where changes are made and then pushed to `main` to render on the public site once the content/changes are complete. This branch is not rendered on the public site (although it can be if needed).

### Versioning

- The base version numbers (e.g. `1.2` for a version number `1.2.3`) will always match the release - for example, for the interim release, the Docs version will be `1.1.0` when first published
- The third number (e.g. `3` for a version number `1.2.3`) will change whenever there’s a major content adjustment, including:
    - Addition of new information
    - Changes to existing information that changes the interpretation of the content 
    - Reorganization of the pages that leads to URL changes
- Changes that do not warrant a new version include styling and formatting updates that do not change the meaning/interpretation of the content

**NOTE:** The current version is `1.0.1`. This is due to the fact that the workflow designed by ABCD ([see details](#abcd-workflow)) was being used at first, which automatically incremented the version after a small change was made. It's possible (though not good practice) to delete tags and release versions on GitHub, but the publication automatically made to Zenodo whenever a new version is tagged, is permanent.

### Development for Future Releases 

Content that is under development, but not to be included in the website until a future release, is currently being developed on a separate GitHub repository housed under the DCAN-Lab org: [https://github.com/DCAN-Labs/beta-repo](https://github.com/DCAN-Labs/beta-repo). This repository is rendered on a separate ReadtheDocs site here: [https://beta-repo.readthedocs.io/latest/](https://beta-repo.readthedocs.io/latest/). The website has a discrete name so that users won't accidentally stumble upon it when searching for HBCD and get confused. However, it is still public of course.

**An alternative solution** is to create a new branch on the the public NBDC repo - [https://github.com/nbdc-datahub/hbcd-docs](https://github.com/nbdc-datahub/hbcd-docs) - called `1.1` for example, and render it so that it's accessible via the flyout menu in the bottom right-hand corner (see details on ReadtheDocs documentation [here](https://docs.readthedocs.com/platform/stable/flyout-menu.html#addons-flyout-menu)). The downside is that if users stumble upon it, it may confuse them, although we can just be sure to explain clearly on the landing page that it's dev content for future releases and shouldn't be referenced. 

### ABCD Workflow

The ABCD workflow for web dev is more complex, but may be good to employ in the future as the website expands:

- No active development is performed on the public repository
- Instead, a separate private repo is housed elsewhere (e.g. for HBCD it would be housed under the DCAN-Labs GitHub org). To push the content of the private repository to the public repository, you open a PR to merge your dev branch with `main`. They developed a utility using GitHub actions that then pushes these changes to the public repo housed on the NBDC GitHub org for rendering on the public site. This utility also automatically increments the version. 