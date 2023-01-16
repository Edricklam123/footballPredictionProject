# Author: Edrick
# Create date: Jan 16, 2023


# Libraries
import os
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


    def get_league_code(self, verbose=False):
        """
        Get the league code name for the league, e.g. Premier League -> E, Scotland -> SC
        :param url:
        :return:
        """
        code_book_dict = {}
        for k, url in self.link_map.items():
            url = os.path.join(self.main_url, url)
            # Get in the url
            res = requests.get(url).text
            soup = BeautifulSoup(res, 'lxml')

            # Check the code
            code_name_dict = {}
            pattern = r'[A-Z]{1,5}[0-9]{,2}\.(csv|xlsx)'
            for a in soup.find_all('a', href=True):
                if re.search(pattern, a['href']):
                    key = a.text
                    if key.lower() in ['excel', 'csv', '']:
                        key = re.search(r'/(.*)\.', a['href']).group(1)
                    code_name_dict[key] = a['href']

            code_book_dict[k] = code_name_dict
            if verbose == True:
                print(k.title())
                print(code_name_dict)
            # Go to the next url

        # Call cleaning function
        self._clean_code_name_ava_year(code_book_dict)

    def _clean_code_name_ava_year(self, code_book_dict):
        # Extract the earliest year and code name one by one
        for league in code_book_dict:
            for division in code_book_dict[league]:
                meta_data = code_book_dict[league][division].split('/')[-2:]
                start_year = meta_data[0]
                code_name = meta_data[1].split('.')[0]

                code_book_dict[league][division] = {'start_year':start_year, 'code_name':code_name}

        # Create dataframe from dict
        # Ref: https://stackoverflow.com/questions/24988131/nested-dictionary-to-multiindex-dataframe-where-dictionary-keys-are-column-label
        df = pd.DataFrame.from_dict(code_book_dict, orient='index').stack().to_frame()
        df = pd.DataFrame(df[0].values.tolist(), index=df.index)
        self.ava_data_table_stat = df

        print(df)

class dataDownloader:
    """
    This class should inherit from the checker to get the request functions.
    """
    def __init__(self, start_year, end_year, league_code:str):
        pass