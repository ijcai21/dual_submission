# Anonymous double submissions check

This repo contains scripts to help the detection of double submissions.

Two different detections:
- Title match: both conferences make hash signatures of all the titles. Then hash signatures can be compared to find exact matches

- PDF content word frequency: both conferences compute the word frequency histograms for every paper. Then histograms can be compared.

Tested in ubuntu 20.04

## Installation

Requirements:
 * python3 and virtualenv
 * lib-poppler-cpp-dev


Create virtual environment

```virtualenv env ```

Activate virtualenv

```source env/bin/activate```

Install python libraries

```pip install -r requirements.txt```

When finish the execution you can leave virtualenv with

```deactivate```

## Script 1: Title hash

  1. Add titles to input.txt, one title per line.
  2. run script ```python hash.py```

Hashes will be stored in output.txt

## Script 2: Word histogram

  1. Place the PDFs in the pdf directory
  2. run script ```python get_histograms.py```

Histograms will be stored in the csv directory

Few notes on the word histogram
*  Authors are not included in the word count. In fact the script ingores all words until it finds the word "Abstract"
*  Words with less than 5 characters or only appearing once in the text are ignored.