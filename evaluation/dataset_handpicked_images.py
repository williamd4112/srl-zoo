# DEFINING A SET OF PREDEFINED IMAGES WE WANT ITS CORRESPONDING STATES FOR:
# they represent left up, right up, down right, down left corner and pushing button images (clockwise hand movement. Used by makeMovieFromPlotStates.py
REPRESENTATIVE_DIFFERENT_IMAGES = {
    COLORFUL75: ['colorful75/record_008/recorded_cameras_head_camera_2_image_compressed/frame00012.jpg',
                 'colorful75/record_008/recorded_cameras_head_camera_2_image_compressed/frame00087.jpg',
                 'colorful75/record_008/recorded_cameras_head_camera_2_image_compressed/frame00149.jpg',
                 'colorful75/record_008/recorded_cameras_head_camera_2_image_compressed/frame00011.jpg',
                 'colorful75/record_008/recorded_cameras_head_camera_2_image_compressed/frame00234.jpg'],
    COLORFUL: ['colorful75/record_008/recorded_cameras_head_camera_2_image_compressed/frame00012.jpg',
               'colorful75/record_008/recorded_cameras_head_camera_2_image_compressed/frame00087.jpg',
               'colorful75/record_008/recorded_cameras_head_camera_2_image_compressed/frame00149.jpg',
               'colorful75/record_008/recorded_cameras_head_camera_2_image_compressed/frame00011.jpg',
               'colorful75/record_008/recorded_cameras_head_camera_2_image_compressed/frame00234.jpg'],
    COMPLEX_DATA: ['complexData/record_008/recorded_cameras_head_camera_2_image_compressed/frame00001.jpg',
                   'complexData/record_008/recorded_cameras_head_camera_2_image_compressed/frame00070.jpg',
                   'complexData/record_008/recorded_cameras_head_camera_2_image_compressed/frame00103.jpg',
                   'complexData/record_008/recorded_cameras_head_camera_2_image_compressed/frame00176.jpg',
                   'complexData/record_008/recorded_cameras_head_camera_2_image_compressed/frame00109.jpg'],
    STATIC_BUTTON_SIMPLEST: ['staticButtonSimplest/record_043/recorded_camera_top/frame00000.jpg',
                             'staticButtonSimplest/record_043/recorded_camera_top/frame00020.jpg',
                             'staticButtonSimplest/record_043/recorded_camera_top/frame00071.jpg',
                             'staticButtonSimplest/record_043/recorded_camera_top/frame00028.jpg',
                             'staticButtonSimplest/record_043/recorded_camera_top/frame00050.jpg',
                             'staticButtonSimplest/record_043/recorded_camera_top/frame00009.jpg'],
    MOBILE_ROBOT: ['mobileRobot/record_008/recorded_camera_top/frame00001.jpg',
                   'mobileRobot/record_008/recorded_camera_top/frame00072.jpg',
                   'mobileRobot/record_008/recorded_camera_top/frame00063.jpg',
                   'mobileRobot/record_008/recorded_camera_top/frame00011.jpg',
                   'mobileRobot/record_008/recorded_camera_top/frame00048.jpg',
                   'mobileRobot/record_008/recorded_camera_top/frame00090.jpg']}
# NEW DATASET AFTER ICRA18
NONSTATIC_BUTTON = []

# 50 lines, 49 images (1 repeated by error) IMAGES TEST SET HANDPICKED TO SHOW VISUAL VARIABILITY
IMG_TEST_SET = {
    'staticButtonSimplest/record_000/recorded_cameras_head_camera_2_image_compressed/frame00000.jpg',
    'staticButtonSimplest/record_000/recorded_cameras_head_camera_2_image_compressed/frame00012.jpg',
    'staticButtonSimplest/record_000/recorded_cameras_head_camera_2_image_compressed/frame00015.jpg',
    'staticButtonSimplest/record_000/recorded_cameras_head_camera_2_image_compressed/frame00042.jpg',
    'staticButtonSimplest/record_000/recorded_cameras_head_camera_2_image_compressed/frame00039.jpg',
    'staticButtonSimplest/record_000/recorded_cameras_head_camera_2_image_compressed/frame00065.jpg',
    'staticButtonSimplest/record_000/recorded_cameras_head_camera_2_image_compressed/frame00048.jpg',
    'staticButtonSimplest/record_000/recorded_cameras_head_camera_2_image_compressed/frame00080.jpg',
    'staticButtonSimplest/record_000/recorded_cameras_head_camera_2_image_compressed/frame00004.jpg',
    'staticButtonSimplest/record_000/recorded_cameras_head_camera_2_image_compressed/frame00078.jpg',

    'staticButtonSimplest/record_008/recorded_cameras_head_camera_2_image_compressed/frame00056.jpg',
    'staticButtonSimplest/record_008/recorded_cameras_head_camera_2_image_compressed/frame00047.jpg',
    'staticButtonSimplest/record_008/recorded_cameras_head_camera_2_image_compressed/frame00033.jpg',
    'staticButtonSimplest/record_008/recorded_cameras_head_camera_2_image_compressed/frame00005.jpg',
    'staticButtonSimplest/record_008/recorded_cameras_head_camera_2_image_compressed/frame00026.jpg',
    'staticButtonSimplest/record_008/recorded_cameras_head_camera_2_image_compressed/frame00056.jpg',

    'staticButtonSimplest/record_011/recorded_cameras_head_camera_2_image_compressed/frame00003.jpg',
    'staticButtonSimplest/record_011/recorded_cameras_head_camera_2_image_compressed/frame00056.jpg',
    'staticButtonSimplest/record_011/recorded_cameras_head_camera_2_image_compressed/frame00063.jpg',
    'staticButtonSimplest/record_011/recorded_cameras_head_camera_2_image_compressed/frame00035.jpg',
    'staticButtonSimplest/record_011/recorded_cameras_head_camera_2_image_compressed/frame00015.jpg',

    'staticButtonSimplest/record_019/recorded_cameras_head_camera_2_image_compressed/frame00009.jpg',
    'staticButtonSimplest/record_019/recorded_cameras_head_camera_2_image_compressed/frame00074.jpg',
    'staticButtonSimplest/record_019/recorded_cameras_head_camera_2_image_compressed/frame00049.jpg',

    'staticButtonSimplest/record_022/recorded_cameras_head_camera_2_image_compressed/frame00039.jpg',
    'staticButtonSimplest/record_022/recorded_cameras_head_camera_2_image_compressed/frame00085.jpg',
    'staticButtonSimplest/record_022/recorded_cameras_head_camera_2_image_compressed/frame00000.jpg',

    'staticButtonSimplest/record_031/recorded_cameras_head_camera_2_image_compressed/frame00000.jpg',
    'staticButtonSimplest/record_031/recorded_cameras_head_camera_2_image_compressed/frame00007.jpg',
    'staticButtonSimplest/record_031/recorded_cameras_head_camera_2_image_compressed/frame00070.jpg',

    'staticButtonSimplest/record_036/recorded_cameras_head_camera_2_image_compressed/frame00085.jpg',
    'staticButtonSimplest/record_036/recorded_cameras_head_camera_2_image_compressed/frame00023.jpg',
    'staticButtonSimplest/record_036/recorded_cameras_head_camera_2_image_compressed/frame00036.jpg',

    'staticButtonSimplest/record_037/recorded_cameras_head_camera_2_image_compressed/frame00053.jpg',
    'staticButtonSimplest/record_037/recorded_cameras_head_camera_2_image_compressed/frame00083.jpg',
    'staticButtonSimplest/record_037/recorded_cameras_head_camera_2_image_compressed/frame00032.jpg',

    'staticButtonSimplest/record_040/recorded_cameras_head_camera_2_image_compressed/frame00045.jpg',
    'staticButtonSimplest/record_040/recorded_cameras_head_camera_2_image_compressed/frame00003.jpg',
    'staticButtonSimplest/record_040/recorded_cameras_head_camera_2_image_compressed/frame00080.jpg',

    'staticButtonSimplest/record_048/recorded_cameras_head_camera_2_image_compressed/frame00034.jpg',
    'staticButtonSimplest/record_048/recorded_cameras_head_camera_2_image_compressed/frame00059.jpg',
    'staticButtonSimplest/record_048/recorded_cameras_head_camera_2_image_compressed/frame00089.jpg',
    'staticButtonSimplest/record_048/recorded_cameras_head_camera_2_image_compressed/frame00030.jpg',

    'staticButtonSimplest/record_050/recorded_cameras_head_camera_2_image_compressed/frame00064.jpg',
    'staticButtonSimplest/record_050/recorded_cameras_head_camera_2_image_compressed/frame00019.jpg',
    'staticButtonSimplest/record_050/recorded_cameras_head_camera_2_image_compressed/frame00008.jpg',

    'staticButtonSimplest/record_052/recorded_cameras_head_camera_2_image_compressed/frame00000.jpg',
    'staticButtonSimplest/record_052/recorded_cameras_head_camera_2_image_compressed/frame00008.jpg',
    'staticButtonSimplest/record_052/recorded_cameras_head_camera_2_image_compressed/frame00068.jpg',
    'staticButtonSimplest/record_052/recorded_cameras_head_camera_2_image_compressed/frame00025.jpg'}
# print(len(IMG_TEST_SET))

# 50 unique images
COMPLEX_TEST_SET = {
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00030.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00003.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00021.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00025.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00014.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00027.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00034.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00016.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00001.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00026.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00015.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00011.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00047.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00020.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00012.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00029.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00045.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00049.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00039.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00038.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00032.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00028.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00037.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00005.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00004.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00040.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00017.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00008.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00006.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00031.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00035.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00042.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00000.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00036.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00002.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00044.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00018.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00041.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00013.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00033.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00048.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00009.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00024.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00010.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00022.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00043.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00007.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00023.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00019.jpg',
    'complexData/record_025/recorded_cameras_head_camera_2_image_compressed/frame00046.jpg'
}
# print(len(COMPLEX_TEST_SET))


# 56 Images
ROBOT_TEST_SET = {
    'mobileRobot/record_005/recorded_camera_top/frame00001.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00002.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00003.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00004.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00005.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00006.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00007.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00008.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00009.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00010.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00011.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00012.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00013.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00014.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00015.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00016.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00017.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00018.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00019.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00020.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00021.jpg',
    'mobileRobot/record_005/recorded_camera_top/frame00022.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00048.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00049.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00050.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00051.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00052.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00053.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00054.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00055.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00056.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00057.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00058.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00059.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00060.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00061.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00062.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00063.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00064.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00065.jpg',
    'mobileRobot/record_000/recorded_camera_top/frame00066.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00010.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00011.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00012.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00013.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00014.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00015.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00016.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00017.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00018.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00019.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00020.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00021.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00022.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00023.jpg',
    'mobileRobot/record_004/recorded_camera_top/frame00024.jpg'
}

# 50 Images: NOTE: IMPORTANT: RECORD_150 is a special one created with multi colors domain randomization WITHIN the same sequence (other sequences are not)
# in order to have a varied dataset in the test set.
COLORFUL_TEST_SET = {
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00030.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00003.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00021.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00025.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00014.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00027.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00034.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00016.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00001.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00026.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00015.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00011.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00047.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00020.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00012.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00029.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00045.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00049.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00039.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00038.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00032.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00028.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00037.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00005.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00004.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00040.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00017.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00008.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00006.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00031.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00035.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00042.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00000.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00036.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00002.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00044.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00018.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00041.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00013.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00033.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00048.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00009.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00024.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00010.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00022.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00043.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00007.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00023.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00019.jpg',
    'colorful/record_150/recorded_cameras_head_camera_2_image_compressed/frame00046.jpg'
}

COLORFUL75_TEST_SET = {
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00030.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00003.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00021.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00025.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00014.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00027.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00034.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00016.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00001.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00026.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00015.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00011.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00047.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00020.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00012.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00029.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00045.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00049.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00039.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00038.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00032.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00028.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00037.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00005.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00004.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00040.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00017.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00008.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00006.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00031.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00035.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00042.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00000.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00036.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00002.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00044.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00018.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00041.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00013.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00033.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00048.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00009.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00024.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00010.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00022.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00043.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00007.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00023.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00019.jpg',
    'colorful75/record_150/recorded_cameras_head_camera_2_image_compressed/frame00046.jpg'
}

NONSTATIC_BUTTON_TEST_SET = {
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00030.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00003.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00021.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00025.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00014.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00027.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00034.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00016.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00001.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00026.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00015.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00011.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00047.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00020.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00012.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00029.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00045.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00049.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00039.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00038.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00032.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00028.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00037.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00005.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00004.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00040.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00017.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00008.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00006.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00031.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00035.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00042.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00000.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00036.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00002.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00044.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00018.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00041.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00013.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00033.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00048.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00009.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00024.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00010.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00022.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00043.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00007.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00023.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00019.jpg',
    'nonStaticButton/record_025/recorded_cameras_head_camera_2_image_compressed/frame00046.jpg'
}
