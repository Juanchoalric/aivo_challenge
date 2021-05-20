import pandas as pd
import os


class CountryFilterService:
    @classmethod
    def country_filter(cls, param):
        """

        Filter the given Dataframe if the value given is greater than the value stored
        and check for Total Inequality
        """
        df_life_satisfaction = cls.__read_from_countries_dataset()
        df_filtered = df_life_satisfaction[
            (df_life_satisfaction["Value"] > param) &
            (df_life_satisfaction["Inequality"] == "Total")
            ]
        response = {'countries': []}
        for _, row in df_filtered.iterrows():
            response["countries"].append(
                {
                    "country": row["Country"],
                    "flags": row["Flags"],
                    "indicator": row["Indicator"],
                    "inequality": row["Inequality"],
                    "measure": row["Measure"],
                    "powerCode": row["PowerCode"],
                    "reference Period": row["Reference Period"],
                    "unit": row["Unit"],
                    "value": row["Value"]
                }
            )
        return response

    @classmethod
    def __read_from_countries_dataset(cls):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'countries.csv')
        return pd.read_csv(my_file).fillna("")
