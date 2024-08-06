from collections import UserDict
from record import Record

class AddressBook(UserDict):
    """
    Class for managing records in an address book.
    """

    def add_record(self, record: Record) -> None:
        """
        Adds a record to the address book if it doesn't already exist.

        Args:
            record (Record): The record to be added.
        """
        if record.name.value in self.data:
            print(f"Contact {record.name.value} already exists.")
        else:
            self.data[record.name.value] = record
            print(f"Contact {record.name.value} added successfully.")

    def find(self, name: str) -> Record:
        """
        Finds a record by name.

        Args:
            name (str): The name to search for.

        Returns:
            Record: The found record or None if the record is not found.
        """
        if name in self.data:
            return self.data[name]
        else:
            print(f"Contact {name} not found.")
            return None

    def delete(self, name: str) -> bool:
        """
        Deletes a record by name.

        Args:
            name (str): The name of the record to delete.

        Returns:
            bool: True if the record was deleted, False if the record was not found.
        """
        if name in self.data:
            del self.data[name]
            return True
        return False