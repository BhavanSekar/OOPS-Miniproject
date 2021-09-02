# Deblurring of images using SRCNN( Super resolution Convolutional neural networks)


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


