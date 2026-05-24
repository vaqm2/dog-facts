"""This module defines the main function to display dog breed information using
Streamlit. The function initializes the Streamlit app, fetches dog breed information
using the DogFacts class, and displays it in a tabular format.
"""


#!/usr/bin/env python3

import streamlit as st
import pandas as pd

from fetch_facts import DogFacts


def main() -> None:
    """The main function to display dog breed information using Streamlit.
    This function initializes the Streamlit app, fetches dog breed information
    using the DogFacts class, and displays it in a tabular format.
    """
    st.title("Dog Breeds Information")
    st.write("Here are some dog breeds and their attributes:")
    dog_facts = DogFacts()
    breeds_info = dog_facts.fetch()
    df = pd.DataFrame(breeds_info)
    st.dataframe(df)


if __name__ == "__main__":
    main()
