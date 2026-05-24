"""This module defines the DogFacts class, which is responsible for fetching and
processing dog breed information from the Dog API. The class includes methods to
retrieve a list of dog breeds, extract their attributes, and flatten the data
into a more readable format. The main method, `fetch`, orchestrates the entire
process and returns a list of flattened breed attributes.
"""

#!/usr/bin/env python3

import requests


class DogFacts:
    """A class to fetch and process dog breed information from the Dog API."""

    def __init__(self):
        self.base_url = "https://dogapi.dog/api/v2"

    def _fetch_dog_breeds(self) -> list:
        """Fetches a list of dog breeds from the API.

        :return: A list of dog breeds with their attributes.
        :rtype: list
        """
        try:
            response = requests.get(
                f"{self.base_url}/breeds?",
                params={"page[number]": 1, "page[size]": 10},
                timeout=10,
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching dog breeds: {e}")
            return []
        data = response.json()
        breeds = data.get("data", [])
        return breeds

    def fetch(self) -> list:
        """Fetches and flattens dog breed attributes.
        :return: A list of flattened dog breed attributes.
        :rtype: list
        """
        breeds = self._fetch_dog_breeds()
        breed_attributes = [breeds.get("attributes", {}) for breeds in breeds]
        return self._flatten_breed_attributes(breed_attributes)

    def _flatten_breed_attributes(self, breed_attributes: list) -> list:
        """Flattens the breed attributes into a more readable format.
        :param breed_attributes: A list of breed attributes to flatten.
        :type breed_attributes: list
        :return: A list of flattened breed attributes.
        :rtype: list
        """
        flattened = []
        for attributes in breed_attributes:
            flattened.append(
                {
                    "name": attributes.get("name"),
                    "description": attributes.get("description"),
                    "min_life_span": f"{attributes.get('life', {}).get('min', 'N/A')}",
                    "max_life_span": f"{attributes.get('life', {}).get('max', 'N/A')} years",
                    "male_weight_min": f"{attributes.get('male_weight', {}).get('min', 'N/A')}",
                    "male_weight_max": f"{attributes.get('male_weight', {}).get('max', 'N/A')} kg",
                    "female_weight_min": f"{attributes.get('female_weight', {}).get('min', 'N/A')}",
                    "female_weight_max": f"{attributes.get('female_weight', {}).get('max', 'N/A')} kg",
                    "hypoallergenic": attributes.get("hypoallergenic", "N/A"),
                }
            )
        return flattened
