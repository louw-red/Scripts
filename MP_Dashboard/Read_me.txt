This script allows the user to generate an excel file that contains summarized information on a modelpoint folder location.

It's best utilized on MP_field with FINITE number of possible values. IE:

Good for investigation like: "How many policies are in which IRP class on a product level and also total level"
Bad for investigation like: "How many policies have a SA below a R1m" 

input the mp folder location, csv extension type, output location and columns you are interested in.
for 1 column as input (columns = ["COMM_MODEL"]), output will be an excel workbook that has a sheet named according to column specified in input.


Sheet will look like:

product_name | Comm_model = 1 | Comm_model = 2
prod_x       |     5000       |      32424
prod_y       |        0       |       2134
prod_z       |     4343       |        232
