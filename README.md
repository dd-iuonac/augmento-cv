Augmentation system for CV ML algorithms.

Prerequisites:
- python and opencv installed on local computer,
- a Test directory containing 5 images with various content (e.g. saved from web) of the size 640 x 480.
Specification:
Using Python and OpenCV write a program that:
- Allows user to select a directory on local disk. (e.g. using tkinter library)
- Read all .jpg images from this directory and, for each of them, apply a set of predefined augmentation algorithms with a set of predefined parameters. (e.g. Rotation with +15 degree).
- The augmentation algorithms and corresponding parameters to be applied will be loaded when the program starts from a configuration file (plain text, xml etc.)
- The results of augmentation process will be saved on a new directory (output dir), having the same name with the original one plus the "_aug" suffix.
- Each augmented image will be saved in the output dir having the name of augmentation algorithm as suffix followed by an incremental number starting with "_1". 

Obs: the supported augmentation methods will be implemented during weeks 1-6.

Input/output example:

Config file content  (plain file example):
Rotation 15
Tint red20

Test dir:
i1.jpg, i2.jpg, i3.jpg, car.jpg, i5.jpg

Test_aug dir:
i1_Rotation_1.jpg, i2_Rotation_2.jpg, i3_Rotation_3.jpg, car_Rotation_4.jpg, i5_Rotation_5.jpg, i1_Tint_6.jpg, i2_Tint_7.jpg, i3_Tint_8.jpg, car_Tint_9.jpg, i5_Tint_10.jpg