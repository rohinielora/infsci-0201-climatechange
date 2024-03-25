import pandas as pd

class Model:
    def __init__(self, data_access):
        self.data_access = data_access
        self._countries_geojson = self.load_countries_geojson()
        self._temperature_df = None  # Initialize with None
        self._std_df = None  # Initialize with None
        self.load_and_process_temperature_data()
        self.load_and_process_std_data()

    @property
    def temperature_df(self):
        return self._temperature_df

    @temperature_df.setter
    def temperature_df(self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Temperature data must be a pandas DataFrame.")
        if df.empty:
            raise ValueError("Temperature DataFrame cannot be empty.")
        self._temperature_df = df

    # Similarly for std_df
    @property
    def std_df(self):
        return self._std_df

    @std_df.setter
    def std_df(self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Standard deviation data must be a pandas DataFrame.")
        if df.empty:
            raise ValueError("Standard deviation DataFrame cannot be empty.")
        self._std_df = df

    def load_and_process_temperature_data(self):
        df = self.data_access.load_csv_data("../data/FAOSTAT_temperature.csv")
        temp_df = df[df["Element"] == "Temperature change"]
        countries_dict = {
            # Insert your countries_dict here
        }
        temp_df = self.align_country_names(temp_df, countries_dict)
        mean_temp_df = temp_df.groupby('Area')['Value'].mean().reset_index()
        return mean_temp_df

    def load_and_process_std_data(self):
        df = self.data_access.load_csv_data("../data/FAOSTAT_temperature.csv")
        std_df = df[df["Element"] == "Standard Deviation"]
        countries_dict = {
            # Insert your countries_dict here
        }
        std_df = self.align_country_names(std_df, countries_dict)
        mean_std_df = std_df.groupby('Area')['Value'].mean().reset_index()
        return mean_std_df

    def get_countries_geojson(self):
        return self.countries_geojson

    def get_temperature_data(self):
        return self.temperature_df

    def get_std_dev_data(self):
        return self.std_df
