### Polygon Orthogonalizer
Pip implementation for polygons of [orthogonalize-polygon](https://github.com/Mashin6/orthogonalize-polygon/tree/master) which performs squaring/orthogonalization of polygons, in other words making all its angles 90˚ or 180˚, which is usefull for automated adjustment of building footprint shapes. Script uses GeoPandas and Shapely packages and is an improved implementation of JOSM Orthogonalize function. Credits to all the respective involved authors

## Installation

You can install OSM Conflator using pip:

```shell
pip install orthogonalizer
```

## Usage

Here's an example of how to use Polygon orthogonalizer in your Python code:

```python
from orthogonalizer import othogonalize_poly

geojson_str = '{"type": "FeatureCollection", "features": ... }'

orthogonalized_poly = othogonalize_poly(geojson_str)

print(orthogonalized_poly)
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request. When contributing to this project, please follow the Contributing Guidelines.

## License

This project is licensed under the GNU General Public License v3.0 License. See the LICENSE file for more information.