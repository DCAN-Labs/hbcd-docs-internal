# Web Development Workflow & Versioning

The repository for HBCD Docs is housed under the NBDC Data Hub organization ([https://github.com/nbdc-datahub](https://github.com/nbdc-datahub)) on GitHub, which is where the website repos as well as additional ABCD/ABCC- and HBCD-specific utilities are housed: [https://github.com/nbdc-datahub/hbcd-docs](https://github.com/nbdc-datahub/hbcd-docs)

## Active Development For Release 1.0

The branch `dev` is used for development purposes, where changes are made and then pushed to `main` to render on the public site once the content/changes are complete. This branch is not rendered on the public site (although it can be if needed). *This bare bones workflow allows for rapid, streamlined collaboration and development,* but has disadvantages over the ABCD workflow (see details at [end of page](#abcd-workflow))

## Development for Future Releases 

Content that is under development, but not to be included in the website until a future release, is currently being developed on a separate GitHub repository housed under the DCAN-Lab org: [https://github.com/DCAN-Labs/beta-repo](https://github.com/DCAN-Labs/beta-repo). This repository is rendered on a separate ReadtheDocs site here: [https://beta-repo.readthedocs.io/latest/](https://beta-repo.readthedocs.io/latest/). The website has a discrete name so that users won't accidentally stumble upon it when searching for HBCD and get confused. However, it is still public of course.

### Alternative Solution

An alternative solution is to create a new branch on the the public NBDC repo - [https://github.com/nbdc-datahub/hbcd-docs](https://github.com/nbdc-datahub/hbcd-docs) - called `1.1` for example, and render it so that it's accessible via the flyout menu in the bottom right-hand corner (see details on ReadtheDocs documentation [here](https://docs.readthedocs.com/platform/stable/flyout-menu.html#addons-flyout-menu)). The downside is that if users stumble upon it, it may confuse them, although we can just be sure to explain clearly on the landing page that it's dev content for future releases and shouldn't be referenced. 

## Versioning

- The base version numbers (e.g. `1.2` for a version number `1.2.3`) will always match the release - for example, for the interim release, the Docs version will be `1.1.0` when first published
- The third number (e.g. `3` for a version number `1.2.3`) will change whenever there’s a major content adjustment, including:
    - Addition of new information
    - Changes to existing information that changes the interpretation of the content 
    - Reorganization of the pages that leads to URL changes
- Changes that do not warrant a new version include styling and formatting updates that do not change the meaning/interpretation of the content

**NOTE:** The current version is `1.0.3`. This is due to the fact that the workflow designed by ABCD ([see details in next section](#abcd-workflow)) was being used at first, which automatically incremented the version after a small change was made. It's possible (though not good practice) to delete tags and release versions on GitHub, but the publication automatically made to Zenodo whenever a new version is tagged, is permanent.

## ABCD Workflow

The ABCD workflow for web dev is more complex, but may be good to employ in the future as the website expands:

- No active development is performed on the public repository
- Instead, a separate private repo is housed elsewhere (e.g. for HBCD it would be housed under the DCAN-Labs GitHub org). To push the content of the private repository to the public repository, you open a PR to merge your dev branch with `main`. They developed a utility using GitHub actions that then pushes these changes to the public repo housed on the NBDC GitHub org for rendering on the public site. This utility also automatically increments the version. 
- Prioritization of privacy for content under development and automation

### Comparison With HBCD Workflow

The advantage of the ABCD workflow is that it keeps more information strictly. The HBCD workflow allows for rapid collaboration and development suitable for the smaller scale of the HBCD Docs site, but is all fully public. It compensates for this by making certain information harder to find so as not to confuse the user, including:

- For [active development](#active-development-for-release-10), hosting a separate `dev` branch that is not rendered on the website, so content is only pushed to `main` when it's fully developed
- Hosting content to be added for future release (see [Development for Future Releases](#development-for-future-releases) above):
    - In an entirely separate repository rendered via a ReadtheDocs site with an obscure name
    - The repository mimics the structure of the main site where needed (eg has a "Study Instruments" section so that the content can be easily merged with the main site), but is otherwise entirely stripped of any content from the public site that isn't being used for development


### Additional ABCD Workflow Details

#### Deployment using [dsm-gha-release_repo](https://github.com/ucsd-dsm/dsm-gha-release_repo) utility 

The dsm-gha-release_repo utility makes creating a versioned release in the public repository a one-step process, using a manually triggered GitHub Action to automate the following steps:

- Squashes all commits to private repo into one 
- Push to the public repo hosted on the nbdc-datahub to create versioned release
- Automatically increments version number using major version string stored as an org variable 

#### HBCD Adaptation (for potential future use)

This utility has been adapted for HBCD in a forked repository, [DCAN-Labs/dsm-gha-release_repo](https://github.com/DCAN-Labs/dsm-gha-release_repo):

- [workflow.yml](https://github.com/DCAN-Labs/dsm-gha-release_repo/blob/main/.github/workflows/workflow.yml)
- DCAN-Labs/dsm-gha-release_re settings at bottom of page [here](https://github.com/DCAN-Labs/dsm-gha-release_repo/settings/actions) to make accessible to DCAN-Labs repos
- Addition of version variable and github token as variable and secret in repo settings [here](https://github.com/DCAN-Labs/hbcd-release-docs/settings/secrets/actions): `VAR_RELEASE_VERSION_MAJOR` value set to 1.0 - this defines the major version. minor version (e.g. 1.0.0) is what will be automatically incremented by github action
- The [private HBCD Docs repo](https://github.com/DCAN-Labs/hbcd-release-docs) hosted under DCAN-Labs org contains [`.github/workflows/copy_repo.yaml`](https://github.com/DCAN-Labs/hbcd-release-docs/blob/main/.github/workflows/copy_repo.yaml) file that automatically triggers this utility every time there is a push to `main`
    
