# Deblurring of images using SRCNN( Super resolution Convolutional neural networks)

[![Pylint](https://github.com/BhavanSekar/OOPS-Miniproject/actions/workflows/pylint.yml/badge.svg)](https://github.com/BhavanSekar/OOPS-Miniproject/actions/workflows/pylint.yml)
[![Buildandtest](https://github.com/BhavanSekar/OOPS-Miniproject/actions/workflows/Buildandtest.yml/badge.svg)](https://github.com/BhavanSekar/OOPS-Miniproject/actions/workflows/Buildandtest.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/a94bf2202d2b445b852ee2d6022dc4cd)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BhavanSekar/OOPS-Miniproject&amp;utm_campaign=Badge_Grade)
[![Code quality](https://www.code-inspector.com/project/27227/score/svg)
[![Code Grade](https://www.code-inspector.com/project/27227/status/svg)

| Folder           | Description                                   |
|------------------|-----------------------------------------------|
| 1_Requirements   | Documents detailing requirements and features |
| 2_Design         | Documents specifying design details           |
| 3_Implementation | All implemented code                          |
| 4_Test_plan      | Documents with test plans                     |
| 5_Testing        | Documents for testing code                    |

## Project Structure for implementation

Download the input files from Dataset folder.
Download the codes in src from Implementation.


├───input

│   ├───bicubic_2x

│   ├───Set5

│   ├───T91

│   ├───train_mscale.h5

├───outputs

├───src

│   ├───srcnn.py

│   ├───test.py

│   ├───train.py

## How to run

Download the makefile, Variables.c file and the main.c file and run the following command in the bash(cmd or terminal with gcc installed). Ensure that the variables.c file is added to the path.

**For windows**

```bash
cd ".../src" [Move to SRC directory]
python train.py
python test.py
```

**For Linux**

```bash
cd ".../src" [Move to SRC directory]
python train.py
python test.py
```


