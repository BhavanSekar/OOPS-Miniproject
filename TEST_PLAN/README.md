# Test Plan

## High Level Test Plan

| Test ID |                 Description                |                    Exp I/P                    |          Exp O/P         | Actual O/P |    Type Of Test   |
|:-------:|:------------------------------------------:|:---------------------------------------------:|:------------------------:|:----------:|:-----------------:|
| H_01    |        Visualisation of images             |  Blur Image                                   | Sharp Image                   | Sharp Image(SUCCESS) | Requirement based |
| H_02    | Visualisation of graph plots               |  Blur Image(Dataset)                          | Plot                          | SUCCESS              | Scenario based    |
| H_01| Progression of training in output folder       |  Blur Image                                   | Image saved after every epoch | SUCCESS              | Scenario based    |


## Low level test plan


| Test ID |    Description    |                    Exp I/P                    |         Exp O/P         |    Actual O/P  |  Type Of Test  |
|:-------:|:-----------------:|:---------------------------------------------:|:-----------------------:|:--------------:|:--------------:|
| L_01    | Image resolution(I/P Layer) and output layer | 504 * 504 * 1 | 504 * 504 * 1 | 504 * 504 * 1(SUCCESS) | Requirement based |
| L_02    | Image resolution(I/P Layer) and output layer | 288 * 288 * 1 | 288 * 288 * 1 | 288 * 288 * 1(SUCCESS) | Requirement based |
| L_03    | Image resolution(I/P Layer) and output layer | 252 * 252 * 1 | 252 * 252 * 1 | 252 * 252 * 1(SUCCESS) | Requirement based |
| L_04    | Image resolution(I/P Layer) and output layer | 276 * 276 * 1 | 276 * 276 * 1 | 276 * 276 * 1(SUCCESS) | Requirement based |
| L_05    | Image resolution(I/P Layer) and output layer | 336 * 228 * 1 | 336 * 228 * 1 | 336 * 228 * 1(SUCCESS) | Requirement based |
