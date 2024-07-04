import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect powdery mildew parasitised leaves have clear marks/signs, "
        f"typically in the surface of the leaf, that can differentiate them from an uninfected leaves. \n\n"
        f"* An Image Montage shows that typically a parasitised leaves have color marks across it. "
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )
