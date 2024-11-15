from abc import ABC, abstractmethod
from pathlib import Path


class DataSource(ABC):
    @abstractmethod
    def get_data(self) -> list[dict]:
        pass


class CSVDataSource(DataSource):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_data(self) -> list[dict]:
        import csv

        with Path(self.file_path).open(encoding="utf-8") as file:
            return list(csv.DictReader(file))


class APIDataSource(DataSource):
    def __init__(self, api_url: str):
        self.api_url = api_url

    def get_data(self) -> list[dict]:
        import requests

        response = requests.get(self.api_url, timeout=10)
        return response.json()


class JSONDataSource(DataSource):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_data(self) -> list[dict]:
        import json

        with Path(self.file_path).open(encoding="utf-8") as file:
            return json.load(file)


class DatabaseDataSource(DataSource):
    def __init__(self, db_connection, query: str):
        self.db_connection = db_connection
        self.query = query

    def get_data(self) -> list[dict]:
        cursor = self.db_connection.cursor()
        cursor.execute(self.query)
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row, strict=False)) for row in cursor.fetchall()]
