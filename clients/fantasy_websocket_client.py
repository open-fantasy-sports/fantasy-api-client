from clients.websocket_client import WebsocketClient
from messages.fantasy_msgs import *


class FantasyWebsocketClient(WebsocketClient):

    async def send_sub_users(self, data: SubUser):
        return await self.send_and_get_resp("SubUser", data)

    async def send_sub_leagues(self, data: SubLeague):
        return await self.send_and_get_resp("SubLeague", data)

    async def send_sub_drafts(self, data: SubDraft):
        return await self.send_and_get_resp("SubDraft", data)

    async def send_insert_leagues(self, data: List[League]):
        return await self.send_and_get_resp("League", data)

    async def send_insert_periods(self, data: List[Period]):
        return await self.send_and_get_resp("Period", data)

    async def send_insert_stat_multipliers(self, data: List[StatMultiplier]):
        return await self.send_and_get_resp("StatMultiplier", data)

    async def send_insert_users(self, data: List[ExternalUser]):
        return await self.send_and_get_resp("ExternalUser", data)

    async def send_insert_fantasy_teams(self, data: List[FantasyTeam]):
        return await self.send_and_get_resp("FantasyTeam", data)

    async def send_insert_draft_queues(self, data: List[DraftQueue]):
        return await self.send_and_get_resp("DraftQueue", data)

    async def send_update_draft_choices(self, data: List[DraftChoice]):
        return await self.send_and_get_resp("DraftChoice", data)

    async def send_insert_pick(self, data: List[Pick]):
        return await self.send_and_get_resp("Pick", data)

    async def send_insert_active_pick(self, data: List[ActivePick]):
        return await self.send_and_get_resp("ActivePick", data)