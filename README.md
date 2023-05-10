# https://github.com/WM-SEMERU/CodeSyntaxConcept

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

This file will become your README and also the index of your
documentation.

## Install

``` sh
pip install https://github.com/WM_SEMERU/CodeSyntaxConcept
```

### Setup

Step 1 - create a conda virtual Enviroment:

``` sh
conda create -n CodeSyntaxConcept
conda activate CodeSyntaxConcept
```

Step 2 - install nbdev

``` sh
conda install -c fastai nbdev
```

Step 3 - build the library

``` sh
nbdev_export
```

Step 4 - install dependencies

``` sh
pip install .
```

### Downloading the grammar

``` python
from CodeSyntaxConcept.loader import *

download_grammars(['python'])
```

    /scratch1/svelascodimate/CodeSyntaxConcept/CodeSyntaxConcept/grammars
