import sys
# so we can include the pypins package in the search path
sys.path.append("../")

from services.pypi.actions import FetchCatalog


def main():
    FetchCatalog().execute()

if __name__ == "__main__":
    main()