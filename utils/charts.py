import matplotlib.pyplot as plt
import pandas as pd
import base64
import io

def dataframe_to_chart(df: pd.DataFrame):
    if df.shape[1] < 2:
        return None

    x = df.iloc[:, 0]
    y = df.iloc[:, 1]

    plt.figure()
    plt.bar(x, y)
    plt.xticks(rotation=45)

    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    plt.close()

    return base64.b64encode(buf.getvalue()).decode()
