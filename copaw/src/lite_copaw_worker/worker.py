"""
LiteWorker: lightweight variant of copaw_worker.Worker.

Runs headless only (no web console) to minimize resource usage.
Reuses sync, bridge, and MatrixChannel from copaw_worker.
"""
from __future__ import annotations

import logging

from copaw_worker.config import WorkerConfig
from copaw_worker.worker import Worker

logger = logging.getLogger(__name__)


class LiteWorker(Worker):
    """Headless-only worker for lite CoPaw runtime."""

    def __init__(self, config: WorkerConfig) -> None:
        config.console_port = None
        super().__init__(config)

    async def _run_copaw(self) -> None:
        await self._run_copaw_headless()
