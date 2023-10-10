from setuptools import setup

setup_params = {
    "name": "biota",
    "version": "0.3",
    "description": "Tools to generate aboveground biomass forest change maps from ALOS PALSAR/PALSAR-2 mosaic data.",
    "url": "https://bitbucket.org/sambowers/biota",
    "author": "Samuel Bowers",
    "author_email": "sam.bowers@ed.ac.uk",
    "license": "GNU General Public License",
    "zip_safe": False,
    "packages": [
        "biota",
    ],
    "package_data": {
        "biota": [
            "cfg/*",
        ]
    },
    "install_requires": ["scipy", "scikit-image"],
}

setup(**setup_params)
