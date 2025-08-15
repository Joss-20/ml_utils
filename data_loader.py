class DataLoader:
    def load_csv(self, filepath, parse_dates=None, drop_na=False):
        df = pd.read_csv(filepath)
        if parse_dates:
            for col in parse_dates:
                df[col] = pd.to_datetime(df[col], errors="coerce")
        if drop_na:
            df.dropna(inplace=True)
        return df