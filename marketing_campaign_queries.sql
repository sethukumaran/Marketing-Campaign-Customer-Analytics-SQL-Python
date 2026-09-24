-- Marketing Campaign Analysis | SQLite-compatible
-- Assumes a cleaned table named marketing_campaign with TotalSpend,
-- TotalPurchases and TotalCampaignAccepted derived during ingestion.

SELECT COUNT(*) AS customers,
       ROUND(AVG(Income),2) AS avg_income,
       ROUND(AVG(TotalSpend),2) AS avg_total_spend,
       ROUND(AVG(Response)*100,2) AS response_rate_pct,
       ROUND(AVG(Complain)*100,2) AS complaint_rate_pct
FROM marketing_campaign;

SELECT 'Wines' AS category, SUM(MntWines) AS spend FROM marketing_campaign
UNION ALL SELECT 'Fruits', SUM(MntFruits) FROM marketing_campaign
UNION ALL SELECT 'Meat', SUM(MntMeatProducts) FROM marketing_campaign
UNION ALL SELECT 'Fish', SUM(MntFishProducts) FROM marketing_campaign
UNION ALL SELECT 'Sweets', SUM(MntSweetProducts) FROM marketing_campaign
UNION ALL SELECT 'Gold', SUM(MntGoldProds) FROM marketing_campaign
ORDER BY spend DESC;

SELECT SUM(NumWebPurchases) AS web_purchases,
       SUM(NumCatalogPurchases) AS catalog_purchases,
       SUM(NumStorePurchases) AS store_purchases
FROM marketing_campaign;

SELECT Education, COUNT(*) AS customers,
       ROUND(AVG(Income),2) AS avg_income,
       ROUND(AVG(TotalSpend),2) AS avg_spend,
       ROUND(AVG(Response)*100,2) AS response_rate_pct
FROM marketing_campaign
GROUP BY Education ORDER BY avg_spend DESC;

SELECT (Kidhome + Teenhome) AS children, COUNT(*) AS customers,
       ROUND(AVG(TotalSpend),2) AS avg_spend,
       ROUND(AVG(Response)*100,2) AS response_rate_pct
FROM marketing_campaign
GROUP BY children ORDER BY children;

SELECT CASE WHEN Recency <= 30 THEN '0-30'
            WHEN Recency <= 60 THEN '31-60'
            WHEN Recency <= 90 THEN '61-90'
            ELSE '91-120' END AS recency_band,
       COUNT(*) AS customers,
       ROUND(AVG(TotalSpend),2) AS avg_spend,
       ROUND(AVG(Response)*100,2) AS response_rate_pct
FROM marketing_campaign
GROUP BY recency_band
ORDER BY MIN(Recency);

SELECT (AcceptedCmp1 + AcceptedCmp2 + AcceptedCmp3 + AcceptedCmp4 + AcceptedCmp5) AS prior_acceptances,
       COUNT(*) AS customers,
       ROUND(AVG(Response)*100,2) AS current_response_rate_pct,
       ROUND(AVG(TotalSpend),2) AS avg_spend
FROM marketing_campaign
GROUP BY prior_acceptances ORDER BY prior_acceptances;

SELECT ID, Income, Education, Marital_Status, Recency, TotalSpend, Response
FROM marketing_campaign ORDER BY TotalSpend DESC LIMIT 20;

SELECT NumWebVisitsMonth, COUNT(*) AS customers,
       ROUND(AVG(NumWebPurchases),2) AS avg_web_purchases,
       ROUND(AVG(Response)*100,2) AS response_rate_pct
FROM marketing_campaign
GROUP BY NumWebVisitsMonth ORDER BY NumWebVisitsMonth;

SELECT Education, COUNT(*) AS customers,
       ROUND(AVG(Complain)*100,2) AS complaint_rate_pct
FROM marketing_campaign
GROUP BY Education ORDER BY complaint_rate_pct DESC;
