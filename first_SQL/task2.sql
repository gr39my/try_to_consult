-- ■課題2
-- shop_purchasesテーブルを利用して、ユーザー(user_id)が初回に購入する商品(product_id)として
-- 人気が高い順に3つのproduct_idと商品名をセットでお答えください。またそれぞれの商品は何名が初回購入しているでしょうか。
-- 同一のユーザーはpurchase_idの番号が小さい方が最初に購入されたと考えます。

with tmp as(
SELECT user_id
, MIN(purchase_id) as purchase_id
FROM shop_purchases
GROUP BY user_id
)
SELECT b.product_id
, b.prod_name as 商品名
, COUNT(*) as 初回購入人数
FROM tmp,shop_purchases a
	LEFT JOIN products_master b
	ON a.product_id = b.product_id
WHERE tmp.purchase_id = a.purchase_id
GROUP BY b.product_id,b.prod_name
ORDER BY 初回購入人数 DESC;


/*
初回購入する商品として人気が高い順に3つのproduct_idと商品名：
    ①product_id:10 , 商品名:ブラウス 長袖  
    ②product_id:11 , 商品名:Tシャツ（デザイン） 半袖 , 
    ③product_id:13 , 商品名:Tシャツ（キャラクター） 半袖
それぞれの商品の初回購入者数：① 69名, ② 66名, ③ 65名

*/

