

def transformation_clean_line_practices(df):
    df=select_certain_cols_from_list(df,key_cols=['id','site_page'],search_name='capabilities')
    df=df.explode('capabilities').rename({"capabilities": "practices"})
    df = df.with_columns(pl.lit(datetime.now(timezone.utc)).cast(pl.Datetime).alias("syncstartdatetime"))
    return df
