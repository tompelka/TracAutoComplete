# -*- coding: utf-8 -*-
#Copyright (C) 2013 Red Hat, Inc.

from trac.core import Component, implements
from trac.ticket.api import ITicketManipulator, ITicketActionController
from trac.env import Environment

class FillInTheComplete(Component):
    implements(ITicketManipulator)

    def _get_close_action(self):
        return ['resolve']

    ### ITicketManipulator methods

    def prepare_ticket(self, req, ticket):
        pass

    def validate_ticket(self, req, ticket):
        self.log.debug("Req action %s", req.args)
        if ticket.exists:
            if req.args['action'] in self._get_close_action():
                self.log.debug("Setting up complete")
                ticket.values['complete'] = '100'
                self.log.debug("Complete = %s", ticket.values['complete'])
        else:
            ticket.values['complete'] = '0'

        return []

