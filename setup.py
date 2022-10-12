from setuptools import setup

setup(
        name="debugmode",
        version="1.3.9",
        install_requires=[],#'sys' 
        entry_points={
            "console_scripts":[
                "debugmode = debugmode:main"
            ]
        }
)