# Data_augmentation
可進行圖片不同角度旋轉與水平翻轉，如果有給定標記座標即可計算旋轉後的位置，也能輸出成yolo所需格式並以txt做儲存。

<h3>需要參數:</h3>

 - image : 經讀入的圖片array。
 - angle : 旋轉角度。


 - <h4>可給也可以不給 : </h4>

   - point : 左上右下座標
      >一組 : point = [ [left_top_X,left_top_Y , right_down_X,right_down_Y] ]。
      <br>多組 : point = [ [left_top_X,left_top_Y , right_down_X,right_down_Y],
                      [left_top_X,left_top_Y , right_down_X,right_down_Y],
                      [left_top_X,left_top_Y , right_down_X,right_down_Y] ]。
   - keep_size : 圖片是否要超出邊界。

---

<h2>API</h2>

---
- <h4>ET -可以取得的資源</h4>

  - get_after_spin_image() : 取得旋轉後的圖片。
  - get_after_spin_point() : 取的旋轉後的座標。
  - get_yolo_point() : 取得將原始座標成yolo座標
  
- <h4>SAVE -可以儲存的資源</h4>

  - save_yolo_point_txt(save_path) : 將座標轉換成yolo座標後輸出txt至指定路徑
