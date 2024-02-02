FROM jupyter/base-notebook

USER root

# Instalar las dependencias necesarias
RUN pip install flask pandas scikit-learn seaborn matplotlib kneed

# Copiar el contenido de la carpeta actual al directorio de trabajo en el contenedor
COPY . /home/jovyan/work

WORKDIR /home/jovyan/work

EXPOSE 5000

CMD ["jupyter", "notebook", "--ip='*'", "--port=5000", "--no-browser", "--allow-root"]
