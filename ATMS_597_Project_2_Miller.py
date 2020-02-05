{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ATMS 597- Project-2_Miller.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPpHj927JIAzrjmV1bTRaD8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rmiller34/ATMS-597-SP-2020/blob/master/ATMS_597_Project_2_Miller.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yyUl1qCsNWzH",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import requests\n",
        "\n",
        "def make_request(endpoint, payload=None):\n",
        "    \"\"\"\n",
        "    Make a request to a specific endpoint on the weather API\n",
        "    passing headers and optional payload.\n",
        "    \n",
        "    Parameters:\n",
        "        - endpoint: The endpoint of the API you want to \n",
        "                    make a GET request to.\n",
        "        - payload: A dictionary of data to pass along \n",
        "                   with the request.\n",
        "    \n",
        "    Returns:\n",
        "        Response object.\n",
        "    \"\"\"\n",
        "    return requests.get(\n",
        "        f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data',\n",
        "        headers={\n",
        "            'token': 'vqnLQeiBSuNfAVMcjmCbPyyHnppczzpZ'\n",
        "        },\n",
        "        params=payload\n",
        "    )"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jNKo4fU5OnUW",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 33
        },
        "outputId": "52c64bee-e77e-4cba-e95e-498c047bac69"
      },
      "source": [
        "\n",
        "import datetime\n",
        "\n",
        "from IPython import display # for updating the cell dynamically\n",
        "\n",
        "current = datetime.date(2018, 1, 1)\n",
        "end = datetime.date(2019, 1, 1)\n",
        "\n",
        "results = []\n",
        "\n",
        "while current < end:\n",
        "    # update the cell with status information\n",
        "    display.clear_output(wait=True)\n",
        "    display.display(f'Gathering data for {str(current)}')\n",
        "    \n",
        "    response = make_request(\n",
        "        'data', \n",
        "        {\n",
        "            'datasetid' : 'GHCND', # Global Historical Climatology Network - Daily (GHCND) dataset\n",
        "            'locationid' : 'CITY:US360019', # NYC\n",
        "            'startdate' : current,\n",
        "            'enddate' : current,\n",
        "            'units' : 'metric',\n",
        "            'limit' : 1000 # max allowed\n",
        "        }\n",
        "    )\n",
        "\n",
        "    if response.ok:\n",
        "        # we extend the list instead of appending to avoid getting a nested list\n",
        "        results.extend(response.json()['results'])\n",
        "\n",
        "    # update the current date to avoid an infinite loop\n",
        "    current += datetime.timedelta(days=1)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "'Gathering data for 2018-08-06'"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rSD9HDFYSV0M",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.DataFrame(results)\n",
        "df.head()"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}