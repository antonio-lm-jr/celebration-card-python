from dependency_injector import containers, providers

from src.application.cases.create_celebration import CreateCelebrationUseCase
from src.application.cases.get_celebration import GetCelebrationUseCase
from src.application.ports.repository import CelebrationRepositoryInterface
from src.infra.repository.celebration_repository import CelebrationRepository
from src.infra.repository.service.conn_interface import ConnInterface
from src.infra.repository.service.tinydb_adapter import TinyDBConnAdapter
from src.settings.base import settings


class Adapters(containers.DeclarativeContainer):
    conn: ConnInterface = providers.Singleton(TinyDBConnAdapter, url_db=settings.DB_URL)
    celebration_repository: CelebrationRepositoryInterface = providers.Factory(
        CelebrationRepository, conn=conn
    )


class UseCases(containers.DeclarativeContainer):
    adapters = providers.DependenciesContainer()

    create_celebration = providers.Factory(
        CreateCelebrationUseCase, repository=adapters.celebration_repository
    )

    get_celebration = providers.Factory(
        GetCelebrationUseCase, repository=adapters.celebration_repository
    )
