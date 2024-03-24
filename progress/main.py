from DataAccess import DataAccess
from Model import Model
from View import View

def main():
    data_access = DataAccess()
    model = Model(data_access)
    view = View()

    # Get processed temperature data and geojson from the model
    temperature_data = model.get_temperature_data()
    countries_geojson = model.get_geojson()

    # Use the view to plot the temperature standard deviation
    view.plot_temperature_std_dev(countries_geojson, temperature_data)

if __name__ == "__main__":
    main()

