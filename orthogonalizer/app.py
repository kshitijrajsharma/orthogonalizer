import json

from shapely.geometry import Polygon, mapping

from .utils import apply_algorithm, validate_geojson


def othogonalize_poly(geojson_str, maxAngleChange=15, skewTolerance=15):
    """Orthogonalizes Polygon Geojson

    Args:
        geojson_str (_type_): Input geojson string or JSON object
        maxAngleChange (int, optional): angle (0,45> degrees. Sets the maximum angle deviation
                         from the cardinal direction for the segment to be still
                         considered to continue in the same direction as the
                         previous segment. Defaults to 15.
        skewTolerance (int, optional): angle <0,45> degrees. Sets skew tolerance for segments that
                        are at 45˚±Tolerance angle from the overal rectangular shape
                        of the polygon. Usefull when preserving e.g. bay windows on a
                        house. Defaults to 15.

    Raises:
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: Updated and corrected GEojson
    """
    if isinstance(geojson_str, str):
        geojson = validate_geojson(geojson_str)
    elif isinstance(geojson_str, dict):
        geojson = geojson_str
    else:
        raise ValueError(
            "Invalid input. Please provide a valid GeoJSON string or JSON object."
        )
    input_features = geojson["features"]
    output_features = []
    for feature in input_features:
        if feature["type"] != "Polygon":
            raise ValueError("Only polygons are supported")
        orthogonalized_poly = apply_algorithm(
            Polygon(feature["coordinates"][0]), maxAngleChange, skewTolerance
        )

        orthogonalized_poly_geojson = {
            "type": "Feature",
            "properties": {},
            "geometry": json.dumps(mapping(orthogonalized_poly)),
        }
        output_features.append(orthogonalized_poly_geojson)
    geojson["features"] = output_features
    return geojson
