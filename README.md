# prepare-publication-in-The-Cryosphere
Take a latex file as input and renumber+zip+copy the figures to upload to The Cryosphere.

The journal "The Cryosphere" requires the figures in Latex to be numbered f01.pdf, f02.pdf, ... If like me, you use sementic names for your figure file names, it is error prone and time consuming to rename the file names in the format required by The Cryopshere. This script reads from stdin a latex file, and write a new latex file. It also renames the figures and prepares a zip. The figures are also copied to the "figs/" directory.*

**Usage**:
```bash
./prepare-figures-tc.py <mypaper.tex >paper-for-tc.tex
```
