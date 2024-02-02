from flask import Flask, jsonify
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

app = Flask(__name__)

# Ruta al archivo CSV
url = "https://storage.googleapis.com/the_public_bucket/wine-clustering.csv"

# Lee el dataset como pandas dataframe
winedata = pd.read_csv(url)

# Puedes definir rutas y funciones aquí para manejar las solicitudes de la API
@app.route('/get_wine_data', methods=['GET'])
def get_wine_data():
    try:
        # Retorna los datos del vino como JSON
        wine_data_json = winedata.to_dict(orient='records')
        return jsonify({"wine_data": wine_data_json, "message": "Wine data retrieved successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/run_analysis', methods=['GET'])
def run_analysis():
    try:
        # Realizar análisis y clustering
        scaler = StandardScaler()
        wineEscalado = scaler.fit_transform(winedata)

        kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
        labels = kmeans.fit_predict(wineEscalado)

        # Convertir el array de Numpy a un DataFrame de Pandas
        wine_clustered = pd.DataFrame(data=wineEscalado, columns=winedata.columns)
        wine_clustered['ClusterLabel'] = labels

        # Calcular la media de cada característica dentro de cada cluster
        cluster_means = wine_clustered.groupby('ClusterLabel').mean()

        # Visualización
        plt.figure(figsize=(12, 8))
        sns.heatmap(cluster_means, annot=True, cmap='viridis')
        plt.title('Perfil de Características por Cluster')
        plt.savefig('analysis_result.png')  # Guardar la visualización como imagen

        return jsonify({"message": "Analysis completed successfully!", "result_image": "analysis_result.png"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
