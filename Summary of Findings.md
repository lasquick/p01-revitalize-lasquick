# Summary of Findings

### Summary of National Poverty and Inequality Findings

1.	County poverty rates in 2018: In 2018, the 10 counties with the highest poverty rates were located primarily in South Dakota and southern states, including Mississippi, Louisiana, and Alabama. Todd County, SD, had the highest poverty rate (55.10%).

Top 10 Counties with the Highest Poverty Rates
  1.	Todd County, South Dakota             	55.10
  2.	Jefferson County, Mississippi         	49.72
  3.	Oglala Lakota County, South Dakota    	49.32
  4.	East Carroll Parish, Louisiana        	48.63
  5.	Mellette County, South Dakota         	48.32
  6.	Jackson County, South Dakota          	47.74
  7.	Corson County, South Dakota           	44.25
  8.	Claiborne County, Mississippi         	44.04
  9.	Holmes County, Mississippi            	43.58
  10.	Perry County, Alabama                 	41.75

The difference in poverty rates between the highest and tenth highest counties, 13.35%, indicates that these top ten counties may be significant outliers from the rest of the county poverty rates. The analysis also indicates that the total population for each of the top ten counties is fairly small (range of 2055 to 18,075). These small county population sizes are common for rural areas, but the small sample size does indicate that (1) a relatively small number of residents experiencing poverty can contribute to very large poverty rates, and extreme differences in county population size make it difficult to reliably compare county poverty rates across the nation.


2.	National spatial analysis of county poverty rates: Mapping county poverty rates using distribution categories shows clear geographic trends in poverty experiences. Geographic regions that have long been plagued with high poverty rates continue to have much higher rates compared to the national county average. In particular, the Mississippi Delta, Cotton Belt, Western Appalachia, and Southwestern and Great Plains tribal communities have outsized poverty rates. Overall poverty rates are below average in the mid-Atlantic metropolitan area, and the Northern and Central Great Plains are speckled with counties with poverty rates much lower than average.

Overall, this data visualization hides the communities where large numbers of people experiencing poverty are offset by highly populated, affluent areas. Finally, on this map, many communities with lower populations may appear to have significantly better or worse poverty conditions compared to counties with larger populations and more economic diversity to modulate poverty rates.


3.	National comparison of poverty rate changes from 2012 to 2018: Overall, the percentage point change in county poverty rates between 2012 and 2018 ranges from -21.32 to 22.48 percent. The top 10 counties that saw the largest percentage point increases are mostly located in southern states (Georgia, Texas, Alabama, Kentucky, Mississippi), but the county with the largest increase is located in South Dakota.

Top 10 counties by increase in percent poverty:
  1. Jackson County, South Dakota     22.478046
  2. Clinch County, Georgia           17.611842
  3. Cottle County, Texas             16.067033
  4. Jim Hogg County, Texas           15.312270
  5. Perry County, Alabama            14.830037
  6. Leslie County, Kentucky          14.409083
  7. Somervell County, Texas          14.366224
  8. Turner County, Georgia           12.543260
  9. Randolph County, Georgia         11.657655
  10. Issaquena County, Mississippi   11.619374

Counties that experienced the largest decreases are more spatially distanced, but it's worth noting that 4 of the 10 counties are located in Texas.

Top 10 counties by decrease in percent poverty:
  1. Kenedy County, Texas        -21.322551
  2. Esmeralda County, Nevada    -16.985172
  3. Motley County, Texas        -16.027811
  4. Harmon County, Oklahoma     -15.247208
  5. Loup County, Nebraska       -15.203111
  6. San Juan County, Colorado   -14.949258
  7. Hudspeth County, Texas      -14.568698
  8. Baker County, Georgia       -14.519724
  9. Edwards County, Texas       -13.003802
  10. Calhoun County, Florida    -12.560126

The analysis also uses a distributional analysis of county population sizes to explore how changes in poverty rates differ for counties with different population sizes. In general, the largest percentage point changes in poverty occur in counties with populations below 10k, but there are a few counties with populations greater than 10k that experienced percentage point changes in excess of 10 percent. In general, counties with populations above 50k had a few counties with percentage poverty increases nearing 5 percent, and counties also saw percentage point decreases in poverty exceeding 5 percent. These population size limited rankings could be used in the future to explore differences in county-level demographic experiences for counties of different population sizes with large increases or decreases in poverty rates.

Data on the top percentage point changes for counties with population sizes exceeding 100k shows that more populated areas tend to see much smaller changes.

Top 3 100k+ pop counties by increase in percent poverty:
Terrebonne Parish, Louisiana    4.807254
Wichita County, Texas           4.680431
Caddo Parish, Louisiana         4.059541

Top 3 100k+ pop counties by decrease in percent poverty:
Denver County, Colorado           -5.162115
Brazos County, Texas              -4.939345
Buncombe County, North Carolina   -4.424359


4. National spatial comparison of Gini coefficients: The map is designed to identify counties with Gini coefficients that are likely statistically significantly higher or lower than the US Gini coefficient (0.486) (at the 95% confidence interval--although this should be considered a rudimentary comparison rather than a statistical claim). In general, regions of the South, South Texas, and regions of the Southwest and Great Plains likely tribal lands) have higher instances of counties with extremely high inequality. However, high inequality counties are scattered across the county, which may indicate that communities have special circumstances that can exacerbate the difference in the share of income by 20th and 80th percentile earners (Gini coefficient definition).

The top 10 counties with the highest Gini coefficients in 2018 include:
  1.  East Carroll Parish, Louisiana    0.6647
  2.  Harding County, New Mexico        0.6289
  3.  Perry County, Tennessee           0.6254
  4.  New York County, New York         0.5971
  5.  Issaquena County, Mississippi     0.5841
  6.  Dickenson County, Virginia        0.5800
  7.  Leflore County, Mississippi       0.5765
  8.  Lafayette County, Arkansas        0.5762
  9.  Greene County, Georgia            0.5730
  10. Orleans Parish, Louisiana         0.5706

The map also identifies counties with significantly lower inequality levels than the national average. In particular, regions of the Southwest, Great Plains, and Midland Texas have multiple low inequality counties. Overall, it appears that inequality may be higher in the South, Southwest, Appalachia, and along the California and mid-Atlantic coasts. Inequality in general may be lower in the Midwest, Great Plains, and Central and West-Central parts of the country.

### Summary of County Level Exploration of Economic & Demographic Attributes

The script files are set up to allow for researchers to easily pull census tract-level demographic profile data for each of the counties listed on the top 10 highest poverty rate list. This data is then read into QGIS template files, which will populate maps with thematic economic and demographic analyses. However, this summary of findings is limited to discussing the results of the #1 ranked county: Todd County, South Dakota.

Todd County is located in South Central South Dakota along the Nebraska border. Todd County has two census tracts. The script compares the tracts' unemployment rates, incomes per capita, homeownership rates (of occupied properties), immigration rates (regardless of current legal status), and poverty rates.

  Unemployment Rates:
  Census Tract 9401, Todd County, South Dakota    16.08
  Census Tract 9402, Todd County, South Dakota    11.24

  Income per Capita:
  Census Tract 9401, Todd County, South Dakota     9645.96
  Census Tract 9402, Todd County, South Dakota    11876.11

  Tenant Homeownership Rates:
  Census Tract 9401, Todd County, South Dakota    40.49
  Census Tract 9402, Todd County, South Dakota    46.01

  Percent Foreign Born:
  Census Tract 9402, Todd County, South Dakota    0.03
  Census Tract 9401, Todd County, South Dakota    0.01

  Poverty Rates:
  Census Tract 9401, Todd County, South Dakota    58.54
  Census Tract 9402, Todd County, South Dakota    52.56

The data is then mapped to allow for easier comparisons of distributional and categorical data. The maps identify these key findings:
  1. Income Distribution: The income distribution of both tracts are roughly equal, but the median income for tract 9402 is about $1,800 larger.

  2. Race and Ethnicity: Both counties' residents are predominantly Native American, and the second highest racial identity is Multiracial (likely Native American and White, but all multiracial identities are collapsed). White residents are the third largest racial group, and Tract 9402 has a larger share of White residents as well as a number of Asian/Pacific Island residents. These findings indicate that the county is likely partially or entirely located within tribal lands.

  3. Poverty Distribution: Tract 9401 has an outsized population of residents whose income falls below 50% of the federal poverty line, which indicates that county residents may suffer from deep poverty impacts. Tract 9402 has roughly the same number of residents whose income has below 50% FPL, but it also has an increased share of residents whose incomes fall between 50-100% FPL and also those whose incomes exceed 200% FPL. This indicates that Tract 9402 may contain an economic town center (possibly a county seat) that may create economic opportunities that drive up the share of non-poverty residents.

Overall, the results indicate that tract 9401 has slightly worse economic conditions.
