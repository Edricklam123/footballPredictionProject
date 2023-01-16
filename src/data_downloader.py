# Author: Edrick
# Create date: Jan 16, 2023


# Libraries
import requests
import regex as re
import pandas as pd
from bs4 import BeautifulSoup

# Class
class dataOnlineChecker:
    """
    Class checking the data that are available for downloading
    """
    def __init__(self):
        self.data_download_url = r'https://football-data.co.uk/data.php#download'
        self.main_url = r'https://football-data.co.uk/'
        self.link_map = {}

    def check_ava_leagues(self):
        # Available leagues categories
        # Create dictionary for the two types of league for later iteration
        main_league = 'main leagues'
        extra_league = 'extra leagues'
        leagues = {main_league: None, extra_league: None}

        # Make request
        res = requests.get(self.data_download_url).text

        # Make soup
        soup = BeautifulSoup(res, 'lxml')

        # Find out the paragraphs with "leagues"
        para_list = soup.find_all('p')
        for para in para_list:
            if main_league in para.text.lower():
                leagues[main_league] = para
            if extra_league in para.text.lower():
                leagues[extra_league] = para


        # Display main leagues
        for key, para in leagues.items():
            table_league = para.find_next_sibling('table')
            for a in table_league.find_all('a', href=True):
                self.link_map[a.getText()] = a['href']
            df_league = pd.read_html(str(table_league))[0]

            # Clean the league table
            df_league = df_league.drop(0, axis=1)
            df_league.columns = ['League Name', 'Datasets']
            # df_league.index.name = key.title()

            # Print to console
            print('-'*50)
            print(key.title())
            print(df_league)


    def get_league_code(self, url):
        """
        Get the league code name for the league, e.g. Premier League -> E, Scotland -> SC
        :param url:
        :return:
        """
        pass


class dataDownloader:
    """
    This class should inherit from the checker to get the request functions.
    """
    def __init__(self, start_year, end_year, league_code:str):
        pass