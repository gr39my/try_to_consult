-- ■課題1
-- 商品毎の割引状況を把握したいです。
-- shop_purchasesの実売データ(sales_amount)における平均販売価格と、products_masterの定価(list_price)を比較し、
-- 最も割引率の高い商品の商品名とその割引率を求めてください。

SELECT products_master.prod_name
, sum("sales amount") as total_selling_price
, sum("quantity") as total_selling_quantity
, cast(sum("sales amount")as REAL)/sum("quantity") as average_selling_price
, max("list_price") as list_price
, (1 - (cast(sum("sales amount")as REAL) / sum("quantity") / max("list_price"))) * 100 as discount_rate
FROM public.shop_purchases
	LEFT JOIN public.products_master
	ON shop_purchases.product_id = products_master.product_id
GROUP BY products_master.prod_name
ORDER BY discount_rate DESC;


/*
最も割引率の高い商品名：Tシャツ（キャラクター・子供用） 長袖
上記の商品の割引率：7.579831932773107%
*/

