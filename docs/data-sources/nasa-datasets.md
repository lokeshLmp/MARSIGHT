# MARSIGHT – NASA Dataset Research

## 1. Objective

Identify publicly accessible NASA and planetary science datasets suitable for Martian terrain visualization, elevation analysis and mission planning.

## 2. Candidate Data Sources

### 2.1 HiRISE Imagery

Source: https://www.uahirise.org/

Provider: NASA / University of Arizona

Purpose:
- High-resolution Martian surface imagery.
- Geological feature visualization.
- Terrain interpretation.

### 2.2 HiRISE Digital Terrain Models

Source: https://www.uahirise.org/dtm/

Purpose:
- Surface elevation analysis.
- Slope calculation.
- Terrain profile generation.
- Preliminary route evaluation.

### 2.3 NASA Planetary Data System

Source: https://pds.nasa.gov/

Purpose:
- Access planetary mission datasets.
- Investigate original scientific products.
- Obtain metadata and documentation.

### 2.4 NASA Mars Reconnaissance Orbiter

Source: https://science.nasa.gov/mission/mars-reconnaissance-orbiter/

Purpose:
- Investigate orbital observations.
- Identify relevant imaging instruments.
- Explore complementary surface datasets.

## 3. Dataset Evaluation Criteria

Each candidate dataset must be evaluated for:

- Geographic coverage.
- Spatial resolution.
- File format.
- Coordinate reference system.
- Elevation units, where applicable.
- Data quality and uncertainty.
- Accessibility and download requirements.
- Usage and redistribution terms.

## 4. Planned Python Processing

Potential tools:

- Rasterio
- NumPy
- Pandas
- GeoPandas
- Matplotlib
- SciPy

These libraries will be selected after inspecting actual dataset formats.

## 5. Data Management

Original NASA datasets will not be committed in full to GitHub.

The repository will contain:
- Dataset source links.
- Metadata and processing documentation.
- Small permitted sample files.
- Reproducible processing scripts.

## 6. Verification Status

All candidate sources and dataset characteristics must be checked against their original documentation before implementation.