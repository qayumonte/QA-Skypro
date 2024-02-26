Для работы с коллекцией GitHub_issue необходимо:
1. Скачать коллекцию по этой ссылке: https://github.com/qayumonte/QA-Skypro/blob/4669215f8a8500852f959ff5bfc49c62df8443f1/GitHub_issue/git_issue.json
2. Импортировать ее в Postman
3. Откройте список
4. <img width="182" alt="Снимок экрана 2024-02-26 в 04 28 51" src="https://github.com/qayumonte/QA-Skypro/assets/156711500/37e8bb8b-3393-40e6-8d86-d9394e5199d2">
5. Получаем Токен: https://github.com/settings/tokens
6. Затем указаваем в поле "Authorization"
7. В запросе "POST Issue 1" указываем тело запроса, скрипт для проверки статуса и скрипты для записи новых переменных: issue_number и node_id.
8. <img width="1199" alt="Снимок экрана 2024-02-26 в 04 39 14" src="https://github.com/qayumonte/QA-Skypro/assets/156711500/cefb0e7d-a300-4c09-b1cc-cc4bec5675c8">
9. Затем открываем наш список issueb, для этого указываем адрес: https://github.com/ВАШ АККАУНТ/ВАШ РЕПОЗИТОРИЙ/issues/
10. Во вкладке "Preview" будет отображен визуально весь список
11. <img width="1206" alt="Снимок экрана 2024-02-26 в 04 41 48" src="https://github.com/qayumonte/QA-Skypro/assets/156711500/4e1d1630-c89c-4e86-86b7-3f7dc6bfba64">
12. Затем, для переименования указываем в теле запроса новое имя, а в запросе {{issue_number}}, который сохранился при создании.
13. Для блокировки указываем метод PUT и в запросе указываем в конце "lock" ({{url_git}}/{{owner}}/{{repo}}/issues/{{issue_number}}/lock)
14. Для разблокировки указываем метод DEL и в запросе указываем в конце "lock" ({{url_git}}/{{owner}}/{{repo}}/issues/{{issue_number}}/lock)
15. Для удаления указываем метод POST и адрес: https://api.github.com/graphql, далее пишем скрипт, который указан на скриншоте
16. <img width="1219" alt="Снимок экрана 2024-02-26 в 05 04 10" src="https://github.com/qayumonte/QA-Skypro/assets/156711500/a0003039-1438-4e26-ad1c-db61601bbaad">
17. Вам поступит ответ, что issue удалена
