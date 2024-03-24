import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

class View:
    def __init__(self):
        pio.renderers.default = 'iframe'  # Adjust based on your environment

    def plot_std_dev_box(self, std_dev_data):
        fig = px.box(std_dev_data, y="Value")
        fig.update_layout(title="Standard Deviation of Temperature Change")
        fig.show()

    def plot_mean_temp_box(self, mean_temp_data):
        fig = px.box(mean_temp_data, y="Value")
        fig.update_layout(title="Mean Temperature Change")
        fig.show()

    def plot_temperature_change_map(self, geojson, temperature_data):
        fig = go.Figure(go.Choroplethmapbox(geojson=geojson,
                                            locations=temperature_data.Area,
                                            z=temperature_data.Value,
                                            featureidkey="properties.ADMIN",
                                            colorscale=[[0, 'rgb(255,255,255)'],
                                                        [0.5, 'rgb(255,136,0)'],
                                                        [1, 'rgb(255,0,0)']],
                                            zmax=temperature_data['Value'].max(),
                                            text=temperature_data.Area,
                                            hovertemplate="Country: %{text}<br>Temperature Change: %{z}<extra></extra>",
                                            marker_opacity=0.7,
                                            marker_line_width=0))
        fig.update_layout(mapbox_style="carto-positron",
                          mapbox_zoom=1,
                          margin={"r":0,"t":0,"l":0,"b":0},
                          title="Global Temperature Change")
        fig.show()
    
    # Additional plotting methods can be implemented here
