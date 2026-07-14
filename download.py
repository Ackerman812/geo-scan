import streamlit as st
from pathlib import Path


def test_files_download():

    folder = Path(
        "assets/test_images"
    )


    before = folder / "terrain_before.png"

    after = folder / "terrain_after.png"



    if before.exists() and after.exists():


        st.markdown(

        """
        <div class="custom-card">

        <h3>
        🛰 TEST SATELLITE DATA
        </h3>

        <p>
        Download example scans for system demonstration
        </p>

        </div>
        """,

        unsafe_allow_html=True

        )



        col1, col2 = st.columns(2)



        with col1:


            with open(

                before,

                "rb"

            ) as file:


                st.download_button(

                    label=
                    "⬇ BEFORE SCAN",

                    data=file,

                    file_name=
                    "terrain_before.png",

                    mime=
                    "image/png",

                    use_container_width=True

                )



        with col2:


            with open(

                after,

                "rb"

            ) as file:


                st.download_button(

                    label=
                    "⬇ AFTER SCAN",

                    data=file,

                    file_name=
                    "terrain_after.png",

                    mime=
                    "image/png",

                    use_container_width=True

                )


    else:


        st.warning(

            """
            ⚠ Test images not found.

            Check folder:

            assets/test_images/

            Required files:

            terrain_before.png

            terrain_after.png
            """

        )