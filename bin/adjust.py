#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import fontforge
import psMat

GLYPH_UNICODES = [
    0xE0A0,
    0xE0A1,
    0xE0A2,
    0xE0B0,
    0xE0B1,
    0xE0B2,
    0xE0B3
]

def main(font):
    f = fontforge.open(font)

    x_ratio = 1.0
    y_ratio = 1.0
    x_diff = 0
    y_diff = 0

    scale = psMat.scale(x_ratio, y_ratio)
    translate = psMat.translate(x_diff, y_diff)
    transform = psMat.compose(scale, translate)
    for code in GLYPH_UNICODES:
        f[code].transform(transform)

    fontname = font.replace("Source Han Code JP", "SourceHanCodeJP")
    f.generate(fontname)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("One ttf file one time.")
    main(sys.argv[1])
