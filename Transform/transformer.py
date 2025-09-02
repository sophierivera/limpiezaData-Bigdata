class Transformer:
    """
    Clase para transformar y limpiar los datos de usuarios/jugadores.
    """
    def __init__(self, df):
        self.df = df

    def clean(self):
        """
        Realiza limpieza y transformación de los datos.
        """
        import pandas as pd
        df = self.df.copy()

        # Eliminar filas con UserID nulo (clave primaria)
        df = df.dropna(subset=['UserID'])

        # Conversión de columnas numéricas
        num_cols = [
            'Age',
            'SessionCount',
            'AverageSessionLength',
            'InAppPurchaseAmount',
            'FirstPurchaseDaysAfterInstall'
        ]
        for col in num_cols:
            if col in df.columns:
                df[col] = (
                    pd.to_numeric(
                        df[col].astype(str).str.replace(',', '.', regex=False), 
                        errors='coerce'
                    )
                    .fillna(0)
                )

        # Normalizar columnas de texto
        text_cols = [
            'Gender',
            'Country',
            'Device',
            'GameGenre',
            'SpendingSegment',
            'PaymentMethod'
        ]
        for col in text_cols:
            if col in df.columns:
                df[col] = df[col].fillna('Unknown').astype(str).str.strip()

        # Conversión de fechas
        if 'LastPurchaseDate' in df.columns:
            df['LastPurchaseDate'] = pd.to_datetime(df['LastPurchaseDate'], errors='coerce')

        self.df = df
        return self.df
