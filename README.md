# ml_course_itmo
Проект в рамках курса повышения квалификации на базе университета ИТМО "Машинное обучение для анализа научных данных".

[Сертификат](https://drive.google.com/drive/folders/1dpLtXS3apfdA2T_2hlCIoYvsGl0T9p3Y).

# Data
Данные для анализа взяты с сайта Kaggle и доступны по [ссылке](https://www.kaggle.com/datasets/slehkyi/extended-football-stats-for-european-leagues-xg).

# Постановка задачи
Задача: предсказывать результат матчей (классификация: победа, ничья, поражение) в чемпионате на основании информации о последних пяти матчах команд и количества набранных очков в сезоне на момент начала встречи.

# Метрики
Accuracy и f1-мера.

# Используемые библиотеки.
pandas, sklearn, matplotlib, seaborn, optuna, plotly.

# task1_EDA_Baseline.ipynb
- Формирование признаков.
- Обучение базовых моделей.
- Интерактивные графики набора очков командами с использованием библиотеки Plotly. Доступны по [ссылке](https://zamnikita.github.io/ml_course_itmo/getting_points_by_each_team_plots.html) на GitHub Page. 

# task2_EDA_Baseline.ipynb
- Формирование дополнительных признаков.
- Обучение базовых моделей.
- Обучение ансамблевых моделей.
- Подбор гиперпараметров с помощью библиотеки Optuna.
- Интерпритация моделей.
