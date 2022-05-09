from setuptools import setup, find_packages


test_require = ["dls-hazzathread", "dls-mainiac", "logging-formatter"]


def main():
    """Main method collecting all the parameters to setup."""
    name = "dls-signals"
    version = "0.0.6"
    description = "Library for collecting signal timing during a running program."
    author = "David Erb, KITS - Controls"
    author_email = "KITS@maxiv.lu.se"
    license = "GPLv3"
    url = "https://gitlab.maxiv.lu.se/kits-maxiv/dls-signals"
    packages = find_packages(".", exclude=["tests"])
    install_requires = (["setuptools"],)

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
        extras_require={"tests": test_require},
    )


if __name__ == "__main__":
    main()
