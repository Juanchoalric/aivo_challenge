import pandas as pd

class CountryFilterService:
    @classmethod
    def country_filter(cls, params):
        """

        Filter the given Dataframe if the value given is greater than the value stored
        and check for Total Inequality
        """
        df_life_satisfaction = __read_from_countries_dataset()
        df_filtered = df_life_satisfaction[
            (df_life_satisfaction["Value"] > float(params["life_satisfaction_index"])) & 
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

    def __read_from_countries_dataset():
        return pd.read_csv("app\countries.csv")
