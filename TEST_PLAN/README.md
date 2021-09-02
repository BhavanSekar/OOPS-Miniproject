# Test Plan

## High Level Test Plan

| Test ID |                 Description                |                    Exp I/P                    |          Exp O/P         | Actual O/P |    Type Of Test   |
|:-------:|:------------------------------------------:|:---------------------------------------------:|:------------------------:|:----------:|:-----------------:|
| H_01    |        Visualisation of images             |  System setup                                 | System setup successful  | SUCCESS    | Requirement based |
| H_02    | Visualisation of graph plots | Application opens on system                   | Execution of application | SUCCESS    | Scenario based    |
| H_01| Progression of training in output folder | Login is required | Main Menu<br>1.Add Books<br>2.Search Books<br>3.View Books<br>4.Delete Book<br> 5.Update Password<br>0.EXIT| PASS | Scenario based|
| H_05    | Close Application                          | Integer '0' from the user  | Application gets closed  | Exit the program-SUCCESS    | Scenario based    |


## Low level test plan


| Test ID |    Description    |                    Exp I/P                    |         Exp O/P         |    Actual O/P  |  Type Of Test  |
|:-------:|:-----------------:|:---------------------------------------------:|:-----------------------:|:--------------:|:--------------:|
| L_01    | Image resolution(I/P Layer) and output layer | 504 * 504 * 1 | 504 * 504 * 1 | 504 * 504 * 1 | Requirement based |
| L_02    | Image resolution(I/P Layer) and output layer | 288 * 288 * 1 | 288 * 288 * 1 | 288 * 288 * 1 | Requirement based |
| L_03    | Image resolution(I/P Layer) and output layer | 252 * 252 * 1 | 252 * 252 * 1 | 252 * 252 * 1 | Requirement based |
| L_04    | Image resolution(I/P Layer) and output layer | 276 * 276 * 1 | 276 * 276 * 1 | 276 * 276 * 1 | Requirement based |
| L_05    | Image resolution(I/P Layer) and output layer | 336 * 228 * 1 | 336 * 228 * 1 | 336 * 228 * 1 | Requirement based |
