<a id="readme-top"></a>

<div align="center">
<h1> PriceTrackerBot </h1>
<p> PriceTrackerBot is a scrapper written in python. </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#aboutheproject">About The Project</a>
    </li>
    <li>
      <a href="#gettingstarted">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
        <a href="#usage">Usage</a>
        <ul>
         <li><a href="#Add an Item to *list_items.json*">Add an Item to <i>list_items.json</i></a></li>
         <li><a href="#Add Website Information to *generic_website_list.csv*">Add Website Information to <i> generic_website_list.csv</i></a></li>
         <li><a href="#How to run ?">How to run ?</a></li>
        </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>


## About the Project <a id="aboutheproject"></a>

PriceTrackerBot is a personnal project to find out whether the lowest or the desired price of an item has been tracked. As an exemple, PriceTrackerBot has been used to track hardware prices.

<p align="right">[<a href="#readme-top">back to top</a>]</p>

## Getting Started <a id="gettingstarted"></a>

### Prerequisites <a id="prerequisites"></a>

Before installing PriceTrackerBot, make sure you have the following installed:

- Python 3.10+
- Pip
- Git 

Python packages required to run PriceTrackerBot: 

- Plyer
- Requests
- Selenium
- Beautifulsoup4

<p align="right">[<a href="#readme-top">back to top</a>]</p>

### Installation <a id="installation"></a>

1. Clone the repo.
    ```sh
    git clone https://github.com/YoungWildChimp/PriceTrackerBot.git
    ```
2. Navigate to the project directory.
    ```sh
    cd PriceTracketBot
    ```
3. Install the required Python packages.
    ```sh
    pip install plyer requests selenium beautifulsoup4
    ```

<p align="right">[<a href="#readme-top">back to top</a>]</p>

## Usage <a id="usage"></a>
This section gives some informations to use and run PriceTrackerBot.

* ### Add an Item to *list_items.json* <a id="Add an Item to *list_items.json*"></a>
    If you already have a *list_items.json* file, skip steps 1 and 2 and proceed to step 3.

    1. Create a new file named *list_items.json* in PriceTrackerBot's directory.
    2. From *template_list_items.json*, copy & paste the contents into *list_items.json*.
    3. Go to your browser and copy and paste the URL of the item you want to track into the "url" field in *list_items.json*.
    4. Set a desired price.

    ```json                    
    [
	    {
		    "url" = "insert URL",
		    "lowest_price" = null,
		    "desired_price" = 00.0,
		    "date" == null
	    }
    ]
    ```
*  ### Add Website Information to *generic_website_list.csv* <a id="Add Website Information to *generic_website_list.csv*"></a>
    If your item is on a website that is not listed in *generic_website_list.csv*, follow these steps to add it:

    1. Open *generic_website_list.csv*.
    2. Add the website's name.
    3. Go on the item's page, right-click on the item's price, **Inspect** and find the class name (e.g class="price", where "price" is the class name).
    4. For *website_rendering*, find out whether the website is uses HTML or JS (i.e JavaScript). If you cannot find this information, use "JS". It may take longer, but it should work. 

* ### How to run ? <a id="How to run ?"></a>
    Currently, PriceTrackerBot has two different modes:

    - Quick_Check: Tracks the item's price **once**.
        ```sh
        PriceTrackerBot().run(quick_check = True)
        ```
    - Regular_Check: **Regularly** tracks the item's price in the background.
        ```sh
        PriceTrackerBot().run(sleep_duration = 21600)
        ```
        *Note: sleep_duration (in seconds) is the time between two price checks.*

    To change PriceTrackerBot mode, edit the code and modify *line 172* according to your needs.
<p align="right">[<a href="#readme-top">back to top</a>]</p>

## Roadmap <a id="roadmap"></a>
- [ ] Add other websites informations (i.e *website_name*, *website_information_price*, *website_rendering*) to *generic_website_list.csv*.
- [ ] Store historical track prices.
- [ ] Plot track price evolution over time.
- [ ] Build a user-friendly Graphical User Interface (GUI).
<p align="right">[<a href="#readme-top">back to top</a>]</p>

## Contributing <a id="contributing"></a>
It is an open source project, feel free to fork the repo and create a pull request. You can also open an issue in order to develop your enhancement.
<p align="right">[<a href="#readme-top">back to top</a>]</p>





