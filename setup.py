from setuptools import setup, find_packages


def main():
    name = "dls-siggy"
    version = "2.0.2"
    description = "Python library for simple Unix signal capture."
    author = "David Erb"
    author_email = "david.erb@diamond.ac.uk"
    license = "GPLv3"
    url = "https://github.com"
    packages = find_packages(exclude=["tests", "*.tests.*", "tests.*", "tests"])
    install_requires = []
    include_package_data = True

    setup(
        name=name,
        version=version,
        description=description,
        author=author,
        author_email=author_email,
        license=license,
        url=url,
        packages=packages,
        install_requires=install_requires,
        include_package_data=include_package_data,
    )


if __name__ == "__main__":
    main()
