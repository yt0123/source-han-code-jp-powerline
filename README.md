# The Font Adpating Powerline to Source Han Code JP

### Dependencies

- fontforge

For Installation on OS X
```
brew install fontforge --with-python
```

### Usage

1. To split True-Type-Collectoin to True-Type-Font
```
bin/ttc2ttf SourceHanCodeJP.ttc
```

2. To adapt Powerline to True-Type-Font
```
fontforge -lang=py -script ./fontpatcher/scripts/powerline-fontpatcher ./fonts/Source\ Han\ Code\ JP\ {Font Type}.ttf
```

3. To fixed some glyphs
```
bin/adjust Source\ Han\ Code\ JP\ {Font Type}\ for \Powerline.ttf
```
