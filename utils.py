def summarize(df):
    if df.empty:
        return "No results found."

    if df.shape[1] == 2:
        col1, col2 = df.columns
        try:
            top = df.iloc[0]
            return f"{top[col1]} has the highest {col2.replace('_', ' ')} ({top[col2]})."
        except:
            return "Summary not available."
    return "Summary not available."
