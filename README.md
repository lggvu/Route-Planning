Some datasets for the project (all included in the **dat** folder)
- `route-info`: Distance between ADJACENT cities, the final column is the toll cost to travel between two adjacent cities.
- `air-info`: Flight distance between two cities (if there exists a flight route).
- `heuristics`: The distance as crow flies between two arbitrary cities (31x31 matrix)
- `city-label`: The label for each city in the 32 given cities.

-Explain data processing
1. Use Pandas to read the 'route-info.csv' and 'air-info.csv' file
2. Convert their data frame into numpy array( data and data1)
3. Create a column present the total cost between cities( sum of path cost and toll station) ( fee ) 
4. Using two matrix data and fee to create a new matrix contain total cost between adjacent cities ( final_fee)
5. Merge the cost data of using taxi to travel and the cost data of flights.
6. create a dictionary named 'map'
7. 'map' is a dictionary with key is a city name and value is a list of adjacent cities and theirs cost to that city. 
for example : { laocai:[ (HaGiang,300000),(VietTri,312000)]}
8. Using two file 'city-label' and 'heuristics.csv' to write a function to return heuristics dict of a city
  
