Cesium.Ion.defaultAccessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyMGZjYzI5OS0wZDQ2LTRkMTctOGY0Yi1lZWE3Y2U4ZTQ5ZDEiLCJpZCI6MTI1MjUsInNjb3BlcyI6WyJhc3IiLCJnYyJdLCJpYXQiOjE1NjEyMjIwMjl9.swoqaLkpdCJ0g8USzCJr_z5k1md3UvPdpMqleOUHyL4';
var viewer = new Cesium.Viewer('cesiumContainer', {
    terrainProvider: Cesium.createWorldTerrain(),
    animation: false,
    baseLayerPicker: false,
    fullscreenButton: false,
    homeButton: false,
    navigationHelpButton: false,
    geocoder: false,
    sceneModePicker: false,
    timeline: false
  });

// function addGeoJSON() {
//   viewer.dataSources.add(Cesium.GeoJsonDataSource.load('/historical-basemaps-master/world_1914.geojson', {
//     stroke: Cesium.Color.HOTPINK,
//     fill: Cesium.Color.PINK,
//     strokeWidth: 3
//   }));
// }

// addGeoJSON();

var dataSourcePromise = Cesium.GeoJsonDataSource.load('gz_2010_us_040_00_500k.json').then(
  function(dataSource) {
    viewer.dataSources.add(dataSource);
    viewer.zoomTo(dataSource);
  }
);