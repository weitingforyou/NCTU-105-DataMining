#HW4_DocumentClustering
將100篇新聞斷詞切字後去計算tf-idf值，並以該文章的tf-idf值當特徵值再以kmeans分群

##Steps
###1. 將資料讀取進來並以jieba(python,要額外下載)套件斷詞,也可以用ckip中文斷詞系統
* 因為中文不像英文每個詞已經分開好了，所以需要斷詞才能計算 tf-idf 值 <br>
* 例如：川普當選美國總統。 -> 川普 當選 美國 總統 。 <br> 
* 才能夠丟進sklearn的function計算 tf-idf 值 <br>
* 文章斷完詞之後會有很多沒有意義的文字(stopword停用詞)，將其刪除之後會計算 tf-idf 值會比較有意義，可以自行建立stopword表或用jieba的關鍵詞抽取 <br>

###2.用sklearn中的sklearn.feature_extraction.text去計算 tf-idf
* 先將文章的轉成向量在去計算 tf-idf (內建的function) <br> 
* 計算完後資料會變成很大的矩陣，每一列代表一篇文章，會有幾百欄，每個欄位都是一個詞，每個欄位的值代表那篇文章中那個詞的 tf-idf 值 <br> 

###3.每篇文章都會有幾百個特徵值，在進行kmeans分群
* 自行決定分幾群 <br> 
 <br>
 <br> 

依據每個人處理資料的方式不同，會有不同的答案。 <br> 
最後可以將分群出來的文章，同一群的放在一起，看是不是相似的文章。 <br> 
