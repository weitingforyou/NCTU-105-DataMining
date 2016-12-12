#HW3_Spark_Decision Tree
連線至國家高速網路中心的運算資源 <br>
利用Spark 進行作業一 的決策樹分類法(分散式版本) <br>
 
##1.連線至運算資源
請使用ssh連線軟體(例:putty) <br>
操作請參考 https://www.gitbook.com/book/ogre0403/nchc-braavos-user-guide/details <br>
 
##2.修改密碼
登入自己的帳號後，可以利用passwd指令修改密碼，請務必記住自己的密碼，登入錯誤超過一定次數IP會被國網中心封鎖而無法連線。
 
 
##3.處理資料並上傳至HDFS
 (1) 使用作業一同一份資料集，處理方式相同    <br> 
    i.把空值以0替代     <br>
    ii.Death Year , Book of Death , Death Chapter三者取一個，將有數值的轉成1     <br>
    iii.將Allegiances欄位的文字資料轉成dummy的特徵，以1或0表達   <br>
  <br>
 (2) 國網中心教學
 
 
###4.編寫／修改程式碼
資料集前75%是訓練集、後25%當測試集 <br>
可透過google 搜尋 spark 決策樹 教學，選擇適合自己的教學文章  <br>
ex. http://hadoopspark.blogspot.tw/2016/04/spark-mllib.html <br>
 
###5.執行指令，利用spark進行運算
國網中心教學 <br>
 
 
###6.目標
 (1) 產出預測結果 <br>
 (2) 計算accuracy, recall, precision <br>
