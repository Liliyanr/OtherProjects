# Задание от Завода Слоистый пластик.

## Есть набор данных по вкладкам + гугл-таблицы

### Что нужно:
- Факт продажи по менеджерам и направлениям
- Прогноз продаж по менеджерам и направлениям на 2026

Анализ с помощью Power Query, SQL.
Визуализация дашборд Power BI.

SQL

WITH
sp AS (
SELECT DISTINCT s.id_1c, s.direction
FROM spr_partners s)

SELECT 
sp.direction AS "Направление",
bc.`Ответсвенный для прогноза` AS "Менеджер",
bc.`Потенциал сумма` AS "План",
s. Amount AS "Факт",
s. Date

FROM doc_Sales s 
LEFT JOIN doc_OrderSales os ON os.`id 1c` = ds.Zakaz_id_1c
LEFT JOIN b_uts_crm_deal bu ON  bu.`№ ЗК` = os.Number
LEFT JOIN b_crm_deal bc ON bc.ID = bu.VALUE
LEFT JOIN sp ON s.`Partner id` = sp.`id 1c`
