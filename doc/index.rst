.. vim: set fileencoding=utf-8 :
.. Elie Khoury <Elie.Khoury@idiap.ch>
.. Fri 12 Jun 11:34:43 CEST 2015
.. Copyright (C) 2012-2015 Idiap Research Institute, Martigny, Switzerland



.. _xspear:


On the Vulnerability of Speaker Verification to Realistic Voice Spoofing
============================================================================

This package contains the experiments done in the following paper published at IEEE BTAS 2015::

    @inproceedings{avspoof,
      author = {Serife Kucur Erg\"unay and Elie Khoury and Alexandros Lazaridis and S\'ebastien Marcel },
      title = {On the Vulnerability of Speaker Verification to Realistic Voice Spoofing},
      booktitle = {IEEE Intl. Conf. on Biometrics: Theory, Applications and Systems (BTAS)},
      year = {2015},
      url = {https://publidiap.idiap.ch/downloads//papers/2015/KucurErgunay_IEEEBTAS_2015.pdf}
    }
    


I- Installation
--------------------

`xspear.btas2015`_ is based on the `BuildOut`_ python linking system. You only need to use buildout to bootstrap and have a working environment ready for
experiments::

  $ python bootstrap
  $ ./bin/buildout

This also requires that bob (>= 2.0) is installed.


II- Running experiments
------------------------

The above two commands will automatically download all desired packages from `pypi`_ and generate some scripts in the bin directory.
The interface for the AVspoof database (bob.db.avspoof_btas2015) will be downloaded automatically. You only need to download the AVspoof data (it is free of charge but requires to sign the EULA) ::

    $ https://www.idiap.ch/dataset/avspoof


Then to run the I-Vector scripts::

   $ bin/train_ivector.py -vv -d avspoof -p mod-4hz -e mfcc-60 -a ivec-avspoof -s ivec --groups world -g demanding 
   $ bin/verify.py -vv -d avspoof -p energy-2gauss -e mfcc-60 -a ivec-avspoof -s ivec --groups {dev,eval} -g demanding --skip-projector-training

To run the ISV scripts::

   $ bin/train_isv.py -vv -d avspoof -p mod-4hz -e mfcc-60 -a ivec-avspoof -s isv --groups world -g demanding
   $ bin/verify.py -vv -d avspoof -p energy-2gauss -e mfcc-60 -a ivec-avspoof -s isv --groups {dev,eval} -g demanding --skip-projector-training

Notice that the pre-processing of the training data is done using 4Hz modulation energy (mod-4hz) based voice activity detection (VAD) while the preprocessing of the DEV and EVAL set is done using Two-Gaussians energy-based VAD. 

To evaluate the two systems::

   $ bin/evaluate_vulnerability.py  -d /path/to/ivec/nonorm/scores-dev -e /path/to/ivec/nonorm/scores-eval
   $ bin/evaluate_vulnerability.py  -d /path/to/isv/nonorm/scores-dev -e /path/to/isv/nonorm/scores-eval 

For I-vectors, the expected output error rates are ::

  ---------------  male  -----------------
  ----------------------------------------------
  EER = 6.9%       Threshold = 43.973
  replay_phone1 : 29.1%
  replay_phone2 : 27.7%
  replay_laptop : 39.8%
  replay_laptop_HQ : 77.4%
  speech_synthesis_logical_access : 96.5%
  speech_synthesis_physical_access : 60.6%
  speech_synthesis_physical_access_HQ : 93.5%
  voice_conversion_logical_access : 92.6%
  voice_conversion_physical_access : 84.0%
  voice_conversion_physical_access_HQ : 88.8%

  ---------------  female  -----------------
  ----------------------------------------------
  EER = 17.5%      Threshold = 44.632
  replay_phone1 : 11.8%
  replay_phone2 : 11.1%
  replay_laptop : 32.2%
  replay_laptop_HQ : 69.4%
  speech_synthesis_logical_access : 81.5%
  speech_synthesis_physical_access : 69.5%
  speech_synthesis_physical_access_HQ : 83.7%
  voice_conversion_logical_access : 71.6%
  voice_conversion_physical_access : 75.8%
  voice_conversion_physical_access_HQ : 73.0%



For ISV, the expected output error rates are ::

  ---------------  male  -----------------
  ----------------------------------------------
  EER = 4.9%       Threshold = 0.597
  replay_phone1 : 19.2%
  replay_phone2 : 45.9%
  replay_laptop : 45.3%
  replay_laptop_HQ : 74.1%
  speech_synthesis_logical_access : 97.0%
  speech_synthesis_physical_access : 65.9%
  speech_synthesis_physical_access_HQ : 94.1%
  voice_conversion_logical_access : 93.4%
  voice_conversion_physical_access : 77.4%
  voice_conversion_physical_access_HQ : 89.3%

  ---------------  female  -----------------
  ----------------------------------------------
  EER = 10.6%      Threshold = 0.690
  replay_phone1 : 12.2%
  replay_phone2 : 23.1%
  replay_laptop : 35.7%
  replay_laptop_HQ : 68.5%
  speech_synthesis_logical_access : 83.5%
  speech_synthesis_physical_access : 67.9%
  speech_synthesis_physical_access_HQ : 83.7%
  voice_conversion_logical_access : 71.2%
  voice_conversion_physical_access : 50.7%
  voice_conversion_physical_access_HQ : 73.0%



.. _Bob: http://www.idiap.ch/software/bob
.. _local.bob.recipe: https://github.com/idiap/local.bob.recipe
.. _gridtk: https://pypi.python.org/pypi/gridtk
.. _BuildOut: http://www.buildout.org/
.. _NIST: http://www.nist.gov/itl/iad/ig/focs.cfm
.. _bob.db.verification.filelist: https://pypi.python.org/pypi/bob.db.verification.filelist
.. _xspear.btas2015: https://pypi.python.org/pypi/xspear.btas2015
.. _pypi: https://pypi.python.org/pypi
.. _Voxforge: http://www.voxforge.org/
.. _BANCA: http://www.ee.surrey.ac.uk/CVSSP/banca/
.. _TIMIT: http://www.ldc.upenn.edu/Catalog/catalogEntry.jsp?catalogId=LDC93S1
.. _logistic regression: http://en.wikipedia.org/wiki/Logistic_regression
.. _Spro: https://gforge.inria.fr/projects/spro
.. _HTK: http://htk.eng.cam.ac.uk/
.. _bob.db.mobio: https://pypi.python.org/pypi/bob.db.mobio
