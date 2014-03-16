import os, sys
import logging
import inspect
from openerp.addons.web.session import OpenERPSession

MAESTRANO_ROOT = os.path.abspath(inspect.getfile(inspect.currentframe()) + '/../../../../maestrano/')

# Load context
execfile(MAESTRANO_ROOT + '/app/init/base.py')
from MaestranoService import MaestranoService
from MnoSsoSession import MnoSsoSession

_logger = logging.getLogger(__name__)
_logger.warning('****************MNO: Overriding OpenERPSession class')



class OpenERPSession(OpenERPSession):
    _name = 'OpenERPSession'
    _inherit = 'web.session.OpenERPSession'
    
    def assert_valid(self, force=False):
        """
        Ensures this session is valid (logged into the openerp server)
        """
        _logger.warning('****************MNO: In asset_valid method')
        maestrano = MaestranoService.getInstance()
        maestrano.setSession(self.context)
        
        if (self._uid and not force):
            uid = self._uid
        else:
            uid = self.proxy("common").login(self._db, self._login, self._password)
        
        if uid:
            # check maestrano session is still valid
            if maestrano.getSsoSession().isValid():
                return
            else:
                raise AuthenticationError("Authentication failure")
        else:
            raise AuthenticationError("Authentication failure")