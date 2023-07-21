# ACE WorldState Microservice

## Executive Overview

The ACE WorldState Microservice is an integral part of the Autonomous Cognitive Entity (ACE) framework. ACE is a pioneering project aimed at creating autonomous systems based on Large Language Models (LLMs) that possess above-human level reasoning, moral discernment, and a range of other sophisticated capabilities.

Within the ACE framework, the WorldState Microservice plays an essential role. Its primary function is to curate and maintain an up-to-date "world state" by collecting news items from various public data sources. This world state data repository informs the Global Strategy layer (L2) of the ACE framework, providing it with the global context required to make strategic decisions.

## Purpose within ACE

The WorldState Microservice functions as the window to the world for the Global Strategy layer, offering necessary context and updates on global developments. By persistently gathering and storing data from numerous RSS feeds, it provides a reliable source of information to base strategic decisions upon.

The data retrieved and processed by this microservice also ensures transparency and facilitates out-of-band monitoring. Therefore, it's not only critical for the functioning of the ACE framework but also for the safety and stability of the system.

## Functionality

This Python-based microservice fetches data from RSS feeds listed in a configuration file and saves the news items to individual YAML files, maintaining a local repository of news items. It also provides a simple REST API that allows users to search these news items based on keyword or date.

## Setup and Usage

### Requirements

- Python 3.x
- Flask (for the REST API)

### Setup

1. Clone the repository and navigate to the project's root directory.
2. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the `fetch_rss_feeds.py` script to fetch news items from the RSS feeds and save them to YAML files:

    ```bash
    python fetch_rss_feeds.py
    ```

    Note: You can modify the list of RSS feeds by editing the `config.yaml` file.

### Running the REST API

1. Start the Flask server by running the `worldstate.py` script:

    ```bash
    python app.py
    ```

2. The server will start on `localhost:5000`.

3. You can search the news items by sending a GET request to `http://localhost:5000/search`. Use the `keyword` and `date` query parameters to filter news items by keyword or date. For example, `http://localhost:5000/search?keyword=AI&date=2023-07-22`.

## Conclusion

The ACE WorldState Microservice is a key building block in the creation of autonomous systems within the ACE framework. It ensures that strategic decisions made by the ACE system are based on the most up-to-date, global information. The WorldState Microservice also provides an excellent example of how LLMs and frontier AI technologies can be harnessed in novel ways to drive innovation in the field of autonomous systems.