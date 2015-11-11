#!/usr/bin/env python

import bob.bio.base
import bob.db.avspoof_btas2015


# directory where the wave files are stored
avspoof_input_dir = "/idiap/project/lobi/AVSpoof/data/"
avspoof_input_ext = ".wav"



database = bob.bio.base.database.DatabaseBob(
    database = bob.db.avspoof_btas2015.Database(
        original_directory = avspoof_input_dir,
        original_extension =avspoof_input_ext,
    ),
    name = 'avspoof',
    protocol = '.',
)
