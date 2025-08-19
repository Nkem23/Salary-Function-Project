{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "ir",
      "display_name": "R"
    },
    "language_info": {
      "name": "R"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "IMzr44Z3MHaT"
      },
      "outputs": [],
      "source": [
        "# Unzip the file into a folder\n",
        "unzip(\"Employee_Profile.zip\", exdir = \"unzipped_data\")\n",
        "\n",
        "# Display the extracted files\n",
        "list.files(\"unzipped_data\")"
      ]
    }
  ]
}