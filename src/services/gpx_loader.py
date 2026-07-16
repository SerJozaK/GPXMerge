from pathlib import Path
import gpxpy


class GPXLoader:

    def __init__(self):
        pass

    def load(self, filename):

        path = Path(filename)

        with open(path, "r", encoding="utf-8") as f:
            gpx = gpxpy.parse(f)

        return gpx

    def get_track_points(self, gpx):

        points = []

        for track in gpx.tracks:

            for segment in track.segments:

                for point in segment.points:

                    points.append(point)

        return points

    def count_points(self, gpx):

        return len(self.get_track_points(gpx))