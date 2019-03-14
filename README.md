# Простой интернет магазин на Django
***

Приложение shop реализует базовый функционал: каталог продуктов, детальную информацию об отдельном продукте, а также
рекомендательную систему с использованием бд Redis.

cart - корзина товаров, с возможностью увеличить/уменьшить количество выбранного товара, либо удалить его из корзины.

orders - страница окончательного оформления заказ. Сдесь сохраняются реквизиты покупателя. После окончательного
подтверждения заказа пользователю посылается e-mail c информацией в формате pdf при помощи менеджера очередей Celery.
