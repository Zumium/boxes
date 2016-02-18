#! /usr/bin/env python3
from setuptools import setup

setup(
	name="boxes",
	version="1.0.2",
	license="Apache License",
	description="file organization tool",
	author="Zumium",
	author_email="martin007323@gmail.com",
	packages=['boxes','boxes.handlers'],
	package_data={
		'boxes':['README.md','LICENSE']
	},
	entry_points="""
	[console_scripts]
	boxes = boxes.main:main
	""",
)
