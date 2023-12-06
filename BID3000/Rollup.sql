SELECT TimeYear, TimeMOnth, Sum(SalesDollar) AS SumSales
FROM SSSales, SSStore, SStimeDim
WHERE SSSales.StoreId = SSStore.StoreID
AND SSSales.TImeNo = SSTimeDim.TimeNo
AND(StoreNation = 'USA'
   OR StoreNation = 'Canada')
AND TimeYear = 2016
GROUP BY ROLLUP (TimeYear, TimeMonth)