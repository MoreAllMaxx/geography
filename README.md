Для запуска приложения 
1. В папку [geography/](geography/) добавьте файл settings.py, скопируйте в него содержимое 
файла [settings.py.default](geography/settings.py.default). Добавьте соответствующую информацию 
в SECRET_KEY, DATABASES.
2. Установите необходимые пакеты:

`pip install -r requirements.txt`

3. Включите локально mysql:

`$ sudo service mysql start`

(изменить настройки подключения можно в [settings.py](devices/devices/settings.py))

4. Запустите веб-приложение:

`python manage.py runserver`

5. По адресу http://127.0.0.1:8000/api/ будет запущена API с созданием и получением записки.