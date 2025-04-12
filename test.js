let API_KEY = "AIzaSyDbAeFnVoU4_popnPt99jUPRUT5YIfFMoI";
const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;
 

app.get('/route', async (req, res) => {
    try {
        const url = 'https://routes.googleapis.com/directions/v2:computeRoutes';

        // Request payload
        const payload = {
            origin: {
                location: {
                    latLng: {
                        latitude: 37.419734,
                        longitude: -122.0827784,
                    },
                },
            },
            destination: {
                location: {
                    latLng: {
                        latitude: 37.417670,
                        longitude: -122.079595,
                    },
                },
            },
            travelMode: 'DRIVE',
            routingPreference: 'TRAFFIC_AWARE',
            computeAlternativeRoutes: false,
            routeModifiers: {
                avoidTolls: false,
                avoidHighways: false,
                avoidFerries: false,
            },
            languageCode: 'en-US',
            units: 'IMPERIAL',
        };

        // Request headers
        const headers = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': API_KEY,
            'X-Goog-FieldMask': 'routes.polyline.encodedPolyline',
        };

        // Make the POST request
        const response = await axios.post(url, payload, { headers });

        // Extract encoded polyline
        const polyline = response.data.routes[0].polyline.encodedPolyline;
        res.json({ polyline });
    } catch (error) {
        console.error('Error fetching routes:', error.response ? error.response.data : error.message);
        res.status(500).send('Error fetching routes');
    }
});

// Serve the frontend
app.use(express.static('public'));

// Start the server
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
