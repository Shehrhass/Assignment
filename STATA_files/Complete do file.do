*Starting up (working directory and formatting)
pwd  
help pwd
cd "D:\2025\CEU\Degree program\Coding for Economists\Assignment"
pwd
set linesize 255 

*Creating a log file 
capture log close // make sure nothing is open
log using "Coding_Final_Assignment", replace

*Importing dataset
import delimited "D:\2025\CEU\Degree program\Coding for Economists\Assignment\data\airbnb_raw.csv", varnames(1)

*Understanding dataset
browse
list in 1
clear

* Transforming the price 
summ price
rename price d_price
browse d_price
summ d_price
destring d_price, replace ignore("$ ,")

*Removing dollar signs
replace d_price = subinstr(d_price, "$", "", .)
*Removing commas
replace d_price = subinstr(d_price, ",", "", .)
*Trimming
replace d_price = trim(d_price)
*Destringing
destring d_price, replace

gen d_price_num = real(d_price)
browse d_price d_price_num
drop d_price
rename d_price_num d_price
tab d_price

*Summary table for d_price
summ d_price
describe d_price

*d_price distribution as box plot
drop if missing(d_price) | d_price > 220
graph box d_price, title("Distribution of Airbnb Prices") ytitle("Price ($)") box(1, lcolor(blue))

save airbnb_clean.dta, replace


