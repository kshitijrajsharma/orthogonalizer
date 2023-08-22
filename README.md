### Polygon Orthogonalizer
Pip implementation for polygons of [orthogonalize-polygon](https://github.com/Mashin6/orthogonalize-polygon/tree/master) which is an improved implementation of JOSM Orthogonalize function (JOSM Q Function). Credits to all the respective involved authors

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

## Options : 

**maxAngleChange (int, optional)**: 
angle (0,45> degrees. Sets the maximum angle deviation
from the cardinal direction for the segment to be still
considered to continue in the same direction as the
previous segment. Defaults to 15.

**skewTolerance (int, optional)**: 
angle <0,45> degrees. 
Sets skew tolerance for segments that
are at 45˚±Tolerance angle from the overal rectangular shape
of the polygon. Usefull when preserving e.g. bay windows on a
house. Defaults to 15.

## Example 
Input ---> Output
![image](https://github.com/kshitijrajsharma/orthogonalizer/assets/36752999/97d2233c-c8c9-4417-80e1-16964f48383f)


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request. When contributing to this project, please follow the Contributing Guidelines.

## License

This project is licensed under the GNU General Public License v3.0 License. See the LICENSE file for more information.
