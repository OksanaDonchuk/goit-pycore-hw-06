from typing import List, Optional
from name import Name
from phone import Phone

class Record:
    """
    Class for storing information about a contact, including the name and list of phone numbers.
    """

    def __init__(self, name: str):
        """
        Initializes a record with a name.

        Args:
            name (str): The name of the contact.
        """
        self.name = Name(name)
        self.phones: List[Phone] = []

    def add_phone(self, phone_number: str) -> None:
        """
        Adds a phone number to the record.

        Args:
            phone_number (str): The phone number to add.
        """
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number: str) -> bool:
        """
        Removes a phone number from the record.

        Args:
            phone_number (str): The phone number to remove.

        Returns:
            bool: True if the phone number was removed, False if the phone number was not found.
        """
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return True
        return False

    def edit_phone(self, old_phone_number: str, new_phone_number: str) -> bool:
        """
        Edits a phone number in the record.

        Args:
            old_phone_number (str): The old phone number to edit.
            new_phone_number (str): The new phone number to replace the old one.

        Returns:
            bool: True if the phone number was edited, False if the old phone number was not found.
        """
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone.value = phone.validate_phone(new_phone_number)
                return True
        return False

    def find_phone(self, phone_number: str) -> Optional[Phone]:
        """
        Finds a phone number in the record.

        Args:
            phone_number (str): The phone number to find.

        Returns:
            Optional[Phone]: The found phone number or None if the phone number was not found.
        """
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self) -> str:
        """
        Returns a string representation of the record.

        Returns:
            str: A string representation of the record.
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(phone.value for phone in self.phones)}"