#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import fontforge


def main(font_collection):
    for font in fontforge.fontsInFile(font_collection):
        f = fontforge.open("%s(%s)" % (font_collection, font))
        f.cidFlatten()
        f.generate("fonts/%s.ttf" % font)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("One ttc file one time.")
    main(sys.argv[1])
