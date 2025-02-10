# DeepGeek API

¡Bienvenido al proyecto **DeepGeek API**! Esta es una API desarrollada en Flask que utiliza el modelo de
lenguaje DeepSeek para analizar respuestas de usuarios y determinar qué héroe de cómic encaja mejor con sus
características.

---

## 🚀 Características principales

- **Análisis de personalidad**: Los usuarios responden un cuestionario, y la API determina qué héroe de cómic coincide
  mejor con sus respuestas.
- **Integración con DeepSeek**: Utiliza el modelo de lenguaje DeepSeek para generar respuestas precisas y detalladas.
- **Estructura modular**: El proyecto está organizado en módulos para facilitar el mantenimiento y la escalabilidad.

---

## 📂 Estructura del proyecto

```
├── .venv               # Entorno Virtual que maneja las dependencias
├── app/
│   ├── core/             # Configuración que usa las variables de entorno
│   ├── models/           # Modelos de datos
│   ├── routes/           # Rutas de la API
│   ├── services/         # Lógica de negocio y servicios
│   ├── utils/            # Utilidades adicionales
│   ├── init.py           # Inicialización de la aplicación Flask
│   ├── main.py           # Punto de entrada principal
├── .env                # Archivo de configuración con variables de entorno
├── .gitignore          # Archivo que maneja que carpetas o archivos se ignorarán en GIT
├── README.md
└── requirements.txt    # Dependencias del proyecto
```

---

## 🛠️ Requisitos

- Python 3.8 o superior
- Flask
- DeepSeek API Key (obtén una en [DeepSeek](https://www.deepseek.com/))

---

## 🚀 Instalación

### 1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/RogerCS17/deepgeek-backend.git
   cd deepgeek-backend
   ```

### 2. **Crea un entorno virtual**:

   ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

### 3. **Instala las dependencias**:

   ```bash
    pip install -r requirements.txt
   ```

### 4. **Configura las variables de entorno**:

Crea un archivo `.env` en la raíz del proyecto y agrega tu API Key de DeepSeek

   ```bash
    API_KEY=API_KEY_DEEPSEEK
   ```

### 5. **Ejecuta la aplicación**:

   ```bash
    cd app
    flask --app main run
   ```