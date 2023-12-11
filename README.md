### Инструкция по сборке и запуску приложения

Для запуска данного веб приложения необходим `python3-flask`, который устанавливается с помощью команды

`sudo apt install python3-flask`

Чтобы скачать приложение необходимо склонировать репозиторий

`git clone https://github.com/Rosamon/vulnerable_python_web.git && cd vulnerable_python_web`


Далее необходимо использовать виртуальную среду

`python -m venv env && source ./env/bin/activate`

Скачать необходимые библиотеки из файла requirements.txt

pip install -r requirements.txt

Затем стоит запустить приложение через команду flask

`FLASK_APP=webapp.py FLASK_DEBUG=1 flask run`


### Proof of Concept

#### XSS - имплементировано в файле resources_xss.py
> Кнопка Leave a comment
1. Перейти на страницу http://127.0.0.1:5000/xss
2. Ввести комментарий в форму в виде <script>alert(123)</script>
3. Получить подтверждение эксплуатации путем перезагрузки страницы


#### SQLi - имплементировано в файле resources_sqli.py
> Кнопка Visit your Profile (if authorized)
1. Аторизоватся по адресу http://127.0.0.1:5000/bruteforce - ввести логин user, пароль user; Нажать на кнопку Login
2. Перейти по адресу http://127.0.0.1:5000/sqli
3. Ввести в поле иньекцию: secret' OR 1=1 --
4. Нажать на кнопку
5. Увидеть информацию не принадлежащую пользователю user (если ввести только secret - выведет информацию о текущем пользователе)

#### IDOR - имплементировано в файле resources_idor.py
> Кнопка View your secret (if authorized)
1. Аторизоватся по адресу http://127.0.0.1:5000/bruteforce - ввести логин user, пароль user; Нажать на кнопку Login
2. Перейти по адресу http://127.0.0.1:5000/idor
3. Изменить URL c http://127.0.0.1:5000/idor/<number> на http://127.0.0.1:5000/idor/1
4. Получить доступ к секрету пользователя с id = 1, то есть admin

#### OS command injection - имплементировано в файле resources_osci.py
> Кнопка Read about our strategy
1. Перейти по адресу http://127.0.0.1:5000/osci?filename=strategy.txt
2. Дописать в URL любую команду, например http://127.0.0.1:5000/osci?filename=strategy.txt;cat ./instance/flag.txt
3. Увидеть в конце текста результат выполнения команды, если использовался пример, то можно увидеть WOW You got access to the super secret place!!!


#### path traversal - имплементировано в файле resources_path.py
> Кнопка Read about our company
1. Перейти по адресу http://127.0.0.1:5000/path_traversal?filename=about.txt
2. Дописать вместо about.txt любой путь, например http://127.0.0.1:5000/path_traversal?filename=instance/flag.txt
3. Увидеть содержимое этого файла


#### brute force - имплементировано в файле resources_bruteforce.py
Достаточно запустить скрипт `LoginAttack.py`, который перебирает пароли для пользователя admin.


### Дополнительные комментарии
Можно было бы сделать запуск через файл, но я не имею опыта в запуске таким способом, и когда я начал - появились неотслеживаемые ошибки.
Зарегестрировать пользователя можно по кнопке главного меню register.
