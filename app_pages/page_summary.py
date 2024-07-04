import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Farmy & Food is agricultural company and recently they are facing a challenge "
        f"where their cherry plantations have been presenting powdery mildew, "
        f"which is a fungal disease that affects a wide range of plants. \n"
        f"* Currently, the process is to manually verify if a given cherry tree contains "
        f"powdery mildew and an employee spends around 30 minutes in each tree.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 4208 images taken from "
        f"a manually generated database of leaf images with "
        f"healthy and powdery mildew leaves")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/tehcentr2014/cherry_leaves/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"a healty and powdery mildew leaves visually.\n"
        f"* 2 - The client is interested in telling whether a given leaves contains a powdery mildew or not. "
        )
