# Marketing-Campaign-Customer-Analytics-SQL-Python
This portfolio project analyzes 2,240 customers across 29 original fields covering demographics, income, product spending, purchase channels, campaign history, recency and response.

### Headline findings
- Overall campaign response rate: **14.91%**.
- Average total spend: **605.80**; median: **396.00**, indicating a right-skewed customer-value distribution.
- Wines are the largest product-spend category, followed by meat.
- Store purchases are the largest purchase channel in this historical sample.
- Customers with 0–30 days recency show a **23.9%** response rate versus **5.6%** at 91–120 days.
- Customers with no previous campaign acceptances show an **8.2%** current response rate, compared with **31.1%** after one previous acceptance and **50.6%** after two. Higher-acceptance groups are small and should be treated cautiously.
- PhD customers average about **672.41** in spend and **21%** response, while Graduation averages about **619.90** and **13%**.
- Total spend is positively associated with income and purchase activity, especially catalog and store purchases.

## Business Objectives
1. Understand customer value and spending behavior.
2. Identify high-value customer segments.
3. Compare web, catalog and store purchasing behavior.
4. Measure historical campaign response.
5. Identify recency and prior-campaign patterns associated with response.
6. Convert findings into practical marketing actions.

## Data Preparation
The Python workflow:
- Reads the tab-delimited CSV.
- Converts `Dt_Customer` to datetime.
- Converts `Income` to numeric.
- Checks missing values and duplicates.
- Creates `TotalSpend`, `TotalPurchases`, `TotalCampaignAccepted`, `Children`, `Age_2014`, and `RecencyBand`.

### Data-quality observations
- 2,240 rows.
- 24 missing income values.
- 0 duplicate rows.
- `Year_Birth` contains an unusually old value (1893), so age analysis should include outlier treatment.
- Very small categories such as `Absurd`, `YOLO` and `Alone` should not drive strategic conclusions.

## Key Business Insights

### 1. Customer value is concentrated
Mean spend is 605.80 versus a median of 396.00. This suggests a smaller high-value customer group contributes disproportionately to spend.

**Action:** Build RFM/value tiers instead of treating all customers identically.

### 2. Wines and meat dominate product spend
Approximate recorded spend:
- Wines: 680,816
- Meat: 373,968
- Gold: 98,609
- Fish: 84,057
- Sweets: 60,621
- Fruits: 58,917

**Action:** Test wine/meat bundles and complementary cross-sell offers.

### 3. Store is the largest purchase channel
Purchase volume:
- Store: 12,970
- Web: 9,150
- Catalog: 5,963

**Action:** Preserve store conversion strength while testing digital journeys for customers with high online engagement.

### 4. Recency is strongly associated with response
Response:
- 0–30 days: 23.9%
- 31–60 days: 13.6%
- 61–90 days: 9.2%
- 91–120 days: 5.6%

**Action:** Use recency as a campaign-prioritization feature; use different reactivation messaging for lapsed customers.

### 5. Prior campaign acceptance is a useful propensity signal
Current response rises sharply with the number of previous campaign acceptances. The highest groups are small, so estimates are unstable.

**Action:** Include prior campaign engagement in propensity models and validate out-of-sample.

### 6. Customer segments differ in value
PhD customers have higher average spend and response than the larger Graduation group. Basic customers have much lower spend and response, but the group is small.

**Action:** Test segment-specific offers rather than relying on a single campaign message.

### 7. Household composition is associated with spend
Customers with no children in the `Kidhome` field have materially higher average spend than customers with one or two children.

**Action:** Include household structure as a segmentation feature alongside income and recency.

## Analytical Caveats
- Historical correlation does not establish causation.
- Previous campaign acceptance can contain selection bias because prior targeting may not have been random.
- Small demographic groups can produce unstable rates.
- Missing income needs explicit handling in production models.
- Revalidate the findings on current data before operational use.

## Key business findings
- 2,240 customers and 29 original columns.
- Overall campaign response rate: 14.91%.
- Average customer spend: 605.80; median: 396.00, showing a right-skewed customer-value distribution.
- Wines are the largest spending category at 680,816, followed by meat products at 373,968.
- Store purchases lead channel volume with 12,970 purchases, followed by web and catalog.
- Customers with 0–30 days recency have a 23.9% response rate, versus only 5.6% for customers at 91–120 days.
- Customers with no previous campaign acceptance have an 8.2% current response rate, compared with 31.1% after one previous acceptance and 50.6% after two.
- PhD customers average approximately 672.41 in spend versus 619.90 for Graduation customers.
- Income and purchasing activity have meaningful positive associations with total customer spend.

## Conclusion
The dataset supports a shift from broad marketing toward **value-, recency- and engagement-based segmentation**. The strongest practical signals are customer spend, purchase channel, recency and prior campaign engagement. The next maturity step is an RFM + propensity framework validated with out-of-sample data and controlled experimentation.
