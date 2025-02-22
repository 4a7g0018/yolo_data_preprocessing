import cv2
import math
import json
from Data_augmentation import Data_augmentation

JSON_PATH = 'resource/train.json'
# JSON_PATH = 'resource/test.json'
IMAGE_PATH = 'resource/train_data'
# IMAGE_PATH = 'resource/test_data'

BLACK_LIST = ["39120.png", "39449.png", "39458.png", "39459.png", "41944.png", "44861.png", "45193.png", "45195.png",
              "45488.png", "45784.png", "45787.png", "457887.png", "45819.png", "45824.png", "45828.png", "45846.png",
              "45847.png", "45848.png", "45850.png", "45851.png", "45852.png", "46030.png", "46652.png", "46940.png",
              "46982.png", "47010.png", "47012.png", "47013.png", "47014.png", "47017.png", "47020.png", "47021.png",
              "47196.png", "47263.png", "48908.png", "56590.png", "56687.png", "56688.png", "56689.png", "56700.png",
              "567880.png", "57467.png", "57741.png", "57876.png", "57881.png", "57882.png", "57883.png", "57891.png",
              "57895.png", "59227.png", "59442.png", "40050.png", "44864.png", "44865.png", "48872.png", "55840.png",
              "62061.png", "69916.png", "59623.png", "61912.png", "69154.png", "69156.png", "69491.png", "61692.png",
              "68882.png", "68883.png", "68884.png"]

TRAIN = ['36237.png', '36285.png', '36338.png', '36342.png', '36343.png', '36345.png', '39402.png', '39405.png',
         '39406.png', '39411.png', '39413.png', '39416.png', '39505.png', '39508.png', '39512.png', '39794.png',
         '39803.png', '40006.png', '40019.png', '40410.png', '40415.png', '40417.png', '40419.png', '40453.png',
         '40845.png', '40846.png', '40848.png', '41097.png', '41098.png', '41129.png', '41498.png', '41520.png',
         '41802.png', '41820.png', '41823.png', '41959.png', '41960.png', '48925.png', '48942.png', '48943.png',
         '45268.png', '45269.png', '45271.png', '45272.png', '45275.png', '45276.png', '45279.png', '45281.png',
         '45477.png', '45478.png', '45479.png', '45493.png', '45496.png', '45497.png', '45498.png', '45523.png',
         '45530.png', '45594.png', '45605.png', '45607.png', '45672.png', '45673.png', '45674.png', '45717.png',
         '45785.png', '45786.png', '45788.png', '45789.png', '45791.png', '45818.png', '45821.png', '45823.png',
         '45831.png', '45849.png', '45971.png', '45988.png', '45994.png', '46028.png', '46029.png', '46031.png',
         '46032.png', '46035.png', '46036.png', '46037.png', '46038.png', '46039.png', '46040.png', '46042.png',
         '46047.png', '46048.png', '46362.png', '46912.png', '46984.png', '46985.png', '47210.png', '48839.png',
         '48844.png', '48845.png', '48873.png', '48883.png', '48884.png', '48887.png', '48889.png', '48890.png',
         '48896.png', '55801.png', '55816.png', '55997.png', '56003.png', '56575.png', '56736.png', '56737.png',
         '56740.png', '56749.png', '56776.png', '56784.png', '56787.png', '56788.png', '56793.png', '57550.png',
         '57601.png', '57711.png', '57720.png', '57729.png', '57745.png', '57794.png', '57838.png', '57846.png',
         '57850.png', '57852.png', '57873.png', '57878.png', '57900.png', '57901.png', '57903.png', '57905.png',
         '57918.png', '57926.png', '57933.png', '57936.png', '57941.png', '57942.png', '57943.png', '57945.png',
         '59055.png', '58879.png', '58881.png', '59059.png', '59361.png', '59422.png', '59424.png', '59425.png',
         '59506.png', '59655.png', '59658.png', '59726.png', '60220.png', '60224.png', '60738.png', '60753.png',
         '60758.png', '60759.png', '60761.png', '60763.png', '60768.png', '60779.png', '60780.png', '60902.png',
         '60904.png', '60997.png', '61698.png', '61701.png', '61702.png', '61704.png', '61706.png', '61707.png',
         '61708.png', '61709.png', '61992.png', '62039.png', '62043.png', '62049.png', '62050.png', '62069.png',
         '62079.png', '67514.png', '67515.png', '67516.png', '67548.png', '68874.png', '68875.png', '68885.png',
         '68886.png', '68888.png', '68889.png', '68890.png', '68892.png', '68914.png', '68917.png', '68923.png',
         '68928.png', '68931.png', '68942.png', '68943.png', '68944.png', '68945.png', '68946.png', '68947.png',
         '68948.png', '68996.png', '68997.png', '69024.png', '69127.png', '69133.png', '69136.png', '69377.png',
         '69396.png', '69397.png', '69399.png', '69401.png', '69402.png', '69430.png', '69514.png', '69546.png',
         '69547.png', '69548.png', '69549.png', '69553.png', '69559.png', '69579.png', '69581.png', '69582.png',
         '69584.png', '69841.png', '69914.png', '69915.png', '69917.png', '69936.png', '69937.png', '69938.png',
         '69939.png']

VAL = ['69940.png', '69942.png', '70015.png', '70022.png', '70058.png', '70316.png', '70339.png', '70394.png',
       '70397.png', '70417.png', '70424.png', '70449.png', '70460.png', '70488.png', '70920.png', '36365.png',
       '39408.png', '39412.png', '39414.png', '39748.png', '39790.png', '39994.png', '40111.png', '40421.png',
       '41128.png', '41165.png', '41518.png', '41798.png', '48932.png', '45208.png', '45495.png', '45529.png',
       '45606.png', '45742.png', '45783.png', '45817.png', '45820.png', '45822.png', '45827.png', '45926.png',
       '45969.png', '46041.png', '46938.png', '46986.png', '48868.png', '55908.png', '56582.png', '56779.png',
       '56790.png', '57885.png', '57897.png', '57906.png', '59355.png', '59420.png', '59421.png', '59573.png',
       '59576.png', '59665.png', '60752.png', '60755.png', '62055.png', '68891.png', '69139.png', '69400.png',
       '69568.png', '69580.png', '70019.png', '70020.png', '70326.png', '39511.png', '39796.png', '40367.png',
       '40412.png', '45816.png', '46939.png', '56618.png', '56752.png', '56796.png', '56806.png', '60766.png',
       '61695.png', '69544.png', '70016.png']

STYLE = [[0, True], [5, True], [-5, True], [10, True], [-10, True],
         [0, False], [5, False], [-5, False], [10, False], [-10, False]]


def main():
    for s in STYLE:
        angle = s[0]
        flip = s[1]
        # angle = 0
        # flip=True
        with open(JSON_PATH) as j:
            json_data = json.load(j)

            for content in json_data:
                # 確定這組中有骨裂
                if 'Fracture' in content['syms'] and content['file_name'] not in BLACK_LIST:

                    """
                    file_name   --圖片名稱
                    boxes       --標記位置(左上、右下)
                    syms        --標記類別(骨裂、氣胸...)
                    """

                    file_name = content['file_name']
                    boxes = content['boxes']
                    syms = content['syms']
                    fracture_index_list = []

                    if file_name in VAL:
                        SAVE_PATH = 'resource/val'
                    else:
                        SAVE_PATH = 'resource/train'

                    index_number = 0
                    # 紀錄骨裂在syms陣列中的index
                    for s in syms:
                        if s == 'Fracture':
                            fracture_index_list.append(index_number)
                        index_number += 1
                    print("file_name :", file_name, "  fracture_quantity :", len(fracture_index_list))
                    image = cv2.imread(IMAGE_PATH + '/' + file_name)

                    point = []
                    for indexs in fracture_index_list:
                        # left_up = (boxes[indexs][0], boxes[indexs][1])
                        # right_down = (boxes[indexs][2], boxes[indexs][3])
                        # color = (0, 0, 255)  # red
                        # thickness = 2  # 寬度 (-1 表示填滿)
                        # cv2.rectangle(image, left_up, right_down, color, thickness)
                        point.append([boxes[indexs][0], boxes[indexs][1], boxes[indexs][2], boxes[indexs][3]])
                    # cv2.imwrite('resource/ANS_{}'.format(file_name), image)

                    data_augmentation = Data_augmentation(image=image, angle=angle, point=point, flip_image=flip,
                                                          keep_size=False)
                    new_image = data_augmentation.get_after_spin_image()
                    new_points = data_augmentation.get_after_spin_point()
                    # for new_point in new_points:
                    #     left_up = (new_point[0], new_point[1])
                    #     right_down = (new_point[2], new_point[3])
                    #     color = (255, 0, 0)  # red
                    #     thickness = 2  # 寬度 (-1 表示填滿)
                    #     cv2.rectangle(new_image, left_up, right_down, color, thickness)

                    if angle < 0:
                        angle_name = "1" + str(angle)[1:]
                    else:
                        angle_name = str(angle)

                    if flip:
                        flip_name = "1"
                    else:
                        flip_name = "0"

                    cv2.imwrite(SAVE_PATH + '/{}{}{}'.format(angle_name, flip_name, file_name), new_image[:, :, 0])
                    # cv2.imwrite(SAVE_PATH + '/{}_{}_{}'.format(angle_name,flip_name, file_name), new_image)
                    txt_file_name = file_name.replace('.png', '')
                    data_augmentation.save_yolo_point_txt(
                        SAVE_PATH + '/{}{}{}'.format(angle_name, flip_name, txt_file_name))
                    # data_augmentation.save_yolo_point_txt(SAVE_PATH + '/{}_{}_{}'.format(angle_name,flip_name, txt_file_name))


if __name__ == '__main__':
    main()
