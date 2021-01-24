from .base_api import BaseAPI


class TendermintAPI(BaseAPI):
    async def proposals(self):
        res = await self._c.get(f"/gov/proposals")
        return res["result"]
