import pandas as pd

from pathlib import Path


RAW_DIR = Path("data/raw")
CLEAN_DATA_DIR = Path("data/clean_data")

# Ensure processed directory exists
CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)


def main():
    for file_path in RAW_DIR.rglob("*.csv"):
        try:
            df = pd.read_csv(file_path, sep=";", encoding="latin1")
            df_clean = transform_df(df)

            output_path = CLEAN_DATA_DIR / file_path.name
            df_clean.to_csv(output_path, index=False,
                            sep=",", encoding='latin1')
        except Exception as e:
            print("Error: ", str(e))
        finally:
            # Create codes and region
            create_region_codes()


def rename_cols(cols_list: list[str]):
    clean_cols = []
    for col in cols_list:
        if 'Comunidades y Ciudades' in col:
            clean_cols.append('region')
        else:
            clean_cols.append(col.lower().replace(' ', '_'))
    return clean_cols


def transform_df(df: pd.DataFrame):
    """Clean dataframe.
        Rename cols,
        Rebuild df,
        Remove numbers and dots,
        Extract code and name
    """
    # Clean cols
    clean_cols = rename_cols(df.columns.values)
    df.columns = clean_cols

    # Rebuild df
    if 'total_nacional' in df.columns:
        # we will add a new "code" for Total==00 and Ceuta y meililla=18
        # We get the "Total_Nacional", is not ceuta and the region is empty
        mask_total = (df["total_nacional"] == "Total Nacional") & (
            df["region"].isna())
        df.loc[mask_total, "region"] = "00 Total Nacional"

        # Get ceuta and replace values
        mask_ceuta = df["total_nacional"] == 'Ceuta y Melilla'
        df.loc[mask_ceuta, "region"] = '18 Ceuta y Melilla'
        df.drop(columns=["total_nacional"], inplace=True)

    # Remove numbers and points
    if 'tipo_de_indicador' in df.columns:
        df["tipo_de_indicador"] = df["tipo_de_indicador"].str.replace(
            r"^\d+(\.\d+)*\.\s*", "", regex=True)
        # Remove some "-" that i saw
        df["tipo_de_indicador"] = df["tipo_de_indicador"].str.replace(
            r"^-+\s*", "", regex=True)
    if 'principales_indicadores' in df.columns:
        df["principales_indicadores"] = df["principales_indicadores"].str.replace(
            r"^\d+(\.\d+)*\.\s*", "", regex=True)

    if 'region' in df.columns:
        # Extract code and name
        df[["code", "region_name"]
           ] = df["region"].str.extract(r"^(\d+)\s+(.*)")
        # print(df)
        # Drop region as we dont need it and rename to region again (keep region_Code though)
        df.drop(columns=["region"], inplace=True)
        df.rename(columns={"region_name": "region"}, inplace=True)

        # Reorder new cols in the front
        new_order_cols = ["code", "region"] + \
            [col for col in df.columns if col not in ["code", "region"]]
        df = df[new_order_cols]

    return df


def create_region_codes():
    REGION_CODES = {
        "Total Nacional": "00",
        "Andalucía": "01",
        "Aragón": "02",
        "Asturias, Principado de": "03",
        "Balears, Illes": "04",
        "Canarias": "05",
        "Cantabria": "06",
        "Castilla y León": "07",
        "Castilla - La Mancha": "08",
        "Cataluña": "09",
        "Comunitat Valenciana": "10",
        "Extremadura": "11",
        "Galicia": "12",
        "Madrid, Comunidad de": "13",
        "Murcia, Región de": "14",
        "Navarra, Comunidad Foral de": "15",
        "País Vasco": "16",
        "Rioja, La": "17",
        "Ceuta y Melilla": "18"
    }
    df_region = pd.DataFrame([
        {"code": code, "region": name}
        for name, code in REGION_CODES.items()
    ])
    
    df_region.to_csv("data/clean_data/region_codes.csv",
                    index=False, sep=";", encoding="latin1")
    

if __name__ == "__main__":
    main()
