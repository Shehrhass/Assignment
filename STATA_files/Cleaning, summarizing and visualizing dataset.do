*Starting up (working directory and formatting)
pwd  
help pwd
cd "D:\2025\CEU\Degree program\Coding for Economists\Assignment"
pwd
set linesize 255 

*Importing dataset
import delimited "D:\2025\CEU\Degree program\Coding for Economists\Assignment\data\airbnb_raw.csv", varnames(1)

*Cleaning data
tab d_price
drop if missing(d_price) | d_price > 220

*Summary table for d_price
summ d_price
describe d_price

*d_price distribution as box plot
graph box d_price, title("Distribution of Airbnb Prices") ytitle("Price ($)") box(1, lcolor(blue))

save airbnb_clean.dta, replace


