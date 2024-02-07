READ ME

About
This python code is used to process Excel outputs from OpenLCA software. The output consists of 13 interactive Plotly graphs helping visualize just about everything within the Excel file. 

The primary goal here was to help visualize the “Other column” that is often extremely large and incoherent when deciphering the top 5 processes visualization that the OpenLCA software provides; however the other visualizations were made in order to give a comprehensive overview of all the data present. 

Interactive Plotly Graphs
With most Plotly visualizations you will notice a legend in the top right of the screen. This legend is interactive when first made and can be customized before saving the visualization. Depending on the graph the legend will be referencing: Category, Sub-Category, Continent, Group, Flow, and a more specific OpenLCA categorization (Industrial Standard Industrial Classification of All Economic Activities (ISIC))

Primary things to edit when before running
You must change to file path to the directory in which your file is located
Specifying general compounds specific to your interest, here CO2, Methane, and Hydrogen are specified
After initially specifying compounds the first thing printed in the terminal will be all compounds that contain these keywords, from here you can further specify to more specific compounds
When obtaining the top X flows/processes, ‘X’ is editable to number of your choosing
I have encountered 2 different formats for these OpenLCA outputs, I recommended using the default in the code however if you notice errors within the first few graphs or receive and error when running the code simply try editing in/out line 713

IDE Choice
This code is much more digestible when open on Visual Studio Code (One of the most popular Python IDEs) due to the usage of #region and #endregion dropdowns used to collapse specific sections turning these 1600+ lines into 14 lines when fully collapse

Visualization Breakdown
Graph 1: Top Processes in GWP (Global Warming Potential) 100 Impact category (Excluding Other)
Graph 2: Impact Categories and Their Values Split by Category of Flow
Graph 3: Impact Categories and Their Values Split by Sub-Category of Flow
Graph 4: Emissions by Category
Graph 5: Emissions by Sub-Category
Graph 6: Impact by Continent for Different Impact Categories
Graph 7: Kg of CO2, Methane and Hydrogen Compounds
Graph 8: Kg of CO2, Methane, and Hydrogen
Graph 9: Kg of CO2, Methane and Hydrogen Compounds of Specific Compounds
Graph 10: Top 20 Flows in GWP 100 Impact Category
Graph 11: Top Processes in GWP 100 Impact Category (Excluding Other)
Graph 12: “Other” Processes in GWP 100 Impact Category
Graph 13: Kg of CO2 Equivalent for CO2, Methane, and Hydrogen of Specific Compounds
