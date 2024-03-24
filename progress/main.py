from DataAccess import DataAccess
from Model import Model
from View import View

def main():
    data_access = DataAccess()
    model = Model(data_access)
    view = View()

    std_dev_data = model.get_std_dev_data()
    mean_temp_data = model.get_temperature_data()
    countries_geojson = model.get_countries_geojson()

    view.plot_std_dev_box(std_dev_data)
    view.plot_mean_temp_box(mean_temp_data)
    view.plot_temperature_change_map(countries_geojson, mean_temp_data)

if __name__ == "__main__":
    main()
