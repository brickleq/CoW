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
    timeline: true,
  });

  