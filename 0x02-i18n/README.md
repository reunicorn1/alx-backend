# 0x02. i18n

Internationalization, often abbreviated as i18n, is the process of designing a software application so that it can be adapted to various languages and regions without engineering changes. This involves structuring your code in a way that makes it easy to swap out text, images, date and time formats, and other locale-specific elements.
Localization, often abbreviated as l10n, is the process of adapting an internationalized application for a specific region or language by adding locale-specific components and translating text. This involves actually creating the translated content and other resources that your application will use when it runs in a specific locale.

## Flask-Babel

Flask-Babel is a Flask extension that provides support for Babel, an internationalization (i18n) and localization (l10n) framework for Python. It allows your Flask application to support translations of text and locale-specific formatting of dates, times, and numbers. This is particularly useful when you're developing a web application that needs to support multiple languages.

## Tasks/Files


|    Tasks       |     Files                     |
|----------------|-------------------------------|
|0. Basic Flask app|``0-app.py``, ``templates/0-index.html``|
|1. Basic Babel setup|``1-app.py``, ``templates/1-index.html``|
|2. Get locale from request|``2-app.py``, ``templates/2-index.html``|
|3. Parametrize templates|`3-app.py, babel.cfg, templates/3-index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po, translations/en/LC_MESSAGES/messages.mo, translations/fr/LC_MESSAGES/messages.mo`|
|4. Force locale with URL parameter|`4-app.py, templates/4-index.html`|
|5. Mock logging in|``5-app.py``, ``templates/5-index.html``|
|6. Use user locale|``6-app.py``, ``templates/6-index.html``|
|7. Infer appropriate time zone|``7-app.py``, ``templates/7-index.html``|


