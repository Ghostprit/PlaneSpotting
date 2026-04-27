# PlaneSpotting

This project focuses on obtaining real-time flight data of flights above the region of Lithuania using OpenSky Network API

# Features

- Real-time flight tracking
- Map with an option to zoom and pan around
- Data of each flight consisting of a callsign, origin country, altitude and velocity
- Automatic information update every 30 seconds
- Dummy data fallback if connection to OpenSky Network API is unavailable

# Technology stack

- Backend: Python, Flask
- Frontend: JavaScript, Leaflet.js, HTML
- Deployments: AWS, Docker

# Project structure

Planespotting/
├── app.py                  
├── Dockerfile             
├── requirements.txt       
├── test.sh                
├── templates/
│   └── index.html         
└── .github/
    └── workflows/
        └── deploy.yml    

# Requirements

- Python 3.14 or above
- Docker

# Deployment using Docker

- Open the repository directory using "cd" /.../PlaneSpotting

- docker build -t planespotting .

- docker run -p 80:80 planespotting

# Deployment using AWS EC2

PlaneSpotting supports GitHub Actions workflow to automate deployment

    ## Configure GitHub secrets:
        - "EC2IPPS": EC2 public IP address
        - "USERNAME": SSH username
        - "SSH_KEY": Private SSH key
    
    ## Pushing code to "main" triggers GitHub Actions deployment

    ## EC2 instance should have ~/deploy.sh that:
        - Enters PlaneSpotting directory
        - Pulls latest code
        - Builds new Docker image
        - Stops and removes old Docker directories
        - Runs the new container

# Web App Endpoints

"\" Main map of the application
"\api\flights" Fetched data from OpenSky Network API
"\health" Health check

# Customization

- Edit the url inside app.py to change the bounds from which the flight data is getting pulled

- Adjust the update interval by editing templates/index.html:
        setInterval(updateFlights, 30000);

- Adjust map settings like the initial, max and min zoom, bounds and center
        var map ...

- Switch tile layer provider:
        L.tileLayer ...

- Change plane icon, size, anchor and popup anchor:
        var planeIcon ...

- Change dummy flight data:
        const dummyFlights ...
