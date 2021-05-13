<div align="center">
	<h1>Notion SDK for Python</h1>
	<p>
		<b>A simple and easy to use client for the <a href="https://developers.notion.com">Notion API</a></b>
    <b>Inspired by <a href="https://github.com/makenotion/notion-sdk-js">notion-sdk-js</a></b>
	</p>
	<br>
	<br>
	<br>
</div>

## Installation

```
$ pip install notion-sdk-py
```

## Usage

> Before getting started, [create an integration](https://www.notion.com/my-integrations) and find the token.
>
> [→ Learn more about authorization](https://developers.notion.com/docs/authorization).

Import and initialize a client using an **integration token** or an OAuth **access token**.

```py
import os
from notion.api import Notion

# Initializing a client
const notion = Notion(auth=os.getenv("AUTH_TOKEN"))

# retrieve databases
notion.retrieve_database(database_id="897e5a76-ae52-4b48-9fdf-e71f5945d1af");
```
