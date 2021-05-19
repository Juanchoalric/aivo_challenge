class CountryFilterService:
    @classmethod
    def country_filter(cls, df, params):
        """
        
        Filter the given Dataframe if the value given is greater than the value stored
        and check for Total Inequality
        """
        df_filtered = df[(df["Value"] > float(params["value"])) & (df["Inequality"] == "Total")]
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
