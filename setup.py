import setuptools
import tomli

project = tomli.load(open("pyproject.toml", "rb"))["project"]

setuptools.setup(
    name="hyphern",
    version=project["version"],
    url=project["urls"]["Homepage"],
    author=project["authors"][0]["name"],
    author_email=project["authors"][0]["email"],
)
