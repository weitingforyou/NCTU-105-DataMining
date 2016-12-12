#HW1_Decision Tree
預測角色是否死亡

##資料集
https://www.kaggle.com/mylesoneill/game-of-thrones <br>
第二份資料的character-deeaths.csv

其中三個欄位 Death Year , Book of Death , Death Chapter 取其中一個欄位當預測目標用即可 <br>
請將欄位的空值轉成0(代表存活)，有數值的轉成1(代表死亡)

##Steps

### 1.檔案處理
請先將資料隨機排序，可在excel上處理 <br>

### 2.在weka上的流程為:
http://www.cs.waikato.ac.nz/ml/weka/ <br>
(weka需要java) <br>
<br>
   (1)將資料處理(轉成0/1 ,或binary 的yes/no 等等) <br>
   (2)用weka讀取(如果換成0/1還需要處理 filter->unsupervised->attribute->NumericToNominal) <br>
   (3)選擇決策樹分類(資料集前75%是訓練集、後25%當測試集) <br>
   (4)結果 <br>

### 3.在python上的流程
http://scikit-learn.org/stable/modules/tree.html <br>
(scikit-learn上的決策樹教學) <br>
<br>
   (1)將資料讀取進來(可用pandas套件) <br>
   (2)將資料處理(請用程式碼處理) <br>
     2-1把空值以0替代 <br>
     2-2Death Year , Book of Death , Death Chapter三者取一個，將有數值的轉成1 <br>
     2-3將Allegiances底下的家族轉成dummy的特徵(底下有幾種分類就會變成幾個特徵，值是0或1，本來的資料集就會再增加好幾十種特徵) <br>
   (3)使用python 中scikit-learn上的decision tree(前75%是訓練集、後25%當測試集,可以先試著將網頁範例(iris)跑出來在使用這次作業的資料集) <br>
   (4)計算Precision Rate , Recall Rate , Accuracy <br>
   (5)產出決策樹的圖 <br>
      p.s 記得限制樹的深度，以免結果無法顯示 <br>
