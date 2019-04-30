import json
import urllib.request as urlreq
import dash
import dash_html_components as html
import dash_bio as dashbio

model_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/model_data.js').read()
styles_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/styles_data.js').read()
model_data = json.loads(model_data)
styles_data = json.loads(styles_data)

app = dash.Dash(__name__)

component = dashbio.Molecule3dViewer(
    id='molecule3dviewer',
    styles=styles_data,
    backgroundOpacity='0',
    modelData=model_data,
    selectionType='atom'
)

app.layout = html.Div([component, html.Div(id='output')])


@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('molecule3dviewer', 'selectedAtomIds')]
)
def print_selected(selected):
    if selected is None or len(selected) == 0:
        return "No atoms selected."
    selected = [str(selection) for selection in selected]
    return 'Selected atom IDs: ' + ', '.join(selected)


if __name__ == '__main__':
    app.run_server(debug=True)
