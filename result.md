# Tehran Taxi Price Comparison

## Project Overview and Result Description

### Project Overview

This project aimed to automate the process of collecting and analyzing taxi fare data from two ride-hailing services, Snapp and Tapsi, in Tehran, Iran. The goal was to monitor the fare prices for a specific route over a 24-hour period and understand how these prices correlate with traffic conditions.

**Route:**
- **From:** Azadi Square, Tehran
- **To:** Madar Square, Mirdamad Boulevard, Tehran

**Components:**
1. **Snapp Price Collection Script:** A Python script using Selenium to collect fare prices from Snapp.
2. **Tapsi Price Collection Script:** A Python script using Selenium to collect fare prices from Tapsi.
3. **Traffic Data Collection:** Collecting traffic data to analyze its impact on fare prices.
4. **Data Visualization:** Using matplotlib to visualize the fare prices and traffic conditions over time.

### Result Description

The provided plot compares the fare prices of Snapp and Tapsi with the traffic conditions over a 24-hour period. Here’s a detailed explanation of the results:

**1. Price Trends:**
- **Tapsi Price (Yellow Line):** The fare prices for Tapsi start at around 120,000 Tomans at noon and show considerable fluctuations throughout the day, peaking at approximately 160,000 Tomans in the late evening. Thereafter, prices gradually decrease and stabilize around 100,000 Tomans after midnight before dropping significantly in the early morning hours.
- **Snapp Price (Green Line):** The fare prices for Snapp start at around 90,000 Tomans at noon and remain relatively stable compared to Tapsi. There are some fluctuations, but the overall trend is less volatile, with prices generally staying between 80,000 to 100,000 Tomans.

**2. Traffic Conditions (Red Line):**
- The traffic data, measured in minutes, indicates the time taken to travel the route. Traffic peaks occur in the late evening, around 9 PM, with travel times reaching around 55 minutes. Traffic then decreases steadily, reaching its lowest point early in the morning, around 6 AM, before slightly increasing again as the day progresses.

**3. Correlation Analysis:**
- **Tapsi Prices:** There is a noticeable correlation between Tapsi prices and traffic conditions. As traffic peaks in the late evening, Tapsi prices also reach their highest. This suggests that Tapsi's pricing model is sensitive to traffic conditions, possibly incorporating dynamic pricing based on demand and traffic.
- **Snapp Prices:** Snapp prices, on the other hand, exhibit a weaker correlation with traffic conditions. Although there are some price increases during peak traffic times, the fluctuations are less pronounced compared to Tapsi. This indicates that Snapp may employ a more stable pricing model that is less influenced by traffic conditions.

### Key Insights:
1. **Dynamic Pricing in Tapsi:** Tapsi's fare prices are highly responsive to traffic conditions, resulting in significant price surges during peak traffic times.
2. **Stable Pricing in Snapp:** Snapp maintains a more consistent pricing strategy, with less volatility in fare prices irrespective of traffic conditions.
3. **Traffic Impact:** Traffic conditions have a direct impact on ride-hailing prices, with increased travel times correlating with higher fare prices, especially for Tapsi.

### Conclusion:
The project successfully collected and analyzed the fare prices of two major ride-hailing services in Tehran over a 24-hour period. The visualization highlights the differences in pricing strategies between Snapp and Tapsi, with Tapsi exhibiting a dynamic pricing model responsive to traffic conditions, while Snapp maintains a more stable fare structure. This analysis can be useful for understanding pricing behaviors and for users to plan their rides considering the traffic conditions and potential fare surges.

### Future Work:
1. **Extended Data Collection:** Collecting data over multiple days or weeks to identify longer-term trends and patterns.
2. **Additional Routes:** Analyzing fare prices and traffic conditions for different routes within the city.
3. **Incorporating Other Factors:** Considering additional variables such as weather conditions, special events, and holidays to further understand their impact on fare prices.

This comprehensive analysis provides valuable insights into the pricing dynamics of ride-hailing services in Tehran, aiding both users and service providers in making informed decisions.
