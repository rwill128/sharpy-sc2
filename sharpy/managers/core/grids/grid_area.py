from .build_area import BuildArea
from .zone_area import ZoneArea
from .cliff import Cliff


class GridArea:
    def __init__(self, area: BuildArea):
        self.Area: BuildArea = area
        self.ZoneIndex = ZoneArea.NoZone
        self.BuildingIndex = -1
        self.Cliff = Cliff.No
