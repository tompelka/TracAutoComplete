# -*- coding: utf-8 -*-
#Copyright (C) 2013 Red Hat, Inc.

from trac.core import Component, implements
from trac.ticket.api import ITicketManipulator, ITicketActionController

class FillInTheComplete(Component):
    implements(ITicketManipulator, ITicketActionController)

    ### ITicketManipulator methods

    def prepare_ticket(self, req, ticket):
        pass

    def validate_ticket(self, req, ticket):
        self.log.debug("Ticket %r", ticket)
        if ticket.exists and ticket['complete']:
            ticket.values['complete'] = '100'

        return []

    def _get_close_status(self):
        return ['closed']

    def get_ticket_actions(self, req, ticket):
        self.log.debug("Ticket %r", ticket)
        actions_we_handle = []
        if ticket['status'] in self.get_all_status():
            actions_we_handle = [(0,'testing')]
        return actions_we_handle

    def apply_action_side_effects(self, req, ticket, action):
        self.log.debug("Ticket %r", ticket)
        pass
