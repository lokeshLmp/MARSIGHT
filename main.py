from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="MARSIGHT API",
    description=(
        "Research prototype API for planetary terrain intelligence and "
        "Mars mission-planning experiments. Current release exposes project "
        "status and capability metadata; scientific processing endpoints "
        "will be added as they are implemented and validated."
    ),
    version="0.1.0",
)

# Allow the future web interface to call this API. Restrict origins when the
# production frontend domain is available.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["system"])
def root():
    return {
        "name": "MARSIGHT",
        "status": "online",
        "version": app.version,
        "message": "Planetary terrain intelligence API is running.",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", tags=["system"])
def health():
    return {"status": "healthy", "service": "marsight-api"}


@app.get("/api/v1/project", tags=["project"])
def project_info():
    return {
        "name": "MARSIGHT",
        "purpose": "Planetary terrain intelligence and mission-planning research",
        "release": "0.1.0",
        "implementation_status": "foundation",
        "limitations": [
            "This deployment currently provides API foundation and metadata only.",
            "No live NASA data feed is connected.",
            "No operational astronaut navigation or mission-safety decisions are supported.",
        ],
    }


@app.get("/api/v1/capabilities", tags=["project"])
def capabilities():
    return {
        "capabilities": [
            {
                "name": "Mars terrain exploration",
                "status": "planned",
                "description": "Explore verified planetary imagery and terrain products.",
            },
            {
                "name": "Elevation and slope analysis",
                "status": "planned",
                "description": "Process elevation models and derive terrain measurements.",
            },
            {
                "name": "Terrain hazard assessment",
                "status": "experimental",
                "description": "Evaluate terrain properties with documented uncertainty.",
            },
            {
                "name": "Candidate route evaluation",
                "status": "planned",
                "description": "Compare candidate routes using measurable terrain properties.",
            },
            {
                "name": "AI-assisted explanations",
                "status": "planned",
                "description": "Explain verified analysis outputs without inventing measurements.",
            },
        ],
        "status_definitions": {
            "implemented": "Available in this deployed release.",
            "experimental": "Under research and not validated for operational use.",
            "planned": "Not implemented in this release.",
        },
    }
