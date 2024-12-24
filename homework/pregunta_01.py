"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01(file_path='files/input/clusters_report.txt'):
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
    
    import pandas as pd
    
    clusters = []
    current_cluster = None
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        start_processing = False
        
        for line in lines:
            if not line.strip():
                continue
                
            if '----' in line:
                start_processing = True
                continue
                
            if not start_processing:
                continue
                
            if line.strip()[0].isdigit():
                parts = line.split()
                current_cluster = {
                    'cluster': int(parts[0]),
                    'cantidad_de_palabras_clave': int(parts[1]),
                    'porcentaje_de_palabras_clave': float(parts[2].replace(',', '.').replace('%', '')),
                    'principales_palabras_clave': ''
                }
                
                current_cluster['principales_palabras_clave'] = ' '.join(parts[4:])
                clusters.append(current_cluster)
            
            elif current_cluster is not None:
                current_cluster['principales_palabras_clave'] += ' ' + line.strip()
    
    for cluster in clusters:
        keywords = cluster['principales_palabras_clave']
        keywords = keywords.replace('\n', ' ')
        keywords = keywords.replace('.', '')
        keywords = ' '.join(keywords.split())
        keywords = keywords.split(',')
        keywords = [keyword.strip() for keyword in keywords if keyword.strip()]
        cluster['principales_palabras_clave'] = ', '.join(keywords)

    df = pd.DataFrame(clusters)

    return df