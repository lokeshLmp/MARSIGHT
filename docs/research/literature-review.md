# MARSIGHT – Literature Review

## 1. Introduction

This literature review examines existing research and technologies relevant to Martian terrain mapping, planetary remote sensing, terrain analysis and autonomous rover navigation.

The objective is to identify scientific methods that can support the development of MARSIGHT.

## 2. Research Areas

### 2.1 Mars Orbital Imaging

High-resolution orbital imagery provides detailed observations of Martian surface features, including craters, rocks, dunes and geological formations.

NASA's Mars Reconnaissance Orbiter carries the HiRISE instrument, which captures high-resolution images of the Martian surface.

Relevance to MARSIGHT:
- Surface visualization.
- Identification of geological features.
- Supporting terrain interpretation.

### 2.2 Digital Terrain Models

Digital Terrain Models represent surface elevation as spatially organized numerical data.

They can support:
- Elevation visualization.
- Slope calculations.
- Terrain profile generation.
- Preliminary route evaluation.

### 2.3 Terrain Classification

Terrain classification involves identifying different surface types using imagery and numerical characteristics.

Potential classes for investigation include:
- Bedrock.
- Sandy terrain.
- Rock fields.
- Crater regions.
- Dunes.

Machine learning and image-processing techniques may help classify terrain, provided suitable labelled datasets are available.

### 2.4 Autonomous Navigation and Path Planning

Planetary rover navigation research investigates how robotic vehicles can identify traversable terrain and plan routes while avoiding obstacles.

Potential techniques for MARSIGHT include:
- Grid-based pathfinding.
- A* search.
- Terrain-cost maps.
- Elevation and slope constraints.

These techniques will be evaluated using available data rather than assumed to guarantee astronaut safety.

## 3. Important Scientific Resources

1. NASA HiRISE – High Resolution Imaging Science Experiment.
   https://www.uahirise.org/

2. NASA Planetary Data System.
   https://pds.nasa.gov/

3. NASA Mars Reconnaissance Orbiter.
   https://science.nasa.gov/mission/mars-reconnaissance-orbiter/

4. NASA Mars 2020 Perseverance Mission.
   https://science.nasa.gov/mission/mars-2020-perseverance/

5. USGS Astrogeology.
   https://astrogeology.usgs.gov/

## 4. Proposed Research Methodology

MARSIGHT will investigate the following workflow:

1. Acquire suitable planetary imagery and elevation datasets.
2. Inspect their formats, spatial resolution and coordinate reference systems.
3. Process the datasets using Python.
4. Calculate terrain characteristics such as elevation variation and slope.
5. Visualize the results using geospatial tools.
6. Evaluate possible routes using defined terrain costs.
7. Present the analysis through an interactive web interface.

## 5. Research Gaps to Investigate

- Integration of multiple planetary datasets into one interface.
- Accessible visualization of scientific terrain information.
- Combining terrain measurements with route evaluation.
- Communicating uncertainty and data limitations.
- Connecting scientific