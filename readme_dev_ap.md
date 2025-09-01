## Add AP (Apte57) documentation. 08-31-2025
start with pdfs:
 ap1_bookmark.pdf, ap2_bookmark.pdf,  ap3_bookmark.pdf.
```
curl -o ap1_bookmark.pdf https://www.sanskrit-lexicon.uni-koeln.de/scans/APScan/2014_retired/downloads/ap1_bookmark.pdf

curl -o ap2_bookmark.pdf https://www.sanskrit-lexicon.uni-koeln.de/scans/APScan/2014_retired/downloads/ap2_bookmark.pdf

curl -o ap3_bookmark.pdf https://www.sanskrit-lexicon.uni-koeln.de/scans/APScan/2014_retired/downloads/ap3_bookmark.pdf
```

Open one of these in Adobe Acrobat
Open bookmarks
Select sequence of page bookmarks
Choose 'print pages' and name appropriately.

The resulting frontmatter and appendices pdfs are named:

```
ap57_vol1_frontmatter.pdf
ap57_vol2_preface.pdf
ap57_vol3_preface.pdf
ap57_vol3_apdxA_prosody.pdf
ap57_vol3_apdxB_writers.pdf
ap57_vol3_apdxC_geography.pdf
ap57_vol3_apdxD_lexicons.pdf
ap57_vol3_apdxE_maxims.pdf
ap57_vol3_apdxF_grammaticalTerms.pdf
```
## copy the above 9 files to source/_static folder

## steps in local installation

* Add 'ap line' to source/dictionaries/index.rst
* new file source/dictionaries/ap.rst -- edit as appropriate
* activate virtual environment
  * source myenv/Scripts/activate
* update 'build' directory based on 'source' directory
  * csl-doc is current directory
  * sphinx-build -b html source build
* push to github  (git add, git push)
* deactivate  # the virtual enfironment
## steps in Cologne
* cd .../scans/csldev/csldoc
* git pull
