```appium_project/
│
├── 📁 tests/ # Casos de prueba organizados por funcionalidad
│ ├── test_login.py
│ ├── test_registration.py
│ └── **init**.py
│
├── 📁 pages/ # Page Object Model (POM): representa pantallas de la app
│ ├── login_page.py
│ ├── home_page.py
│ └── **init**.py
│
├── 📁 utils/ # Utilidades y helpers
│ ├── driver_factory.py # Inicialización del driver Appium
│ ├── logger.py # Logging personalizado
│ └── config.py # Configuración general
│
├── 📁 resources/ # Archivos como APKs, capturas, etc.
│ └── my_app.apk
│
├── 📁 reports/ # Reportes de pruebas (Allure, HTMLTestRunner, etc.)
│ └── ...
│
├── conftest.py # Hooks y fixtures de pytest
├── requirements.txt # Dependencias del proyecto
├── README.md # Instrucciones del proyecto
└── pytest.ini # Configuraciones de pytest```
