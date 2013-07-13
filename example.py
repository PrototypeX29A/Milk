#!/usr/bin/python

from milk import FileDrop, SoxDrop

drum = FileDrop('3146__robbiesurp__TAMA_Steel6.wav')

drum_by24 = SoxDrop((drum, ), "trim 0 0:0:0.14")
drum_by8 = SoxDrop((drum, ), "trim 0 0:0:0.42")

triplet = SoxDrop((drum_by24, drum_by24, drum_by24), "")

ostinato = SoxDrop((drum_by8, triplet, drum_by8, triplet, drum_by8, drum_by8, drum_by8, triplet, drum_by8, triplet, triplet, triplet), "")

ostinato.play();

