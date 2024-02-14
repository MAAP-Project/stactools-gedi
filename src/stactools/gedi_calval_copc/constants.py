from datetime import datetime
from typing import Optional

from pystac import Extent, SpatialExtent, TemporalExtent
from pystac.utils import str_to_datetime

COLLECTION_START: Optional[datetime] = str_to_datetime("2001-01-01T00:00:00.000Z")
TEMPORAL_EXTENT = TemporalExtent([[COLLECTION_START, None]])
SPATIAL_EXTENT = SpatialExtent(
    [
        [-85.3121431, 9.1557835, -79.846044, 9.1274357],
        [-88.5533271, 46.6775162, -88.4704196, 46.6076283],
        [-115.8458579, 45.271288, -115.6760494, 44.6299228],
        [-116.8360319, 48.3745398, -116.7375511, 48.3440162],
        [-116.4114544, 47.8405382, -116.1978039, 47.7426007],
        [-115.7402841, 46.4369485, -115.5648893, 46.3155705],
        [-123.4971471, 38.8005092, -122.4711968, 38.2240142],
        [-122.4348301, 36.9804709, -119.0221486, 36.8508176],
        [-115.7605506, 45.0384903, -115.736248, 44.9979642],
        [-116.6695944, 47.8380691, -116.189556, 47.6349606],
        [-116.9861954, 46.8653832, -116.6481306, 46.7700198],
        [-116.1911687, 45.7158832, -115.9755629, 45.4942469],
        [-116.5511833, 47.7487417, -116.4851769, 47.7199618],
        [142.3844159, -25.4003433, 147.6189914, -25.7895408],
        [-115.8361112, 46.1023891, -115.6613919, 45.9403881],
        [-116.3522009, 47.2886779, -116.0289725, 47.1331918],
        [-116.8478416, 48.3746815, -116.7352503, 48.3361686],
        [-119.1464948, 44.2509373, -118.9489381, 44.0783967],
        [-115.1613612, 44.3453846, -115.0242097, 44.2645588],
        [145.6299423, -17.1178027, 145.6346743, -17.1223529],
        [-115.8264022, 46.6482542, -114.3722411, 45.6475094],
        [11.4235832, 46.0038111, 11.4271766, 46.0012677],
        [9.3157507, 0.6173897, 9.4229706, 0.5382093],
        [111.2892479, -30.0833467, 155.7179351, -43.1031025],
    ]
)
EXTENT = Extent(SPATIAL_EXTENT, TEMPORAL_EXTENT)
KEYWORDS = ["LIDAR", "GEDI", "CALVAL", "COPC", "POINTCLOUD"]
DESCRIPTION = "Cloud Optimized Point Cloud (COPC) version for the Global Ecosystem Dynamics Investigation (GEDI) Calibration/Validation Airborne Lidar Dataset"
