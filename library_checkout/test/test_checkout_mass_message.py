from odoo import exceptions
from odoo.tests import common


class TestWizard(common.SingleTransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestWizard, self).setUp(*args, **kwargs)
        # Add test setup code here....

    def test_01_button_send(self):
        """Send button should create message on checkout"""
        # add test code