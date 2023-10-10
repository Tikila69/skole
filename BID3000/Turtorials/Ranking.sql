SELECT ItemId, ItemBrand, ItemUnitPrice,
RANK() OVER ( ORDER BY ItemUnitPrice ) AS RankUnitPrice
FROM SSItem;

SELECT CustName, SUM(SalesDollar) AS SumSales,
RANK() OVER (ORDER BY SUM(SalesDollar) DESC) SalesRank
FROM SSSales, SSCustomer
WHERE SSSales.CustId = SSCustomer.CustId
GROUP BY CustName;


SELECT ItemBrand, AVG(SalesDollar) AS AvgSales,
	RANK() OVER (ORDER BY AVG(SalesDollar)DESC) AS AvgSalesRank
FROM SSSales, SSItem, SSTimeDim
WHERE SSSales.Itemid = SSItem.Itemid AND SSSales.TimeNo = SSTimeDim.TimeNo
	AND TimeYear BETWEEN 2014 AND 2015
GROUP BY ItemBrand






SELECT CustState, CustName, SUM(SalesDollar) AS SumSales,
	RANK() OVER (PARTITION BY CustState
				ORDER BY SUM(SalesDollar)DESC) AS SalesRank
FROM SSSales, SSCustomer
WHERE SSSales.CustId = SSCustomer.CustId
GROUP BY CustState, CustName
ORDER BY CustState


SELECT CustZip, SUM(SalesUnits) AS SumSalesUnits,
	RANK() OVER (ORDER BY SUM(SalesUnits)DESC) AS SURank,
	DENSE_RANK() OVER (ORDER BY SUM(SalesUnits)DESC) AS SUDensRank,
	NTILE(4) OVER (ORDER BY SUM(SalesUnits)DESC) AS SUTile,
	ROW_NUMBER() OVER (ORDER BY SUM(SalesUnits)DESC) AS SURowNum
FROM SSSales, SSCustomer
WHERE SSSales.Custid = SSCustomer.CustID
GROUP BY CustZip



SELECT ItemBrand, TimeYear, COUNT(SSSales.Itemid) AS CountSales,
	DENSE_RANK() OVER(PARTITION BY TimeYear
					ORDER BY COUNT(SSSales.Itemid)DESC) AS SalesDensRank
FROM SSSales, SSItem, SSTimeDim
WHERE SSSales.ItemID = SSItem.ItemID AND SSSales.TimeNo = SSTimeDim.TimeNo
GROUP By Itembrand, TimeYear
HAVING COUNT(SSSales.ItemID) > 5



SELECT ItemBrand, TimeMonth, SUM(SalesDollar) AS SUMSalesDollar,
	DENSE_RANK() OVER(PARTITION BY TimeMonth
					  ORDER BY SUM(SalesDollar)DESC) AS DRSalesDollar,
	RANK() OVER(PARTITION BY TimeMonth
				ORDER BY SUM(SalesDollar)DESC) AS RSalesDollar
FROM SSSales, SSTimeDim, SSItem
WHERE SSSales.TimeNo = SSTimeDim.TimeNo AND SSItem.ItemID = SSSales.ItemID AND TimeYear = 2014
GROUP BY ItemBrand, TimeMonth



