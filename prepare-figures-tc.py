#!/usr/bin/env python


import shutil
import sys
import re
from pathlib import Path
from zipfile import ZipFile


if __name__ == '__main__':

    counter = 1

    figsdir = Path("figs")
    figsdir.mkdir(exist_ok=True)

    with ZipFile("figs.zip", 'w') as zip_obj:

        for line in sys.stdin:
            m = re.match(r"(\\includegraphics(?:\[.*\])?){(.*?)}", line)
            if m:
                oldimg = Path(m.group(2))
                if not oldimg.exists():
                    raise Exception(f"the file {oldimg} does not exist")

                newimg = Path(f"f{counter:02}{oldimg.suffix}")
                counter += 1

                shutil.copy(oldimg, figsdir / newimg)
                zip_obj.write(oldimg, newimg.name)

                line = line.replace(m.group(0), f"{m.group(1)}{{{newimg}}}")
            print(line, end='')

