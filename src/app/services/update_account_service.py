import logging

from injector import inject

from src.app.commands.update_account import UpdateAccount
from src.app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from src.domain.model.account import Account
from src.domain.model.contact_information import ContactInformation

logger = logging.getLogger(__name__)


class UpdateAccountService:
    __account_repository: AccountRepository

    @inject
    def __init__(self, account_repository: AccountRepository) -> None:
        self.__account_repository = account_repository

    def update(self, update_account: UpdateAccount) -> Account:
        account = Account(
            update_account.id,
            ContactInformation(update_account.email, update_account.cellphones),
        )
        logger.info(f"Updating account {account.id}")
        return self.__account_repository.update(update_account.id, account)
