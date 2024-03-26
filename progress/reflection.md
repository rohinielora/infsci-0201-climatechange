
1. Understanding of Class and Object-Oriented Programming Principles.

In my project, principles of Object-Oriented Programming are showcased through the creation and interaction of the classes “DataAccess”, “Model”, and “View”.

In the class, “DataAccess”, I manage data retrieval by loading data from CSV and files named GeoJSON. In the class “Model”, I utilize the class, “DataAccess” to process the data in preparation for visualization. My class, “View” presents data. The View class only serves in taking data and rendering it, without concern for the data processing or storing.


2. Awareness of Data Types and Type-checking

I showcased my understanding of different data types through the manipulation of data frames with “pandas” and in my work with JSON data. Specifically, in the class DataAccess and the class Model, methods I employed such as “load_csv_data” and “load_and_process_temperature_data” deal with a plethora of different data types including pandas dataframes, lists and dictionaries. In working with a diversity in data types, I was aware of handling this correctly as I did not want to cause runtime errors. 


3. Use of Property Decorators for Data Encapsulation and Validation

In this climate change project, the property decorators are utilized for data encapsulation/validation in the Model class. Specifically, by applying @property and @setter, data attributes (such as temperature_df and std_df) are safely encapsulated and put through confirmation that they are non-empty data frames. Through applying this method, I am ensuring the integrity of the data while also checking for common data issues. 





4. Reading from JSON/CSV Files

The project demonstrates practical skills in handling real-world data by reading from JSON and CSV files. The `DataAccess` class's methods `load_csv_data` and `load_geojson_data` showcase how to read these file formats using pandas and the `json` module, respectively. 

Additionally, incorporating the plotly library for data visualizaiton (as seen within the View class) demonstrates this project’s application of python for creating interactive charts and maps that transform raw data. 


5. Processing Data with List, Dict, and String Manipulation

This project exemplifies the manipulation of lists, dictionaries, and strings through the process of aligning country names between different data sources and aggregating temperature data. This is showcased specifically in the `Model` class.

