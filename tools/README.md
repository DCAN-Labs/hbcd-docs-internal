# README - How to use autoparsing code for known issues and updates

## Step 1: download monday.com data

- select all items within the "RTDs" view on monday.com (https://ucsd-actri.monday.com/boards/6045591843/views/238003683) and export
- unclick "subitems" - we do not need these
- Next open in excel and strip out extra rows

## `parse-by-domain.py`
This updates the known issues page based on the `latest.xlsx` file



`make-release-notes.py` - for this one, define BR at top of script before running