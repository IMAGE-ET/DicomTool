Python 2.7 DICOM Viewer
=======================

Python 2.7 DICOM Viewer is a python application for reading and annotating [DICOM](http://medical.nema.org/) files. 

The annotations created with the application can be saved to a JSON file for analysis.  

Requirements
------------
* numpy
* pydicom

Limitations
-----------
File export is limited to .ps files (ghostscript) for the time being.

Setting up the development environment
--------------------------------------
Install `conda-env` if you don't have it yet:
> conda install conda-env

Then `git clone` this repo, `cd` into the root, execute:
> conda env create

Running
-------
> activate dicomtool

> python Python2.7DicomViewer.py

Documentation
-------------
pydicom [documentation](https://pydicom.readthedocs.org/en/latest/).
