"""
Injector configuration.

Define dependency injection configuration by binding interfaces to its
implementations.
"""
from injector import singleton, Binder


# Ports
from src.phone_records.application.services.call_service import CallService
from src.phone_records.infrastructure.call_repository import CallRepository

# Adapters
from src.phone_records.application.services.impl.default_call_service import (
    DefaultCallService,
)
from src.phone_records.infrastructure.impl.default_call_repository import (
    DefaultCallRepository,
)


def configure(binder: Binder):
    """Dependency Injection configuration.

    :param binder: Bind interfaces to implementations
    :type binder: Binder
    """
    binder.bind(CallService, to=DefaultCallService, scope=singleton)  # type: ignore
    binder.bind(CallRepository, to=DefaultCallRepository, scope=singleton)  # type: ignore
