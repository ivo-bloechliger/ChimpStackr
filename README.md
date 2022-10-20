# ChimpStackr
![GitHub all releases](https://img.shields.io/github/downloads/noah-peeters/ChimpStackr/total) ![GitHub release (latest by date)](https://img.shields.io/github/downloads/noah-peeters/ChimpStackr/latest/total) [![chimpstackr](https://snapcraft.io/chimpstackr/badge.svg)](https://snapcraft.io/chimpstackr) ![GitHub repo size](https://img.shields.io/github/repo-size/noah-peeters/ChimpStackr) ![GitHub](https://img.shields.io/github/license/noah-peeters/ChimpStackr) ![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/noah-peeters/ChimpStackr/latest)

<p align="center">
  <img src="https://user-images.githubusercontent.com/17707805/196983883-84ec7174-74d3-4833-b9f6-16b84e19280d.png" width="300"/>
</p>

Open source multi-platform program for focus stacking many images.

View the [wiki](https://github.com/noah-peeters/ChimpStackr/wiki/Basic-usage) for instructions.

Focus stacking is often a necessity when working with high-magnification pictures...
Chimpstackr implements the laplacian pyramid fusion algorithm (see: [Sources](#sources))
## Table of contents
* [Installation](#installation)
* [Gallery](#gallery)
* [Build from source](#build-from-source-code)
* [Sources](#sources)
## Installation
Installation instructions per supported platform.
### Windows
* Download the latest release from GitHub, and run the ".exe" file
### Linux
* Snapcraft: https://snapcraft.io/chimpstackr

## Gallery
Work in progress...

## Build from source code
* Clone repository
* Install python requirements:  ``pip install -r requirements.txt``
* Run file ``src/run.py`` to start the program
### Local build  (snapcraft)
* Run build: ```snapcraft```
* Install local snap: ```snap install *.snap --dangerous --devmode```

## Sources
* Focus stacking algorithm (slightly adapted) implemented from:
Wang, W., & Chang, F. (2011b). A Multi-focus Image Fusion Method Based on Laplacian Pyramid. _Journal of Computers_, _6_(12).

* DFT image alignment algorithm adapted from: https://github.com/matejak/imreg_dft
